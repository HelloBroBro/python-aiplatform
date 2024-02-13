# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Classes for working with language models."""

import dataclasses
import os
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

from google.cloud import storage

from google.cloud import aiplatform
from google.cloud.aiplatform import base
from google.cloud.aiplatform import initializer as aiplatform_initializer
from google.cloud.aiplatform import utils as aiplatform_utils
from google.cloud.aiplatform.utils import gcs_utils
from vertexai._model_garden import _model_garden_models

from google.cloud.aiplatform.compat.services import (
    model_garden_service_client,
)
from google.cloud.aiplatform.compat.types import (
    pipeline_state as gca_pipeline_state,
)

try:
    import pandas
except ImportError:
    pandas = None


_LOGGER = base.Logger(__name__)

# Model Evaluation constants
_TEXT_CLASSIFICATION_TASK_NAME = "text-classification"
_TEXT_GENERATION_TASK_NAME = "text-generation"
_QA_TASK_NAME = "question-answering"
_SUMMARIZATION_TASK_NAME = "summarization"

_EVALUATION_TASKS = frozenset(
    [
        _TEXT_CLASSIFICATION_TASK_NAME,
        _TEXT_GENERATION_TASK_NAME,
        _QA_TASK_NAME,
        _SUMMARIZATION_TASK_NAME,
    ]
)


_TEXT_CLASSIFICATION_TEMPLATE_URL = "https://us-kfp.pkg.dev/vertex-evaluation/pipeline-templates/evaluation-llm-classification-pipeline"
_TEXT_GENERATION_QA_SUMMARIZATION_TEMPLATE_URL = "https://us-kfp.pkg.dev/vertex-evaluation/pipeline-templates/evaluation-llm-text-generation-pipeline"

_EVALUATION_TEMPLATE_VERSION_TAG = "2.9.0"

_EVALUATION_TEMPLATE_URLS = {
    _TEXT_CLASSIFICATION_TASK_NAME: f"{_TEXT_CLASSIFICATION_TEMPLATE_URL}/{_EVALUATION_TEMPLATE_VERSION_TAG}",
    _TEXT_GENERATION_TASK_NAME: f"{_TEXT_GENERATION_QA_SUMMARIZATION_TEMPLATE_URL}/{_EVALUATION_TEMPLATE_VERSION_TAG}",
    _QA_TASK_NAME: f"{_TEXT_GENERATION_QA_SUMMARIZATION_TEMPLATE_URL}/{_EVALUATION_TEMPLATE_VERSION_TAG}",
    _SUMMARIZATION_TASK_NAME: f"{_TEXT_GENERATION_QA_SUMMARIZATION_TEMPLATE_URL}/{_EVALUATION_TEMPLATE_VERSION_TAG}",
}


_EVALUATION_PIPELINE_COMPONENT_IDENTIFIER = "fpc-llm-evaluation"

_BATCH_PREDICTION_ROW_LIMIT = 30000

_EVAL_SUPPORTED_BASE_MODELS = ["text-bison@001", "text-bison@002"]

T = TypeVar("T", bound="_EvaluationMetricBase")


def _check_dataset_is_within_size_limit(
    data: "pandas.DataFrame",
) -> None:

    if len(data) < _BATCH_PREDICTION_ROW_LIMIT:
        return

    raise ValueError(
        f"Your evaluation dataset size exceeds the limit of {_BATCH_PREDICTION_ROW_LIMIT}"
    )


def _get_model_resource_name_and_validate(
    model_name: str,
    model_info: _model_garden_models._ModelInfo,
) -> str:
    """Returns the resource name string for the model.

    Model Registry resource names will stay the same. For Publisher Models, we need to
    pass the full resource name (publishers/google/models/text-bison@001) to the evaluation
    template and ensure the base model supports evaluation.

    Args:
        model_name (str):
            Required. The full resource name of the Model Registry model or base publisher model
            to run evaluation on.
        model_info (_model_garden_models._ModelInfo):
            Required. The _ModelInfo object for the instance.

    Returns:
        The formatted model_name string.

    Raises:
        ValueError
            If a base PublisherModel was provided and the model doesn't support evaluation.
    """

    if "publishers/" not in model_name:
        # Model Registry resource
        return model_name

    else:
        if model_info.tuning_model_id in _EVAL_SUPPORTED_BASE_MODELS:
            return f"{model_info.publisher_model_resource.name}@{model_info.publisher_model_resource.version_id}"

        raise ValueError(
            f"The provided model {model_name} does not support evaluation."
        )


