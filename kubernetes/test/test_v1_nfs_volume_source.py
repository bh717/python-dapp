# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.1-660c2a2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_nfs_volume_source import V1NFSVolumeSource


class TestV1NFSVolumeSource(unittest.TestCase):
    """ V1NFSVolumeSource unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1NFSVolumeSource(self):
        """
        Test V1NFSVolumeSource
        """
        model = kubernetes.client.models.v1_nfs_volume_source.V1NFSVolumeSource()


if __name__ == '__main__':
    unittest.main()
