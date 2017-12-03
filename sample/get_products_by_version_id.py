from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_product.ProductApi()

try:
    api_response = api_instance.get_products_by_version_id('5a2398d54fce095c804ad79c', )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_products_by_version_id: %s\n" % e)