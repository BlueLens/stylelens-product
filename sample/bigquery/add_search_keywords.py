from __future__ import print_function
from stylelens_product.bigquery.amazon_search_keywords import AmazonSearchKeywords
from pprint import pprint
# create an instance of the API class

api_instance = AmazonSearchKeywords()

keywords = []
keyword = {}
keyword['keywords'] = 'sss2'
keyword['search_index'] = 'HC8000'
keyword['response_groups'] = 'HG8000'
keyword['browse_node'] = 'amazon'
keyword['sort'] = 'amazon'

keywords.append(keyword)

try:
  api_response = api_instance.add_keywords(keywords)
except Exception as e:
  print("Exception when calling add_keywords: %s\n" % e)
