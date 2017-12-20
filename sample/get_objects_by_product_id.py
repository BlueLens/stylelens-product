from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_product.ObjectApi()
object = stylelens_product.Object() # Product | Product object that needs to be added to the db.



try:
    # Get a object
    api_response = api_instance.get_object_by_id("5a13a92a247c1a00017051c2")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->add_product: %s\n" % e)