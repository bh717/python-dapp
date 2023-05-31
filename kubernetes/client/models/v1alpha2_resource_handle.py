# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.27
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1alpha2ResourceHandle(object):
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
        'data': 'str',
        'driver_name': 'str'
    }

    attribute_map = {
        'data': 'data',
        'driver_name': 'driverName'
    }

    def __init__(self, data=None, driver_name=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha2ResourceHandle - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data = None
        self._driver_name = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if driver_name is not None:
            self.driver_name = driver_name

    @property
    def data(self):
        """Gets the data of this V1alpha2ResourceHandle.  # noqa: E501

        Data contains the opaque data associated with this ResourceHandle. It is set by the controller component of the resource driver whose name matches the DriverName set in the ResourceClaimStatus this ResourceHandle is embedded in. It is set at allocation time and is intended for processing by the kubelet plugin whose name matches the DriverName set in this ResourceHandle.  The maximum size of this field is 16KiB. This may get increased in the future, but not reduced.  # noqa: E501

        :return: The data of this V1alpha2ResourceHandle.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this V1alpha2ResourceHandle.

        Data contains the opaque data associated with this ResourceHandle. It is set by the controller component of the resource driver whose name matches the DriverName set in the ResourceClaimStatus this ResourceHandle is embedded in. It is set at allocation time and is intended for processing by the kubelet plugin whose name matches the DriverName set in this ResourceHandle.  The maximum size of this field is 16KiB. This may get increased in the future, but not reduced.  # noqa: E501

        :param data: The data of this V1alpha2ResourceHandle.  # noqa: E501
        :type: str
        """

        self._data = data

    @property
    def driver_name(self):
        """Gets the driver_name of this V1alpha2ResourceHandle.  # noqa: E501

        DriverName specifies the name of the resource driver whose kubelet plugin should be invoked to process this ResourceHandle's data once it lands on a node. This may differ from the DriverName set in ResourceClaimStatus this ResourceHandle is embedded in.  # noqa: E501

        :return: The driver_name of this V1alpha2ResourceHandle.  # noqa: E501
        :rtype: str
        """
        return self._driver_name

    @driver_name.setter
    def driver_name(self, driver_name):
        """Sets the driver_name of this V1alpha2ResourceHandle.

        DriverName specifies the name of the resource driver whose kubelet plugin should be invoked to process this ResourceHandle's data once it lands on a node. This may differ from the DriverName set in ResourceClaimStatus this ResourceHandle is embedded in.  # noqa: E501

        :param driver_name: The driver_name of this V1alpha2ResourceHandle.  # noqa: E501
        :type: str
        """

        self._driver_name = driver_name

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
        if not isinstance(other, V1alpha2ResourceHandle):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha2ResourceHandle):
            return True

        return self.to_dict() != other.to_dict()
