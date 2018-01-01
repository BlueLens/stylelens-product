from __future__ import print_function
import time
import stylelens_product
from stylelens_product.products import Products
from pprint import pprint
# create an instance of the API class
api_instance = Products()

version_id = "5a47ccfe4dfd7d90b84eb710"


try:
    api_response = api_instance.get_size_products(version_id=version_id)
    pprint('total products: ' + str(api_response))
    api_response = api_instance.get_size_products(version_id=version_id, is_processed=True)
    pprint('Processed products: ' + str(api_response))
    api_response = api_instance.get_size_products(version_id=version_id, is_classified=True)
    pprint('Classified products: ' + str(api_response))
except Exception as e:
    print("Exception when calling get_size_products: %s\n" % e)