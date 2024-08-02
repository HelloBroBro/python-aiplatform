# -*- coding: utf-8 -*-

# Copyright 2024 Google LLC
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

from typing import Callable, Optional, Union
import warnings

from vertexai.generative_models import _generative_models
from vertexai.preview.evaluation import constants
from vertexai.preview.evaluation.metrics import _base

_DEPRECATION_WARNING_MESSAGE = (
    "After google-cloud-aiplatform>1.63.0, using metric class"
    " `PairwiseQuestionAnsweringQuality` will result in an error. Please use"
    " string metric name `pairwise_question_answering_quality` or define a"
    " PairwiseMetric instead."
)


class PairwiseQuestionAnsweringQuality(_base.PairwiseMetric):
    """The Side-by-side(SxS) Pairwise Metric for Question Answering Quality."""

    _metric_name = constants.Metric.PAIRWISE_QUESTION_ANSWERING_QUALITY

    def __init__(
        self,
        *,
        baseline_model: Optional[
            Union[_generative_models.GenerativeModel, Callable[[str], str]]
        ] = None,
        use_reference: bool = False,
        version: Optional[int] = None
    ):
        warnings.warn(message=_DEPRECATION_WARNING_MESSAGE)
        super().__init__(
            metric=PairwiseQuestionAnsweringQuality._metric_name,
            baseline_model=baseline_model,
            use_reference=use_reference,
            version=version,
        )
