# Copyright 2023 Google LLC. All Rights Reserved.
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

"""Unit tests for frameworks base module."""

# pylint: disable=line-too-long
# pylint: disable=missing-function-docstring
# pylint: disable=protected-access

from AutoMLOps.frameworks.base import Component, Pipeline
from AutoMLOps.utils.utils import write_yaml_file
import pytest

DEFAULTS1 = {
    'gcp':
        {
            'af_registry_location': 'us-central1',
            'project_id': 'my_project',
            'af_registry_name': 'my_af_registry'
        }
    }
DEFAULTS2 = {
    'gcp':
        {
            'af_registry_location': 'us-central1',
            'project_id': 'my_project',
            'af_registry_name': 'my_af_registry'
        }
    }

@pytest.fixture(params=[DEFAULTS1, DEFAULTS2])
def defaults_dict(request, tmpdir):
    """Writes temporary yaml file fixture using defaults parameterized dictionaries during pytest session scope.

    Returns:
        str: Path of yaml file.
    """
    yaml_path = tmpdir.join('test.yaml')
    write_yaml_file(yaml_path, request.param, 'w')
    return {'path': yaml_path, 'vals': request.param}

@pytest.mark.parametrize(
    'component_spec',
    ['test1', 'test2']
)
def test_Component(defaults_dict, component_spec):
    """Tests the Component base class, the parent class that defines a general abstraction of a Component.

    Args:
        component_spec (dict): Dictionary of component specs including details
            of component image, startup command, and args.
        defaults_file (str): Path to the default config variables yaml.
    """
    path = defaults_dict['path']
    defaults = defaults_dict['vals']

    my_component = Component(component_spec=component_spec, defaults_file=path)
    assert my_component._af_registry_location == defaults['gcp']['af_registry_location']
    assert my_component._af_registry_name == defaults['gcp']['af_registry_name']
    assert my_component._project_id == defaults['gcp']['project_id']
    assert my_component._component_spec == component_spec

@pytest.mark.parametrize(
    'custom_training_job_specs',
    [
        [{'component_spec': 'mycomp1', 'other': 'myother'}],
        [
            {
                'component_spec': 'train_model',
                'display_name': 'train-model-accelerated',
                'machine_type': 'a2-highgpu-1g',
                'accelerator_type': 'NVIDIA_TESLA_A100',
                'accelerator_count': '1',
            }
        ],
        [
            {
                'component_spec': 'train_model',
                'display_name': 'train-model-accelerated'
            },
            {
                'component_spec': 'test_model',
                'display_name': 'test-model-accelerated'
            }
        ]
    ]
)
def test_Pipeline(defaults_dict, custom_training_job_specs):
    """Tests the Pipeline base class, the parent class that defines a general abstraction of a Pipeline.

    Args:
        custom_training_job_specs (List[Dict]): Specifies the specs to run the training job with.
        defaults_file (str): Path to the default config variables yaml.
    """
    path = defaults_dict['path']
    defaults = defaults_dict['vals']

    my_pipeline = Pipeline(custom_training_job_specs=custom_training_job_specs, defaults_file=path)
    assert my_pipeline._project_id == defaults['gcp']['project_id']
    assert my_pipeline._custom_training_job_specs == custom_training_job_specs