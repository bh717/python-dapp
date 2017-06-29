# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1NetworkPolicySpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, ingress=None, pod_selector=None):
        """
        V1NetworkPolicySpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'ingress': 'list[V1NetworkPolicyIngressRule]',
            'pod_selector': 'V1LabelSelector'
        }

        self.attribute_map = {
            'ingress': 'ingress',
            'pod_selector': 'podSelector'
        }

        self._ingress = ingress
        self._pod_selector = pod_selector

    @property
    def ingress(self):
        """
        Gets the ingress of this V1NetworkPolicySpec.
        List of ingress rules to be applied to the selected pods. Traffic is allowed to a pod if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic source is the pod's local node, OR if the traffic matches at least one ingress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy does not allow any traffic (and serves solely to ensure that the pods it selects are isolated by default)

        :return: The ingress of this V1NetworkPolicySpec.
        :rtype: list[V1NetworkPolicyIngressRule]
        """
        return self._ingress

    @ingress.setter
    def ingress(self, ingress):
        """
        Sets the ingress of this V1NetworkPolicySpec.
        List of ingress rules to be applied to the selected pods. Traffic is allowed to a pod if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic source is the pod's local node, OR if the traffic matches at least one ingress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy does not allow any traffic (and serves solely to ensure that the pods it selects are isolated by default)

        :param ingress: The ingress of this V1NetworkPolicySpec.
        :type: list[V1NetworkPolicyIngressRule]
        """

        self._ingress = ingress

    @property
    def pod_selector(self):
        """
        Gets the pod_selector of this V1NetworkPolicySpec.
        Selects the pods to which this NetworkPolicy object applies. The array of ingress rules is applied to any pods selected by this field. Multiple network policies can select the same set of pods. In this case, the ingress rules for each are combined additively. This field is NOT optional and follows standard label selector semantics. An empty podSelector matches all pods in this namespace.

        :return: The pod_selector of this V1NetworkPolicySpec.
        :rtype: V1LabelSelector
        """
        return self._pod_selector

    @pod_selector.setter
    def pod_selector(self, pod_selector):
        """
        Sets the pod_selector of this V1NetworkPolicySpec.
        Selects the pods to which this NetworkPolicy object applies. The array of ingress rules is applied to any pods selected by this field. Multiple network policies can select the same set of pods. In this case, the ingress rules for each are combined additively. This field is NOT optional and follows standard label selector semantics. An empty podSelector matches all pods in this namespace.

        :param pod_selector: The pod_selector of this V1NetworkPolicySpec.
        :type: V1LabelSelector
        """
        if pod_selector is None:
            raise ValueError("Invalid value for `pod_selector`, must not be `None`")

        self._pod_selector = pod_selector

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1NetworkPolicySpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
