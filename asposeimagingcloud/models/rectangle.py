#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="rectangle.py">
#    Copyright (c) 2018-2020 Aspose Pty Ltd. All rights reserved.
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


class Rectangle(object):
    """
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'x': 'float',
        'y': 'float',
        'width': 'float',
        'height': 'float'
    }

    attribute_map = {
        'x': 'X',
        'y': 'Y',
        'width': 'Width',
        'height': 'Height'
    }

    def __init__(self, x=None, y=None, width=None, height=None):
        """Rectangle - a model defined in Swagger"""
        super(Rectangle, self).__init__()

        self._x = None
        self._y = None
        self._width = None
        self._height = None

        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

    @property
    def x(self):
        """Gets the x of this Rectangle.


        :return: The x of this Rectangle.
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this Rectangle.


        :param x: The x of this Rectangle.
        :type: float
        """
        if x is None:
            raise ValueError("Invalid value for `x`, must not be `None`")
        self._x = x

    @property
    def y(self):
        """Gets the y of this Rectangle.


        :return: The y of this Rectangle.
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this Rectangle.


        :param y: The y of this Rectangle.
        :type: float
        """
        if y is None:
            raise ValueError("Invalid value for `y`, must not be `None`")
        self._y = y

    @property
    def width(self):
        """Gets the width of this Rectangle.


        :return: The width of this Rectangle.
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Rectangle.


        :param width: The width of this Rectangle.
        :type: float
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")
        self._width = width

    @property
    def height(self):
        """Gets the height of this Rectangle.


        :return: The height of this Rectangle.
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Rectangle.


        :param height: The height of this Rectangle.
        :type: float
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")
        self._height = height

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
        if not isinstance(other, Rectangle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
