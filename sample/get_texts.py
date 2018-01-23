from __future__ import print_function
from stylelens_product.hosts import Hosts
from stylelens_product.products import Products
from pprint import pprint
# create an instance of the API class
host_api = Hosts()
product_api = Products()

try:
    hosts = host_api.get_hosts()
    for host in hosts:
      products = product_api.get_products_by_hostcode_and_version_id(host['host_code'], offset=100, limit=1)
      for p in products:
        print('host_code: ' + p['host_code'])
        print('name     : ' + p['name'])
        print('cate     : ' + str(p['cate']))
        print('tags     : ' + str(p['tags']))
        print('_________')

except Exception as e:
    print("Exception when calling get_hosts: %s\n" % e)