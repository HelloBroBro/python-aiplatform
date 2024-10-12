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

from google.auth.transport.requests import AuthorizedSession  # type: ignore
import json  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming
from google.api_core import gapic_v1

from google.protobuf import json_format
from google.api_core import operations_v1
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore

from requests import __version__ as requests_version
import dataclasses
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings


from google.cloud.aiplatform_v1beta1.types import tensorboard
from google.cloud.aiplatform_v1beta1.types import tensorboard_experiment
from google.cloud.aiplatform_v1beta1.types import (
    tensorboard_experiment as gca_tensorboard_experiment,
)
from google.cloud.aiplatform_v1beta1.types import tensorboard_run
from google.cloud.aiplatform_v1beta1.types import tensorboard_run as gca_tensorboard_run
from google.cloud.aiplatform_v1beta1.types import tensorboard_service
from google.cloud.aiplatform_v1beta1.types import tensorboard_time_series
from google.cloud.aiplatform_v1beta1.types import (
    tensorboard_time_series as gca_tensorboard_time_series,
)
from google.longrunning import operations_pb2  # type: ignore


from .rest_base import _BaseTensorboardServiceRestTransport
from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)


class TensorboardServiceRestInterceptor:
    """Interceptor for TensorboardService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the TensorboardServiceRestTransport.

    .. code-block:: python
        class MyCustomTensorboardServiceInterceptor(TensorboardServiceRestInterceptor):
            def pre_batch_create_tensorboard_runs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_tensorboard_runs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_tensorboard_time_series(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_tensorboard_time_series(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_read_tensorboard_time_series_data(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_read_tensorboard_time_series_data(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_tensorboard(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_tensorboard(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_tensorboard_experiment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_tensorboard_experiment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_tensorboard_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_tensorboard_run(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_tensorboard_time_series(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_tensorboard_time_series(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_tensorboard(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_tensorboard(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_tensorboard_experiment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_tensorboard_experiment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_tensorboard_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_tensorboard_run(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_tensorboard_time_series(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_tensorboard_time_series(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_tensorboard_time_series_data(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_tensorboard_time_series_data(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_tensorboard(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_tensorboard(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_tensorboard_experiment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_tensorboard_experiment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_tensorboard_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_tensorboard_run(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_tensorboard_time_series(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_tensorboard_time_series(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_tensorboard_experiments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_tensorboard_experiments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_tensorboard_runs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_tensorboard_runs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_tensorboards(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_tensorboards(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_tensorboard_time_series(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_tensorboard_time_series(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_read_tensorboard_blob_data(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_read_tensorboard_blob_data(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_read_tensorboard_size(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_read_tensorboard_size(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_read_tensorboard_time_series_data(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_read_tensorboard_time_series_data(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_read_tensorboard_usage(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_read_tensorboard_usage(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_tensorboard(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_tensorboard(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_tensorboard_experiment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_tensorboard_experiment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_tensorboard_run(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_tensorboard_run(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_tensorboard_time_series(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_tensorboard_time_series(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_write_tensorboard_experiment_data(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_write_tensorboard_experiment_data(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_write_tensorboard_run_data(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_write_tensorboard_run_data(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = TensorboardServiceRestTransport(interceptor=MyCustomTensorboardServiceInterceptor())
        client = TensorboardServiceClient(transport=transport)


    """

    def pre_batch_create_tensorboard_runs(
        self,
        request: tensorboard_service.BatchCreateTensorboardRunsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.BatchCreateTensorboardRunsRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for batch_create_tensorboard_runs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_batch_create_tensorboard_runs(
        self, response: tensorboard_service.BatchCreateTensorboardRunsResponse
    ) -> tensorboard_service.BatchCreateTensorboardRunsResponse:
        """Post-rpc interceptor for batch_create_tensorboard_runs

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_batch_create_tensorboard_time_series(
        self,
        request: tensorboard_service.BatchCreateTensorboardTimeSeriesRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.BatchCreateTensorboardTimeSeriesRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for batch_create_tensorboard_time_series

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_batch_create_tensorboard_time_series(
        self, response: tensorboard_service.BatchCreateTensorboardTimeSeriesResponse
    ) -> tensorboard_service.BatchCreateTensorboardTimeSeriesResponse:
        """Post-rpc interceptor for batch_create_tensorboard_time_series

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_batch_read_tensorboard_time_series_data(
        self,
        request: tensorboard_service.BatchReadTensorboardTimeSeriesDataRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.BatchReadTensorboardTimeSeriesDataRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for batch_read_tensorboard_time_series_data

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_batch_read_tensorboard_time_series_data(
        self, response: tensorboard_service.BatchReadTensorboardTimeSeriesDataResponse
    ) -> tensorboard_service.BatchReadTensorboardTimeSeriesDataResponse:
        """Post-rpc interceptor for batch_read_tensorboard_time_series_data

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_create_tensorboard(
        self,
        request: tensorboard_service.CreateTensorboardRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[tensorboard_service.CreateTensorboardRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_tensorboard

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_create_tensorboard(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_tensorboard

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_create_tensorboard_experiment(
        self,
        request: tensorboard_service.CreateTensorboardExperimentRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.CreateTensorboardExperimentRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for create_tensorboard_experiment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_create_tensorboard_experiment(
        self, response: gca_tensorboard_experiment.TensorboardExperiment
    ) -> gca_tensorboard_experiment.TensorboardExperiment:
        """Post-rpc interceptor for create_tensorboard_experiment

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_create_tensorboard_run(
        self,
        request: tensorboard_service.CreateTensorboardRunRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.CreateTensorboardRunRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for create_tensorboard_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_create_tensorboard_run(
        self, response: gca_tensorboard_run.TensorboardRun
    ) -> gca_tensorboard_run.TensorboardRun:
        """Post-rpc interceptor for create_tensorboard_run

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_create_tensorboard_time_series(
        self,
        request: tensorboard_service.CreateTensorboardTimeSeriesRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.CreateTensorboardTimeSeriesRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for create_tensorboard_time_series

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_create_tensorboard_time_series(
        self, response: gca_tensorboard_time_series.TensorboardTimeSeries
    ) -> gca_tensorboard_time_series.TensorboardTimeSeries:
        """Post-rpc interceptor for create_tensorboard_time_series

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_delete_tensorboard(
        self,
        request: tensorboard_service.DeleteTensorboardRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[tensorboard_service.DeleteTensorboardRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_tensorboard

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_delete_tensorboard(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_tensorboard

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_delete_tensorboard_experiment(
        self,
        request: tensorboard_service.DeleteTensorboardExperimentRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.DeleteTensorboardExperimentRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for delete_tensorboard_experiment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_delete_tensorboard_experiment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_tensorboard_experiment

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_delete_tensorboard_run(
        self,
        request: tensorboard_service.DeleteTensorboardRunRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.DeleteTensorboardRunRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for delete_tensorboard_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_delete_tensorboard_run(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_tensorboard_run

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_delete_tensorboard_time_series(
        self,
        request: tensorboard_service.DeleteTensorboardTimeSeriesRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.DeleteTensorboardTimeSeriesRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for delete_tensorboard_time_series

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_delete_tensorboard_time_series(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_tensorboard_time_series

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_export_tensorboard_time_series_data(
        self,
        request: tensorboard_service.ExportTensorboardTimeSeriesDataRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.ExportTensorboardTimeSeriesDataRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for export_tensorboard_time_series_data

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_export_tensorboard_time_series_data(
        self, response: tensorboard_service.ExportTensorboardTimeSeriesDataResponse
    ) -> tensorboard_service.ExportTensorboardTimeSeriesDataResponse:
        """Post-rpc interceptor for export_tensorboard_time_series_data

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_get_tensorboard(
        self,
        request: tensorboard_service.GetTensorboardRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[tensorboard_service.GetTensorboardRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_tensorboard

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_get_tensorboard(
        self, response: tensorboard.Tensorboard
    ) -> tensorboard.Tensorboard:
        """Post-rpc interceptor for get_tensorboard

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_get_tensorboard_experiment(
        self,
        request: tensorboard_service.GetTensorboardExperimentRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.GetTensorboardExperimentRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for get_tensorboard_experiment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_get_tensorboard_experiment(
        self, response: tensorboard_experiment.TensorboardExperiment
    ) -> tensorboard_experiment.TensorboardExperiment:
        """Post-rpc interceptor for get_tensorboard_experiment

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_get_tensorboard_run(
        self,
        request: tensorboard_service.GetTensorboardRunRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[tensorboard_service.GetTensorboardRunRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_tensorboard_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_get_tensorboard_run(
        self, response: tensorboard_run.TensorboardRun
    ) -> tensorboard_run.TensorboardRun:
        """Post-rpc interceptor for get_tensorboard_run

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_get_tensorboard_time_series(
        self,
        request: tensorboard_service.GetTensorboardTimeSeriesRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.GetTensorboardTimeSeriesRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for get_tensorboard_time_series

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_get_tensorboard_time_series(
        self, response: tensorboard_time_series.TensorboardTimeSeries
    ) -> tensorboard_time_series.TensorboardTimeSeries:
        """Post-rpc interceptor for get_tensorboard_time_series

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_list_tensorboard_experiments(
        self,
        request: tensorboard_service.ListTensorboardExperimentsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.ListTensorboardExperimentsRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for list_tensorboard_experiments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_list_tensorboard_experiments(
        self, response: tensorboard_service.ListTensorboardExperimentsResponse
    ) -> tensorboard_service.ListTensorboardExperimentsResponse:
        """Post-rpc interceptor for list_tensorboard_experiments

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_list_tensorboard_runs(
        self,
        request: tensorboard_service.ListTensorboardRunsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.ListTensorboardRunsRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for list_tensorboard_runs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_list_tensorboard_runs(
        self, response: tensorboard_service.ListTensorboardRunsResponse
    ) -> tensorboard_service.ListTensorboardRunsResponse:
        """Post-rpc interceptor for list_tensorboard_runs

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_list_tensorboards(
        self,
        request: tensorboard_service.ListTensorboardsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[tensorboard_service.ListTensorboardsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_tensorboards

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_list_tensorboards(
        self, response: tensorboard_service.ListTensorboardsResponse
    ) -> tensorboard_service.ListTensorboardsResponse:
        """Post-rpc interceptor for list_tensorboards

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_list_tensorboard_time_series(
        self,
        request: tensorboard_service.ListTensorboardTimeSeriesRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.ListTensorboardTimeSeriesRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for list_tensorboard_time_series

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_list_tensorboard_time_series(
        self, response: tensorboard_service.ListTensorboardTimeSeriesResponse
    ) -> tensorboard_service.ListTensorboardTimeSeriesResponse:
        """Post-rpc interceptor for list_tensorboard_time_series

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_read_tensorboard_blob_data(
        self,
        request: tensorboard_service.ReadTensorboardBlobDataRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.ReadTensorboardBlobDataRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for read_tensorboard_blob_data

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_read_tensorboard_blob_data(
        self, response: rest_streaming.ResponseIterator
    ) -> rest_streaming.ResponseIterator:
        """Post-rpc interceptor for read_tensorboard_blob_data

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_read_tensorboard_size(
        self,
        request: tensorboard_service.ReadTensorboardSizeRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.ReadTensorboardSizeRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for read_tensorboard_size

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_read_tensorboard_size(
        self, response: tensorboard_service.ReadTensorboardSizeResponse
    ) -> tensorboard_service.ReadTensorboardSizeResponse:
        """Post-rpc interceptor for read_tensorboard_size

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_read_tensorboard_time_series_data(
        self,
        request: tensorboard_service.ReadTensorboardTimeSeriesDataRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.ReadTensorboardTimeSeriesDataRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for read_tensorboard_time_series_data

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_read_tensorboard_time_series_data(
        self, response: tensorboard_service.ReadTensorboardTimeSeriesDataResponse
    ) -> tensorboard_service.ReadTensorboardTimeSeriesDataResponse:
        """Post-rpc interceptor for read_tensorboard_time_series_data

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_read_tensorboard_usage(
        self,
        request: tensorboard_service.ReadTensorboardUsageRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.ReadTensorboardUsageRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for read_tensorboard_usage

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_read_tensorboard_usage(
        self, response: tensorboard_service.ReadTensorboardUsageResponse
    ) -> tensorboard_service.ReadTensorboardUsageResponse:
        """Post-rpc interceptor for read_tensorboard_usage

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_update_tensorboard(
        self,
        request: tensorboard_service.UpdateTensorboardRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[tensorboard_service.UpdateTensorboardRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_tensorboard

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_update_tensorboard(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_tensorboard

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_update_tensorboard_experiment(
        self,
        request: tensorboard_service.UpdateTensorboardExperimentRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.UpdateTensorboardExperimentRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for update_tensorboard_experiment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_update_tensorboard_experiment(
        self, response: gca_tensorboard_experiment.TensorboardExperiment
    ) -> gca_tensorboard_experiment.TensorboardExperiment:
        """Post-rpc interceptor for update_tensorboard_experiment

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_update_tensorboard_run(
        self,
        request: tensorboard_service.UpdateTensorboardRunRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.UpdateTensorboardRunRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for update_tensorboard_run

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_update_tensorboard_run(
        self, response: gca_tensorboard_run.TensorboardRun
    ) -> gca_tensorboard_run.TensorboardRun:
        """Post-rpc interceptor for update_tensorboard_run

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_update_tensorboard_time_series(
        self,
        request: tensorboard_service.UpdateTensorboardTimeSeriesRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.UpdateTensorboardTimeSeriesRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for update_tensorboard_time_series

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_update_tensorboard_time_series(
        self, response: gca_tensorboard_time_series.TensorboardTimeSeries
    ) -> gca_tensorboard_time_series.TensorboardTimeSeries:
        """Post-rpc interceptor for update_tensorboard_time_series

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_write_tensorboard_experiment_data(
        self,
        request: tensorboard_service.WriteTensorboardExperimentDataRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.WriteTensorboardExperimentDataRequest,
        Sequence[Tuple[str, str]],
    ]:
        """Pre-rpc interceptor for write_tensorboard_experiment_data

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_write_tensorboard_experiment_data(
        self, response: tensorboard_service.WriteTensorboardExperimentDataResponse
    ) -> tensorboard_service.WriteTensorboardExperimentDataResponse:
        """Post-rpc interceptor for write_tensorboard_experiment_data

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_write_tensorboard_run_data(
        self,
        request: tensorboard_service.WriteTensorboardRunDataRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[
        tensorboard_service.WriteTensorboardRunDataRequest, Sequence[Tuple[str, str]]
    ]:
        """Pre-rpc interceptor for write_tensorboard_run_data

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_write_tensorboard_run_data(
        self, response: tensorboard_service.WriteTensorboardRunDataResponse
    ) -> tensorboard_service.WriteTensorboardRunDataResponse:
        """Post-rpc interceptor for write_tensorboard_run_data

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_get_location(
        self,
        request: locations_pb2.GetLocationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[locations_pb2.GetLocationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_list_locations(
        self,
        request: locations_pb2.ListLocationsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[locations_pb2.ListLocationsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_get_iam_policy(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_set_iam_policy(
        self,
        request: iam_policy_pb2.SetIamPolicyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_test_iam_permissions(
        self,
        request: iam_policy_pb2.TestIamPermissionsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[iam_policy_pb2.TestIamPermissionsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.CancelOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_delete_operation(
        self,
        request: operations_pb2.DeleteOperationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.GetOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_list_operations(
        self,
        request: operations_pb2.ListOperationsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.ListOperationsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response

    def pre_wait_operation(
        self,
        request: operations_pb2.WaitOperationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.WaitOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for wait_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TensorboardService server.
        """
        return request, metadata

    def post_wait_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for wait_operation

        Override in a subclass to manipulate the response
        after it is returned by the TensorboardService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class TensorboardServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: TensorboardServiceRestInterceptor


class TensorboardServiceRestTransport(_BaseTensorboardServiceRestTransport):
    """REST backend synchronous transport for TensorboardService.

    TensorboardService

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "aiplatform.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[TensorboardServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'aiplatform.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            url_scheme=url_scheme,
            api_audience=api_audience,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or TensorboardServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
                "google.longrunning.Operations.CancelOperation": [
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/agents/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/apps/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/endpoints/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/extensions/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/customJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tuningJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/indexes/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/migratableResources/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/notebookExecutionJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/notebookRuntimes/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/notebookRuntimeTemplates/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/persistentResources/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/schedules/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/specialistPools/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/agents/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/apps/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/edgeDevices/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/endpoints/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/exampleStores/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/extensionControllers/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/customJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/indexes/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/modelMonitors/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/migratableResources/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/models/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/notebookExecutionJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/notebookRuntimes/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/notebookRuntimeTemplates/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/persistentResources/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/trials/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/trainingPipelines/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/pipelineJobs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/schedules/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/specialistPools/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}:cancel",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/agents/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/apps/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/endpoints/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*}/operations",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/extensions/*}/operations",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/customJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/indexes/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/migratableResources/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/notebookExecutionJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/notebookRuntimes/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/notebookRuntimeTemplates/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/persistentResources/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/schedules/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/specialistPools/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/agents/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/apps/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/edgeDevices/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/endpoints/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/customJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/evaluationTasks/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/exampleStores/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/extensionControllers/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/indexes/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/modelMonitors/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/migratableResources/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/models/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/notebookExecutionJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/notebookRuntimes/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/notebookRuntimeTemplates/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/persistentResources/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/solvers/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/trials/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/trainingPipelines/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/pipelineJobs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/schedules/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/specialistPools/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/agents/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/apps/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/edgeDeploymentJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/endpoints/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/extensions/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/customJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tuningJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/indexes/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/migratableResources/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/notebookExecutionJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/notebookRuntimes/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/notebookRuntimeTemplates/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/persistentResources/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/schedules/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/specialistPools/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/agents/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/apps/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/edgeDevices/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/endpoints/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/evaluationTasks/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/exampleStores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/extensionControllers/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/customJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/indexes/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/modelMonitors/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/migratableResources/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/models/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/notebookExecutionJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/notebookRuntimes/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/notebookRuntimeTemplates/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/persistentResources/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/solvers/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/trials/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/trainingPipelines/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/pipelineJobs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/schedules/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/specialistPools/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/agents/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/apps/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/endpoints/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/extensions/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/customJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tuningJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/indexes/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/migratableResources/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/models/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/notebookExecutionJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/notebookRuntimes/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/notebookRuntimeTemplates/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/persistentResources/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/schedules/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/specialistPools/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}:wait",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}:wait",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/operations/*}:wait",
                    },
                    {
                        "method": "get",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}:wait",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/agents/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/apps/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/edgeDevices/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/endpoints/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/evaluationTasks/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/exampleStores/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/extensionControllers/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/customJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/dataLabelingJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/hyperparameterTuningJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/indexes/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/indexEndpoints/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/modelMonitors/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/migratableResources/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/models/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/notebookExecutionJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/notebookRuntimes/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/notebookRuntimeTemplates/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/persistentResources/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/reasoningEngines/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/solvers/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/studies/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/trials/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/trainingPipelines/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/pipelineJobs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/schedules/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/specialistPools/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/features/*}/operations",
                    },
                ],
                "google.longrunning.Operations.WaitOperation": [
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/agents/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/apps/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/endpoints/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/extensions/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/customJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tuningJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/indexes/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/migratableResources/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/notebookExecutionJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/notebookRuntimes/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/notebookRuntimeTemplates/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/persistentResources/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/schedules/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/specialistPools/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/agents/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/apps/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/edgeDevices/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/endpoints/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/evaluationTasks/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/exampleStores/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/extensionControllers/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/customJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/indexes/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/modelMonitors/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/migratableResources/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/models/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/notebookExecutionJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/notebookRuntimes/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/notebookRuntimeTemplates/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/persistentResources/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/trials/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/trainingPipelines/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/pipelineJobs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/schedules/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/specialistPools/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/operations/*}:wait",
                    },
                    {
                        "method": "post",
                        "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}:wait",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1beta1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _BatchCreateTensorboardRuns(
        _BaseTensorboardServiceRestTransport._BaseBatchCreateTensorboardRuns,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.BatchCreateTensorboardRuns")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.BatchCreateTensorboardRunsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> tensorboard_service.BatchCreateTensorboardRunsResponse:
            r"""Call the batch create tensorboard
            runs method over HTTP.

                Args:
                    request (~.tensorboard_service.BatchCreateTensorboardRunsRequest):
                        The request object. Request message for
                    [TensorboardService.BatchCreateTensorboardRuns][google.cloud.aiplatform.v1beta1.TensorboardService.BatchCreateTensorboardRuns].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.tensorboard_service.BatchCreateTensorboardRunsResponse:
                        Response message for
                    [TensorboardService.BatchCreateTensorboardRuns][google.cloud.aiplatform.v1beta1.TensorboardService.BatchCreateTensorboardRuns].

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseBatchCreateTensorboardRuns._get_http_options()
            )
            request, metadata = self._interceptor.pre_batch_create_tensorboard_runs(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseBatchCreateTensorboardRuns._get_transcoded_request(
                http_options, request
            )

            body = _BaseTensorboardServiceRestTransport._BaseBatchCreateTensorboardRuns._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseBatchCreateTensorboardRuns._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._BatchCreateTensorboardRuns._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = tensorboard_service.BatchCreateTensorboardRunsResponse()
            pb_resp = tensorboard_service.BatchCreateTensorboardRunsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_batch_create_tensorboard_runs(resp)
            return resp

    class _BatchCreateTensorboardTimeSeries(
        _BaseTensorboardServiceRestTransport._BaseBatchCreateTensorboardTimeSeries,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "TensorboardServiceRestTransport.BatchCreateTensorboardTimeSeries"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.BatchCreateTensorboardTimeSeriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> tensorboard_service.BatchCreateTensorboardTimeSeriesResponse:
            r"""Call the batch create tensorboard
            time series method over HTTP.

                Args:
                    request (~.tensorboard_service.BatchCreateTensorboardTimeSeriesRequest):
                        The request object. Request message for
                    [TensorboardService.BatchCreateTensorboardTimeSeries][google.cloud.aiplatform.v1beta1.TensorboardService.BatchCreateTensorboardTimeSeries].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.tensorboard_service.BatchCreateTensorboardTimeSeriesResponse:
                        Response message for
                    [TensorboardService.BatchCreateTensorboardTimeSeries][google.cloud.aiplatform.v1beta1.TensorboardService.BatchCreateTensorboardTimeSeries].

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseBatchCreateTensorboardTimeSeries._get_http_options()
            )
            (
                request,
                metadata,
            ) = self._interceptor.pre_batch_create_tensorboard_time_series(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseBatchCreateTensorboardTimeSeries._get_transcoded_request(
                http_options, request
            )

            body = _BaseTensorboardServiceRestTransport._BaseBatchCreateTensorboardTimeSeries._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseBatchCreateTensorboardTimeSeries._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._BatchCreateTensorboardTimeSeries._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = tensorboard_service.BatchCreateTensorboardTimeSeriesResponse()
            pb_resp = tensorboard_service.BatchCreateTensorboardTimeSeriesResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_batch_create_tensorboard_time_series(resp)
            return resp

    class _BatchReadTensorboardTimeSeriesData(
        _BaseTensorboardServiceRestTransport._BaseBatchReadTensorboardTimeSeriesData,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "TensorboardServiceRestTransport.BatchReadTensorboardTimeSeriesData"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.BatchReadTensorboardTimeSeriesDataRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> tensorboard_service.BatchReadTensorboardTimeSeriesDataResponse:
            r"""Call the batch read tensorboard
            time series data method over HTTP.

                Args:
                    request (~.tensorboard_service.BatchReadTensorboardTimeSeriesDataRequest):
                        The request object. Request message for
                    [TensorboardService.BatchReadTensorboardTimeSeriesData][google.cloud.aiplatform.v1beta1.TensorboardService.BatchReadTensorboardTimeSeriesData].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.tensorboard_service.BatchReadTensorboardTimeSeriesDataResponse:
                        Response message for
                    [TensorboardService.BatchReadTensorboardTimeSeriesData][google.cloud.aiplatform.v1beta1.TensorboardService.BatchReadTensorboardTimeSeriesData].

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseBatchReadTensorboardTimeSeriesData._get_http_options()
            )
            (
                request,
                metadata,
            ) = self._interceptor.pre_batch_read_tensorboard_time_series_data(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseBatchReadTensorboardTimeSeriesData._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseBatchReadTensorboardTimeSeriesData._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._BatchReadTensorboardTimeSeriesData._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = tensorboard_service.BatchReadTensorboardTimeSeriesDataResponse()
            pb_resp = tensorboard_service.BatchReadTensorboardTimeSeriesDataResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_batch_read_tensorboard_time_series_data(resp)
            return resp

    class _CreateTensorboard(
        _BaseTensorboardServiceRestTransport._BaseCreateTensorboard,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.CreateTensorboard")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.CreateTensorboardRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create tensorboard method over HTTP.

            Args:
                request (~.tensorboard_service.CreateTensorboardRequest):
                    The request object. Request message for
                [TensorboardService.CreateTensorboard][google.cloud.aiplatform.v1beta1.TensorboardService.CreateTensorboard].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseCreateTensorboard._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_tensorboard(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseCreateTensorboard._get_transcoded_request(
                http_options, request
            )

            body = _BaseTensorboardServiceRestTransport._BaseCreateTensorboard._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseCreateTensorboard._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._CreateTensorboard._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_tensorboard(resp)
            return resp

    class _CreateTensorboardExperiment(
        _BaseTensorboardServiceRestTransport._BaseCreateTensorboardExperiment,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.CreateTensorboardExperiment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.CreateTensorboardExperimentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> gca_tensorboard_experiment.TensorboardExperiment:
            r"""Call the create tensorboard
            experiment method over HTTP.

                Args:
                    request (~.tensorboard_service.CreateTensorboardExperimentRequest):
                        The request object. Request message for
                    [TensorboardService.CreateTensorboardExperiment][google.cloud.aiplatform.v1beta1.TensorboardService.CreateTensorboardExperiment].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.gca_tensorboard_experiment.TensorboardExperiment:
                        A TensorboardExperiment is a group of
                    TensorboardRuns, that are typically the
                    results of a training job run, in a
                    Tensorboard.

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseCreateTensorboardExperiment._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_tensorboard_experiment(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseCreateTensorboardExperiment._get_transcoded_request(
                http_options, request
            )

            body = _BaseTensorboardServiceRestTransport._BaseCreateTensorboardExperiment._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseCreateTensorboardExperiment._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._CreateTensorboardExperiment._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gca_tensorboard_experiment.TensorboardExperiment()
            pb_resp = gca_tensorboard_experiment.TensorboardExperiment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_tensorboard_experiment(resp)
            return resp

    class _CreateTensorboardRun(
        _BaseTensorboardServiceRestTransport._BaseCreateTensorboardRun,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.CreateTensorboardRun")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.CreateTensorboardRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> gca_tensorboard_run.TensorboardRun:
            r"""Call the create tensorboard run method over HTTP.

            Args:
                request (~.tensorboard_service.CreateTensorboardRunRequest):
                    The request object. Request message for
                [TensorboardService.CreateTensorboardRun][google.cloud.aiplatform.v1beta1.TensorboardService.CreateTensorboardRun].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.gca_tensorboard_run.TensorboardRun:
                    TensorboardRun maps to a specific
                execution of a training job with a given
                set of hyperparameter values, model
                definition, dataset, etc

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseCreateTensorboardRun._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_tensorboard_run(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseCreateTensorboardRun._get_transcoded_request(
                http_options, request
            )

            body = _BaseTensorboardServiceRestTransport._BaseCreateTensorboardRun._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseCreateTensorboardRun._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = (
                TensorboardServiceRestTransport._CreateTensorboardRun._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gca_tensorboard_run.TensorboardRun()
            pb_resp = gca_tensorboard_run.TensorboardRun.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_tensorboard_run(resp)
            return resp

    class _CreateTensorboardTimeSeries(
        _BaseTensorboardServiceRestTransport._BaseCreateTensorboardTimeSeries,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.CreateTensorboardTimeSeries")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.CreateTensorboardTimeSeriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> gca_tensorboard_time_series.TensorboardTimeSeries:
            r"""Call the create tensorboard time
            series method over HTTP.

                Args:
                    request (~.tensorboard_service.CreateTensorboardTimeSeriesRequest):
                        The request object. Request message for
                    [TensorboardService.CreateTensorboardTimeSeries][google.cloud.aiplatform.v1beta1.TensorboardService.CreateTensorboardTimeSeries].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.gca_tensorboard_time_series.TensorboardTimeSeries:
                        TensorboardTimeSeries maps to times
                    series produced in training runs

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseCreateTensorboardTimeSeries._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_tensorboard_time_series(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseCreateTensorboardTimeSeries._get_transcoded_request(
                http_options, request
            )

            body = _BaseTensorboardServiceRestTransport._BaseCreateTensorboardTimeSeries._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseCreateTensorboardTimeSeries._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._CreateTensorboardTimeSeries._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gca_tensorboard_time_series.TensorboardTimeSeries()
            pb_resp = gca_tensorboard_time_series.TensorboardTimeSeries.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_tensorboard_time_series(resp)
            return resp

    class _DeleteTensorboard(
        _BaseTensorboardServiceRestTransport._BaseDeleteTensorboard,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.DeleteTensorboard")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.DeleteTensorboardRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete tensorboard method over HTTP.

            Args:
                request (~.tensorboard_service.DeleteTensorboardRequest):
                    The request object. Request message for
                [TensorboardService.DeleteTensorboard][google.cloud.aiplatform.v1beta1.TensorboardService.DeleteTensorboard].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseDeleteTensorboard._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_tensorboard(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseDeleteTensorboard._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseDeleteTensorboard._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._DeleteTensorboard._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_tensorboard(resp)
            return resp

    class _DeleteTensorboardExperiment(
        _BaseTensorboardServiceRestTransport._BaseDeleteTensorboardExperiment,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.DeleteTensorboardExperiment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.DeleteTensorboardExperimentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete tensorboard
            experiment method over HTTP.

                Args:
                    request (~.tensorboard_service.DeleteTensorboardExperimentRequest):
                        The request object. Request message for
                    [TensorboardService.DeleteTensorboardExperiment][google.cloud.aiplatform.v1beta1.TensorboardService.DeleteTensorboardExperiment].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.operations_pb2.Operation:
                        This resource represents a
                    long-running operation that is the
                    result of a network API call.

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseDeleteTensorboardExperiment._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_tensorboard_experiment(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseDeleteTensorboardExperiment._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseDeleteTensorboardExperiment._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._DeleteTensorboardExperiment._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_tensorboard_experiment(resp)
            return resp

    class _DeleteTensorboardRun(
        _BaseTensorboardServiceRestTransport._BaseDeleteTensorboardRun,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.DeleteTensorboardRun")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.DeleteTensorboardRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete tensorboard run method over HTTP.

            Args:
                request (~.tensorboard_service.DeleteTensorboardRunRequest):
                    The request object. Request message for
                [TensorboardService.DeleteTensorboardRun][google.cloud.aiplatform.v1beta1.TensorboardService.DeleteTensorboardRun].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseDeleteTensorboardRun._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_tensorboard_run(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseDeleteTensorboardRun._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseDeleteTensorboardRun._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = (
                TensorboardServiceRestTransport._DeleteTensorboardRun._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_tensorboard_run(resp)
            return resp

    class _DeleteTensorboardTimeSeries(
        _BaseTensorboardServiceRestTransport._BaseDeleteTensorboardTimeSeries,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.DeleteTensorboardTimeSeries")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.DeleteTensorboardTimeSeriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete tensorboard time
            series method over HTTP.

                Args:
                    request (~.tensorboard_service.DeleteTensorboardTimeSeriesRequest):
                        The request object. Request message for
                    [TensorboardService.DeleteTensorboardTimeSeries][google.cloud.aiplatform.v1beta1.TensorboardService.DeleteTensorboardTimeSeries].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.operations_pb2.Operation:
                        This resource represents a
                    long-running operation that is the
                    result of a network API call.

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseDeleteTensorboardTimeSeries._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_tensorboard_time_series(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseDeleteTensorboardTimeSeries._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseDeleteTensorboardTimeSeries._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._DeleteTensorboardTimeSeries._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_tensorboard_time_series(resp)
            return resp

    class _ExportTensorboardTimeSeriesData(
        _BaseTensorboardServiceRestTransport._BaseExportTensorboardTimeSeriesData,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "TensorboardServiceRestTransport.ExportTensorboardTimeSeriesData"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.ExportTensorboardTimeSeriesDataRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> tensorboard_service.ExportTensorboardTimeSeriesDataResponse:
            r"""Call the export tensorboard time
            series data method over HTTP.

                Args:
                    request (~.tensorboard_service.ExportTensorboardTimeSeriesDataRequest):
                        The request object. Request message for
                    [TensorboardService.ExportTensorboardTimeSeriesData][google.cloud.aiplatform.v1beta1.TensorboardService.ExportTensorboardTimeSeriesData].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.tensorboard_service.ExportTensorboardTimeSeriesDataResponse:
                        Response message for
                    [TensorboardService.ExportTensorboardTimeSeriesData][google.cloud.aiplatform.v1beta1.TensorboardService.ExportTensorboardTimeSeriesData].

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseExportTensorboardTimeSeriesData._get_http_options()
            )
            (
                request,
                metadata,
            ) = self._interceptor.pre_export_tensorboard_time_series_data(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseExportTensorboardTimeSeriesData._get_transcoded_request(
                http_options, request
            )

            body = _BaseTensorboardServiceRestTransport._BaseExportTensorboardTimeSeriesData._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseExportTensorboardTimeSeriesData._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._ExportTensorboardTimeSeriesData._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = tensorboard_service.ExportTensorboardTimeSeriesDataResponse()
            pb_resp = tensorboard_service.ExportTensorboardTimeSeriesDataResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_export_tensorboard_time_series_data(resp)
            return resp

    class _GetTensorboard(
        _BaseTensorboardServiceRestTransport._BaseGetTensorboard,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.GetTensorboard")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.GetTensorboardRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> tensorboard.Tensorboard:
            r"""Call the get tensorboard method over HTTP.

            Args:
                request (~.tensorboard_service.GetTensorboardRequest):
                    The request object. Request message for
                [TensorboardService.GetTensorboard][google.cloud.aiplatform.v1beta1.TensorboardService.GetTensorboard].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.tensorboard.Tensorboard:
                    Tensorboard is a physical database
                that stores users' training metrics. A
                default Tensorboard is provided in each
                region of a Google Cloud project. If
                needed users can also create extra
                Tensorboards in their projects.

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseGetTensorboard._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_tensorboard(request, metadata)
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseGetTensorboard._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseGetTensorboard._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._GetTensorboard._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = tensorboard.Tensorboard()
            pb_resp = tensorboard.Tensorboard.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_tensorboard(resp)
            return resp

    class _GetTensorboardExperiment(
        _BaseTensorboardServiceRestTransport._BaseGetTensorboardExperiment,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.GetTensorboardExperiment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.GetTensorboardExperimentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> tensorboard_experiment.TensorboardExperiment:
            r"""Call the get tensorboard
            experiment method over HTTP.

                Args:
                    request (~.tensorboard_service.GetTensorboardExperimentRequest):
                        The request object. Request message for
                    [TensorboardService.GetTensorboardExperiment][google.cloud.aiplatform.v1beta1.TensorboardService.GetTensorboardExperiment].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.tensorboard_experiment.TensorboardExperiment:
                        A TensorboardExperiment is a group of
                    TensorboardRuns, that are typically the
                    results of a training job run, in a
                    Tensorboard.

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseGetTensorboardExperiment._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_tensorboard_experiment(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseGetTensorboardExperiment._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseGetTensorboardExperiment._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = (
                TensorboardServiceRestTransport._GetTensorboardExperiment._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = tensorboard_experiment.TensorboardExperiment()
            pb_resp = tensorboard_experiment.TensorboardExperiment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_tensorboard_experiment(resp)
            return resp

    class _GetTensorboardRun(
        _BaseTensorboardServiceRestTransport._BaseGetTensorboardRun,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.GetTensorboardRun")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.GetTensorboardRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> tensorboard_run.TensorboardRun:
            r"""Call the get tensorboard run method over HTTP.

            Args:
                request (~.tensorboard_service.GetTensorboardRunRequest):
                    The request object. Request message for
                [TensorboardService.GetTensorboardRun][google.cloud.aiplatform.v1beta1.TensorboardService.GetTensorboardRun].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.tensorboard_run.TensorboardRun:
                    TensorboardRun maps to a specific
                execution of a training job with a given
                set of hyperparameter values, model
                definition, dataset, etc

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseGetTensorboardRun._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_tensorboard_run(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseGetTensorboardRun._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseGetTensorboardRun._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._GetTensorboardRun._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = tensorboard_run.TensorboardRun()
            pb_resp = tensorboard_run.TensorboardRun.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_tensorboard_run(resp)
            return resp

    class _GetTensorboardTimeSeries(
        _BaseTensorboardServiceRestTransport._BaseGetTensorboardTimeSeries,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.GetTensorboardTimeSeries")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.GetTensorboardTimeSeriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> tensorboard_time_series.TensorboardTimeSeries:
            r"""Call the get tensorboard time
            series method over HTTP.

                Args:
                    request (~.tensorboard_service.GetTensorboardTimeSeriesRequest):
                        The request object. Request message for
                    [TensorboardService.GetTensorboardTimeSeries][google.cloud.aiplatform.v1beta1.TensorboardService.GetTensorboardTimeSeries].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.tensorboard_time_series.TensorboardTimeSeries:
                        TensorboardTimeSeries maps to times
                    series produced in training runs

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseGetTensorboardTimeSeries._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_tensorboard_time_series(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseGetTensorboardTimeSeries._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseGetTensorboardTimeSeries._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = (
                TensorboardServiceRestTransport._GetTensorboardTimeSeries._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = tensorboard_time_series.TensorboardTimeSeries()
            pb_resp = tensorboard_time_series.TensorboardTimeSeries.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_tensorboard_time_series(resp)
            return resp

    class _ListTensorboardExperiments(
        _BaseTensorboardServiceRestTransport._BaseListTensorboardExperiments,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.ListTensorboardExperiments")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.ListTensorboardExperimentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> tensorboard_service.ListTensorboardExperimentsResponse:
            r"""Call the list tensorboard
            experiments method over HTTP.

                Args:
                    request (~.tensorboard_service.ListTensorboardExperimentsRequest):
                        The request object. Request message for
                    [TensorboardService.ListTensorboardExperiments][google.cloud.aiplatform.v1beta1.TensorboardService.ListTensorboardExperiments].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.tensorboard_service.ListTensorboardExperimentsResponse:
                        Response message for
                    [TensorboardService.ListTensorboardExperiments][google.cloud.aiplatform.v1beta1.TensorboardService.ListTensorboardExperiments].

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseListTensorboardExperiments._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_tensorboard_experiments(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseListTensorboardExperiments._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseListTensorboardExperiments._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._ListTensorboardExperiments._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = tensorboard_service.ListTensorboardExperimentsResponse()
            pb_resp = tensorboard_service.ListTensorboardExperimentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_tensorboard_experiments(resp)
            return resp

    class _ListTensorboardRuns(
        _BaseTensorboardServiceRestTransport._BaseListTensorboardRuns,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.ListTensorboardRuns")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.ListTensorboardRunsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> tensorboard_service.ListTensorboardRunsResponse:
            r"""Call the list tensorboard runs method over HTTP.

            Args:
                request (~.tensorboard_service.ListTensorboardRunsRequest):
                    The request object. Request message for
                [TensorboardService.ListTensorboardRuns][google.cloud.aiplatform.v1beta1.TensorboardService.ListTensorboardRuns].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.tensorboard_service.ListTensorboardRunsResponse:
                    Response message for
                [TensorboardService.ListTensorboardRuns][google.cloud.aiplatform.v1beta1.TensorboardService.ListTensorboardRuns].

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseListTensorboardRuns._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_tensorboard_runs(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseListTensorboardRuns._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseListTensorboardRuns._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = (
                TensorboardServiceRestTransport._ListTensorboardRuns._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = tensorboard_service.ListTensorboardRunsResponse()
            pb_resp = tensorboard_service.ListTensorboardRunsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_tensorboard_runs(resp)
            return resp

    class _ListTensorboards(
        _BaseTensorboardServiceRestTransport._BaseListTensorboards,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.ListTensorboards")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.ListTensorboardsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> tensorboard_service.ListTensorboardsResponse:
            r"""Call the list tensorboards method over HTTP.

            Args:
                request (~.tensorboard_service.ListTensorboardsRequest):
                    The request object. Request message for
                [TensorboardService.ListTensorboards][google.cloud.aiplatform.v1beta1.TensorboardService.ListTensorboards].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.tensorboard_service.ListTensorboardsResponse:
                    Response message for
                [TensorboardService.ListTensorboards][google.cloud.aiplatform.v1beta1.TensorboardService.ListTensorboards].

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseListTensorboards._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_tensorboards(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseListTensorboards._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseListTensorboards._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._ListTensorboards._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = tensorboard_service.ListTensorboardsResponse()
            pb_resp = tensorboard_service.ListTensorboardsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_tensorboards(resp)
            return resp

    class _ListTensorboardTimeSeries(
        _BaseTensorboardServiceRestTransport._BaseListTensorboardTimeSeries,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.ListTensorboardTimeSeries")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.ListTensorboardTimeSeriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> tensorboard_service.ListTensorboardTimeSeriesResponse:
            r"""Call the list tensorboard time
            series method over HTTP.

                Args:
                    request (~.tensorboard_service.ListTensorboardTimeSeriesRequest):
                        The request object. Request message for
                    [TensorboardService.ListTensorboardTimeSeries][google.cloud.aiplatform.v1beta1.TensorboardService.ListTensorboardTimeSeries].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.tensorboard_service.ListTensorboardTimeSeriesResponse:
                        Response message for
                    [TensorboardService.ListTensorboardTimeSeries][google.cloud.aiplatform.v1beta1.TensorboardService.ListTensorboardTimeSeries].

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseListTensorboardTimeSeries._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_tensorboard_time_series(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseListTensorboardTimeSeries._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseListTensorboardTimeSeries._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._ListTensorboardTimeSeries._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = tensorboard_service.ListTensorboardTimeSeriesResponse()
            pb_resp = tensorboard_service.ListTensorboardTimeSeriesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_tensorboard_time_series(resp)
            return resp

    class _ReadTensorboardBlobData(
        _BaseTensorboardServiceRestTransport._BaseReadTensorboardBlobData,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.ReadTensorboardBlobData")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                stream=True,
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.ReadTensorboardBlobDataRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> rest_streaming.ResponseIterator:
            r"""Call the read tensorboard blob
            data method over HTTP.

                Args:
                    request (~.tensorboard_service.ReadTensorboardBlobDataRequest):
                        The request object. Request message for
                    [TensorboardService.ReadTensorboardBlobData][google.cloud.aiplatform.v1beta1.TensorboardService.ReadTensorboardBlobData].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.tensorboard_service.ReadTensorboardBlobDataResponse:
                        Response message for
                    [TensorboardService.ReadTensorboardBlobData][google.cloud.aiplatform.v1beta1.TensorboardService.ReadTensorboardBlobData].

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseReadTensorboardBlobData._get_http_options()
            )
            request, metadata = self._interceptor.pre_read_tensorboard_blob_data(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseReadTensorboardBlobData._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseReadTensorboardBlobData._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = (
                TensorboardServiceRestTransport._ReadTensorboardBlobData._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = rest_streaming.ResponseIterator(
                response, tensorboard_service.ReadTensorboardBlobDataResponse
            )
            resp = self._interceptor.post_read_tensorboard_blob_data(resp)
            return resp

    class _ReadTensorboardSize(
        _BaseTensorboardServiceRestTransport._BaseReadTensorboardSize,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.ReadTensorboardSize")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.ReadTensorboardSizeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> tensorboard_service.ReadTensorboardSizeResponse:
            r"""Call the read tensorboard size method over HTTP.

            Args:
                request (~.tensorboard_service.ReadTensorboardSizeRequest):
                    The request object. Request message for
                [TensorboardService.ReadTensorboardSize][google.cloud.aiplatform.v1beta1.TensorboardService.ReadTensorboardSize].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.tensorboard_service.ReadTensorboardSizeResponse:
                    Response message for
                [TensorboardService.ReadTensorboardSize][google.cloud.aiplatform.v1beta1.TensorboardService.ReadTensorboardSize].

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseReadTensorboardSize._get_http_options()
            )
            request, metadata = self._interceptor.pre_read_tensorboard_size(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseReadTensorboardSize._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseReadTensorboardSize._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = (
                TensorboardServiceRestTransport._ReadTensorboardSize._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = tensorboard_service.ReadTensorboardSizeResponse()
            pb_resp = tensorboard_service.ReadTensorboardSizeResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_read_tensorboard_size(resp)
            return resp

    class _ReadTensorboardTimeSeriesData(
        _BaseTensorboardServiceRestTransport._BaseReadTensorboardTimeSeriesData,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.ReadTensorboardTimeSeriesData")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.ReadTensorboardTimeSeriesDataRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> tensorboard_service.ReadTensorboardTimeSeriesDataResponse:
            r"""Call the read tensorboard time
            series data method over HTTP.

                Args:
                    request (~.tensorboard_service.ReadTensorboardTimeSeriesDataRequest):
                        The request object. Request message for
                    [TensorboardService.ReadTensorboardTimeSeriesData][google.cloud.aiplatform.v1beta1.TensorboardService.ReadTensorboardTimeSeriesData].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.tensorboard_service.ReadTensorboardTimeSeriesDataResponse:
                        Response message for
                    [TensorboardService.ReadTensorboardTimeSeriesData][google.cloud.aiplatform.v1beta1.TensorboardService.ReadTensorboardTimeSeriesData].

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseReadTensorboardTimeSeriesData._get_http_options()
            )
            request, metadata = self._interceptor.pre_read_tensorboard_time_series_data(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseReadTensorboardTimeSeriesData._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseReadTensorboardTimeSeriesData._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._ReadTensorboardTimeSeriesData._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = tensorboard_service.ReadTensorboardTimeSeriesDataResponse()
            pb_resp = tensorboard_service.ReadTensorboardTimeSeriesDataResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_read_tensorboard_time_series_data(resp)
            return resp

    class _ReadTensorboardUsage(
        _BaseTensorboardServiceRestTransport._BaseReadTensorboardUsage,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.ReadTensorboardUsage")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.ReadTensorboardUsageRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> tensorboard_service.ReadTensorboardUsageResponse:
            r"""Call the read tensorboard usage method over HTTP.

            Args:
                request (~.tensorboard_service.ReadTensorboardUsageRequest):
                    The request object. Request message for
                [TensorboardService.ReadTensorboardUsage][google.cloud.aiplatform.v1beta1.TensorboardService.ReadTensorboardUsage].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.tensorboard_service.ReadTensorboardUsageResponse:
                    Response message for
                [TensorboardService.ReadTensorboardUsage][google.cloud.aiplatform.v1beta1.TensorboardService.ReadTensorboardUsage].

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseReadTensorboardUsage._get_http_options()
            )
            request, metadata = self._interceptor.pre_read_tensorboard_usage(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseReadTensorboardUsage._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseReadTensorboardUsage._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = (
                TensorboardServiceRestTransport._ReadTensorboardUsage._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = tensorboard_service.ReadTensorboardUsageResponse()
            pb_resp = tensorboard_service.ReadTensorboardUsageResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_read_tensorboard_usage(resp)
            return resp

    class _UpdateTensorboard(
        _BaseTensorboardServiceRestTransport._BaseUpdateTensorboard,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.UpdateTensorboard")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.UpdateTensorboardRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update tensorboard method over HTTP.

            Args:
                request (~.tensorboard_service.UpdateTensorboardRequest):
                    The request object. Request message for
                [TensorboardService.UpdateTensorboard][google.cloud.aiplatform.v1beta1.TensorboardService.UpdateTensorboard].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseUpdateTensorboard._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_tensorboard(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseUpdateTensorboard._get_transcoded_request(
                http_options, request
            )

            body = _BaseTensorboardServiceRestTransport._BaseUpdateTensorboard._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseUpdateTensorboard._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._UpdateTensorboard._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_tensorboard(resp)
            return resp

    class _UpdateTensorboardExperiment(
        _BaseTensorboardServiceRestTransport._BaseUpdateTensorboardExperiment,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.UpdateTensorboardExperiment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.UpdateTensorboardExperimentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> gca_tensorboard_experiment.TensorboardExperiment:
            r"""Call the update tensorboard
            experiment method over HTTP.

                Args:
                    request (~.tensorboard_service.UpdateTensorboardExperimentRequest):
                        The request object. Request message for
                    [TensorboardService.UpdateTensorboardExperiment][google.cloud.aiplatform.v1beta1.TensorboardService.UpdateTensorboardExperiment].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.gca_tensorboard_experiment.TensorboardExperiment:
                        A TensorboardExperiment is a group of
                    TensorboardRuns, that are typically the
                    results of a training job run, in a
                    Tensorboard.

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseUpdateTensorboardExperiment._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_tensorboard_experiment(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseUpdateTensorboardExperiment._get_transcoded_request(
                http_options, request
            )

            body = _BaseTensorboardServiceRestTransport._BaseUpdateTensorboardExperiment._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseUpdateTensorboardExperiment._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._UpdateTensorboardExperiment._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gca_tensorboard_experiment.TensorboardExperiment()
            pb_resp = gca_tensorboard_experiment.TensorboardExperiment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_tensorboard_experiment(resp)
            return resp

    class _UpdateTensorboardRun(
        _BaseTensorboardServiceRestTransport._BaseUpdateTensorboardRun,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.UpdateTensorboardRun")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.UpdateTensorboardRunRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> gca_tensorboard_run.TensorboardRun:
            r"""Call the update tensorboard run method over HTTP.

            Args:
                request (~.tensorboard_service.UpdateTensorboardRunRequest):
                    The request object. Request message for
                [TensorboardService.UpdateTensorboardRun][google.cloud.aiplatform.v1beta1.TensorboardService.UpdateTensorboardRun].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.gca_tensorboard_run.TensorboardRun:
                    TensorboardRun maps to a specific
                execution of a training job with a given
                set of hyperparameter values, model
                definition, dataset, etc

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseUpdateTensorboardRun._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_tensorboard_run(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseUpdateTensorboardRun._get_transcoded_request(
                http_options, request
            )

            body = _BaseTensorboardServiceRestTransport._BaseUpdateTensorboardRun._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseUpdateTensorboardRun._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = (
                TensorboardServiceRestTransport._UpdateTensorboardRun._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gca_tensorboard_run.TensorboardRun()
            pb_resp = gca_tensorboard_run.TensorboardRun.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_tensorboard_run(resp)
            return resp

    class _UpdateTensorboardTimeSeries(
        _BaseTensorboardServiceRestTransport._BaseUpdateTensorboardTimeSeries,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.UpdateTensorboardTimeSeries")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.UpdateTensorboardTimeSeriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> gca_tensorboard_time_series.TensorboardTimeSeries:
            r"""Call the update tensorboard time
            series method over HTTP.

                Args:
                    request (~.tensorboard_service.UpdateTensorboardTimeSeriesRequest):
                        The request object. Request message for
                    [TensorboardService.UpdateTensorboardTimeSeries][google.cloud.aiplatform.v1beta1.TensorboardService.UpdateTensorboardTimeSeries].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.gca_tensorboard_time_series.TensorboardTimeSeries:
                        TensorboardTimeSeries maps to times
                    series produced in training runs

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseUpdateTensorboardTimeSeries._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_tensorboard_time_series(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseUpdateTensorboardTimeSeries._get_transcoded_request(
                http_options, request
            )

            body = _BaseTensorboardServiceRestTransport._BaseUpdateTensorboardTimeSeries._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseUpdateTensorboardTimeSeries._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._UpdateTensorboardTimeSeries._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gca_tensorboard_time_series.TensorboardTimeSeries()
            pb_resp = gca_tensorboard_time_series.TensorboardTimeSeries.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_tensorboard_time_series(resp)
            return resp

    class _WriteTensorboardExperimentData(
        _BaseTensorboardServiceRestTransport._BaseWriteTensorboardExperimentData,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "TensorboardServiceRestTransport.WriteTensorboardExperimentData"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.WriteTensorboardExperimentDataRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> tensorboard_service.WriteTensorboardExperimentDataResponse:
            r"""Call the write tensorboard
            experiment data method over HTTP.

                Args:
                    request (~.tensorboard_service.WriteTensorboardExperimentDataRequest):
                        The request object. Request message for
                    [TensorboardService.WriteTensorboardExperimentData][google.cloud.aiplatform.v1beta1.TensorboardService.WriteTensorboardExperimentData].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.tensorboard_service.WriteTensorboardExperimentDataResponse:
                        Response message for
                    [TensorboardService.WriteTensorboardExperimentData][google.cloud.aiplatform.v1beta1.TensorboardService.WriteTensorboardExperimentData].

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseWriteTensorboardExperimentData._get_http_options()
            )
            request, metadata = self._interceptor.pre_write_tensorboard_experiment_data(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseWriteTensorboardExperimentData._get_transcoded_request(
                http_options, request
            )

            body = _BaseTensorboardServiceRestTransport._BaseWriteTensorboardExperimentData._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseWriteTensorboardExperimentData._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._WriteTensorboardExperimentData._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = tensorboard_service.WriteTensorboardExperimentDataResponse()
            pb_resp = tensorboard_service.WriteTensorboardExperimentDataResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_write_tensorboard_experiment_data(resp)
            return resp

    class _WriteTensorboardRunData(
        _BaseTensorboardServiceRestTransport._BaseWriteTensorboardRunData,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.WriteTensorboardRunData")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: tensorboard_service.WriteTensorboardRunDataRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> tensorboard_service.WriteTensorboardRunDataResponse:
            r"""Call the write tensorboard run
            data method over HTTP.

                Args:
                    request (~.tensorboard_service.WriteTensorboardRunDataRequest):
                        The request object. Request message for
                    [TensorboardService.WriteTensorboardRunData][google.cloud.aiplatform.v1beta1.TensorboardService.WriteTensorboardRunData].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, str]]): Strings which should be
                        sent along with the request as metadata.

                Returns:
                    ~.tensorboard_service.WriteTensorboardRunDataResponse:
                        Response message for
                    [TensorboardService.WriteTensorboardRunData][google.cloud.aiplatform.v1beta1.TensorboardService.WriteTensorboardRunData].

            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseWriteTensorboardRunData._get_http_options()
            )
            request, metadata = self._interceptor.pre_write_tensorboard_run_data(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseWriteTensorboardRunData._get_transcoded_request(
                http_options, request
            )

            body = _BaseTensorboardServiceRestTransport._BaseWriteTensorboardRunData._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseWriteTensorboardRunData._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = (
                TensorboardServiceRestTransport._WriteTensorboardRunData._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = tensorboard_service.WriteTensorboardRunDataResponse()
            pb_resp = tensorboard_service.WriteTensorboardRunDataResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_write_tensorboard_run_data(resp)
            return resp

    @property
    def batch_create_tensorboard_runs(
        self,
    ) -> Callable[
        [tensorboard_service.BatchCreateTensorboardRunsRequest],
        tensorboard_service.BatchCreateTensorboardRunsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateTensorboardRuns(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_create_tensorboard_time_series(
        self,
    ) -> Callable[
        [tensorboard_service.BatchCreateTensorboardTimeSeriesRequest],
        tensorboard_service.BatchCreateTensorboardTimeSeriesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateTensorboardTimeSeries(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_read_tensorboard_time_series_data(
        self,
    ) -> Callable[
        [tensorboard_service.BatchReadTensorboardTimeSeriesDataRequest],
        tensorboard_service.BatchReadTensorboardTimeSeriesDataResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchReadTensorboardTimeSeriesData(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_tensorboard(
        self,
    ) -> Callable[
        [tensorboard_service.CreateTensorboardRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTensorboard(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_tensorboard_experiment(
        self,
    ) -> Callable[
        [tensorboard_service.CreateTensorboardExperimentRequest],
        gca_tensorboard_experiment.TensorboardExperiment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTensorboardExperiment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_tensorboard_run(
        self,
    ) -> Callable[
        [tensorboard_service.CreateTensorboardRunRequest],
        gca_tensorboard_run.TensorboardRun,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTensorboardRun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_tensorboard_time_series(
        self,
    ) -> Callable[
        [tensorboard_service.CreateTensorboardTimeSeriesRequest],
        gca_tensorboard_time_series.TensorboardTimeSeries,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTensorboardTimeSeries(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_tensorboard(
        self,
    ) -> Callable[
        [tensorboard_service.DeleteTensorboardRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTensorboard(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_tensorboard_experiment(
        self,
    ) -> Callable[
        [tensorboard_service.DeleteTensorboardExperimentRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTensorboardExperiment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_tensorboard_run(
        self,
    ) -> Callable[
        [tensorboard_service.DeleteTensorboardRunRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTensorboardRun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_tensorboard_time_series(
        self,
    ) -> Callable[
        [tensorboard_service.DeleteTensorboardTimeSeriesRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTensorboardTimeSeries(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_tensorboard_time_series_data(
        self,
    ) -> Callable[
        [tensorboard_service.ExportTensorboardTimeSeriesDataRequest],
        tensorboard_service.ExportTensorboardTimeSeriesDataResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportTensorboardTimeSeriesData(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_tensorboard(
        self,
    ) -> Callable[[tensorboard_service.GetTensorboardRequest], tensorboard.Tensorboard]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTensorboard(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_tensorboard_experiment(
        self,
    ) -> Callable[
        [tensorboard_service.GetTensorboardExperimentRequest],
        tensorboard_experiment.TensorboardExperiment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTensorboardExperiment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_tensorboard_run(
        self,
    ) -> Callable[
        [tensorboard_service.GetTensorboardRunRequest], tensorboard_run.TensorboardRun
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTensorboardRun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_tensorboard_time_series(
        self,
    ) -> Callable[
        [tensorboard_service.GetTensorboardTimeSeriesRequest],
        tensorboard_time_series.TensorboardTimeSeries,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTensorboardTimeSeries(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_tensorboard_experiments(
        self,
    ) -> Callable[
        [tensorboard_service.ListTensorboardExperimentsRequest],
        tensorboard_service.ListTensorboardExperimentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTensorboardExperiments(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_tensorboard_runs(
        self,
    ) -> Callable[
        [tensorboard_service.ListTensorboardRunsRequest],
        tensorboard_service.ListTensorboardRunsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTensorboardRuns(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_tensorboards(
        self,
    ) -> Callable[
        [tensorboard_service.ListTensorboardsRequest],
        tensorboard_service.ListTensorboardsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTensorboards(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_tensorboard_time_series(
        self,
    ) -> Callable[
        [tensorboard_service.ListTensorboardTimeSeriesRequest],
        tensorboard_service.ListTensorboardTimeSeriesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTensorboardTimeSeries(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def read_tensorboard_blob_data(
        self,
    ) -> Callable[
        [tensorboard_service.ReadTensorboardBlobDataRequest],
        tensorboard_service.ReadTensorboardBlobDataResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ReadTensorboardBlobData(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def read_tensorboard_size(
        self,
    ) -> Callable[
        [tensorboard_service.ReadTensorboardSizeRequest],
        tensorboard_service.ReadTensorboardSizeResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ReadTensorboardSize(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def read_tensorboard_time_series_data(
        self,
    ) -> Callable[
        [tensorboard_service.ReadTensorboardTimeSeriesDataRequest],
        tensorboard_service.ReadTensorboardTimeSeriesDataResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ReadTensorboardTimeSeriesData(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def read_tensorboard_usage(
        self,
    ) -> Callable[
        [tensorboard_service.ReadTensorboardUsageRequest],
        tensorboard_service.ReadTensorboardUsageResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ReadTensorboardUsage(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_tensorboard(
        self,
    ) -> Callable[
        [tensorboard_service.UpdateTensorboardRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTensorboard(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_tensorboard_experiment(
        self,
    ) -> Callable[
        [tensorboard_service.UpdateTensorboardExperimentRequest],
        gca_tensorboard_experiment.TensorboardExperiment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTensorboardExperiment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_tensorboard_run(
        self,
    ) -> Callable[
        [tensorboard_service.UpdateTensorboardRunRequest],
        gca_tensorboard_run.TensorboardRun,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTensorboardRun(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_tensorboard_time_series(
        self,
    ) -> Callable[
        [tensorboard_service.UpdateTensorboardTimeSeriesRequest],
        gca_tensorboard_time_series.TensorboardTimeSeries,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTensorboardTimeSeries(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def write_tensorboard_experiment_data(
        self,
    ) -> Callable[
        [tensorboard_service.WriteTensorboardExperimentDataRequest],
        tensorboard_service.WriteTensorboardExperimentDataResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._WriteTensorboardExperimentData(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def write_tensorboard_run_data(
        self,
    ) -> Callable[
        [tensorboard_service.WriteTensorboardRunDataRequest],
        tensorboard_service.WriteTensorboardRunDataResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._WriteTensorboardRunData(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseTensorboardServiceRestTransport._BaseGetLocation,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: locations_pb2.GetLocationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> locations_pb2.Location:

            r"""Call the get location method over HTTP.

            Args:
                request (locations_pb2.GetLocationRequest):
                    The request object for GetLocation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                locations_pb2.Location: Response from GetLocation method.
            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseGetLocation._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseGetLocation._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._GetLocation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = locations_pb2.Location()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_location(resp)
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(
        _BaseTensorboardServiceRestTransport._BaseListLocations,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: locations_pb2.ListLocationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> locations_pb2.ListLocationsResponse:

            r"""Call the list locations method over HTTP.

            Args:
                request (locations_pb2.ListLocationsRequest):
                    The request object for ListLocations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                locations_pb2.ListLocationsResponse: Response from ListLocations method.
            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseListLocations._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseListLocations._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._ListLocations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_locations(resp)
            return resp

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _GetIamPolicy(
        _BaseTensorboardServiceRestTransport._BaseGetIamPolicy,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.GetIamPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: iam_policy_pb2.GetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> policy_pb2.Policy:

            r"""Call the get iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.GetIamPolicyRequest):
                    The request object for GetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                policy_pb2.Policy: Response from GetIamPolicy method.
            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseGetIamPolicy._get_transcoded_request(
                http_options, request
            )

            body = _BaseTensorboardServiceRestTransport._BaseGetIamPolicy._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseGetIamPolicy._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._GetIamPolicy._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_iam_policy(resp)
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _SetIamPolicy(
        _BaseTensorboardServiceRestTransport._BaseSetIamPolicy,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.SetIamPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: iam_policy_pb2.SetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> policy_pb2.Policy:

            r"""Call the set iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.SetIamPolicyRequest):
                    The request object for SetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                policy_pb2.Policy: Response from SetIamPolicy method.
            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseSetIamPolicy._get_transcoded_request(
                http_options, request
            )

            body = _BaseTensorboardServiceRestTransport._BaseSetIamPolicy._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseSetIamPolicy._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._SetIamPolicy._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_set_iam_policy(resp)
            return resp

    @property
    def test_iam_permissions(self):
        return self._TestIamPermissions(self._session, self._host, self._interceptor)  # type: ignore

    class _TestIamPermissions(
        _BaseTensorboardServiceRestTransport._BaseTestIamPermissions,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.TestIamPermissions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: iam_policy_pb2.TestIamPermissionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> iam_policy_pb2.TestIamPermissionsResponse:

            r"""Call the test iam permissions method over HTTP.

            Args:
                request (iam_policy_pb2.TestIamPermissionsRequest):
                    The request object for TestIamPermissions method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                iam_policy_pb2.TestIamPermissionsResponse: Response from TestIamPermissions method.
            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseTestIamPermissions._get_http_options()
            )
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseTestIamPermissions._get_transcoded_request(
                http_options, request
            )

            body = _BaseTensorboardServiceRestTransport._BaseTestIamPermissions._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseTestIamPermissions._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = (
                TensorboardServiceRestTransport._TestIamPermissions._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = iam_policy_pb2.TestIamPermissionsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_test_iam_permissions(resp)
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseTensorboardServiceRestTransport._BaseCancelOperation,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.CancelOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> None:

            r"""Call the cancel operation method over HTTP.

            Args:
                request (operations_pb2.CancelOperationRequest):
                    The request object for CancelOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseCancelOperation._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseCancelOperation._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._CancelOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BaseTensorboardServiceRestTransport._BaseDeleteOperation,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.DeleteOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> None:

            r"""Call the delete operation method over HTTP.

            Args:
                request (operations_pb2.DeleteOperationRequest):
                    The request object for DeleteOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseDeleteOperation._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseDeleteOperation._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._DeleteOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseTensorboardServiceRestTransport._BaseGetOperation,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.GetOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:

            r"""Call the get operation method over HTTP.

            Args:
                request (operations_pb2.GetOperationRequest):
                    The request object for GetOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                operations_pb2.Operation: Response from GetOperation method.
            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseGetOperation._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseGetOperation._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._GetOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.Operation()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_operation(resp)
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(
        _BaseTensorboardServiceRestTransport._BaseListOperations,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.ListOperationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.ListOperationsResponse:

            r"""Call the list operations method over HTTP.

            Args:
                request (operations_pb2.ListOperationsRequest):
                    The request object for ListOperations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                operations_pb2.ListOperationsResponse: Response from ListOperations method.
            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseListOperations._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseListOperations._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._ListOperations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_operations(resp)
            return resp

    @property
    def wait_operation(self):
        return self._WaitOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _WaitOperation(
        _BaseTensorboardServiceRestTransport._BaseWaitOperation,
        TensorboardServiceRestStub,
    ):
        def __hash__(self):
            return hash("TensorboardServiceRestTransport.WaitOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: operations_pb2.WaitOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:

            r"""Call the wait operation method over HTTP.

            Args:
                request (operations_pb2.WaitOperationRequest):
                    The request object for WaitOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                operations_pb2.Operation: Response from WaitOperation method.
            """

            http_options = (
                _BaseTensorboardServiceRestTransport._BaseWaitOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_wait_operation(request, metadata)
            transcoded_request = _BaseTensorboardServiceRestTransport._BaseWaitOperation._get_transcoded_request(
                http_options, request
            )

            # Jsonify the query params
            query_params = _BaseTensorboardServiceRestTransport._BaseWaitOperation._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = TensorboardServiceRestTransport._WaitOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.Operation()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_wait_operation(resp)
            return resp

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("TensorboardServiceRestTransport",)
