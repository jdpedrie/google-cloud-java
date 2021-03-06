# Copyright 2018 Google LLC
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

"""This script is used to synthesize generated parts of this library."""

import synthtool as s
import synthtool.gcp as gcp

gapic = gcp.GAPICGenerator()
common_templates = gcp.CommonTemplates()

# tasks has two product names, and a poorly named artman yaml
v1beta1_library = gapic.java_library(
    service='asset',
    version='v1beta1',
    config_path='artman_cloudasset_v1beta1.yaml',
    artman_output_name='')

s.copy(v1beta1_library / 'gapic-google-cloud-asset-v1beta1/src', 'src')
s.copy(v1beta1_library / 'grpc-google-cloud-asset-v1beta1/src', '../../google-api-grpc/grpc-google-cloud-asset-v1beta1/src')
s.copy(v1beta1_library / 'proto-google-cloud-asset-v1beta1/src', '../../google-api-grpc/proto-google-cloud-asset-v1beta1/src')