def _get_template_url(task_name: str) -> Optional[str]:
    """Returns the pipeline template to use for the evaluation task.

    Args:
        task_name (str):
            Required. The name of the evaluation task to run.

    Returns:
        The evaluation pipeline template path.
    """

    return _EVALUATION_TEMPLATE_URLS.get(task_name)


@dataclasses.dataclass
class _EvaluationTaskSpec:
    """Base class for task-specific model evaluation configuration parameters.

    This class should not be instantiated directly, instead use the subclass corresponding
    to your evaluation task.

    Args:
        ground_truth_data (Union[List[str], str, pandas.DataFrame]):
            Required. The ground truth data to use for this evaluation job. This can be
            either a Pandas DataFrame, a Cloud Storage URI of your JSONL data file, or a list of multiple
            JSONL files on Cloud Storage.

    Raises:
        ValueError:
            If task_spec.ground_truth_data is formatted incorrectly.
            If task_spec.ground_truth_data is a Pandas DataFrame and exceeds 1000 rows.
            If task_spec.ground_truth_data is not a string, list, or Pandas DataFrame.
    """

    ground_truth_data: Union[List[str], str, "pandas.DataFrame"]

    @property
    def task_name(self) -> str:
        pass

    def __post_init__(self):

        if isinstance(self.ground_truth_data, str):
            self.ground_truth_data = [self.ground_truth_data]

        if isinstance(self.ground_truth_data, list) and not all(
            item.startswith("gs://") for item in self.ground_truth_data
        ):
            raise ValueError("Please provide a valid GCS URI starting with 'gs://'")

        if pandas and isinstance(self.ground_truth_data, pandas.DataFrame):

            _check_dataset_is_within_size_limit(self.ground_truth_data)


@dataclasses.dataclass
class EvaluationTextClassificationSpec(_EvaluationTaskSpec):
    """Spec for text classification model evaluation tasks.

    Args:
        target_column_name (str):
            Required. The label column in the dataset provided in `ground_truth_data`. Required when task_name='text-classification'.
        class_names (List[str]):
            Required. A list of all possible label names in your dataset. Required when task_name='text-classification'.
    """

    target_column_name: str
    class_names: List[str]

    @property
    def task_name(self) -> str:
        return "text-classification"


@dataclasses.dataclass
class EvaluationTextGenerationSpec(_EvaluationTaskSpec):
    """Spec for text generation model evaluation tasks."""

    @property
    def task_name(self) -> str:
        return "text-generation"


@dataclasses.dataclass
class EvaluationQuestionAnsweringSpec(_EvaluationTaskSpec):
    """Spec for question answering model evaluation tasks."""

    task_name: str = "question-answering"


@dataclasses.dataclass
class EvaluationTextSummarizationSpec(_EvaluationTaskSpec):
    """Spec for text summarization model evaluation tasks."""

    task_name: str = "summarization"


@dataclasses.dataclass
class _EvaluationMetricBase:
    """Base class for returned evaulation metrics."""

    @property
    def input_dataset_paths(self) -> str:
        """The Google Cloud Storage paths to the dataset used for this evaluation."""
        pass

    @property
    def task_name(self) -> str:
        """The type of evaluation task for the evaluation.."""
        pass


@dataclasses.dataclass
class EvaluationMetric(_EvaluationMetricBase):
    """The evaluation metric response.

    Args:
        bleu (float):
            Optional. BLEU (Bilingual evauation understudy). Scores based on sacrebleu implementation.
        rougeLSum (float):
            Optional. ROUGE-L (Longest Common Subsequence) scoring at summary level.
    """

    bleu: Optional[float] = None
    rougeLSum: Optional[float] = None


