# coding: utf-8
# -----------------------------------------------------------------------------
# <copyright company="Aspose" file="search_context_status.py">
#   Copyright (c) 2019 Aspose Pty Ltd. All rights reserved.
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a
#  copy  of this software and associated documentation files (the "Software"),
#  to deal  in the Software without restriction, including without limitation
#  the rights  to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell  copies of the Software, and to permit persons to whom the
#  Software is  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM,  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------
import pprint
import re
import six


class SearchContextStatus(object):
    """Search context status.
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

    def __init__(self, id=None, search_status=None):
        """SearchContextStatus - a model defined in Swagger"""

        self._id = None
        self._search_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if search_status is not None:
            self.search_status = search_status

    @property
    def id(self):
        """Gets the id of this SearchContextStatus.

        Gets or sets the identifier.

        :return: The id of this SearchContextStatus.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SearchContextStatus.

        Gets or sets the identifier.

        :param id: The id of this SearchContextStatus.
        :type: str
        """
        self._id = id

    @property
    def search_status(self):
        """Gets the search_status of this SearchContextStatus.

        Gets or sets the status.

        :return: The search_status of this SearchContextStatus.
        :rtype: str
        """
        return self._search_status

    @search_status.setter
    def search_status(self, search_status):
        """Sets the search_status of this SearchContextStatus.

        Gets or sets the status.

        :param search_status: The search_status of this SearchContextStatus.
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
