from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_product.ProductApi()

product_ids = ['5a13a91f247c1a0001705196','5a13a920247c1a0001705198','5a0d7221db467900017ae1f4','5a0d722adb467900017ae224','5a0d722adb467900017ae226']
try:
    api_response = api_instance.get_products_by_ids(product_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_products_by_ids: %s\n" % e)