# stylelens_product.ObjectApi

All URIs are relative to *http://api.stylelens.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_objects**](ObjectApi.md#get_objects) | **POST** /objects | Query to search multiple objects


# **get_objects**
> GetObjectsResponse get_objects(file=file)

Query to search multiple objects



### Example 
```python
from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = stylelens_product.ObjectApi()
file = '/path/to/file.txt' # file | Image file to upload (only support jpg format yet) (optional)

try: 
    # Query to search multiple objects
    api_response = api_instance.get_objects(file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectApi->get_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| Image file to upload (only support jpg format yet) | [optional] 

### Return type

[**GetObjectsResponse**](GetObjectsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

