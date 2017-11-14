# stylelens_product.VersionApi

All URIs are relative to *http://product.stylelens.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_version**](VersionApi.md#add_version) | **POST** /versions | Add a new Version
[**get_latest_version**](VersionApi.md#get_latest_version) | **GET** /versions/latest | Gat latest Version
[**get_version_by_id**](VersionApi.md#get_version_by_id) | **GET** /versions/{versionId} | Gat Version by ID


# **add_version**
> AddVersionResponse add_version(body=body)

Add a new Version



### Example 
```python
from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = stylelens_product.VersionApi()
body = stylelens_product.Version() # Version | Version object that needs to be added to the db. (optional)

try: 
    # Add a new Version
    api_response = api_instance.add_version(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionApi->add_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Version**](Version.md)| Version object that needs to be added to the db. | [optional] 

### Return type

[**AddVersionResponse**](AddVersionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_version**
> LatestVersionResponse get_latest_version()

Gat latest Version

Returns a latest Version

### Example 
```python
from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = stylelens_product.VersionApi()

try: 
    # Gat latest Version
    api_response = api_instance.get_latest_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionApi->get_latest_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LatestVersionResponse**](LatestVersionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_by_id**
> GetVersionResponse get_version_by_id(version_id)

Gat Version by ID

Returns a Version

### Example 
```python
from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = stylelens_product.VersionApi()
version_id = 'version_id_example' # str | ID of Version to return

try: 
    # Gat Version by ID
    api_response = api_instance.get_version_by_id(version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionApi->get_version_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**| ID of Version to return | 

### Return type

[**GetVersionResponse**](GetVersionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

