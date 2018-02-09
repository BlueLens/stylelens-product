from __future__ import print_function
from stylelens_product.products import Products
from pprint import pprint
api_instance = Products()

try:
    # Added a new Product
    api_response = api_instance.get_products_by_keyword('coating', only_text=True, is_processed_for_text_class_model=False, offset=0, limit=1000)
    pprint(api_response)
except Exception as e:
    print("Exception when calling ProductApi->get_products_by_keyword: %s\n" % e)