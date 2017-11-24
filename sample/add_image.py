from __future__ import print_function
import stylelens_product
from stylelens_product.models.box_object import BoxObject
from stylelens_product.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_product.ImageApi()
image = stylelens_product.Image() # Product | Product object that needs to be added to the db.
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

products = []
products.append(product)
boxes_array = []
box_obj = BoxObject()
box_array = [0.323, 0.232325, 4.232, 452.11]

box_obj.box = box_array
box_obj.products = products

boxes_array.append(box_obj)

image.url = "http://xxx.yyy"
image.boxes = boxes_array


try:
    # Added a new Image
    api_response = api_instance.add_image(image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->add_product: %s\n" % e)