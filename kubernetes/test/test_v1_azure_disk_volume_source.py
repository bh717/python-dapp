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
from kubernetes.client.models.v1_azure_disk_volume_source import V1AzureDiskVolumeSource


class TestV1AzureDiskVolumeSource(unittest.TestCase):
    """ V1AzureDiskVolumeSource unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1AzureDiskVolumeSource(self):
        """
        Test V1AzureDiskVolumeSource
        """
        model = kubernetes.client.models.v1_azure_disk_volume_source.V1AzureDiskVolumeSource()


if __name__ == '__main__':
    unittest.main()
