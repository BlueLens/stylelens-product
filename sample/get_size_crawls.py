from __future__ import print_function
from stylelens_product.crawls import Crawls
from pprint import pprint
# create an instance of the API class
api_instance = Crawls()

version_id = "5a47ccfe4dfd7d90b84eb710"

try:
    api_response = api_instance.get_size_crawls(version_id=version_id)
    pprint(api_response)
except Exception as e:
    print("Exception when calling get_size_crawls: %s\n" % e)