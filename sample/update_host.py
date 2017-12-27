from __future__ import print_function
import time
import stylelens_product
from stylelens_product.hosts import Hosts
from pprint import pprint
# create an instance of the API class
api_instance = Hosts()

host = {}
host['host_code'] = "HC0062"
host['version_id'] = "1234"
host['crawl_status'] = "todo"

try:
    api_response = api_instance.update_host(host)
    pprint(api_response)
except Exception as e:
    print("Exception when calling update_host: %s\n" % e)