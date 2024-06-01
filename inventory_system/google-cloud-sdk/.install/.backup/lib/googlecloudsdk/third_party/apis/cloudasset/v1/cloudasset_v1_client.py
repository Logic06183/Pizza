"""Generated client library for cloudasset version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.cloudasset.v1 import cloudasset_v1_messages as messages


class CloudassetV1(base_api.BaseApiClient):
  """Generated client library for service cloudasset version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://cloudasset.googleapis.com/'
  MTLS_BASE_URL = 'https://cloudasset.mtls.googleapis.com/'

  _PACKAGE = 'cloudasset'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'CloudassetV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new cloudasset handle."""
    url = url or self.BASE_URL
    super(CloudassetV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.assets = self.AssetsService(self)
    self.effectiveIamPolicies = self.EffectiveIamPoliciesService(self)
    self.feeds = self.FeedsService(self)
    self.operations = self.OperationsService(self)
    self.savedQueries = self.SavedQueriesService(self)
    self.v1 = self.V1Service(self)

  class AssetsService(base_api.BaseApiService):
    """Service class for the assets resource."""

    _NAME = 'assets'

    def __init__(self, client):
      super(CloudassetV1.AssetsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists assets with time and resource types and returns paged results in response.

      Args:
        request: (CloudassetAssetsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListAssetsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}/assets',
        http_method='GET',
        method_id='cloudasset.assets.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['assetTypes', 'contentType', 'pageSize', 'pageToken', 'readTime', 'relationshipTypes'],
        relative_path='v1/{+parent}/assets',
        request_field='',
        request_type_name='CloudassetAssetsListRequest',
        response_type_name='ListAssetsResponse',
        supports_download=False,
    )

  class EffectiveIamPoliciesService(base_api.BaseApiService):
    """Service class for the effectiveIamPolicies resource."""

    _NAME = 'effectiveIamPolicies'

    def __init__(self, client):
      super(CloudassetV1.EffectiveIamPoliciesService, self).__init__(client)
      self._upload_configs = {
          }

    def BatchGet(self, request, global_params=None):
      r"""Gets effective IAM policies for a batch of resources.

      Args:
        request: (CloudassetEffectiveIamPoliciesBatchGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BatchGetEffectiveIamPoliciesResponse) The response message.
      """
      config = self.GetMethodConfig('BatchGet')
      return self._RunMethod(
          config, request, global_params=global_params)

    BatchGet.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}/effectiveIamPolicies:batchGet',
        http_method='GET',
        method_id='cloudasset.effectiveIamPolicies.batchGet',
        ordered_params=['scope'],
        path_params=['scope'],
        query_params=['names'],
        relative_path='v1/{+scope}/effectiveIamPolicies:batchGet',
        request_field='',
        request_type_name='CloudassetEffectiveIamPoliciesBatchGetRequest',
        response_type_name='BatchGetEffectiveIamPoliciesResponse',
        supports_download=False,
    )

  class FeedsService(base_api.BaseApiService):
    """Service class for the feeds resource."""

    _NAME = 'feeds'

    def __init__(self, client):
      super(CloudassetV1.FeedsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a feed in a parent project/folder/organization to listen to its asset updates.

      Args:
        request: (CloudassetFeedsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Feed) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}/feeds',
        http_method='POST',
        method_id='cloudasset.feeds.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/feeds',
        request_field='createFeedRequest',
        request_type_name='CloudassetFeedsCreateRequest',
        response_type_name='Feed',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes an asset feed.

      Args:
        request: (CloudassetFeedsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}/feeds/{feedsId}',
        http_method='DELETE',
        method_id='cloudasset.feeds.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='CloudassetFeedsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details about an asset feed.

      Args:
        request: (CloudassetFeedsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Feed) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}/feeds/{feedsId}',
        http_method='GET',
        method_id='cloudasset.feeds.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='CloudassetFeedsGetRequest',
        response_type_name='Feed',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all asset feeds in a parent project/folder/organization.

      Args:
        request: (CloudassetFeedsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListFeedsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}/feeds',
        http_method='GET',
        method_id='cloudasset.feeds.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/feeds',
        request_field='',
        request_type_name='CloudassetFeedsListRequest',
        response_type_name='ListFeedsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates an asset feed configuration.

      Args:
        request: (CloudassetFeedsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Feed) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}/feeds/{feedsId}',
        http_method='PATCH',
        method_id='cloudasset.feeds.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='updateFeedRequest',
        request_type_name='CloudassetFeedsPatchRequest',
        response_type_name='Feed',
        supports_download=False,
    )

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = 'operations'

    def __init__(self, client):
      super(CloudassetV1.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (CloudassetOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}/operations/{operationsId}/{operationsId1}',
        http_method='GET',
        method_id='cloudasset.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='CloudassetOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class SavedQueriesService(base_api.BaseApiService):
    """Service class for the savedQueries resource."""

    _NAME = 'savedQueries'

    def __init__(self, client):
      super(CloudassetV1.SavedQueriesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a saved query in a parent project/folder/organization.

      Args:
        request: (CloudassetSavedQueriesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SavedQuery) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}/savedQueries',
        http_method='POST',
        method_id='cloudasset.savedQueries.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['savedQueryId'],
        relative_path='v1/{+parent}/savedQueries',
        request_field='savedQuery',
        request_type_name='CloudassetSavedQueriesCreateRequest',
        response_type_name='SavedQuery',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a saved query.

      Args:
        request: (CloudassetSavedQueriesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}/savedQueries/{savedQueriesId}',
        http_method='DELETE',
        method_id='cloudasset.savedQueries.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='CloudassetSavedQueriesDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details about a saved query.

      Args:
        request: (CloudassetSavedQueriesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SavedQuery) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}/savedQueries/{savedQueriesId}',
        http_method='GET',
        method_id='cloudasset.savedQueries.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='CloudassetSavedQueriesGetRequest',
        response_type_name='SavedQuery',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all saved queries in a parent project/folder/organization.

      Args:
        request: (CloudassetSavedQueriesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListSavedQueriesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}/savedQueries',
        http_method='GET',
        method_id='cloudasset.savedQueries.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/savedQueries',
        request_field='',
        request_type_name='CloudassetSavedQueriesListRequest',
        response_type_name='ListSavedQueriesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a saved query.

      Args:
        request: (CloudassetSavedQueriesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SavedQuery) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}/savedQueries/{savedQueriesId}',
        http_method='PATCH',
        method_id='cloudasset.savedQueries.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}',
        request_field='savedQuery',
        request_type_name='CloudassetSavedQueriesPatchRequest',
        response_type_name='SavedQuery',
        supports_download=False,
    )

  class V1Service(base_api.BaseApiService):
    """Service class for the v1 resource."""

    _NAME = 'v1'

    def __init__(self, client):
      super(CloudassetV1.V1Service, self).__init__(client)
      self._upload_configs = {
          }

    def AnalyzeIamPolicy(self, request, global_params=None):
      r"""Analyzes IAM policies to answer which identities have what accesses on which resources.

      Args:
        request: (CloudassetAnalyzeIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AnalyzeIamPolicyResponse) The response message.
      """
      config = self.GetMethodConfig('AnalyzeIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    AnalyzeIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}:analyzeIamPolicy',
        http_method='GET',
        method_id='cloudasset.analyzeIamPolicy',
        ordered_params=['scope'],
        path_params=['scope'],
        query_params=['analysisQuery_accessSelector_permissions', 'analysisQuery_accessSelector_roles', 'analysisQuery_conditionContext_accessTime', 'analysisQuery_identitySelector_identity', 'analysisQuery_options_analyzeServiceAccountImpersonation', 'analysisQuery_options_expandGroups', 'analysisQuery_options_expandResources', 'analysisQuery_options_expandRoles', 'analysisQuery_options_outputGroupEdges', 'analysisQuery_options_outputResourceEdges', 'analysisQuery_resourceSelector_fullResourceName', 'executionTimeout', 'savedAnalysisQuery'],
        relative_path='v1/{+scope}:analyzeIamPolicy',
        request_field='',
        request_type_name='CloudassetAnalyzeIamPolicyRequest',
        response_type_name='AnalyzeIamPolicyResponse',
        supports_download=False,
    )

    def AnalyzeIamPolicyLongrunning(self, request, global_params=None):
      r"""Analyzes IAM policies asynchronously to answer which identities have what accesses on which resources, and writes the analysis results to a Google Cloud Storage or a BigQuery destination. For Cloud Storage destination, the output format is the JSON format that represents a AnalyzeIamPolicyResponse. This method implements the google.longrunning.Operation, which allows you to track the operation status. We recommend intervals of at least 2 seconds with exponential backoff retry to poll the operation result. The metadata contains the metadata for the long-running operation.

      Args:
        request: (CloudassetAnalyzeIamPolicyLongrunningRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('AnalyzeIamPolicyLongrunning')
      return self._RunMethod(
          config, request, global_params=global_params)

    AnalyzeIamPolicyLongrunning.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}:analyzeIamPolicyLongrunning',
        http_method='POST',
        method_id='cloudasset.analyzeIamPolicyLongrunning',
        ordered_params=['scope'],
        path_params=['scope'],
        query_params=[],
        relative_path='v1/{+scope}:analyzeIamPolicyLongrunning',
        request_field='analyzeIamPolicyLongrunningRequest',
        request_type_name='CloudassetAnalyzeIamPolicyLongrunningRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def AnalyzeMove(self, request, global_params=None):
      r"""Analyze moving a resource to a specified destination without kicking off the actual move. The analysis is best effort depending on the user's permissions of viewing different hierarchical policies and configurations. The policies and configuration are subject to change before the actual resource migration takes place.

      Args:
        request: (CloudassetAnalyzeMoveRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AnalyzeMoveResponse) The response message.
      """
      config = self.GetMethodConfig('AnalyzeMove')
      return self._RunMethod(
          config, request, global_params=global_params)

    AnalyzeMove.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}:analyzeMove',
        http_method='GET',
        method_id='cloudasset.analyzeMove',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=['destinationParent', 'view'],
        relative_path='v1/{+resource}:analyzeMove',
        request_field='',
        request_type_name='CloudassetAnalyzeMoveRequest',
        response_type_name='AnalyzeMoveResponse',
        supports_download=False,
    )

    def AnalyzeOrgPolicies(self, request, global_params=None):
      r"""Analyzes organization policies under a scope.

      Args:
        request: (CloudassetAnalyzeOrgPoliciesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AnalyzeOrgPoliciesResponse) The response message.
      """
      config = self.GetMethodConfig('AnalyzeOrgPolicies')
      return self._RunMethod(
          config, request, global_params=global_params)

    AnalyzeOrgPolicies.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}:analyzeOrgPolicies',
        http_method='GET',
        method_id='cloudasset.analyzeOrgPolicies',
        ordered_params=['scope'],
        path_params=['scope'],
        query_params=['constraint', 'filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+scope}:analyzeOrgPolicies',
        request_field='',
        request_type_name='CloudassetAnalyzeOrgPoliciesRequest',
        response_type_name='AnalyzeOrgPoliciesResponse',
        supports_download=False,
    )

    def AnalyzeOrgPolicyGovernedContainers(self, request, global_params=None):
      r"""Analyzes organization policies governed containers (projects, folders or organization) under a scope.

      Args:
        request: (CloudassetAnalyzeOrgPolicyGovernedContainersRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AnalyzeOrgPolicyGovernedContainersResponse) The response message.
      """
      config = self.GetMethodConfig('AnalyzeOrgPolicyGovernedContainers')
      return self._RunMethod(
          config, request, global_params=global_params)

    AnalyzeOrgPolicyGovernedContainers.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}:analyzeOrgPolicyGovernedContainers',
        http_method='GET',
        method_id='cloudasset.analyzeOrgPolicyGovernedContainers',
        ordered_params=['scope'],
        path_params=['scope'],
        query_params=['constraint', 'filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+scope}:analyzeOrgPolicyGovernedContainers',
        request_field='',
        request_type_name='CloudassetAnalyzeOrgPolicyGovernedContainersRequest',
        response_type_name='AnalyzeOrgPolicyGovernedContainersResponse',
        supports_download=False,
    )

    def AnalyzeOrgPolicyGovernedResources(self, request, global_params=None):
      r"""Analyzes organization policies governed resources under a scope.

      Args:
        request: (CloudassetAnalyzeOrgPolicyGovernedResourcesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AnalyzeOrgPolicyGovernedResourcesResponse) The response message.
      """
      config = self.GetMethodConfig('AnalyzeOrgPolicyGovernedResources')
      return self._RunMethod(
          config, request, global_params=global_params)

    AnalyzeOrgPolicyGovernedResources.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}:analyzeOrgPolicyGovernedResources',
        http_method='GET',
        method_id='cloudasset.analyzeOrgPolicyGovernedResources',
        ordered_params=['scope'],
        path_params=['scope'],
        query_params=['constraint', 'filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+scope}:analyzeOrgPolicyGovernedResources',
        request_field='',
        request_type_name='CloudassetAnalyzeOrgPolicyGovernedResourcesRequest',
        response_type_name='AnalyzeOrgPolicyGovernedResourcesResponse',
        supports_download=False,
    )

    def BatchGetAssetsHistory(self, request, global_params=None):
      r"""Batch gets the update history of assets that overlap a time window. For IAM_POLICY content, this API outputs history when the asset and its attached IAM POLICY both exist. This can create gaps in the output history. Otherwise, this API outputs history with asset in both non-delete or deleted status. If a specified asset does not exist, this API returns an INVALID_ARGUMENT error.

      Args:
        request: (CloudassetBatchGetAssetsHistoryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BatchGetAssetsHistoryResponse) The response message.
      """
      config = self.GetMethodConfig('BatchGetAssetsHistory')
      return self._RunMethod(
          config, request, global_params=global_params)

    BatchGetAssetsHistory.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}:batchGetAssetsHistory',
        http_method='GET',
        method_id='cloudasset.batchGetAssetsHistory',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['assetNames', 'contentType', 'readTimeWindow_endTime', 'readTimeWindow_startTime', 'relationshipTypes'],
        relative_path='v1/{+parent}:batchGetAssetsHistory',
        request_field='',
        request_type_name='CloudassetBatchGetAssetsHistoryRequest',
        response_type_name='BatchGetAssetsHistoryResponse',
        supports_download=False,
    )

    def ExportAssets(self, request, global_params=None):
      r"""Exports assets with time and resource types to a given Cloud Storage location/BigQuery table. For Cloud Storage location destinations, the output format is newline-delimited JSON. Each line represents a google.cloud.asset.v1.Asset in the JSON format; for BigQuery table destinations, the output table stores the fields in asset Protobuf as columns. This API implements the google.longrunning.Operation API, which allows you to keep track of the export. We recommend intervals of at least 2 seconds with exponential retry to poll the export operation result. For regular-size resource parent, the export operation usually finishes within 5 minutes.

      Args:
        request: (CloudassetExportAssetsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('ExportAssets')
      return self._RunMethod(
          config, request, global_params=global_params)

    ExportAssets.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}:exportAssets',
        http_method='POST',
        method_id='cloudasset.exportAssets',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}:exportAssets',
        request_field='exportAssetsRequest',
        request_type_name='CloudassetExportAssetsRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def QueryAssets(self, request, global_params=None):
      r"""Issue a job that queries assets using a SQL statement compatible with [BigQuery Standard SQL](http://cloud/bigquery/docs/reference/standard-sql/enabling-standard-sql). If the query execution finishes within timeout and there's no pagination, the full query results will be returned in the `QueryAssetsResponse`. Otherwise, full query results can be obtained by issuing extra requests with the `job_reference` from the a previous `QueryAssets` call. Note, the query result has approximately 10 GB limitation enforced by BigQuery https://cloud.google.com/bigquery/docs/best-practices-performance-output, queries return larger results will result in errors.

      Args:
        request: (CloudassetQueryAssetsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (QueryAssetsResponse) The response message.
      """
      config = self.GetMethodConfig('QueryAssets')
      return self._RunMethod(
          config, request, global_params=global_params)

    QueryAssets.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}:queryAssets',
        http_method='POST',
        method_id='cloudasset.queryAssets',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}:queryAssets',
        request_field='queryAssetsRequest',
        request_type_name='CloudassetQueryAssetsRequest',
        response_type_name='QueryAssetsResponse',
        supports_download=False,
    )

    def SearchAllIamPolicies(self, request, global_params=None):
      r"""Searches all IAM policies within the specified scope, such as a project, folder, or organization. The caller must be granted the `cloudasset.assets.searchAllIamPolicies` permission on the desired scope, otherwise the request will be rejected.

      Args:
        request: (CloudassetSearchAllIamPoliciesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SearchAllIamPoliciesResponse) The response message.
      """
      config = self.GetMethodConfig('SearchAllIamPolicies')
      return self._RunMethod(
          config, request, global_params=global_params)

    SearchAllIamPolicies.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}:searchAllIamPolicies',
        http_method='GET',
        method_id='cloudasset.searchAllIamPolicies',
        ordered_params=['scope'],
        path_params=['scope'],
        query_params=['assetTypes', 'orderBy', 'pageSize', 'pageToken', 'query'],
        relative_path='v1/{+scope}:searchAllIamPolicies',
        request_field='',
        request_type_name='CloudassetSearchAllIamPoliciesRequest',
        response_type_name='SearchAllIamPoliciesResponse',
        supports_download=False,
    )

    def SearchAllResources(self, request, global_params=None):
      r"""Searches all Cloud resources within the specified scope, such as a project, folder, or organization. The caller must be granted the `cloudasset.assets.searchAllResources` permission on the desired scope, otherwise the request will be rejected.

      Args:
        request: (CloudassetSearchAllResourcesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SearchAllResourcesResponse) The response message.
      """
      config = self.GetMethodConfig('SearchAllResources')
      return self._RunMethod(
          config, request, global_params=global_params)

    SearchAllResources.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/{v1Id}/{v1Id1}:searchAllResources',
        http_method='GET',
        method_id='cloudasset.searchAllResources',
        ordered_params=['scope'],
        path_params=['scope'],
        query_params=['assetTypes', 'orderBy', 'pageSize', 'pageToken', 'query', 'readMask'],
        relative_path='v1/{+scope}:searchAllResources',
        request_field='',
        request_type_name='CloudassetSearchAllResourcesRequest',
        response_type_name='SearchAllResourcesResponse',
        supports_download=False,
    )
