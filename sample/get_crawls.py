from __future__ import print_function
import time
import stylelens_product
from stylelens_product.crawls import Crawls
from pprint import pprint
# create an instance of the API class
api_instance = Crawls()

version_id = "11111j"


try:
    api_response = api_instance.get_crawls(version_id=version_id, status='todo')
    pprint(api_response)
except Exception as e:
    print("Exception when calling get_crawls: %s\n" % e)