from __future__ import print_function
from stylelens_product.hosts import Hosts
from pprint import pprint
# create an instance of the API class
api_instance = Hosts()

try:
    api_response = api_instance.get_hosts()
    pprint(api_response)
except Exception as e:
    print("Exception when calling get_hosts: %s\n" % e)