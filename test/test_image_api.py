# coding: utf-8

"""
    bl-db-product

    This is a API document for Product DB

    OpenAPI spec version: 0.0.1
    Contact: master@bluehack.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import stylelens_product
from stylelens_product.rest import ApiException
from stylelens_product.apis.image_api import ImageApi


class TestImageApi(unittest.TestCase):
    """ ImageApi unit test stubs """

    def setUp(self):
        self.api = stylelens_product.apis.image_api.ImageApi()

    def tearDown(self):
        pass

    def test_add_image(self):
        """
        Test case for add_image

        Added a new Image
        """
        pass


if __name__ == '__main__':
    unittest.main()
