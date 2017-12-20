from __future__ import print_function
from stylelens_product.products import Products
from pprint import pprint
# create an instance of the API class
api_instance = Products()

product = {}
product['host_code'] = 'HC1'
product['product_no'] = 'sss2'
product['version_id'] = '1'

try:
  api_response = api_instance.add_product(product)
  pprint(api_response)
except Exception as e:
  print("Exception when calling add_product: %s\n" % e)
