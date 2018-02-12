from __future__ import print_function
from stylelens_product.products import Products
from pprint import pprint
api_instance = Products()

try:
    # api_response = api_instance.get_products_by_keyword('Coat', only_text=True, is_processed_for_text_class_model=False, offset=0, limit=100)
    # pprint(api_response)

    keyword = 'coat'
    test_str = 'coating'

    offset = 0
    limit = 100

    while True:
        api_response = api_instance.get_products_by_keyword(keyword, only_text=True,
                                                            is_processed_for_text_class_model=False,
                                                            offset=offset,
                                                            limit=limit)

        # pprint(api_response)

        for res in api_response:
            name = res.get('name')
            if test_str in name:
                pprint(test_str + ' in keyword: ' + keyword)
                pprint(name)
                pprint(res.get('cate'))
                pprint(res.get('tags'))

        if limit > len(api_response):
            break
        else:
            offset = offset + limit
except Exception as e:
    print("Exception when calling ProductApi->get_products_by_keyword: %s\n" % e)