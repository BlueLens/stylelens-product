from __future__ import print_function
from stylelens_product.products import Products
from pprint import pprint
# create an instance of the API class
api_instance = Products()

product = {}
product['host_code'] = 'HC1'
product['product_no'] = 'sss1'
product['version_id'] = '1'

product2 = {}
product2['host_code'] = 'HC1'
product2['product_no'] = 'sss3'
product2['version_id'] = '1'

products = []
products.append(product)
products.append(product2)

try:
  api_response = api_instance.add_products(products)
except Exception as e:
  print("Exception when calling add_products1: %s\n" % e)
