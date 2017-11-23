# stylelens_product.ProductApi

All URIs are relative to *http://api.stylelens.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_product_by_hostcode_and_product_no**](ProductApi.md#get_product_by_hostcode_and_product_no) | **GET** /products/hosts/{hostCode}/products/{productNo} | Get Product by hostCode and productNo
[**get_product_by_id**](ProductApi.md#get_product_by_id) | **GET** /products/{productId} | Find Product by ID
[**get_products**](ProductApi.md#get_products) | **POST** /products | Query to search products


# **get_product_by_hostcode_and_product_no**
> GetProductResponse get_product_by_hostcode_and_product_no(host_code, product_no)

Get Product by hostCode and productNo

Returns Product belongs to a Host and productNo

### Example 
```python
from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = stylelens_product.ProductApi()
host_code = 'host_code_example' # str | 
product_no = 'product_no_example' # str | 

try: 
    # Get Product by hostCode and productNo
    api_response = api_instance.get_product_by_hostcode_and_product_no(host_code, product_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_product_by_hostcode_and_product_no: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_code** | **str**|  | 
 **product_no** | **str**|  | 

### Return type

[**GetProductResponse**](GetProductResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_by_id**
> GetProductResponse get_product_by_id(product_id)

Find Product by ID

Returns a single Product

### Example 
```python
from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = stylelens_product.ProductApi()
product_id = 'product_id_example' # str | ID of Product to return

try: 
    # Find Product by ID
    api_response = api_instance.get_product_by_id(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_product_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of Product to return | 

### Return type

[**GetProductResponse**](GetProductResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_products**
> GetProductsResponse get_products(file=file)

Query to search products



### Example 
```python
from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = stylelens_product.ProductApi()
file = '/path/to/file.txt' # file | Image file to upload (only support jpg format yet) (optional)

try: 
    # Query to search products
    api_response = api_instance.get_products(file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| Image file to upload (only support jpg format yet) | [optional] 

### Return type

[**GetProductsResponse**](GetProductsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

