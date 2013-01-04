# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Copyright (c) 2012 OpenStack, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from quantum.plugins.openvswitch.ovs_driver_api import OVSDriverAPI


class DummyOVSDriver(OVSDriverAPI):
    """
    Empty implementation of OVSDriverAPI. Used for common OVS plugin within
    Openstack
    """
    def create_tenant_network(self, context, network_id, segmentation_id,
                              segmentation_type):
        pass

    def plug_host(self, context, network_id, segmentation_id, host_id):
        pass

    def unplug_host(self, context, network_id, segmentation_id, host_id):
        pass

    def delete_vlan(self, context, network_id):
        pass

    def get_tenant_network(self, context, networkd_id=None):
        pass