@dataclasses.dataclass
class EvaluationClassificationMetric(_EvaluationMetricBase):
    """The evaluation metric response for classification metrics.

    Args:
        label_name (str):
            Optional. The name of the label associated with the metrics. This is only
            returned when `only_summary_metrics=False` is passed to evaluate().
        auPrc (float):
            Optional. The area under the precision recall curve.
        auRoc (float):
            Optional. The area under the receiver operating characteristic curve.
        logLoss (float):
            Optional. Logarithmic loss.
        confidenceMetrics (List[Dict[str, Any]]):
            Optional. This is only returned when `only_summary_metrics=False` is
            passed to evaluate().
        confusionMatrix (Dict[str, Any]):
          Optional. This is only returned when `only_summary_metrics=False` is
          passed to evaluate().
    """

    label_name: Optional[str] = None
    auPrc: Optional[float] = None
    auRoc: Optional[float] = None
    logLoss: Optional[float] = None
    confidenceMetrics: Optional[List[Dict[str, Any]]] = None
    confusionMatrix: Optional[Dict[str, Any]] = None


@dataclasses.dataclass
class EvaluationSlicedClassificationMetric(_EvaluationMetricBase):
    """The evaluation metric slices returned for classification metrics.

    This is returned when `only_summary_metrics=False` is passed to evaluate().

    Args:
        overall_metrics (EvaluationClassificationMetric):
            The evaluation metrics across all slices of data
        slices (List[EvaluationClassificationMetric]):
            The evaluation metrics for each label slice.
    """

    overall_metrics: Optional[EvaluationClassificationMetric] = None
    slices: Optional[List[EvaluationClassificationMetric]] = None


def _populate_eval_template_params(
    task_spec: _EvaluationTaskSpec,
    model_name: str,
    service_account: Optional[str] = None,
    machine_type: Optional[str] = None,
    network: Optional[str] = None,
    encryption_spec_key_name: Optional[str] = None,
) -> Dict[str, Any]:
    """Populates a dictionary of template parameters for the evaluation PipelineJob.

    Args:
        task_spec (EvaluationTaskSpec):
            The EvaluationTaskSpec passed to evaluate() for this job
        model_name (str):
            The resource name of the model being evaluated. Either a PublisherModel or
            ModelRegistry resource name.
        service_account (Optional[str]):
            The default service account for workload run-as account.
        machine_type (Optional[str]):
            Optional. The type of the machine to run the evaluation job on.
        network (Optional[str]):
            Optional.
        encryption_spec_key_name (Optional[str]):
            Optional.

    Returns:
        Dict[str, Any]:
            A dictionary of template parameter names and values to be passed to the PipelineJob
            running the model evaluation.
    """

    ground_truth_data_gcs_path = task_spec.ground_truth_data

    staging_bucket = aiplatform_initializer.global_config.staging_bucket

    if not staging_bucket:
        staging_bucket = (
            gcs_utils.create_gcs_bucket_for_pipeline_artifacts_if_it_does_not_exist()
        )

    timestamped_eval_directory = (
        f"evaluation_data_{aiplatform_utils.timestamped_unique_name()}"
    )

    if isinstance(task_spec.ground_truth_data, pandas.DataFrame):

        # Convert to jsonl file and upload to gcs
        dataset_uri = os.path.join(
            staging_bucket,
            timestamped_eval_directory,
            "eval_data.jsonl",
        )

        gcs_utils._upload_pandas_df_to_gcs(
            df=task_spec.ground_truth_data, upload_gcs_path=dataset_uri
        )
        ground_truth_data_gcs_path = [dataset_uri]

    template_params = {
        "project": aiplatform_initializer.global_config.project,
        "location": aiplatform_initializer.global_config.location,
        "batch_predict_gcs_destination_output_uri": f"{staging_bucket}/{timestamped_eval_directory}",
        "model_name": model_name,
        "batch_predict_gcs_source_uris": ground_truth_data_gcs_path,
        "service_account": service_account,
        "machine_type": machine_type,
        "encrytion_spec_key_name": encryption_spec_key_name
        or aiplatform_initializer.global_config.encryption_spec_key_name,
        "network": network or aiplatform_initializer.global_config.network,
    }

    if task_spec.task_name == _TEXT_CLASSIFICATION_TASK_NAME:
        template_params["evaluation_class_labels"] = task_spec.class_names
        template_params["target_field_name"] = task_spec.target_column_name
    else:
        template_params["evaluation_task"] = task_spec.task_name

    return template_params


