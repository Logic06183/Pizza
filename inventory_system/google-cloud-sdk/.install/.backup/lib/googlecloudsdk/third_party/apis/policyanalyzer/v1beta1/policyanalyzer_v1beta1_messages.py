"""Generated message classes for policyanalyzer version v1beta1.

"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'policyanalyzer'


class GoogleCloudPolicyanalyzerV1beta1Activity(_messages.Message):
  r"""A GoogleCloudPolicyanalyzerV1beta1Activity object.

  Messages:
    ActivityValue: A struct of custom fields to explain the activity.

  Fields:
    activity: A struct of custom fields to explain the activity.
    activityType: The type of the activity.
    fullResourceName: The full resource name that identifies the resource. For
      examples of full resource names for Google Cloud services, see
      https://cloud.google.com/iam/help/troubleshooter/full-resource-names.
    observationPeriod: The data observation period to build the activity.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ActivityValue(_messages.Message):
    r"""A struct of custom fields to explain the activity.

    Messages:
      AdditionalProperty: An additional property for a ActivityValue object.

    Fields:
      additionalProperties: Properties of the object.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ActivityValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  activity = _messages.MessageField('ActivityValue', 1)
  activityType = _messages.StringField(2)
  fullResourceName = _messages.StringField(3)
  observationPeriod = _messages.MessageField('GoogleCloudPolicyanalyzerV1beta1ObservationPeriod', 4)


class GoogleCloudPolicyanalyzerV1beta1ObservationPeriod(_messages.Message):
  r"""Represents data observation period.

  Fields:
    endTime: The observation end time.
    startTime: The observation start time.
  """

  endTime = _messages.StringField(1)
  startTime = _messages.StringField(2)


class GoogleCloudPolicyanalyzerV1beta1QueryActivityResponse(_messages.Message):
  r"""Response to the `QueryActivity` method.

  Fields:
    activities: The set of activities that match the filter included in the
      request.
    nextPageToken: If there might be more results than those appearing in this
      response, then `nextPageToken` is included. To get the next set of
      results, call this method again using the value of `nextPageToken` as
      `pageToken`.
  """

  activities = _messages.MessageField('GoogleCloudPolicyanalyzerV1beta1Activity', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class PolicyanalyzerProjectsLocationsActivityTypesActivitiesQueryRequest(_messages.Message):
  r"""A PolicyanalyzerProjectsLocationsActivityTypesActivitiesQueryRequest
  object.

  Fields:
    filter: Optional. Optional filter expression to restrict the activities
      returned. Supported filters are: -
      service_account_last_authn.full_resource_name {=} -
      service_account_key_last_authn.full_resource_name {=}
    pageSize: Optional. The maximum number of results to return from this
      request. Max limit is 1000. Non-positive values are ignored. The
      presence of `nextPageToken` in the response indicates that more results
      might be available.
    pageToken: Optional. If present, then retrieve the next batch of results
      from the preceding call to this method. `pageToken` must be the value of
      `nextPageToken` from the previous response. The values of other method
      parameters should be identical to those in the previous call.
    parent: Required. The container resource on which to execute the request.
      Acceptable formats: `projects/[PROJECT_ID|PROJECT_NUMBER]/locations/[LOC
      ATION]/activityTypes/[ACTIVITY_TYPE]` LOCATION here refers to GCP
      Locations: https://cloud.google.com/about/locations/
  """

  filter = _messages.StringField(1)
  pageSize = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)
  parent = _messages.StringField(4, required=True)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
