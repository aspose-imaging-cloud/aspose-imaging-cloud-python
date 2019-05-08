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


class JfifData(object):
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

    def __init__(self, density_units=None, version=None, x_density=None, y_density=None):  # noqa: E501
        """JfifData - a model defined in Swagger"""  # noqa: E501

        self._density_units = None
        self._version = None
        self._x_density = None
        self._y_density = None
        self.discriminator = None

        if density_units is not None:
            self.density_units = density_units
        self.version = version
        self.x_density = x_density
        self.y_density = y_density

    @property
    def density_units(self):
        """Gets the density_units of this JfifData.  # noqa: E501

        Gets or sets the density units.  # noqa: E501

        :return: The density_units of this JfifData.  # noqa: E501
        :rtype: str
        """
        return self._density_units

    @density_units.setter
    def density_units(self, density_units):
        """Sets the density_units of this JfifData.

        Gets or sets the density units.  # noqa: E501

        :param density_units: The density_units of this JfifData.  # noqa: E501
        :type: str
        """

        self._density_units = density_units

    @property
    def version(self):
        """Gets the version of this JfifData.  # noqa: E501

        Gets or sets the version.  # noqa: E501

        :return: The version of this JfifData.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this JfifData.

        Gets or sets the version.  # noqa: E501

        :param version: The version of this JfifData.  # noqa: E501
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def x_density(self):
        """Gets the x_density of this JfifData.  # noqa: E501

        Gets or sets the X density.  # noqa: E501

        :return: The x_density of this JfifData.  # noqa: E501
        :rtype: int
        """
        return self._x_density

    @x_density.setter
    def x_density(self, x_density):
        """Sets the x_density of this JfifData.

        Gets or sets the X density.  # noqa: E501

        :param x_density: The x_density of this JfifData.  # noqa: E501
        :type: int
        """
        if x_density is None:
            raise ValueError("Invalid value for `x_density`, must not be `None`")  # noqa: E501

        self._x_density = x_density

    @property
    def y_density(self):
        """Gets the y_density of this JfifData.  # noqa: E501

        Gets or sets the Y density.  # noqa: E501

        :return: The y_density of this JfifData.  # noqa: E501
        :rtype: int
        """
        return self._y_density

    @y_density.setter
    def y_density(self, y_density):
        """Sets the y_density of this JfifData.

        Gets or sets the Y density.  # noqa: E501

        :param y_density: The y_density of this JfifData.  # noqa: E501
        :type: int
        """
        if y_density is None:
            raise ValueError("Invalid value for `y_density`, must not be `None`")  # noqa: E501

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
        if issubclass(JfifData, dict):
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
        if not isinstance(other, JfifData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other