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
from surveilclient.v2_0.status import hosts
from surveilclient.v2_0.status import metrics
from surveilclient.v2_0.status import services


class StatusManager(surveil_manager.SurveilManager):
    base_url = '/status'

    def __init__(self, http_client):
        super(StatusManager, self).__init__(http_client)
        self.hosts = hosts.HostsManager(self.http_client)
        self.services = services.ServicesManager(self.http_client)
        self.metrics = metrics.MetricsManager(self.http_client)
