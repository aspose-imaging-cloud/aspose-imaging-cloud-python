# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="GifProperties.py">
#   Copyright (c) 2019 Aspose Pty Ltd. All rights reserved.
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
# 
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
# 
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------
import pprint
import re  # noqa: F401

import six


class GifProperties(object):
    """Represents information about image in GIF format.
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
        'has_trailer': 'bool',
        'pixel_aspect_ratio': 'int'
    }

    attribute_map = {
        'background_color': 'BackgroundColor',
        'has_background_color': 'HasBackgroundColor',
        'has_trailer': 'HasTrailer',
        'pixel_aspect_ratio': 'PixelAspectRatio'
    }

    def __init__(self, background_color=None, has_background_color=None, has_trailer=None, pixel_aspect_ratio=None):  # noqa: E501
        """GifProperties - a model defined in Swagger"""  # noqa: E501

        self._background_color = None
        self._has_background_color = None
        self._has_trailer = None
        self._pixel_aspect_ratio = None
        self.discriminator = None

        if background_color is not None:
            self.background_color = background_color
        if has_background_color is not None:
            self.has_background_color = has_background_color
        if has_trailer is not None:
            self.has_trailer = has_trailer
        if pixel_aspect_ratio is not None:
            self.pixel_aspect_ratio = pixel_aspect_ratio

    @property
    def background_color(self):
        """Gets the background_color of this GifProperties.  # noqa: E501

        Gets or sets the background color.  # noqa: E501

        :return: The background_color of this GifProperties.  # noqa: E501
        :rtype: str
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Sets the background_color of this GifProperties.

        Gets or sets the background color.  # noqa: E501

        :param background_color: The background_color of this GifProperties.  # noqa: E501
        :type: str
        """
        self._background_color = background_color

    @property
    def has_background_color(self):
        """Gets the has_background_color of this GifProperties.  # noqa: E501

        Gets or sets a value indicating whether background color is used.  # noqa: E501

        :return: The has_background_color of this GifProperties.  # noqa: E501
        :rtype: bool
        """
        return self._has_background_color

    @has_background_color.setter
    def has_background_color(self, has_background_color):
        """Sets the has_background_color of this GifProperties.

        Gets or sets a value indicating whether background color is used.  # noqa: E501

        :param has_background_color: The has_background_color of this GifProperties.  # noqa: E501
        :type: bool
        """
        if has_background_color is None:
            raise ValueError("Invalid value for `has_background_color`, must not be `None`")  # noqa: E501
        self._has_background_color = has_background_color

    @property
    def has_trailer(self):
        """Gets the has_trailer of this GifProperties.  # noqa: E501

        Gets or sets a value indicating whether image has trailer.  # noqa: E501

        :return: The has_trailer of this GifProperties.  # noqa: E501
        :rtype: bool
        """
        return self._has_trailer

    @has_trailer.setter
    def has_trailer(self, has_trailer):
        """Sets the has_trailer of this GifProperties.

        Gets or sets a value indicating whether image has trailer.  # noqa: E501

        :param has_trailer: The has_trailer of this GifProperties.  # noqa: E501
        :type: bool
        """
        if has_trailer is None:
            raise ValueError("Invalid value for `has_trailer`, must not be `None`")  # noqa: E501
        self._has_trailer = has_trailer

    @property
    def pixel_aspect_ratio(self):
        """Gets the pixel_aspect_ratio of this GifProperties.  # noqa: E501

        Gets or sets the pixel aspect ratio.  # noqa: E501

        :return: The pixel_aspect_ratio of this GifProperties.  # noqa: E501
        :rtype: int
        """
        return self._pixel_aspect_ratio

    @pixel_aspect_ratio.setter
    def pixel_aspect_ratio(self, pixel_aspect_ratio):
        """Sets the pixel_aspect_ratio of this GifProperties.

        Gets or sets the pixel aspect ratio.  # noqa: E501

        :param pixel_aspect_ratio: The pixel_aspect_ratio of this GifProperties.  # noqa: E501
        :type: int
        """
        if pixel_aspect_ratio is None:
            raise ValueError("Invalid value for `pixel_aspect_ratio`, must not be `None`")  # noqa: E501
        self._pixel_aspect_ratio = pixel_aspect_ratio

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
        if not isinstance(other, GifProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
