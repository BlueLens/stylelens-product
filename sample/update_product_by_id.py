from __future__ import print_function
from stylelens_product.products import Products
from pprint import pprint
# create an instance of the API class
api_instance = Products()

product = {}
product['host_code'] = 'HC1'
product['product_no'] = 'lll2'
product['version_id'] = '1'

try:
  api_response = api_instance.update_product_by_id("5a3a32a94dfd7d90b88e2a84", product)
  pprint(api_response)
except Exception as e:
  print("Exception when calling add_product: %s\n" % e)
