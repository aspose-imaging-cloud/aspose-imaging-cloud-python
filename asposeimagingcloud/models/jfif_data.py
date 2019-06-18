# coding: utf-8
# -----------------------------------------------------------------------------
# <copyright company="Aspose" file="JfifData.py">
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


class JfifData(object):
    """Represents JFIF data.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'density_units': 'str',
        'version': 'int',
        'x_density': 'int',
        'y_density': 'int'
    }

    attribute_map = {
        'density_units': 'DensityUnits',
        'version': 'Version',
        'x_density': 'XDensity',
        'y_density': 'YDensity'
    }

    def __init__(self, density_units=None, version=None, x_density=None, y_density=None):
        """JfifData - a model defined in Swagger"""

        self._density_units = None
        self._version = None
        self._x_density = None
        self._y_density = None
        self.discriminator = None

        if density_units is not None:
            self.density_units = density_units
        if version is not None:
            self.version = version
        if x_density is not None:
            self.x_density = x_density
        if y_density is not None:
            self.y_density = y_density

    @property
    def density_units(self):
        """Gets the density_units of this JfifData.

        Gets or sets the density units.

        :return: The density_units of this JfifData.
        :rtype: str
        """
        return self._density_units

    @density_units.setter
    def density_units(self, density_units):
        """Sets the density_units of this JfifData.

        Gets or sets the density units.

        :param density_units: The density_units of this JfifData.
        :type: str
        """
        self._density_units = density_units

    @property
    def version(self):
        """Gets the version of this JfifData.

        Gets or sets the version.

        :return: The version of this JfifData.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this JfifData.

        Gets or sets the version.

        :param version: The version of this JfifData.
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")
        self._version = version

    @property
    def x_density(self):
        """Gets the x_density of this JfifData.

        Gets or sets the X density.

        :return: The x_density of this JfifData.
        :rtype: int
        """
        return self._x_density

    @x_density.setter
    def x_density(self, x_density):
        """Sets the x_density of this JfifData.

        Gets or sets the X density.

        :param x_density: The x_density of this JfifData.
        :type: int
        """
        if x_density is None:
            raise ValueError("Invalid value for `x_density`, must not be `None`")
        self._x_density = x_density

    @property
    def y_density(self):
        """Gets the y_density of this JfifData.

        Gets or sets the Y density.

        :return: The y_density of this JfifData.
        :rtype: int
        """
        return self._y_density

    @y_density.setter
    def y_density(self, y_density):
        """Sets the y_density of this JfifData.

        Gets or sets the Y density.

        :param y_density: The y_density of this JfifData.
        :type: int
        """
        if y_density is None:
            raise ValueError("Invalid value for `y_density`, must not be `None`")
        self._y_density = y_density

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
        if not isinstance(other, JfifData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
