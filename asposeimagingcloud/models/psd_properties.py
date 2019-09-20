#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="psd_properties.py">
#    Copyright (c) 2018-2019 Aspose Pty Ltd. All rights reserved.
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


class PsdProperties(object):
    """Represents information about PSD image
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bits_per_channel': 'int',
        'channels_count': 'int',
        'color_mode': 'str',
        'compression': 'str'
    }

    attribute_map = {
        'bits_per_channel': 'BitsPerChannel',
        'channels_count': 'ChannelsCount',
        'color_mode': 'ColorMode',
        'compression': 'Compression'
    }

    def __init__(self, bits_per_channel=None, channels_count=None, color_mode=None, compression=None):
        """PsdProperties - a model defined in Swagger"""
        super(PsdProperties, self).__init__()

        self._bits_per_channel = None
        self._channels_count = None
        self._color_mode = None
        self._compression = None

        if bits_per_channel is not None:
            self.bits_per_channel = bits_per_channel
        if channels_count is not None:
            self.channels_count = channels_count
        if color_mode is not None:
            self.color_mode = color_mode
        if compression is not None:
            self.compression = compression

    @property
    def bits_per_channel(self):
        """Gets the bits_per_channel of this PsdProperties.

        Gets or sets the bits per channel.

        :return: The bits_per_channel of this PsdProperties.
        :rtype: int
        """
        return self._bits_per_channel

    @bits_per_channel.setter
    def bits_per_channel(self, bits_per_channel):
        """Sets the bits_per_channel of this PsdProperties.

        Gets or sets the bits per channel.

        :param bits_per_channel: The bits_per_channel of this PsdProperties.
        :type: int
        """
        if bits_per_channel is None:
            raise ValueError("Invalid value for `bits_per_channel`, must not be `None`")
        self._bits_per_channel = bits_per_channel

    @property
    def channels_count(self):
        """Gets the channels_count of this PsdProperties.

        Gets or sets the channels count.

        :return: The channels_count of this PsdProperties.
        :rtype: int
        """
        return self._channels_count

    @channels_count.setter
    def channels_count(self, channels_count):
        """Sets the channels_count of this PsdProperties.

        Gets or sets the channels count.

        :param channels_count: The channels_count of this PsdProperties.
        :type: int
        """
        if channels_count is None:
            raise ValueError("Invalid value for `channels_count`, must not be `None`")
        self._channels_count = channels_count

    @property
    def color_mode(self):
        """Gets the color_mode of this PsdProperties.

        Gets or sets the color mode.

        :return: The color_mode of this PsdProperties.
        :rtype: str
        """
        return self._color_mode

    @color_mode.setter
    def color_mode(self, color_mode):
        """Sets the color_mode of this PsdProperties.

        Gets or sets the color mode.

        :param color_mode: The color_mode of this PsdProperties.
        :type: str
        """
        self._color_mode = color_mode

    @property
    def compression(self):
        """Gets the compression of this PsdProperties.

        Gets or sets the compression.

        :return: The compression of this PsdProperties.
        :rtype: str
        """
        return self._compression

    @compression.setter
    def compression(self, compression):
        """Sets the compression of this PsdProperties.

        Gets or sets the compression.

        :param compression: The compression of this PsdProperties.
        :type: str
        """
        self._compression = compression

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
        if not isinstance(other, PsdProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
