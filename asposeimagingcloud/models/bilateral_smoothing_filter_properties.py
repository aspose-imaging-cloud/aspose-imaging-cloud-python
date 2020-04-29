#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="bilateral_smoothing_filter_properties.py">
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

from asposeimagingcloud.models.filter_properties_base import FilterPropertiesBase


class BilateralSmoothingFilterProperties(FilterPropertiesBase):
    """The Bilateral Smoothing Filter Options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'size': 'int',
        'spatial_factor': 'float',
        'spatial_power': 'float',
        'color_factor': 'float',
        'color_power': 'float'
    }

    attribute_map = {
        'size': 'Size',
        'spatial_factor': 'SpatialFactor',
        'spatial_power': 'SpatialPower',
        'color_factor': 'ColorFactor',
        'color_power': 'ColorPower'
    }

    def __init__(self, size=None, spatial_factor=None, spatial_power=None, color_factor=None, color_power=None):
        """BilateralSmoothingFilterProperties - a model defined in Swagger"""
        super(BilateralSmoothingFilterProperties, self).__init__()

        self._size = None
        self._spatial_factor = None
        self._spatial_power = None
        self._color_factor = None
        self._color_power = None

        if size is not None:
            self.size = size
        if spatial_factor is not None:
            self.spatial_factor = spatial_factor
        if spatial_power is not None:
            self.spatial_power = spatial_power
        if color_factor is not None:
            self.color_factor = color_factor
        if color_power is not None:
            self.color_power = color_power

    @property
    def size(self):
        """Gets the size of this BilateralSmoothingFilterProperties.

        Gets or sets the size of the kernel.

        :return: The size of this BilateralSmoothingFilterProperties.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BilateralSmoothingFilterProperties.

        Gets or sets the size of the kernel.

        :param size: The size of this BilateralSmoothingFilterProperties.
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")
        self._size = size

    @property
    def spatial_factor(self):
        """Gets the spatial_factor of this BilateralSmoothingFilterProperties.

        Gets or sets the spatial factor.

        :return: The spatial_factor of this BilateralSmoothingFilterProperties.
        :rtype: float
        """
        return self._spatial_factor

    @spatial_factor.setter
    def spatial_factor(self, spatial_factor):
        """Sets the spatial_factor of this BilateralSmoothingFilterProperties.

        Gets or sets the spatial factor.

        :param spatial_factor: The spatial_factor of this BilateralSmoothingFilterProperties.
        :type: float
        """
        if spatial_factor is None:
            raise ValueError("Invalid value for `spatial_factor`, must not be `None`")
        self._spatial_factor = spatial_factor

    @property
    def spatial_power(self):
        """Gets the spatial_power of this BilateralSmoothingFilterProperties.

        Gets or sets the spatial power.

        :return: The spatial_power of this BilateralSmoothingFilterProperties.
        :rtype: float
        """
        return self._spatial_power

    @spatial_power.setter
    def spatial_power(self, spatial_power):
        """Sets the spatial_power of this BilateralSmoothingFilterProperties.

        Gets or sets the spatial power.

        :param spatial_power: The spatial_power of this BilateralSmoothingFilterProperties.
        :type: float
        """
        if spatial_power is None:
            raise ValueError("Invalid value for `spatial_power`, must not be `None`")
        self._spatial_power = spatial_power

    @property
    def color_factor(self):
        """Gets the color_factor of this BilateralSmoothingFilterProperties.

        Gets or sets the color factor.

        :return: The color_factor of this BilateralSmoothingFilterProperties.
        :rtype: float
        """
        return self._color_factor

    @color_factor.setter
    def color_factor(self, color_factor):
        """Sets the color_factor of this BilateralSmoothingFilterProperties.

        Gets or sets the color factor.

        :param color_factor: The color_factor of this BilateralSmoothingFilterProperties.
        :type: float
        """
        if color_factor is None:
            raise ValueError("Invalid value for `color_factor`, must not be `None`")
        self._color_factor = color_factor

    @property
    def color_power(self):
        """Gets the color_power of this BilateralSmoothingFilterProperties.

        Gets or sets the color power.

        :return: The color_power of this BilateralSmoothingFilterProperties.
        :rtype: float
        """
        return self._color_power

    @color_power.setter
    def color_power(self, color_power):
        """Sets the color_power of this BilateralSmoothingFilterProperties.

        Gets or sets the color power.

        :param color_power: The color_power of this BilateralSmoothingFilterProperties.
        :type: float
        """
        if color_power is None:
            raise ValueError("Invalid value for `color_power`, must not be `None`")
        self._color_power = color_power

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
        if not isinstance(other, BilateralSmoothingFilterProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
