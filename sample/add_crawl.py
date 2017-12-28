from __future__ import print_function
import time
import stylelens_product
from stylelens_product.crawls import Crawls
from pprint import pprint
# create an instance of the API class
api_instance = Crawls()

crawl = {}
crawl['host_code'] = "HCBOK1"
crawl['version_id'] = "11111j"


try:
    api_response = api_instance.add_crawl(crawl)
    pprint(api_response)
except Exception as e:
    print("Exception when calling add_crawl: %s\n" % e)