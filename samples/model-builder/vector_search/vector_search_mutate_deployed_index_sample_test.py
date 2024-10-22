# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import test_constants as constants
from vector_search import vector_search_mutate_deployed_index_sample


def test_vector_search_mutate_deployed_index_sample(
    mock_sdk_init,
    mock_index_endpoint_init,
    mock_index_endpoint_mutate_deployed_index,
):
    vector_search_mutate_deployed_index_sample.vector_search_mutate_deployed_index(
        project=constants.PROJECT,
        location=constants.LOCATION,
        index_endpoint_name=constants.VECTOR_SEARCH_INDEX_ENDPOINT,
        deployed_index_id=constants.VECTOR_SEARCH_DEPLOYED_INDEX_ID,
        min_replica_count=constants.MIN_REPLICA_COUNT,
        max_replica_count=constants.MAX_REPLICA_COUNT,
    )

    # Check client initialization
    mock_sdk_init.assert_called_with(
        project=constants.PROJECT,
        location=constants.LOCATION,
    )

    # Check index endpoint initialization with right index endpoint name
    mock_index_endpoint_init.assert_called_with(
        index_endpoint_name=constants.VECTOR_SEARCH_INDEX_ENDPOINT
    )

    # Check index creation
    mock_index_endpoint_mutate_deployed_index.assert_called_with(
        deployed_index_id=constants.VECTOR_SEARCH_DEPLOYED_INDEX_ID,
        min_replica_count=constants.MIN_REPLICA_COUNT,
        max_replica_count=constants.MAX_REPLICA_COUNT,
    )
