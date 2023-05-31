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


class V1beta2QueuingConfiguration(object):
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
        'hand_size': 'int',
        'queue_length_limit': 'int',
        'queues': 'int'
    }

    attribute_map = {
        'hand_size': 'handSize',
        'queue_length_limit': 'queueLengthLimit',
        'queues': 'queues'
    }

    def __init__(self, hand_size=None, queue_length_limit=None, queues=None, local_vars_configuration=None):  # noqa: E501
        """V1beta2QueuingConfiguration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hand_size = None
        self._queue_length_limit = None
        self._queues = None
        self.discriminator = None

        if hand_size is not None:
            self.hand_size = hand_size
        if queue_length_limit is not None:
            self.queue_length_limit = queue_length_limit
        if queues is not None:
            self.queues = queues

    @property
    def hand_size(self):
        """Gets the hand_size of this V1beta2QueuingConfiguration.  # noqa: E501

        `handSize` is a small positive number that configures the shuffle sharding of requests into queues.  When enqueuing a request at this priority level the request's flow identifier (a string pair) is hashed and the hash value is used to shuffle the list of queues and deal a hand of the size specified here.  The request is put into one of the shortest queues in that hand. `handSize` must be no larger than `queues`, and should be significantly smaller (so that a few heavy flows do not saturate most of the queues).  See the user-facing documentation for more extensive guidance on setting this field.  This field has a default value of 8.  # noqa: E501

        :return: The hand_size of this V1beta2QueuingConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._hand_size

    @hand_size.setter
    def hand_size(self, hand_size):
        """Sets the hand_size of this V1beta2QueuingConfiguration.

        `handSize` is a small positive number that configures the shuffle sharding of requests into queues.  When enqueuing a request at this priority level the request's flow identifier (a string pair) is hashed and the hash value is used to shuffle the list of queues and deal a hand of the size specified here.  The request is put into one of the shortest queues in that hand. `handSize` must be no larger than `queues`, and should be significantly smaller (so that a few heavy flows do not saturate most of the queues).  See the user-facing documentation for more extensive guidance on setting this field.  This field has a default value of 8.  # noqa: E501

        :param hand_size: The hand_size of this V1beta2QueuingConfiguration.  # noqa: E501
        :type: int
        """

        self._hand_size = hand_size

    @property
    def queue_length_limit(self):
        """Gets the queue_length_limit of this V1beta2QueuingConfiguration.  # noqa: E501

        `queueLengthLimit` is the maximum number of requests allowed to be waiting in a given queue of this priority level at a time; excess requests are rejected.  This value must be positive.  If not specified, it will be defaulted to 50.  # noqa: E501

        :return: The queue_length_limit of this V1beta2QueuingConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._queue_length_limit

    @queue_length_limit.setter
    def queue_length_limit(self, queue_length_limit):
        """Sets the queue_length_limit of this V1beta2QueuingConfiguration.

        `queueLengthLimit` is the maximum number of requests allowed to be waiting in a given queue of this priority level at a time; excess requests are rejected.  This value must be positive.  If not specified, it will be defaulted to 50.  # noqa: E501

        :param queue_length_limit: The queue_length_limit of this V1beta2QueuingConfiguration.  # noqa: E501
        :type: int
        """

        self._queue_length_limit = queue_length_limit

    @property
    def queues(self):
        """Gets the queues of this V1beta2QueuingConfiguration.  # noqa: E501

        `queues` is the number of queues for this priority level. The queues exist independently at each apiserver. The value must be positive.  Setting it to 1 effectively precludes shufflesharding and thus makes the distinguisher method of associated flow schemas irrelevant.  This field has a default value of 64.  # noqa: E501

        :return: The queues of this V1beta2QueuingConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._queues

    @queues.setter
    def queues(self, queues):
        """Sets the queues of this V1beta2QueuingConfiguration.

        `queues` is the number of queues for this priority level. The queues exist independently at each apiserver. The value must be positive.  Setting it to 1 effectively precludes shufflesharding and thus makes the distinguisher method of associated flow schemas irrelevant.  This field has a default value of 64.  # noqa: E501

        :param queues: The queues of this V1beta2QueuingConfiguration.  # noqa: E501
        :type: int
        """

        self._queues = queues

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
        if not isinstance(other, V1beta2QueuingConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta2QueuingConfiguration):
            return True

        return self.to_dict() != other.to_dict()
