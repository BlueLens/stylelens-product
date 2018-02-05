from __future__ import print_function
import time
import stylelens_product
from stylelens_product.models import Models
from pprint import pprint
# create an instance of the API class
api_instance = Models()

model = {}
model['type'] = 'text-classification'
model['version_id'] = '1111'
try:
    api_response = api_instance.get_model('text-classification', '1111')
    pprint(api_response)
except Exception as e:
    print("Exception when calling get_model: %s\n" % e)