# stylelens_product.ProductApi

All URIs are relative to *http://product.stylelens.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_product**](ProductApi.md#add_product) | **POST** /products | Added a new Product
[**delete_product_by_id**](ProductApi.md#delete_product_by_id) | **DELETE** /products/{productId} | Deletes a Product
[**get_product_by_id**](ProductApi.md#get_product_by_id) | **GET** /products/{productId} | Find Product by ID
[**get_products_by_hostcode**](ProductApi.md#get_products_by_hostcode) | **GET** /products/hosts/{hostCode} | Get Product by host_code
[**update_product**](ProductApi.md#update_product) | **PUT** /products | Update an existing Product


# **add_product**
> AddProductResponse add_product(body)

Added a new Product



### Example 
```python
from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = stylelens_product.ProductApi()
body = stylelens_product.Product() # Product | Product object that needs to be added to the db.

try: 
    # Added a new Product
    api_response = api_instance.add_product(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->add_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Product**](Product.md)| Product object that needs to be added to the db. | 

### Return type

[**AddProductResponse**](AddProductResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_product_by_id**
> DeleteProductResponse delete_product_by_id(product_id)

Deletes a Product



### Example 
```python
from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = stylelens_product.ProductApi()
product_id = 'product_id_example' # str | Product id to delete

try: 
    # Deletes a Product
    api_response = api_instance.delete_product_by_id(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->delete_product_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product id to delete | 

### Return type

[**DeleteProductResponse**](DeleteProductResponse.md)

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

# **get_products_by_hostcode**
> GetProductsResponse get_products_by_hostcode(host_code)

Get Product by host_code

Returns Products belongs to a Host

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

try: 
    # Get Product by host_code
    api_response = api_instance.get_products_by_hostcode(host_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_products_by_hostcode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_code** | **str**|  | 

### Return type

[**GetProductsResponse**](GetProductsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product**
> UpdateProductResponse update_product(body)

Update an existing Product



### Example 
```python
from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = stylelens_product.ProductApi()
body = stylelens_product.Product() # Product | Product object that needs to be updated to the store

try: 
    # Update an existing Product
    api_response = api_instance.update_product(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->update_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Product**](Product.md)| Product object that needs to be updated to the store | 

### Return type

[**UpdateProductResponse**](UpdateProductResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

