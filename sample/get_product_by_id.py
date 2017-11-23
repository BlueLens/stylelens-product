from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_product.ProductApi()
product = stylelens_product.Product() # Product | Product object that needs to be added to the db.



try:
    api_response = api_instance.get_product_by_id('5a13a809247c1a0001704ecb')
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_products_by_id: %s\n" % e)