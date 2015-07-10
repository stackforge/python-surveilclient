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

import httpretty

from surveilclient.tests.v2_0 import clienttest


class TestServices(clienttest.ClientTest):

    @httpretty.activate
    def test_list(self):
        httpretty.register_uri(
            httpretty.GET, "http://localhost:5311/v2/config/services",
            body='[{"service_name": "service1"}]'
        )

        services = self.client.config.services.list()

        self.assertEqual(
            services,
            [{"service_name": "service1"}]
        )

    @httpretty.activate
    def test_list_templates(self):
        httpretty.register_uri(
            httpretty.GET, "http://localhost:5311/v2/config/services",
            body='[{"service_name": "service1"}]'
        )

        self.client.config.services.list(templates=True)
        self.assertEqual(
            httpretty.last_request().path,
            '/v2/config/services?templates=1'
        )

    @httpretty.activate
    def test_create(self):
        httpretty.register_uri(
            httpretty.POST, "http://localhost:5311/v2/config/services",
            body='{"service_name": "new_service"}'
        )

        self.client.config.services.create(
            service_name="new_service"
        )

        self.assertEqual(
            httpretty.last_request().body.decode(),
            '{"service_name": "new_service"}'
        )

    @httpretty.activate
    def test_delete(self):
        httpretty.register_uri(
            httpretty.DELETE,
            "http://localhost:5311/v2/config/hosts/host_name/" +
            "services/service_description",
            body="body"
        )

        body = self.client.config.services.delete(
            host_name="host_name",
            service_description="service_description"
        )

        self.assertEqual(
            body,
            "body"
        )
