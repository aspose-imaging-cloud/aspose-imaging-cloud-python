# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="DngProperties.py">
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


class DngProperties(object):
    """Represents information about image in DNG format.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'dng_version': 'int',
        'description': 'str',
        'model': 'str',
        'camera_manufacturer': 'str',
        'is_foveon': 'int',
        'software': 'str',
        'raw_count': 'int',
        'filters': 'int',
        'colors_count': 'int',
        'xmp_data': 'str',
        'translation_cfa_dng': 'list[str]'
    }

    attribute_map = {
        'dng_version': 'DngVersion',
        'description': 'Description',
        'model': 'Model',
        'camera_manufacturer': 'CameraManufacturer',
        'is_foveon': 'IsFoveon',
        'software': 'Software',
        'raw_count': 'RawCount',
        'filters': 'Filters',
        'colors_count': 'ColorsCount',
        'xmp_data': 'XmpData',
        'translation_cfa_dng': 'TranslationCfaDng'
    }

    def __init__(self, dng_version=None, description=None, model=None, camera_manufacturer=None, is_foveon=None, software=None, raw_count=None, filters=None, colors_count=None, xmp_data=None, translation_cfa_dng=None):  # noqa: E501
        """DngProperties - a model defined in Swagger"""  # noqa: E501

        self._dng_version = None
        self._description = None
        self._model = None
        self._camera_manufacturer = None
        self._is_foveon = None
        self._software = None
        self._raw_count = None
        self._filters = None
        self._colors_count = None
        self._xmp_data = None
        self._translation_cfa_dng = None
        self.discriminator = None

        if dng_version is not None:
            self.dng_version = dng_version
        if description is not None:
            self.description = description
        if model is not None:
            self.model = model
        if camera_manufacturer is not None:
            self.camera_manufacturer = camera_manufacturer
        if is_foveon is not None:
            self.is_foveon = is_foveon
        if software is not None:
            self.software = software
        if raw_count is not None:
            self.raw_count = raw_count
        if filters is not None:
            self.filters = filters
        if colors_count is not None:
            self.colors_count = colors_count
        if xmp_data is not None:
            self.xmp_data = xmp_data
        if translation_cfa_dng is not None:
            self.translation_cfa_dng = translation_cfa_dng

    @property
    def dng_version(self):
        """Gets the dng_version of this DngProperties.  # noqa: E501

        Gets or sets the DNG version.  # noqa: E501

        :return: The dng_version of this DngProperties.  # noqa: E501
        :rtype: int
        """
        return self._dng_version

    @dng_version.setter
    def dng_version(self, dng_version):
        """Sets the dng_version of this DngProperties.

        Gets or sets the DNG version.  # noqa: E501

        :param dng_version: The dng_version of this DngProperties.  # noqa: E501
        :type: int
        """
        if dng_version is None:
            raise ValueError("Invalid value for `dng_version`, must not be `None`")  # noqa: E501
        self._dng_version = dng_version

    @property
    def description(self):
        """Gets the description of this DngProperties.  # noqa: E501

        Gets or sets the description of colors (RGBG, RGBE, GMCY or GBTG).  # noqa: E501

        :return: The description of this DngProperties.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DngProperties.

        Gets or sets the description of colors (RGBG, RGBE, GMCY or GBTG).  # noqa: E501

        :param description: The description of this DngProperties.  # noqa: E501
        :type: str
        """
        self._description = description

    @property
    def model(self):
        """Gets the model of this DngProperties.  # noqa: E501

        Gets or sets the camera model.  # noqa: E501

        :return: The model of this DngProperties.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this DngProperties.

        Gets or sets the camera model.  # noqa: E501

        :param model: The model of this DngProperties.  # noqa: E501
        :type: str
        """
        self._model = model

    @property
    def camera_manufacturer(self):
        """Gets the camera_manufacturer of this DngProperties.  # noqa: E501

        Gets or sets the camera manufacturer.  # noqa: E501

        :return: The camera_manufacturer of this DngProperties.  # noqa: E501
        :rtype: str
        """
        return self._camera_manufacturer

    @camera_manufacturer.setter
    def camera_manufacturer(self, camera_manufacturer):
        """Sets the camera_manufacturer of this DngProperties.

        Gets or sets the camera manufacturer.  # noqa: E501

        :param camera_manufacturer: The camera_manufacturer of this DngProperties.  # noqa: E501
        :type: str
        """
        self._camera_manufacturer = camera_manufacturer

    @property
    def is_foveon(self):
        """Gets the is_foveon of this DngProperties.  # noqa: E501

        Gets or sets the value indicating whether it's a Foveon matrix.  # noqa: E501

        :return: The is_foveon of this DngProperties.  # noqa: E501
        :rtype: int
        """
        return self._is_foveon

    @is_foveon.setter
    def is_foveon(self, is_foveon):
        """Sets the is_foveon of this DngProperties.

        Gets or sets the value indicating whether it's a Foveon matrix.  # noqa: E501

        :param is_foveon: The is_foveon of this DngProperties.  # noqa: E501
        :type: int
        """
        if is_foveon is None:
            raise ValueError("Invalid value for `is_foveon`, must not be `None`")  # noqa: E501
        self._is_foveon = is_foveon

    @property
    def software(self):
        """Gets the software of this DngProperties.  # noqa: E501

        Gets or sets the software.  # noqa: E501

        :return: The software of this DngProperties.  # noqa: E501
        :rtype: str
        """
        return self._software

    @software.setter
    def software(self, software):
        """Sets the software of this DngProperties.

        Gets or sets the software.  # noqa: E501

        :param software: The software of this DngProperties.  # noqa: E501
        :type: str
        """
        self._software = software

    @property
    def raw_count(self):
        """Gets the raw_count of this DngProperties.  # noqa: E501

        Gets or sets the number of RAW images in file (0 means that the file has not been recognized).  # noqa: E501

        :return: The raw_count of this DngProperties.  # noqa: E501
        :rtype: int
        """
        return self._raw_count

    @raw_count.setter
    def raw_count(self, raw_count):
        """Sets the raw_count of this DngProperties.

        Gets or sets the number of RAW images in file (0 means that the file has not been recognized).  # noqa: E501

        :param raw_count: The raw_count of this DngProperties.  # noqa: E501
        :type: int
        """
        if raw_count is None:
            raise ValueError("Invalid value for `raw_count`, must not be `None`")  # noqa: E501
        self._raw_count = raw_count

    @property
    def filters(self):
        """Gets the filters of this DngProperties.  # noqa: E501

        Gets or sets the bit mask describing the order of color pixels in the matrix.  # noqa: E501

        :return: The filters of this DngProperties.  # noqa: E501
        :rtype: int
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this DngProperties.

        Gets or sets the bit mask describing the order of color pixels in the matrix.  # noqa: E501

        :param filters: The filters of this DngProperties.  # noqa: E501
        :type: int
        """
        if filters is None:
            raise ValueError("Invalid value for `filters`, must not be `None`")  # noqa: E501
        self._filters = filters

    @property
    def colors_count(self):
        """Gets the colors_count of this DngProperties.  # noqa: E501

        Gets or sets the colors count.  # noqa: E501

        :return: The colors_count of this DngProperties.  # noqa: E501
        :rtype: int
        """
        return self._colors_count

    @colors_count.setter
    def colors_count(self, colors_count):
        """Sets the colors_count of this DngProperties.

        Gets or sets the colors count.  # noqa: E501

        :param colors_count: The colors_count of this DngProperties.  # noqa: E501
        :type: int
        """
        if colors_count is None:
            raise ValueError("Invalid value for `colors_count`, must not be `None`")  # noqa: E501
        self._colors_count = colors_count

    @property
    def xmp_data(self):
        """Gets the xmp_data of this DngProperties.  # noqa: E501

        Gets or sets the XMP data.  # noqa: E501

        :return: The xmp_data of this DngProperties.  # noqa: E501
        :rtype: str
        """
        return self._xmp_data

    @xmp_data.setter
    def xmp_data(self, xmp_data):
        """Sets the xmp_data of this DngProperties.

        Gets or sets the XMP data.  # noqa: E501

        :param xmp_data: The xmp_data of this DngProperties.  # noqa: E501
        :type: str
        """
        self._xmp_data = xmp_data

    @property
    def translation_cfa_dng(self):
        """Gets the translation_cfa_dng of this DngProperties.  # noqa: E501

        Gets or sets the translation array for CFA mosaic of DNG format.  # noqa: E501

        :return: The translation_cfa_dng of this DngProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._translation_cfa_dng

    @translation_cfa_dng.setter
    def translation_cfa_dng(self, translation_cfa_dng):
        """Sets the translation_cfa_dng of this DngProperties.

        Gets or sets the translation array for CFA mosaic of DNG format.  # noqa: E501

        :param translation_cfa_dng: The translation_cfa_dng of this DngProperties.  # noqa: E501
        :type: list[str]
        """
        self._translation_cfa_dng = translation_cfa_dng

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
        if not isinstance(other, DngProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
