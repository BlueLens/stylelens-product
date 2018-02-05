from __future__ import print_function
import time
import stylelens_product
from stylelens_product.models import Models
from pprint import pprint
# create an instance of the API class
api_instance = Models()

try:
    api_response = api_instance.add_model('text-classification', '1111')
    pprint(api_response)
except Exception as e:
    print("Exception when calling add_model: %s\n" % e)