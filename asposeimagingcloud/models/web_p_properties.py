# coding: utf-8
# -----------------------------------------------------------------------------
# <copyright company="Aspose" file="WebPProperties.py">
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

import six


class WebPProperties(object):
    """Represents information about image in WEBP format.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'lossless': 'bool',
        'quality': 'float',
        'anim_loop_count': 'int',
        'anim_background_color': 'int'
    }

    attribute_map = {
        'lossless': 'Lossless',
        'quality': 'Quality',
        'anim_loop_count': 'AnimLoopCount',
        'anim_background_color': 'AnimBackgroundColor'
    }

    def __init__(self, lossless=None, quality=None, anim_loop_count=None, anim_background_color=None):
        """WebPProperties - a model defined in Swagger"""

        self._lossless = None
        self._quality = None
        self._anim_loop_count = None
        self._anim_background_color = None
        self.discriminator = None

        if lossless is not None:
            self.lossless = lossless
        if quality is not None:
            self.quality = quality
        if anim_loop_count is not None:
            self.anim_loop_count = anim_loop_count
        if anim_background_color is not None:
            self.anim_background_color = anim_background_color

    @property
    def lossless(self):
        """Gets the lossless of this WebPProperties.

        Gets or sets a value indicating whether these WebPOptions is lossless.

        :return: The lossless of this WebPProperties.
        :rtype: bool
        """
        return self._lossless

    @lossless.setter
    def lossless(self, lossless):
        """Sets the lossless of this WebPProperties.

        Gets or sets a value indicating whether these WebPOptions is lossless.

        :param lossless: The lossless of this WebPProperties.
        :type: bool
        """
        if lossless is None:
            raise ValueError("Invalid value for `lossless`, must not be `None`")
        self._lossless = lossless

    @property
    def quality(self):
        """Gets the quality of this WebPProperties.

        Gets or sets the quality.

        :return: The quality of this WebPProperties.
        :rtype: float
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """Sets the quality of this WebPProperties.

        Gets or sets the quality.

        :param quality: The quality of this WebPProperties.
        :type: float
        """
        if quality is None:
            raise ValueError("Invalid value for `quality`, must not be `None`")
        self._quality = quality

    @property
    def anim_loop_count(self):
        """Gets the anim_loop_count of this WebPProperties.

        Gets or sets the animation loop count.

        :return: The anim_loop_count of this WebPProperties.
        :rtype: int
        """
        return self._anim_loop_count

    @anim_loop_count.setter
    def anim_loop_count(self, anim_loop_count):
        """Sets the anim_loop_count of this WebPProperties.

        Gets or sets the animation loop count.

        :param anim_loop_count: The anim_loop_count of this WebPProperties.
        :type: int
        """
        if anim_loop_count is None:
            raise ValueError("Invalid value for `anim_loop_count`, must not be `None`")
        self._anim_loop_count = anim_loop_count

    @property
    def anim_background_color(self):
        """Gets the anim_background_color of this WebPProperties.

        Gets or sets the color of the animation background.

        :return: The anim_background_color of this WebPProperties.
        :rtype: int
        """
        return self._anim_background_color

    @anim_background_color.setter
    def anim_background_color(self, anim_background_color):
        """Sets the anim_background_color of this WebPProperties.

        Gets or sets the color of the animation background.

        :param anim_background_color: The anim_background_color of this WebPProperties.
        :type: int
        """
        if anim_background_color is None:
            raise ValueError("Invalid value for `anim_background_color`, must not be `None`")
        self._anim_background_color = anim_background_color

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
        if not isinstance(other, WebPProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
