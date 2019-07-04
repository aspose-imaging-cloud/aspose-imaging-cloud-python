#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="jpeg_exif_data.py">
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

from asposeimagingcloud.models.exif_data import ExifData


class JpegExifData(ExifData):
    """Represents EXIF data for JPEG
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'artist': 'str',
        'copyright': 'str',
        'date_time': 'str',
        'image_description': 'str',
        'make': 'str',
        'model': 'str',
        'orientation': 'str',
        'primary_chromaticities': 'list[float]',
        'reference_black_white': 'list[float]',
        'resolution_unit': 'str',
        'software': 'str',
        'transfer_function': 'list[int]',
        'x_resolution': 'float',
        'y_cb_cr_coefficients': 'list[float]',
        'y_cb_cr_positioning': 'str',
        'y_resolution': 'float'
    }

    attribute_map = {
        'artist': 'Artist',
        'copyright': 'Copyright',
        'date_time': 'DateTime',
        'image_description': 'ImageDescription',
        'make': 'Make',
        'model': 'Model',
        'orientation': 'Orientation',
        'primary_chromaticities': 'PrimaryChromaticities',
        'reference_black_white': 'ReferenceBlackWhite',
        'resolution_unit': 'ResolutionUnit',
        'software': 'Software',
        'transfer_function': 'TransferFunction',
        'x_resolution': 'XResolution',
        'y_cb_cr_coefficients': 'YCbCrCoefficients',
        'y_cb_cr_positioning': 'YCbCrPositioning',
        'y_resolution': 'YResolution'
    }

    def __init__(self, artist=None, copyright=None, date_time=None, image_description=None, make=None, model=None, orientation=None, primary_chromaticities=None, reference_black_white=None, resolution_unit=None, software=None, transfer_function=None, x_resolution=None, y_cb_cr_coefficients=None, y_cb_cr_positioning=None, y_resolution=None):
        """JpegExifData - a model defined in Swagger"""

        self._artist = None
        self._copyright = None
        self._date_time = None
        self._image_description = None
        self._make = None
        self._model = None
        self._orientation = None
        self._primary_chromaticities = None
        self._reference_black_white = None
        self._resolution_unit = None
        self._software = None
        self._transfer_function = None
        self._x_resolution = None
        self._y_cb_cr_coefficients = None
        self._y_cb_cr_positioning = None
        self._y_resolution = None
        self.discriminator = None

        if artist is not None:
            self.artist = artist
        if copyright is not None:
            self.copyright = copyright
        if date_time is not None:
            self.date_time = date_time
        if image_description is not None:
            self.image_description = image_description
        if make is not None:
            self.make = make
        if model is not None:
            self.model = model
        if orientation is not None:
            self.orientation = orientation
        if primary_chromaticities is not None:
            self.primary_chromaticities = primary_chromaticities
        if reference_black_white is not None:
            self.reference_black_white = reference_black_white
        if resolution_unit is not None:
            self.resolution_unit = resolution_unit
        if software is not None:
            self.software = software
        if transfer_function is not None:
            self.transfer_function = transfer_function
        if x_resolution is not None:
            self.x_resolution = x_resolution
        if y_cb_cr_coefficients is not None:
            self.y_cb_cr_coefficients = y_cb_cr_coefficients
        if y_cb_cr_positioning is not None:
            self.y_cb_cr_positioning = y_cb_cr_positioning
        if y_resolution is not None:
            self.y_resolution = y_resolution

    @property
    def artist(self):
        """Gets the artist of this JpegExifData.

        Gets or sets the artist.

        :return: The artist of this JpegExifData.
        :rtype: str
        """
        return self._artist

    @artist.setter
    def artist(self, artist):
        """Sets the artist of this JpegExifData.

        Gets or sets the artist.

        :param artist: The artist of this JpegExifData.
        :type: str
        """
        self._artist = artist

    @property
    def copyright(self):
        """Gets the copyright of this JpegExifData.

        Gets or sets the copyright info.

        :return: The copyright of this JpegExifData.
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this JpegExifData.

        Gets or sets the copyright info.

        :param copyright: The copyright of this JpegExifData.
        :type: str
        """
        self._copyright = copyright

    @property
    def date_time(self):
        """Gets the date_time of this JpegExifData.

        Gets or sets the date and time.

        :return: The date_time of this JpegExifData.
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this JpegExifData.

        Gets or sets the date and time.

        :param date_time: The date_time of this JpegExifData.
        :type: str
        """
        self._date_time = date_time

    @property
    def image_description(self):
        """Gets the image_description of this JpegExifData.

        Gets or sets the image description.

        :return: The image_description of this JpegExifData.
        :rtype: str
        """
        return self._image_description

    @image_description.setter
    def image_description(self, image_description):
        """Sets the image_description of this JpegExifData.

        Gets or sets the image description.

        :param image_description: The image_description of this JpegExifData.
        :type: str
        """
        self._image_description = image_description

    @property
    def make(self):
        """Gets the make of this JpegExifData.

        Gets or sets the manufacturer.

        :return: The make of this JpegExifData.
        :rtype: str
        """
        return self._make

    @make.setter
    def make(self, make):
        """Sets the make of this JpegExifData.

        Gets or sets the manufacturer.

        :param make: The make of this JpegExifData.
        :type: str
        """
        self._make = make

    @property
    def model(self):
        """Gets the model of this JpegExifData.

        Gets or sets the model.

        :return: The model of this JpegExifData.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this JpegExifData.

        Gets or sets the model.

        :param model: The model of this JpegExifData.
        :type: str
        """
        self._model = model

    @property
    def orientation(self):
        """Gets the orientation of this JpegExifData.

        Gets or sets the orientation.

        :return: The orientation of this JpegExifData.
        :rtype: str
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this JpegExifData.

        Gets or sets the orientation.

        :param orientation: The orientation of this JpegExifData.
        :type: str
        """
        self._orientation = orientation

    @property
    def primary_chromaticities(self):
        """Gets the primary_chromaticities of this JpegExifData.

        Gets or sets the primary chromaticities.

        :return: The primary_chromaticities of this JpegExifData.
        :rtype: list[float]
        """
        return self._primary_chromaticities

    @primary_chromaticities.setter
    def primary_chromaticities(self, primary_chromaticities):
        """Sets the primary_chromaticities of this JpegExifData.

        Gets or sets the primary chromaticities.

        :param primary_chromaticities: The primary_chromaticities of this JpegExifData.
        :type: list[float]
        """
        self._primary_chromaticities = primary_chromaticities

    @property
    def reference_black_white(self):
        """Gets the reference_black_white of this JpegExifData.

        Gets or sets the reference black and white.

        :return: The reference_black_white of this JpegExifData.
        :rtype: list[float]
        """
        return self._reference_black_white

    @reference_black_white.setter
    def reference_black_white(self, reference_black_white):
        """Sets the reference_black_white of this JpegExifData.

        Gets or sets the reference black and white.

        :param reference_black_white: The reference_black_white of this JpegExifData.
        :type: list[float]
        """
        self._reference_black_white = reference_black_white

    @property
    def resolution_unit(self):
        """Gets the resolution_unit of this JpegExifData.

        Gets or sets the resolution unit.

        :return: The resolution_unit of this JpegExifData.
        :rtype: str
        """
        return self._resolution_unit

    @resolution_unit.setter
    def resolution_unit(self, resolution_unit):
        """Sets the resolution_unit of this JpegExifData.

        Gets or sets the resolution unit.

        :param resolution_unit: The resolution_unit of this JpegExifData.
        :type: str
        """
        self._resolution_unit = resolution_unit

    @property
    def software(self):
        """Gets the software of this JpegExifData.

        Gets or sets the software.

        :return: The software of this JpegExifData.
        :rtype: str
        """
        return self._software

    @software.setter
    def software(self, software):
        """Sets the software of this JpegExifData.

        Gets or sets the software.

        :param software: The software of this JpegExifData.
        :type: str
        """
        self._software = software

    @property
    def transfer_function(self):
        """Gets the transfer_function of this JpegExifData.

        Gets or sets the transfer function.

        :return: The transfer_function of this JpegExifData.
        :rtype: list[int]
        """
        return self._transfer_function

    @transfer_function.setter
    def transfer_function(self, transfer_function):
        """Sets the transfer_function of this JpegExifData.

        Gets or sets the transfer function.

        :param transfer_function: The transfer_function of this JpegExifData.
        :type: list[int]
        """
        self._transfer_function = transfer_function

    @property
    def x_resolution(self):
        """Gets the x_resolution of this JpegExifData.

        Gets or sets the X resolution.

        :return: The x_resolution of this JpegExifData.
        :rtype: float
        """
        return self._x_resolution

    @x_resolution.setter
    def x_resolution(self, x_resolution):
        """Sets the x_resolution of this JpegExifData.

        Gets or sets the X resolution.

        :param x_resolution: The x_resolution of this JpegExifData.
        :type: float
        """
        if x_resolution is None:
            raise ValueError("Invalid value for `x_resolution`, must not be `None`")
        self._x_resolution = x_resolution

    @property
    def y_cb_cr_coefficients(self):
        """Gets the y_cb_cr_coefficients of this JpegExifData.

        Gets or sets the YCbCr coefficients.

        :return: The y_cb_cr_coefficients of this JpegExifData.
        :rtype: list[float]
        """
        return self._y_cb_cr_coefficients

    @y_cb_cr_coefficients.setter
    def y_cb_cr_coefficients(self, y_cb_cr_coefficients):
        """Sets the y_cb_cr_coefficients of this JpegExifData.

        Gets or sets the YCbCr coefficients.

        :param y_cb_cr_coefficients: The y_cb_cr_coefficients of this JpegExifData.
        :type: list[float]
        """
        self._y_cb_cr_coefficients = y_cb_cr_coefficients

    @property
    def y_cb_cr_positioning(self):
        """Gets the y_cb_cr_positioning of this JpegExifData.

        Gets or sets the YCbCr positioning.

        :return: The y_cb_cr_positioning of this JpegExifData.
        :rtype: str
        """
        return self._y_cb_cr_positioning

    @y_cb_cr_positioning.setter
    def y_cb_cr_positioning(self, y_cb_cr_positioning):
        """Sets the y_cb_cr_positioning of this JpegExifData.

        Gets or sets the YCbCr positioning.

        :param y_cb_cr_positioning: The y_cb_cr_positioning of this JpegExifData.
        :type: str
        """
        self._y_cb_cr_positioning = y_cb_cr_positioning

    @property
    def y_resolution(self):
        """Gets the y_resolution of this JpegExifData.

        Gets or sets the Y resolution.

        :return: The y_resolution of this JpegExifData.
        :rtype: float
        """
        return self._y_resolution

    @y_resolution.setter
    def y_resolution(self, y_resolution):
        """Sets the y_resolution of this JpegExifData.

        Gets or sets the Y resolution.

        :param y_resolution: The y_resolution of this JpegExifData.
        :type: float
        """
        if y_resolution is None:
            raise ValueError("Invalid value for `y_resolution`, must not be `None`")
        self._y_resolution = y_resolution

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
        if not isinstance(other, JpegExifData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
