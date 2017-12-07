from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_product.VersionApi()
version = stylelens_product.Version()

version.name = "test7"

try:
    # Added a new Version
    api_response = api_instance.add_version(version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionApi->add_version: %s\n" % e)