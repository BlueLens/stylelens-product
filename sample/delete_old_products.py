from __future__ import print_function
import time
import stylelens_product
from stylelens_product.products import Products
from pprint import pprint
# create an instance of the API class
api_instance = Products()

try:
    api_response = api_instance.delete_old_products(version_id="5a7809f1567d6814379f9203")
    pprint(api_response)
except Exception as e:
    print("Exception when calling delete_old_products: %s\n" % e)