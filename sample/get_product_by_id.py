from __future__ import print_function
import time
from stylelens_product.products import Products
from pprint import pprint
# create an instance of the API class
api_instance = Products()



try:
  res = api_instance.get_product_by_id("5a4e3f914dfd7d90b888598b")
  pprint(res)
except Exception as e:
    print("Exception when calling get_product_by_id: %s\n" % e)