# TODO (b/285947054): update to use public pipeline contract
def _get_gcs_uri_from_pipeline_task_details(
    pipeline_job: aiplatform.PipelineJob,
) -> Optional[str]:
    """Gets the GCS URI from the PipelineJob output.

    Args:
        pipeline_job (aiplatform.PipelineJob)
            The PipelineJob resource to get the metrics GCS URI from

    Returns:
        The GCS URI of the evaluation metrics as a string.
    """

    for task in pipeline_job.task_details:
        if task.task_name == pipeline_job.name and "evaluation_metrics" in task.outputs:
            return task.outputs["evaluation_metrics"].artifacts[0].uri


def _convert_metrics_dict_to_response_type(
    metrics_json: Dict[str, Any],
    metric_type: Type[T],
    metric_name: Optional[str] = None,
) -> EvaluationClassificationMetric:
    metrics_response = metric_type()
    if metric_name:
        metrics_response.label_name = metric_name

    for metric, value in metrics_json.items():
        if hasattr(metrics_response, metric):
            setattr(metrics_response, metric, value)
    return metrics_response


def _format_classification_metrics(
    metrics: Dict[str, Any]
) -> EvaluationSlicedClassificationMetric:
    """Reformats classification metrics returned by the eval pipeline to make them more readable.

    Returned metrics are of type EvaluationSlicedClassificationMetric, with `overall` representing
    the metrics for all data, and `slices` representing the metrics for each label in the dataset.

    Example schema of reformatted metrics:

    EvaluationSlicedClassificationMetrics(
        overall_metrics=EvaluationClassificationMetric(
            auPrc=...
        )
        slices=[
            EvaluationClassificationMetric(
                label_name="overall",
                auPrc=...,
                ...
            ),
            EvaluationClassificationMetric(
                label_name="label_1",
                auPrc=...,
                ...
            ),
            EvaluationClassificationMetric(
                label_name="label_2",
                auPrc=...,
                ...
            )
        ]
    )
    """

    reformatted_metrics = EvaluationSlicedClassificationMetric()

    # TODO: see if we can do this without relying on specific keys, i.e. slicedMetrics

    # First add overall metrics
    overall_metrics = _convert_metrics_dict_to_response_type(
        metrics_json=metrics["slicedMetrics"][0]["metrics"]["classification"],
        metric_type=EvaluationClassificationMetric,
    )
    reformatted_metrics.overall_metrics = overall_metrics

    sliced_metrics = []

    # Then add metrics for each slice
    for idx in range(1, len(metrics["slicedMetrics"])):
        metric_slice_name = metrics["slicedMetrics"][idx]["singleOutputSlicingSpec"][
            "value"
        ]

        sliced_metric = _convert_metrics_dict_to_response_type(
            metrics_json=metrics["slicedMetrics"][idx]["metrics"]["classification"],
            metric_type=EvaluationClassificationMetric,
            metric_name=metric_slice_name,
        )
        sliced_metrics.append(sliced_metric)

    reformatted_metrics.sliced_metrics = sliced_metrics

    return reformatted_metrics


def _get_metrics_from_gcs_uri(
    gcs_uri: str,
) -> Union[
    EvaluationMetric,
    EvaluationClassificationMetric,
    EvaluationSlicedClassificationMetric,
]:
    """Downloads evaluation metrics from GCS path."""

    storage_client = storage.Client(
        credentials=aiplatform_initializer.global_config.credentials
    )

    metrics_json = storage.Blob.from_string(
        uri=gcs_uri, client=storage_client
    ).download_as_text()

    # Sliced classification metrics case, format data
    if "slicedMetrics" in metrics_json:
        return _format_classification_metrics(metrics_json)
    # If classification metrics don't contain slices, use EvaluationClassificationMetric type
    if "auPrc" in metrics_json:
        metrics_response = _convert_metrics_dict_to_response_type(
            metrics_json=metrics_json,
            metric_type=EvaluationClassificationMetric,
        )
    # All other metric types
    else:
        metrics_response = _convert_metrics_dict_to_response_type(
            metrics_json=metrics_json,
            metric_type=EvaluationMetric,
        )
    return metrics_response


