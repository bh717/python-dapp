# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v2alpha1_metric_status import V2alpha1MetricStatus


class TestV2alpha1MetricStatus(unittest.TestCase):
    """ V2alpha1MetricStatus unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV2alpha1MetricStatus(self):
        """
        Test V2alpha1MetricStatus
        """
        model = kubernetes.client.models.v2alpha1_metric_status.V2alpha1MetricStatus()


if __name__ == '__main__':
    unittest.main()
