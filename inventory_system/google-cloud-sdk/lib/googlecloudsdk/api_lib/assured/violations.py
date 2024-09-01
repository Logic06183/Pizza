# -*- coding: utf-8 -*- #
# Copyright 2022 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Utilities Assured Workloads API, Workloads Endpoints."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from apitools.base.py import list_pager
from googlecloudsdk.api_lib.assured import util
from googlecloudsdk.core import resources


def GetViolationURI(resource):
  violation = resources.REGISTRY.ParseRelativeName(
      resource.name,
      collection='assuredworkloads.organizations.locations.workloads.violations'
  )
  return violation.SelfLink()


class ViolationsClient(object):
  """Client for Violations in Assured Workloads API."""

  def __init__(self, release_track, no_http=False):
    self.client = util.GetClientInstance(release_track, no_http)
    self.messages = util.GetMessagesModule(release_track)
    self._release_track = release_track
    self._service = self.client.organizations_locations_workloads_violations

  def List(self, parent, limit=None, page_size=100):
    """List all Assured Workloads violations belonging to the given workload.

    Args:
      parent: str, the parent workload of the Assured Workloads Violations
        to be listed, in the form:
          organizations/{ORG_ID}/locations/{LOCATION}/workloads/{WORKLOAD}.
      limit: int or None, the total number of results to return.
      page_size: int, the number of entries in each batch (affects requests
        made, but not the yielded results).

    Returns:
      A list of all Assured Workloads violations belonging to a given workload.
    """
    list_req = self.messages.AssuredworkloadsOrganizationsLocationsWorkloadsViolationsListRequest(
        parent=parent, pageSize=page_size)
    return list_pager.YieldFromList(
        self._service,
        list_req,
        field='violations',
        batch_size=page_size,
        limit=limit,
        batch_size_attribute=None)

  def Describe(self, name):
    """Describe an existing Assured Workloads Compliance Violation.

    Args:
      name: str, the name for the Assured Workloads Violation being described
        in the form:
        organizations/{ORG_ID}/locations/{LOCATION}/workloads/{WORKLOAD_ID}/violations/{VIOLATION_ID}.

    Returns:
      Specified Assured Workloads Violation.
    """
    describe_req = self.messages.AssuredworkloadsOrganizationsLocationsWorkloadsViolationsGetRequest(
        name=name)
    return self.client.organizations_locations_workloads_violations.Get(
        describe_req)