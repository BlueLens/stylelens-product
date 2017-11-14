from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_product.ProductApi()

try:
    # Delete a Product
    api_response = api_instance.delete_product_by_id('5a0ab9d8db467900017ae1db')
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->delete_product: %s\n" % e)