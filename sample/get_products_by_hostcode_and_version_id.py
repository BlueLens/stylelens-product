from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_product.ProductApi()

try:
    api_response = api_instance.get_products_by_hostcode_and_version_id(host_code="HC0003",
                                                                        version_id='5a2957c74fce095c804de444',
                                                                        is_indexed=False,
                                                                        offset=0,
                                                                        limit=10)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_products_by_hostcode_and_version_id: %s\n" % e)