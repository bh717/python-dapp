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
from kubernetes.client.models.v1beta1_run_as_user_strategy_options import V1beta1RunAsUserStrategyOptions


class TestV1beta1RunAsUserStrategyOptions(unittest.TestCase):
    """ V1beta1RunAsUserStrategyOptions unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1RunAsUserStrategyOptions(self):
        """
        Test V1beta1RunAsUserStrategyOptions
        """
        model = kubernetes.client.models.v1beta1_run_as_user_strategy_options.V1beta1RunAsUserStrategyOptions()


if __name__ == '__main__':
    unittest.main()
