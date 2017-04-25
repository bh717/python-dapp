# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1LabelSelectorRequirement(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, key=None, operator=None, values=None):
        """
        V1LabelSelectorRequirement - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'key': 'str',
            'operator': 'str',
            'values': 'list[str]'
        }

        self.attribute_map = {
            'key': 'key',
            'operator': 'operator',
            'values': 'values'
        }

        self._key = key
        self._operator = operator
        self._values = values

    @property
    def key(self):
        """
        Gets the key of this V1LabelSelectorRequirement.
        key is the label key that the selector applies to.

        :return: The key of this V1LabelSelectorRequirement.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this V1LabelSelectorRequirement.
        key is the label key that the selector applies to.

        :param key: The key of this V1LabelSelectorRequirement.
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def operator(self):
        """
        Gets the operator of this V1LabelSelectorRequirement.
        operator represents a key's relationship to a set of values. Valid operators ard In, NotIn, Exists and DoesNotExist.

        :return: The operator of this V1LabelSelectorRequirement.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this V1LabelSelectorRequirement.
        operator represents a key's relationship to a set of values. Valid operators ard In, NotIn, Exists and DoesNotExist.

        :param operator: The operator of this V1LabelSelectorRequirement.
        :type: str
        """
        if operator is None:
            raise ValueError("Invalid value for `operator`, must not be `None`")

        self._operator = operator

    @property
    def values(self):
        """
        Gets the values of this V1LabelSelectorRequirement.
        values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :return: The values of this V1LabelSelectorRequirement.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this V1LabelSelectorRequirement.
        values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

        :param values: The values of this V1LabelSelectorRequirement.
        :type: list[str]
        """

        self._values = values

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
