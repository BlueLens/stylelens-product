# stylelens_product.ObjectApi

All URIs are relative to *http://product-prod.stylelens.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_object**](ObjectApi.md#add_object) | **POST** /objects | Added a new Object
[**get_object_by_id**](ObjectApi.md#get_object_by_id) | **GET** /objects/{objectId} | Find Object by ID


# **add_object**
> AddObjectResponse add_object(body)

Added a new Object



### Example 
```python
from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = stylelens_product.ObjectApi()
body = stylelens_product.Object() # Object | Object that needs to be added to the db.

try: 
    # Added a new Object
    api_response = api_instance.add_object(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectApi->add_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)| Object that needs to be added to the db. | 

### Return type

[**AddObjectResponse**](AddObjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_by_id**
> GetObjectResponse get_object_by_id(object_id)

Find Object by ID

Returns a single Object

### Example 
```python
from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = stylelens_product.ObjectApi()
object_id = 'object_id_example' # str | ID of Object to return

try: 
    # Find Object by ID
    api_response = api_instance.get_object_by_id(object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectApi->get_object_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**| ID of Object to return | 

### Return type

[**GetObjectResponse**](GetObjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

