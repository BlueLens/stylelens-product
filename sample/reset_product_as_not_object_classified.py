from __future__ import print_function
from stylelens_product.products import Products
from pprint import pprint
# create an instance of the API class
api_instance = Products()

try:
  api_response = api_instance.reset_product_as_not_object_classified()
  pprint(api_response)
except Exception as e:
  print("Exception when calling add_product: %s\n" % e)
