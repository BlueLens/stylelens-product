from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_product.HostApi()

host = {}
host['host_code'] = "HCxxxx1"

try:
    api_response = api_instance.add_host(host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->add_host: %s\n" % e)