# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_capabilities import V1Capabilities


class TestV1Capabilities(unittest.TestCase):
    """ V1Capabilities unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1Capabilities(self):
        """
        Test V1Capabilities
        """
        model = kubernetes.client.models.v1_capabilities.V1Capabilities()


if __name__ == '__main__':
    unittest.main()
