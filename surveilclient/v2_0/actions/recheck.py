# Copyright 2015 - Savoir-Faire Linux inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from surveilclient.common import surveil_manager


class RecheckManager(surveil_manager.SurveilManager):
    base_url = '/actions/recheck'

    def create(self, **kwargs):
        resp, body = self.http_client.json_request(
            self.base_url,
            'POST',
            body=kwargs,
        )
        return body