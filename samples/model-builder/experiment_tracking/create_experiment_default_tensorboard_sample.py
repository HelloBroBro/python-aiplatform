# Copyright 2022 Google LLC
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

#  [START aiplatform_sdk_create_experiment_default_tensorboard_sample]
from google.cloud import aiplatform


def create_experiment_default_tensorboard_sample(
    experiment_name: str,
    experiment_description: str,
    project: str,
    location: str,
):
    aiplatform.init(
        experiment=experiment_name,
        experiment_description=experiment_description,
        project=project,
        location=location,
    )

    tensorboard = aiplatform.Experiment(experiment_name).get_backing_tensorboard_resource()
    print(f"Tensorboard resource name: {tensorboard.name}")


#  [END aiplatform_sdk_create_experiment_default_tensorboard_sample]
