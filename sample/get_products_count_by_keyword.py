from __future__ import print_function
from stylelens_product.products import Products
from pprint import pprint
api_instance = Products()

try:
    # Added a new Product
    api_response = api_instance.get_products_count_by_keyword('재킷')
    pprint(api_response)
except Exception as e:
    print("Exception when calling ProductApi->get_products_count_by_keyword: %s\n" % e)