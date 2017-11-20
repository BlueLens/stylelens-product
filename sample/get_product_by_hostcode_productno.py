from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_product.ProductApi()
product = stylelens_product.Product() # Product | Product object that needs to be added to the db.



try:
    # Added a new Product
    api_response = api_instance.get_products_by_hostcode_and_product_no('HC0002', '949')
    product = product
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->add_product: %s\n" % e)