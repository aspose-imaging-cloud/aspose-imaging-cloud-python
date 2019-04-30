# coding: utf-8

"""
    Aspose.Imaging Cloud API Reference

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DiscUsage(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'used_size': 'int',
        'total_size': 'int'
    }

    attribute_map = {
        'used_size': 'UsedSize',
        'total_size': 'TotalSize'
    }

    def __init__(self, used_size=None, total_size=None):  # noqa: E501
        """DiscUsage - a model defined in Swagger"""  # noqa: E501

        self._used_size = None
        self._total_size = None
        self.discriminator = None

        self.used_size = used_size
        self.total_size = total_size

    @property
    def used_size(self):
        """Gets the used_size of this DiscUsage.  # noqa: E501

        Application used disc space.  # noqa: E501

        :return: The used_size of this DiscUsage.  # noqa: E501
        :rtype: int
        """
        return self._used_size

    @used_size.setter
    def used_size(self, used_size):
        """Sets the used_size of this DiscUsage.

        Application used disc space.  # noqa: E501

        :param used_size: The used_size of this DiscUsage.  # noqa: E501
        :type: int
        """
        if used_size is None:
            raise ValueError("Invalid value for `used_size`, must not be `None`")  # noqa: E501

        self._used_size = used_size

    @property
    def total_size(self):
        """Gets the total_size of this DiscUsage.  # noqa: E501

        Total disc space.  # noqa: E501

        :return: The total_size of this DiscUsage.  # noqa: E501
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this DiscUsage.

        Total disc space.  # noqa: E501

        :param total_size: The total_size of this DiscUsage.  # noqa: E501
        :type: int
        """
        if total_size is None:
            raise ValueError("Invalid value for `total_size`, must not be `None`")  # noqa: E501

        self._total_size = total_size

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(DiscUsage, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DiscUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
