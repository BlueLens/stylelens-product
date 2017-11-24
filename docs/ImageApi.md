# stylelens_product.ImageApi

All URIs are relative to *http://product.stylelens.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_image**](ImageApi.md#add_image) | **POST** /images | Added a new Image


# **add_image**
> AddImageResponse add_image(body)

Added a new Image



### Example 
```python
from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = stylelens_product.ImageApi()
body = stylelens_product.Image() # Image | Product object that needs to be added to the db.

try: 
    # Added a new Image
    api_response = api_instance.add_image(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->add_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Image**](Image.md)| Product object that needs to be added to the db. | 

### Return type

[**AddImageResponse**](AddImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

