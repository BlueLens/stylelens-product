from __future__ import print_function
import time
import stylelens_product
from stylelens_product.products import Products
from pprint import pprint
# create an instance of the API class
api_instance = Products()

version_id = "11111j"


try:
    api_response = api_instance.get_size_not_classified(version_id=version_id)
    pprint(api_response)
except Exception as e:
    print("Exception when calling get_size_not_classified: %s\n" % e)