from __future__ import print_function
import time
import stylelens_product
from stylelens_product.hosts import Hosts
from pprint import pprint
# create an instance of the API class
api_instance = Hosts()

host = {}
host['host_code'] = "HC0008"

try:
    api_response = api_instance.add_host(host)
    pprint(api_response)
except Exception as e:
    print("Exception when calling add_host: %s\n" % e)