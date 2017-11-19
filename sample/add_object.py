from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_product.ObjectApi()
object = stylelens_product.Object() # Product | Product object that needs to be added to the db.

object.version = '1.0.0'
object.bucket = 'object'

try:
    # Added a new Object
    api_response = api_instance.add_object(object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->add_object: %s\n" % e)