from __future__ import print_function
from stylelens_product.bigquery.products import Products
from pprint import pprint
# create an instance of the API class

api_instance = Products()

product = {}
product['product_id'] = 'sss2'
product['host_code'] = 'HC8000'
product['host_group'] = 'HG8000'
product['host_name'] = 'amazon'

try:
  api_response = api_instance.add_product(product)
except Exception as e:
  print("Exception when calling add_product: %s\n" % e)
