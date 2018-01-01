from __future__ import print_function
import time
from stylelens_product.products import Products
from pprint import pprint
# create an instance of the API class
api_instance = Products()

try:
    api_response = api_instance.get_products_by_version_id('5a47ccfe4dfd7d90b84eb710')
    pprint(api_response)
    api_response = api_instance.get_products_by_version_id('5a47ccfe4dfd7d90b84eb710', is_classified=False, is_processed=True)
    pprint(api_response)
except Exception as e:
    print("Exception when calling get_products_by_version_id: %s\n" % e)