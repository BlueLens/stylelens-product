from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_product.ProductApi()

try:
    # Added a new Product
    api_response = api_instance.get_products_by_hostcode('HC0002', offset=1, limit=2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_products_by_hostcode: %s\n" % e)