from __future__ import print_function
from stylelens_product.bigquery.products import Products
from pprint import pprint
# create an instance of the API class

api_instance = Products(google_service_account_json='./service-account-file.json')

product = {}
product['asin'] = 'HC8000'

try:
  api_response = api_instance.add_product(product)
except Exception as e:
  print("Exception when calling add_product: %s\n" % e)
