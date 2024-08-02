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
from typing import Optional
import warnings

from vertexai.preview.evaluation import constants
from vertexai.preview.evaluation.metrics import _base

_DEPRECATION_WARNING_MESSAGE = (
    "After google-cloud-aiplatform>1.63.0, using metric class `Groundedness` will"
    " result in an error. Please use string metric name `groundedness` or define"
    " a PointwiseMetric instead."
)


class Groundedness(_base._ModelBasedMetric):
    """The model-based pointwise metric for Groundedness."""

    _metric_name = constants.Metric.GROUNDEDNESS

    def __init__(self, *, version: Optional[int] = None):
        warnings.warn(message=_DEPRECATION_WARNING_MESSAGE)
        super().__init__(
            metric=Groundedness._metric_name,
            version=version,
        )
