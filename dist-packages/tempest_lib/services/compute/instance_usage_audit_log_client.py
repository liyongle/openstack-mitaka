# Copyright 2013 IBM Corporation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_serialization import jsonutils as json

from tempest_lib.api_schema.response.compute.v2_1 import \
    instance_usage_audit_logs as schema
from tempest_lib.common import rest_client


class InstanceUsagesAuditLogClient(rest_client.RestClient):

    def list_instance_usage_audit_logs(self):
        url = 'os-instance_usage_audit_log'
        resp, body = self.get(url)
        body = json.loads(body)
        self.validate_response(schema.list_instance_usage_audit_log,
                               resp, body)
        return rest_client.ResponseBody(resp, body)

    def show_instance_usage_audit_log(self, time_before):
        url = 'os-instance_usage_audit_log/%s' % time_before
        resp, body = self.get(url)
        body = json.loads(body)
        self.validate_response(schema.get_instance_usage_audit_log, resp, body)
        return rest_client.ResponseBody(resp, body)
