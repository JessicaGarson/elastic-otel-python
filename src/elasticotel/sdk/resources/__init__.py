# Copyright Elasticsearch BV
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

import sys

from opentelemetry.sdk.resources import (
    Resource,
    ResourceDetector,
    PROCESS_RUNTIME_DESCRIPTION,
    PROCESS_RUNTIME_NAME,
    PROCESS_RUNTIME_VERSION,
)


class ProcessRuntimeResourceDetector(ResourceDetector):
    """Subset of upstream ProcessResourceDetector to only fill process runtime attributes"""

    def detect(self) -> "Resource":
        runtime_version = ".".join(
            map(
                str,
                (
                    sys.version_info[:3]
                    if sys.version_info.releaselevel == "final" and not sys.version_info.serial
                    else sys.version_info
                ),
            )
        )
        resource_info = {
            PROCESS_RUNTIME_DESCRIPTION: sys.version,
            PROCESS_RUNTIME_NAME: sys.implementation.name,
            PROCESS_RUNTIME_VERSION: runtime_version,
        }
        return Resource(resource_info)