def _get_metrics_from_pipeline_task_details(
    pipeline_job: aiplatform.PipelineJob,
) -> Union[EvaluationMetric, EvaluationClassificationMetric]:
    """Gets the evaluation metrics from the PipelineJob TaskDetails.

    Args:
        pipeline_job (aiplatform.PipelineJob)
            The PipelineJob resource to get the metrics from

    Returns:
        A dictionary with the evaluation metrics
    """
    metrics = {}

    # TODO (b/292076101): this now uses a public pipelines contract, but still relies on task_details
    for task in pipeline_job.task_details:
        if task.task_name == pipeline_job.name:
            for output in task.outputs:
                for metric_name, metric_value in (
                    task.outputs[output].artifacts[0].metadata.items()
                ):
                    metrics[metric_name] = metric_value

            if "auPrc" in metrics:
                metrics_response = EvaluationClassificationMetric()
            else:
                metrics_response = EvaluationMetric()

            for metric, value in metrics.items():
                if hasattr(metrics_response, metric):
                    setattr(metrics_response, metric, value)
            return metrics_response


class _LanguageModelEvaluationJob:
    """Represents a model evaluation job for LLM models.

    These evaluation jobs are run as a Vertex Pipeline.
    """

    def __init__(
        self,
        pipeline_job: aiplatform.PipelineJob,
    ):
        self._pipeline_job = pipeline_job

    def result(
        self, *, only_summary_metrics: bool
    ) -> Union[EvaluationMetric, EvaluationClassificationMetric]:
        """Blocks on completion of the model evaluation PipelineJob and returns metrics."""

        self._pipeline_job.wait()

        if only_summary_metrics:
            return _get_metrics_from_pipeline_task_details(self._pipeline_job)
        else:
            gcs_uri = _get_gcs_uri_from_pipeline_task_details(self._pipeline_job)
            if gcs_uri:
                return _get_metrics_from_gcs_uri(gcs_uri)


