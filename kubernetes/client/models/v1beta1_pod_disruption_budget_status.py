# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.20
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1beta1PodDisruptionBudgetStatus(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'current_healthy': 'int',
        'desired_healthy': 'int',
        'disrupted_pods': 'dict(str, datetime)',
        'disruptions_allowed': 'int',
        'expected_pods': 'int',
        'observed_generation': 'int'
    }

    attribute_map = {
        'current_healthy': 'currentHealthy',
        'desired_healthy': 'desiredHealthy',
        'disrupted_pods': 'disruptedPods',
        'disruptions_allowed': 'disruptionsAllowed',
        'expected_pods': 'expectedPods',
        'observed_generation': 'observedGeneration'
    }

    def __init__(self, current_healthy=None, desired_healthy=None, disrupted_pods=None, disruptions_allowed=None, expected_pods=None, observed_generation=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1PodDisruptionBudgetStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._current_healthy = None
        self._desired_healthy = None
        self._disrupted_pods = None
        self._disruptions_allowed = None
        self._expected_pods = None
        self._observed_generation = None
        self.discriminator = None

        self.current_healthy = current_healthy
        self.desired_healthy = desired_healthy
        if disrupted_pods is not None:
            self.disrupted_pods = disrupted_pods
        self.disruptions_allowed = disruptions_allowed
        self.expected_pods = expected_pods
        if observed_generation is not None:
            self.observed_generation = observed_generation

    @property
    def current_healthy(self):
        """Gets the current_healthy of this V1beta1PodDisruptionBudgetStatus.  # noqa: E501

        current number of healthy pods  # noqa: E501

        :return: The current_healthy of this V1beta1PodDisruptionBudgetStatus.  # noqa: E501
        :rtype: int
        """
        return self._current_healthy

    @current_healthy.setter
    def current_healthy(self, current_healthy):
        """Sets the current_healthy of this V1beta1PodDisruptionBudgetStatus.

        current number of healthy pods  # noqa: E501

        :param current_healthy: The current_healthy of this V1beta1PodDisruptionBudgetStatus.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and current_healthy is None:  # noqa: E501
            raise ValueError("Invalid value for `current_healthy`, must not be `None`")  # noqa: E501

        self._current_healthy = current_healthy

    @property
    def desired_healthy(self):
        """Gets the desired_healthy of this V1beta1PodDisruptionBudgetStatus.  # noqa: E501

        minimum desired number of healthy pods  # noqa: E501

        :return: The desired_healthy of this V1beta1PodDisruptionBudgetStatus.  # noqa: E501
        :rtype: int
        """
        return self._desired_healthy

    @desired_healthy.setter
    def desired_healthy(self, desired_healthy):
        """Sets the desired_healthy of this V1beta1PodDisruptionBudgetStatus.

        minimum desired number of healthy pods  # noqa: E501

        :param desired_healthy: The desired_healthy of this V1beta1PodDisruptionBudgetStatus.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and desired_healthy is None:  # noqa: E501
            raise ValueError("Invalid value for `desired_healthy`, must not be `None`")  # noqa: E501

        self._desired_healthy = desired_healthy

    @property
    def disrupted_pods(self):
        """Gets the disrupted_pods of this V1beta1PodDisruptionBudgetStatus.  # noqa: E501

        DisruptedPods contains information about pods whose eviction was processed by the API server eviction subresource handler but has not yet been observed by the PodDisruptionBudget controller. A pod will be in this map from the time when the API server processed the eviction request to the time when the pod is seen by PDB controller as having been marked for deletion (or after a timeout). The key in the map is the name of the pod and the value is the time when the API server processed the eviction request. If the deletion didn't occur and a pod is still there it will be removed from the list automatically by PodDisruptionBudget controller after some time. If everything goes smooth this map should be empty for the most of the time. Large number of entries in the map may indicate problems with pod deletions.  # noqa: E501

        :return: The disrupted_pods of this V1beta1PodDisruptionBudgetStatus.  # noqa: E501
        :rtype: dict(str, datetime)
        """
        return self._disrupted_pods

    @disrupted_pods.setter
    def disrupted_pods(self, disrupted_pods):
        """Sets the disrupted_pods of this V1beta1PodDisruptionBudgetStatus.

        DisruptedPods contains information about pods whose eviction was processed by the API server eviction subresource handler but has not yet been observed by the PodDisruptionBudget controller. A pod will be in this map from the time when the API server processed the eviction request to the time when the pod is seen by PDB controller as having been marked for deletion (or after a timeout). The key in the map is the name of the pod and the value is the time when the API server processed the eviction request. If the deletion didn't occur and a pod is still there it will be removed from the list automatically by PodDisruptionBudget controller after some time. If everything goes smooth this map should be empty for the most of the time. Large number of entries in the map may indicate problems with pod deletions.  # noqa: E501

        :param disrupted_pods: The disrupted_pods of this V1beta1PodDisruptionBudgetStatus.  # noqa: E501
        :type: dict(str, datetime)
        """

        self._disrupted_pods = disrupted_pods

    @property
    def disruptions_allowed(self):
        """Gets the disruptions_allowed of this V1beta1PodDisruptionBudgetStatus.  # noqa: E501

        Number of pod disruptions that are currently allowed.  # noqa: E501

        :return: The disruptions_allowed of this V1beta1PodDisruptionBudgetStatus.  # noqa: E501
        :rtype: int
        """
        return self._disruptions_allowed

    @disruptions_allowed.setter
    def disruptions_allowed(self, disruptions_allowed):
        """Sets the disruptions_allowed of this V1beta1PodDisruptionBudgetStatus.

        Number of pod disruptions that are currently allowed.  # noqa: E501

        :param disruptions_allowed: The disruptions_allowed of this V1beta1PodDisruptionBudgetStatus.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and disruptions_allowed is None:  # noqa: E501
            raise ValueError("Invalid value for `disruptions_allowed`, must not be `None`")  # noqa: E501

        self._disruptions_allowed = disruptions_allowed

    @property
    def expected_pods(self):
        """Gets the expected_pods of this V1beta1PodDisruptionBudgetStatus.  # noqa: E501

        total number of pods counted by this disruption budget  # noqa: E501

        :return: The expected_pods of this V1beta1PodDisruptionBudgetStatus.  # noqa: E501
        :rtype: int
        """
        return self._expected_pods

    @expected_pods.setter
    def expected_pods(self, expected_pods):
        """Sets the expected_pods of this V1beta1PodDisruptionBudgetStatus.

        total number of pods counted by this disruption budget  # noqa: E501

        :param expected_pods: The expected_pods of this V1beta1PodDisruptionBudgetStatus.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and expected_pods is None:  # noqa: E501
            raise ValueError("Invalid value for `expected_pods`, must not be `None`")  # noqa: E501

        self._expected_pods = expected_pods

    @property
    def observed_generation(self):
        """Gets the observed_generation of this V1beta1PodDisruptionBudgetStatus.  # noqa: E501

        Most recent generation observed when updating this PDB status. DisruptionsAllowed and other status information is valid only if observedGeneration equals to PDB's object generation.  # noqa: E501

        :return: The observed_generation of this V1beta1PodDisruptionBudgetStatus.  # noqa: E501
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """Sets the observed_generation of this V1beta1PodDisruptionBudgetStatus.

        Most recent generation observed when updating this PDB status. DisruptionsAllowed and other status information is valid only if observedGeneration equals to PDB's object generation.  # noqa: E501

        :param observed_generation: The observed_generation of this V1beta1PodDisruptionBudgetStatus.  # noqa: E501
        :type: int
        """

        self._observed_generation = observed_generation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta1PodDisruptionBudgetStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1PodDisruptionBudgetStatus):
            return True

        return self.to_dict() != other.to_dict()
