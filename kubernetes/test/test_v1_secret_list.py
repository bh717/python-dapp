# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_secret_list import V1SecretList


class TestV1SecretList(unittest.TestCase):
    """ V1SecretList unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1SecretList(self):
        """
        Test V1SecretList
        """
        model = kubernetes.client.models.v1_secret_list.V1SecretList()


if __name__ == '__main__':
    unittest.main()
