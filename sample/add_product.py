from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_product.ProductApi()
product = stylelens_product.Product() # Product | Product object that needs to be added to the db.
feedback = stylelens_product.Feedback() # Product | Product object that needs to be added to the db.
writer = stylelens_product.Writer() # Product | Product object that needs to be added to the db.

product.product_url = "www.bluelens.io"
product.host_url = "www.8seconds.com"
product.host_code = "hc0001"
product.host_name = "8seconds"
product.name = "t-shirt"
product.tags = ['aaa', 'bbb']
product.price = 27100
product.currency_unit = 'KRW'
product.product_url = 'www.8seconds.com/product/xxxxx'
product.product_no = 'GM00391'
product.nation = 'kr'
product.main_image = 'images.8seconds.com/xxx/111.png'

sub_images = []
sub_images.append('images.8conds.com/xxx/111.png')
sub_images.append('images.8conds.com/xxx/112.png')
sub_images.append('images.8conds.com/xxx/113.png')
sub_images.append('images.8conds.com/xxx/114.png')
product.sub_images = sub_images

photos = []
photo = ['image.8seconds.com/yyy/111.png', 'xxx.png']
feedback.photo = photos.append(photo)
feedback.text = 'asdkfjsdlkfjsk'
feedback.write_date = "2017-11-14T08:34:12+00:00"
feedback.total_count = 12
feedback.likes = 7


writer.id = 'hahaha'
writer.grade = 'gold'
writer.height = 172
writer.weight = 62
writer.my_size = 'M'
writer.product_size = 'Small'
writer.color = 'red'

feedbacks = []
feedback.writer = writer

feedbacks.append(feedback)

product.feedback = feedbacks



try:
    # Added a new Product
    api_response = api_instance.add_product(product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->add_product: %s\n" % e)