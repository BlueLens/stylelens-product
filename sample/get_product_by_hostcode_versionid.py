from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_product.ProductApi()
product = stylelens_product.Product() # Product | Product object that needs to be added to the db.



try:
    api_response = api_instance.get_products_by_hostcode_and_version_id('HC0002', '5a2398d54fce095c804ad79c', is_indexed=True)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->add_product: %s\n" % e)