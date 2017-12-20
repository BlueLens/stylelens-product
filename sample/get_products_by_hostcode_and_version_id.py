from __future__ import print_function
import time
import stylelens_product
from stylelens_product.products import Products
from pprint import pprint
# create an instance of the API class
api_instance = Products()

try:
    api_response = api_instance.get_products_by_host_code_and_version_id(host_code="HC0",
                                                                        version_id='1',
                                                                        offset=0,
                                                                        limit=10)
    pprint(api_response)
except Exception as e:
    print("Exception when calling ProductApi->get_products_by_hostcode_and_version_id: %s\n" % e)