from __future__ import print_function
from stylelens_product.products import Products
from bson import ObjectId
from pprint import pprint
api_instance = Products()


products = []

product1 = {}

product1['_id'] = ObjectId("5a6715e936b7a0be34e7d728")
product1['is_processed_for_text_class_model'] = True

product2 = {}

product2['_id'] = ObjectId("5a6715e936b7a0be34e7d72b")
product2['is_processed_for_text_class_model'] = True

products.append(product1)
products.append(product2)

try:
    # Added a new Product
    api_response = api_instance.update_products(products)
    pprint(api_response)
except Exception as e:
    print("Exception when calling update_products: %s\n" % e)