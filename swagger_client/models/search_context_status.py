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


class SearchContextStatus(object):
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
        'id': 'str',
        'search_status': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'search_status': 'SearchStatus'
    }

    def __init__(self, id=None, search_status=None):  # noqa: E501
        """SearchContextStatus - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._search_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if search_status is not None:
            self.search_status = search_status

    @property
    def id(self):
        """Gets the id of this SearchContextStatus.  # noqa: E501

        Gets or sets the identifier.  # noqa: E501

        :return: The id of this SearchContextStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SearchContextStatus.

        Gets or sets the identifier.  # noqa: E501

        :param id: The id of this SearchContextStatus.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def search_status(self):
        """Gets the search_status of this SearchContextStatus.  # noqa: E501

        Gets or sets the status.  # noqa: E501

        :return: The search_status of this SearchContextStatus.  # noqa: E501
        :rtype: str
        """
        return self._search_status

    @search_status.setter
    def search_status(self, search_status):
        """Sets the search_status of this SearchContextStatus.

        Gets or sets the status.  # noqa: E501

        :param search_status: The search_status of this SearchContextStatus.  # noqa: E501
        :type: str
        """

        self._search_status = search_status

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
        if issubclass(SearchContextStatus, dict):
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
        if not isinstance(other, SearchContextStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
