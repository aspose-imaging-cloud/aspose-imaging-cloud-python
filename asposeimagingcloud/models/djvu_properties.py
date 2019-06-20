#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="djvu_properties.py">
#    Copyright (c) 2019 Aspose Pty Ltd. All rights reserved.
#  </copyright>
#  <summary>
#    Permission is hereby granted, free of charge, to any person obtaining a
#   copy  of this software and associated documentation files (the "Software"),
#   to deal  in the Software without restriction, including without limitation
#   the rights  to use, copy, modify, merge, publish, distribute, sublicense,
#   and/or sell  copies of the Software, and to permit persons to whom the
#   Software is  furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all  copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM,  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#   DEALINGS IN THE SOFTWARE.
#  </summary>
#  ----------------------------------------------------------------------------

import pprint
import re
import six


class DjvuProperties(object):
    """Represents properties of djvu file.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'background_color': 'str',
        'has_background_color': 'bool',
        'pages_count': 'int'
    }

    attribute_map = {
        'background_color': 'BackgroundColor',
        'has_background_color': 'HasBackgroundColor',
        'pages_count': 'PagesCount'
    }

    def __init__(
            self,
            background_color=None,
            has_background_color=None,
            pages_count=None):
        """DjvuProperties - a model defined in Swagger"""

        self._background_color = None
        self._has_background_color = None
        self._pages_count = None
        self.discriminator = None

        if background_color is not None:
            self.background_color = background_color
        if has_background_color is not None:
            self.has_background_color = has_background_color
        if pages_count is not None:
            self.pages_count = pages_count

    @property
    def background_color(self):
        """Gets the background_color of this DjvuProperties.

        Gets or sets background color.

        :return: The background_color of this DjvuProperties.
        :rtype: str
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Sets the background_color of this DjvuProperties.

        Gets or sets background color.

        :param background_color: The background_color of this DjvuProperties.
        :type: str
        """
        self._background_color = background_color

    @property
    def has_background_color(self):
        """Gets the has_background_color of this DjvuProperties.

        Gets or sets a value indicating whether background color is used.

        :return: The has_background_color of this DjvuProperties.
        :rtype: bool
        """
        return self._has_background_color

    @has_background_color.setter
    def has_background_color(self, has_background_color):
        """Sets the has_background_color of this DjvuProperties.

        Gets or sets a value indicating whether background color is used.

        :param has_background_color: The has_background_color of this DjvuProperties.
        :type: bool
        """
        if has_background_color is None:
            raise ValueError(
                "Invalid value for `has_background_color`, must not be `None`")
        self._has_background_color = has_background_color

    @property
    def pages_count(self):
        """Gets the pages_count of this DjvuProperties.

        Gets or sets pages count.

        :return: The pages_count of this DjvuProperties.
        :rtype: int
        """
        return self._pages_count

    @pages_count.setter
    def pages_count(self, pages_count):
        """Sets the pages_count of this DjvuProperties.

        Gets or sets pages count.

        :param pages_count: The pages_count of this DjvuProperties.
        :type: int
        """
        if pages_count is None:
            raise ValueError(
                "Invalid value for `pages_count`, must not be `None`")
        self._pages_count = pages_count

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
        if not isinstance(other, DjvuProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
