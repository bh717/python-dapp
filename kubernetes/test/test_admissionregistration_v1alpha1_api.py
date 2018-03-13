# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.apis.admissionregistration_v1alpha1_api import AdmissionregistrationV1alpha1Api


class TestAdmissionregistrationV1alpha1Api(unittest.TestCase):
    """ AdmissionregistrationV1alpha1Api unit test stubs """

    def setUp(self):
        self.api = kubernetes.client.apis.admissionregistration_v1alpha1_api.AdmissionregistrationV1alpha1Api()

    def tearDown(self):
        pass

    def test_create_initializer_configuration(self):
        """
        Test case for create_initializer_configuration

        
        """
        pass

    def test_delete_collection_initializer_configuration(self):
        """
        Test case for delete_collection_initializer_configuration

        
        """
        pass

    def test_delete_initializer_configuration(self):
        """
        Test case for delete_initializer_configuration

        
        """
        pass

    def test_get_api_resources(self):
        """
        Test case for get_api_resources

        
        """
        pass

    def test_list_initializer_configuration(self):
        """
        Test case for list_initializer_configuration

        
        """
        pass

    def test_patch_initializer_configuration(self):
        """
        Test case for patch_initializer_configuration

        
        """
        pass

    def test_read_initializer_configuration(self):
        """
        Test case for read_initializer_configuration

        
        """
        pass

    def test_replace_initializer_configuration(self):
        """
        Test case for replace_initializer_configuration

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
