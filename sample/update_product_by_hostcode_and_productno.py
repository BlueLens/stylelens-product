from __future__ import print_function
from stylelens_product.products import Products
from pprint import pprint

api_instance = Products()

product = {}
product['host_code'] = 'HC1'
product['product_no'] = 'lll2'
product['price'] = '1'

try:
    api_response = api_instance.update_product_by_hostcode_and_productno(product)
    pprint(api_response)
except Exception as e:
    print("Exception when calling ProductApi->update_product_by_id: %s\n" % e)