class _EvaluatableLanguageModel:
    """Mixin class for LLMs that support model evaluation."""

    # TODO (b/282975912): convert training job specific args to a TrainingConfig
    def evaluate(
        self,
        *,
        task_spec: _EvaluationTaskSpec,
        only_summary_metrics: Optional[bool] = True,
        machine_type: Optional[str] = None,
    ) -> Union[
        EvaluationMetric,
        EvaluationClassificationMetric,
        EvaluationSlicedClassificationMetric,
    ]:
        """Runs model evaluation using the provided input and ground truth data.

        This creates an evaluation job and blocks until the job completes, about
        10 - 20 minutes.

        Example:
        ```
        model = TextGenerationModel.from_pretrained("text-bison@001")
        eval_metrics = model.evaluate(
            task_spec=EvaluationTextGenerationSpec(
                ground_truth_data="gs://my-bucket/ground-truth.jsonl",
            )
        )
        ```

        Args:
            task_spec (_EvaluationTaskSpec):
                Required. The configuration spec for your model evaluation job. Choose the spec corresponding
                with the evaluation task you are performing, one of: EvaluationClassificationSpec, EvaluationTextGenerationSpec,
                EvaluationTextSummarizationSpec, EvaluationQuestionAnsweringSpec.

                For example, a valid classification `task_spec` is:
                EvaluationTextClassificationSpec(
                    ground_truth_data=["gs://bucket/path/to/your/data.jsonl"],
                    class_names=["cheddar", "gouda", "camembert"],
                    target_column_name="cheese_type",
                )
            only_summary_metrics (bool):
                Optional. Setting this field to False only affects the metrics returned for text classification tasks.
                When False, text classification metrics will include additional sliced metrics fields, with metrics for
                each label slice in the data.
            machine_type (str):
                Optional. The type of the machine to run the evaluation job on. The default value is "e2-highmem-16". For
                tasks with a large evaluation dataset, a bigger machine type may be required.
                For more details about this input config, see
                https://cloud.google.com/vertex-ai/docs/training/configure-compute#machine-types.

        Returns:
            Union[EvaluationMetric, EvaluationClassificationMetric, List[EvaluationClassificationMetric]]
                The evaluation metrics from this evaluation job. When `only_summary_metrics=False` is passed
                and the evaluation task type is 'text-classification', the return type will be List[EvaluationClassificationMetric],
                where each value in the list is the metrics associated with a particular classification label.
        """

        model_info = _model_garden_models._get_model_info(
            self._model_id,
            schema_to_class_map={self._INSTANCE_SCHEMA_URI: type(self)},
        )
        model_name = _get_model_resource_name_and_validate(
            model_name=self._model_resource_name, model_info=model_info
        )

        # TODO(b/296402511): get service_account from aiplatform_initializer and pass it to the template here and to PipelineJob after cl/539823838 is submitted
        template_params = _populate_eval_template_params(
            task_spec=task_spec,
            model_name=model_name,
            machine_type=machine_type,
            network=aiplatform_initializer.global_config.network,
            encryption_spec_key_name=aiplatform_initializer.global_config.encryption_spec_key_name,
        )

        template_path = _get_template_url(task_spec.task_name)

        pipeline_job = aiplatform.PipelineJob(
            template_path=template_path,
            parameter_values=template_params,
            display_name=f"llm-eval-sdk-{aiplatform_utils.timestamped_unique_name()}",
        )
        pipeline_job.submit()

        eval_job = _LanguageModelEvaluationJob(pipeline_job=pipeline_job)

        _LOGGER.info(
            "Your evaluation job is running and will take 15-20 minutes to complete. Click on the PipelineJob link to view progress."
        )

        # NOTE: only_summary_metrics is passed because getting metrics from the artifact is faster than downloading from GCS
        # GCS is only needed for additional metrics for text-classification tasks
        return eval_job.result(only_summary_metrics=only_summary_metrics)

    def list_evaluation_metrics(
        self,
        *,
        task_name: Optional[str] = None,
        only_summary_metrics: Optional[bool] = True,
    ) -> List[Union[EvaluationMetric, EvaluationClassificationMetric]]:
        """Lists the evaluation metrics from all evaluation jobs run on this model.

        Args:
            task_name (str):
                Optional. The task name to return evaluation metrics for. If provided, this will only return evaluation
                metrics for tasks of the provided type. This matches the possible values passed to EvaluationTaskType.task_name,
                and must be one of 'text-generation', 'text-classification', 'summarization', or 'question-answering'.

        Returns:
            Dict[str, Any]
                The evaluation metrics from all evaluation jobs run on this model.

        """

        model_name = self._model_resource_name

        publisher_model_parts = model_garden_service_client.ModelGardenServiceClient.parse_publisher_model_path(
            "".join(model_name.rpartition("publishers")[1:])
        )

        if publisher_model_parts:
            model_id = publisher_model_parts["model"]
            model_name = f"publishers/google/models/{model_id}"

        filters = f'metadata.component_type.string_value={_EVALUATION_PIPELINE_COMPONENT_IDENTIFIER} AND metadata."input:model_name".string_value={model_name} AND (metadata."input:evaluation_task".string_value={_TEXT_GENERATION_TASK_NAME} OR metadata."input:evaluation_task".string_value={_SUMMARIZATION_TASK_NAME} OR metadata."input:evaluation_task".string_value={_QA_TASK_NAME} OR metadata."input:evaluation_task".string_value={_TEXT_CLASSIFICATION_TASK_NAME})'

        # NOTE: when task_name is appended to the filter the block of OR filters in `filters` above becomes a no-op
        if task_name:
            filters += f' AND metadata."input:evaluation_task".string_value={task_name}'

        filtered_pipeline_executions = aiplatform.Execution.list(
            filter=filters,
            project=aiplatform_initializer.global_config.project,
            location=aiplatform_initializer.global_config.location,
            credentials=aiplatform_initializer.global_config.credentials,
        )

        model_eval_metrics = []

        # TODO (b/285950380): improve performance of this method
        for pipeline_execution in filtered_pipeline_executions:
            if "pipeline_job_resource_name" not in pipeline_execution.metadata:
                continue

            pipeline_job_resource = aiplatform.PipelineJob.get(
                resource_name=pipeline_execution.metadata["pipeline_job_resource_name"]
            )
            eval_job_state = pipeline_job_resource._gca_resource.state

            if (
                eval_job_state
                != gca_pipeline_state.PipelineState.PIPELINE_STATE_SUCCEEDED
            ):
                continue

            metrics = None

            if only_summary_metrics:
                metrics = _get_metrics_from_pipeline_task_details(pipeline_job_resource)
            else:
                gcs_uri = _get_gcs_uri_from_pipeline_task_details(pipeline_job_resource)
                if gcs_uri:
                    metrics = _get_metrics_from_gcs_uri(gcs_uri)

            metrics.input_dataset_paths = pipeline_execution.metadata[
                "input:batch_predict_gcs_source_uris"
            ]
            metrics.task_name = pipeline_execution.metadata["input:evaluation_task"]

            model_eval_metrics.append(metrics)

        return model_eval_metrics
