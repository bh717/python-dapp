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
from kubernetes.client.models.v1alpha1_certificate_signing_request_condition import V1alpha1CertificateSigningRequestCondition


class TestV1alpha1CertificateSigningRequestCondition(unittest.TestCase):
    """ V1alpha1CertificateSigningRequestCondition unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1alpha1CertificateSigningRequestCondition(self):
        """
        Test V1alpha1CertificateSigningRequestCondition
        """
        model = kubernetes.client.models.v1alpha1_certificate_signing_request_condition.V1alpha1CertificateSigningRequestCondition()


if __name__ == '__main__':
    unittest.main()
