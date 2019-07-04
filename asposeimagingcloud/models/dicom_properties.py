#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="dicom_properties.py">
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


class DicomProperties(object):
    """Represents information about image in dicom format.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'planar_configuration': 'int',
        'reds': 'str',
        'greens': 'str',
        'blues': 'str',
        'dicom_header_info_by_bytes': 'str',
        'signed_image': 'bool',
        'dicom_info': 'list[str]',
        'samples_per_pixel': 'int',
        'bits_allocated': 'int',
        'photo_interpretation': 'str',
        'width_tag_found': 'bool',
        'height_tag_found': 'bool',
        'width': 'int',
        'height': 'int',
        'window_centre': 'float',
        'window_width': 'float',
        'pixel_representation': 'int',
        'rescale_intercept': 'float',
        'rescale_slope': 'float',
        'number_of_frames': 'int',
        'length_value': 'int',
        'is_little_endian': 'bool',
        'offset': 'int',
        'dicom_found': 'bool'
    }

    attribute_map = {
        'planar_configuration': 'PlanarConfiguration',
        'reds': 'Reds',
        'greens': 'Greens',
        'blues': 'Blues',
        'dicom_header_info_by_bytes': 'DicomHeaderInfoByBytes',
        'signed_image': 'SignedImage',
        'dicom_info': 'DicomInfo',
        'samples_per_pixel': 'SamplesPerPixel',
        'bits_allocated': 'BitsAllocated',
        'photo_interpretation': 'PhotoInterpretation',
        'width_tag_found': 'WidthTagFound',
        'height_tag_found': 'HeightTagFound',
        'width': 'Width',
        'height': 'Height',
        'window_centre': 'WindowCentre',
        'window_width': 'WindowWidth',
        'pixel_representation': 'PixelRepresentation',
        'rescale_intercept': 'RescaleIntercept',
        'rescale_slope': 'RescaleSlope',
        'number_of_frames': 'NumberOfFrames',
        'length_value': 'LengthValue',
        'is_little_endian': 'IsLittleEndian',
        'offset': 'Offset',
        'dicom_found': 'DicomFound'
    }

    def __init__(self, planar_configuration=None, reds=None, greens=None, blues=None, dicom_header_info_by_bytes=None, signed_image=None, dicom_info=None, samples_per_pixel=None, bits_allocated=None, photo_interpretation=None, width_tag_found=None, height_tag_found=None, width=None, height=None, window_centre=None, window_width=None, pixel_representation=None, rescale_intercept=None, rescale_slope=None, number_of_frames=None, length_value=None, is_little_endian=None, offset=None, dicom_found=None):
        """DicomProperties - a model defined in Swagger"""

        self._planar_configuration = None
        self._reds = None
        self._greens = None
        self._blues = None
        self._dicom_header_info_by_bytes = None
        self._signed_image = None
        self._dicom_info = None
        self._samples_per_pixel = None
        self._bits_allocated = None
        self._photo_interpretation = None
        self._width_tag_found = None
        self._height_tag_found = None
        self._width = None
        self._height = None
        self._window_centre = None
        self._window_width = None
        self._pixel_representation = None
        self._rescale_intercept = None
        self._rescale_slope = None
        self._number_of_frames = None
        self._length_value = None
        self._is_little_endian = None
        self._offset = None
        self._dicom_found = None
        self.discriminator = None

        if planar_configuration is not None:
            self.planar_configuration = planar_configuration
        if reds is not None:
            self.reds = reds
        if greens is not None:
            self.greens = greens
        if blues is not None:
            self.blues = blues
        if dicom_header_info_by_bytes is not None:
            self.dicom_header_info_by_bytes = dicom_header_info_by_bytes
        if signed_image is not None:
            self.signed_image = signed_image
        if dicom_info is not None:
            self.dicom_info = dicom_info
        if samples_per_pixel is not None:
            self.samples_per_pixel = samples_per_pixel
        if bits_allocated is not None:
            self.bits_allocated = bits_allocated
        if photo_interpretation is not None:
            self.photo_interpretation = photo_interpretation
        if width_tag_found is not None:
            self.width_tag_found = width_tag_found
        if height_tag_found is not None:
            self.height_tag_found = height_tag_found
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if window_centre is not None:
            self.window_centre = window_centre
        if window_width is not None:
            self.window_width = window_width
        if pixel_representation is not None:
            self.pixel_representation = pixel_representation
        if rescale_intercept is not None:
            self.rescale_intercept = rescale_intercept
        if rescale_slope is not None:
            self.rescale_slope = rescale_slope
        if number_of_frames is not None:
            self.number_of_frames = number_of_frames
        if length_value is not None:
            self.length_value = length_value
        if is_little_endian is not None:
            self.is_little_endian = is_little_endian
        if offset is not None:
            self.offset = offset
        if dicom_found is not None:
            self.dicom_found = dicom_found

    @property
    def planar_configuration(self):
        """Gets the planar_configuration of this DicomProperties.

        Gets or sets the planar configuration.

        :return: The planar_configuration of this DicomProperties.
        :rtype: int
        """
        return self._planar_configuration

    @planar_configuration.setter
    def planar_configuration(self, planar_configuration):
        """Sets the planar_configuration of this DicomProperties.

        Gets or sets the planar configuration.

        :param planar_configuration: The planar_configuration of this DicomProperties.
        :type: int
        """
        if planar_configuration is None:
            raise ValueError("Invalid value for `planar_configuration`, must not be `None`")
        self._planar_configuration = planar_configuration

    @property
    def reds(self):
        """Gets the reds of this DicomProperties.

        Gets or sets the array of red colors.

        :return: The reds of this DicomProperties.
        :rtype: str
        """
        return self._reds

    @reds.setter
    def reds(self, reds):
        """Sets the reds of this DicomProperties.

        Gets or sets the array of red colors.

        :param reds: The reds of this DicomProperties.
        :type: str
        """
        if reds is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', reds):
            raise ValueError("Invalid value for `reds`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")
        self._reds = reds

    @property
    def greens(self):
        """Gets the greens of this DicomProperties.

        Gets or sets the array of green colors.

        :return: The greens of this DicomProperties.
        :rtype: str
        """
        return self._greens

    @greens.setter
    def greens(self, greens):
        """Sets the greens of this DicomProperties.

        Gets or sets the array of green colors.

        :param greens: The greens of this DicomProperties.
        :type: str
        """
        if greens is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', greens):
            raise ValueError("Invalid value for `greens`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")
        self._greens = greens

    @property
    def blues(self):
        """Gets the blues of this DicomProperties.

        Gets or sets the array of blue colors.

        :return: The blues of this DicomProperties.
        :rtype: str
        """
        return self._blues

    @blues.setter
    def blues(self, blues):
        """Sets the blues of this DicomProperties.

        Gets or sets the array of blue colors.

        :param blues: The blues of this DicomProperties.
        :type: str
        """
        if blues is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', blues):
            raise ValueError("Invalid value for `blues`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")
        self._blues = blues

    @property
    def dicom_header_info_by_bytes(self):
        """Gets the dicom_header_info_by_bytes of this DicomProperties.

        Gets or sets the header information by bytes.

        :return: The dicom_header_info_by_bytes of this DicomProperties.
        :rtype: str
        """
        return self._dicom_header_info_by_bytes

    @dicom_header_info_by_bytes.setter
    def dicom_header_info_by_bytes(self, dicom_header_info_by_bytes):
        """Sets the dicom_header_info_by_bytes of this DicomProperties.

        Gets or sets the header information by bytes.

        :param dicom_header_info_by_bytes: The dicom_header_info_by_bytes of this DicomProperties.
        :type: str
        """
        if dicom_header_info_by_bytes is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', dicom_header_info_by_bytes):
            raise ValueError("Invalid value for `dicom_header_info_by_bytes`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")
        self._dicom_header_info_by_bytes = dicom_header_info_by_bytes

    @property
    def signed_image(self):
        """Gets the signed_image of this DicomProperties.

        Gets or sets a value indicating whether it's a signed image.

        :return: The signed_image of this DicomProperties.
        :rtype: bool
        """
        return self._signed_image

    @signed_image.setter
    def signed_image(self, signed_image):
        """Sets the signed_image of this DicomProperties.

        Gets or sets a value indicating whether it's a signed image.

        :param signed_image: The signed_image of this DicomProperties.
        :type: bool
        """
        if signed_image is None:
            raise ValueError("Invalid value for `signed_image`, must not be `None`")
        self._signed_image = signed_image

    @property
    def dicom_info(self):
        """Gets the dicom_info of this DicomProperties.

        Gets or sets the header information of the DICOM file.

        :return: The dicom_info of this DicomProperties.
        :rtype: list[str]
        """
        return self._dicom_info

    @dicom_info.setter
    def dicom_info(self, dicom_info):
        """Sets the dicom_info of this DicomProperties.

        Gets or sets the header information of the DICOM file.

        :param dicom_info: The dicom_info of this DicomProperties.
        :type: list[str]
        """
        self._dicom_info = dicom_info

    @property
    def samples_per_pixel(self):
        """Gets the samples_per_pixel of this DicomProperties.

        Gets or sets samples per pixel count.

        :return: The samples_per_pixel of this DicomProperties.
        :rtype: int
        """
        return self._samples_per_pixel

    @samples_per_pixel.setter
    def samples_per_pixel(self, samples_per_pixel):
        """Sets the samples_per_pixel of this DicomProperties.

        Gets or sets samples per pixel count.

        :param samples_per_pixel: The samples_per_pixel of this DicomProperties.
        :type: int
        """
        if samples_per_pixel is None:
            raise ValueError("Invalid value for `samples_per_pixel`, must not be `None`")
        self._samples_per_pixel = samples_per_pixel

    @property
    def bits_allocated(self):
        """Gets the bits_allocated of this DicomProperties.

        Gets or sets allocated bits count.

        :return: The bits_allocated of this DicomProperties.
        :rtype: int
        """
        return self._bits_allocated

    @bits_allocated.setter
    def bits_allocated(self, bits_allocated):
        """Sets the bits_allocated of this DicomProperties.

        Gets or sets allocated bits count.

        :param bits_allocated: The bits_allocated of this DicomProperties.
        :type: int
        """
        if bits_allocated is None:
            raise ValueError("Invalid value for `bits_allocated`, must not be `None`")
        self._bits_allocated = bits_allocated

    @property
    def photo_interpretation(self):
        """Gets the photo_interpretation of this DicomProperties.

        Gets or sets the photo interpretation.

        :return: The photo_interpretation of this DicomProperties.
        :rtype: str
        """
        return self._photo_interpretation

    @photo_interpretation.setter
    def photo_interpretation(self, photo_interpretation):
        """Sets the photo_interpretation of this DicomProperties.

        Gets or sets the photo interpretation.

        :param photo_interpretation: The photo_interpretation of this DicomProperties.
        :type: str
        """
        self._photo_interpretation = photo_interpretation

    @property
    def width_tag_found(self):
        """Gets the width_tag_found of this DicomProperties.

        Gets or sets a value indicating whether width tag found.

        :return: The width_tag_found of this DicomProperties.
        :rtype: bool
        """
        return self._width_tag_found

    @width_tag_found.setter
    def width_tag_found(self, width_tag_found):
        """Sets the width_tag_found of this DicomProperties.

        Gets or sets a value indicating whether width tag found.

        :param width_tag_found: The width_tag_found of this DicomProperties.
        :type: bool
        """
        if width_tag_found is None:
            raise ValueError("Invalid value for `width_tag_found`, must not be `None`")
        self._width_tag_found = width_tag_found

    @property
    def height_tag_found(self):
        """Gets the height_tag_found of this DicomProperties.

        Gets or sets a value indicating whether height tag found.

        :return: The height_tag_found of this DicomProperties.
        :rtype: bool
        """
        return self._height_tag_found

    @height_tag_found.setter
    def height_tag_found(self, height_tag_found):
        """Sets the height_tag_found of this DicomProperties.

        Gets or sets a value indicating whether height tag found.

        :param height_tag_found: The height_tag_found of this DicomProperties.
        :type: bool
        """
        if height_tag_found is None:
            raise ValueError("Invalid value for `height_tag_found`, must not be `None`")
        self._height_tag_found = height_tag_found

    @property
    def width(self):
        """Gets the width of this DicomProperties.

        Gets or sets the width.

        :return: The width of this DicomProperties.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this DicomProperties.

        Gets or sets the width.

        :param width: The width of this DicomProperties.
        :type: int
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")
        self._width = width

    @property
    def height(self):
        """Gets the height of this DicomProperties.

        Gets or sets the height.

        :return: The height of this DicomProperties.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this DicomProperties.

        Gets or sets the height.

        :param height: The height of this DicomProperties.
        :type: int
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")
        self._height = height

    @property
    def window_centre(self):
        """Gets the window_centre of this DicomProperties.

        Gets or sets the window centre.

        :return: The window_centre of this DicomProperties.
        :rtype: float
        """
        return self._window_centre

    @window_centre.setter
    def window_centre(self, window_centre):
        """Sets the window_centre of this DicomProperties.

        Gets or sets the window centre.

        :param window_centre: The window_centre of this DicomProperties.
        :type: float
        """
        if window_centre is None:
            raise ValueError("Invalid value for `window_centre`, must not be `None`")
        self._window_centre = window_centre

    @property
    def window_width(self):
        """Gets the window_width of this DicomProperties.

        Gets or sets the width of the window.

        :return: The window_width of this DicomProperties.
        :rtype: float
        """
        return self._window_width

    @window_width.setter
    def window_width(self, window_width):
        """Sets the window_width of this DicomProperties.

        Gets or sets the width of the window.

        :param window_width: The window_width of this DicomProperties.
        :type: float
        """
        if window_width is None:
            raise ValueError("Invalid value for `window_width`, must not be `None`")
        self._window_width = window_width

    @property
    def pixel_representation(self):
        """Gets the pixel_representation of this DicomProperties.

        Gets or sets data representation of the pixel samples.

        :return: The pixel_representation of this DicomProperties.
        :rtype: int
        """
        return self._pixel_representation

    @pixel_representation.setter
    def pixel_representation(self, pixel_representation):
        """Sets the pixel_representation of this DicomProperties.

        Gets or sets data representation of the pixel samples.

        :param pixel_representation: The pixel_representation of this DicomProperties.
        :type: int
        """
        if pixel_representation is None:
            raise ValueError("Invalid value for `pixel_representation`, must not be `None`")
        self._pixel_representation = pixel_representation

    @property
    def rescale_intercept(self):
        """Gets the rescale_intercept of this DicomProperties.

        Gets or sets a value of the rescale intercept.

        :return: The rescale_intercept of this DicomProperties.
        :rtype: float
        """
        return self._rescale_intercept

    @rescale_intercept.setter
    def rescale_intercept(self, rescale_intercept):
        """Sets the rescale_intercept of this DicomProperties.

        Gets or sets a value of the rescale intercept.

        :param rescale_intercept: The rescale_intercept of this DicomProperties.
        :type: float
        """
        if rescale_intercept is None:
            raise ValueError("Invalid value for `rescale_intercept`, must not be `None`")
        self._rescale_intercept = rescale_intercept

    @property
    def rescale_slope(self):
        """Gets the rescale_slope of this DicomProperties.

        Gets or sets a value of the rescale slope.

        :return: The rescale_slope of this DicomProperties.
        :rtype: float
        """
        return self._rescale_slope

    @rescale_slope.setter
    def rescale_slope(self, rescale_slope):
        """Sets the rescale_slope of this DicomProperties.

        Gets or sets a value of the rescale slope.

        :param rescale_slope: The rescale_slope of this DicomProperties.
        :type: float
        """
        if rescale_slope is None:
            raise ValueError("Invalid value for `rescale_slope`, must not be `None`")
        self._rescale_slope = rescale_slope

    @property
    def number_of_frames(self):
        """Gets the number_of_frames of this DicomProperties.

        Gets or sets the number of frames.

        :return: The number_of_frames of this DicomProperties.
        :rtype: int
        """
        return self._number_of_frames

    @number_of_frames.setter
    def number_of_frames(self, number_of_frames):
        """Sets the number_of_frames of this DicomProperties.

        Gets or sets the number of frames.

        :param number_of_frames: The number_of_frames of this DicomProperties.
        :type: int
        """
        if number_of_frames is None:
            raise ValueError("Invalid value for `number_of_frames`, must not be `None`")
        self._number_of_frames = number_of_frames

    @property
    def length_value(self):
        """Gets the length_value of this DicomProperties.

        Gets or sets the length of element.

        :return: The length_value of this DicomProperties.
        :rtype: int
        """
        return self._length_value

    @length_value.setter
    def length_value(self, length_value):
        """Sets the length_value of this DicomProperties.

        Gets or sets the length of element.

        :param length_value: The length_value of this DicomProperties.
        :type: int
        """
        if length_value is None:
            raise ValueError("Invalid value for `length_value`, must not be `None`")
        self._length_value = length_value

    @property
    def is_little_endian(self):
        """Gets the is_little_endian of this DicomProperties.

        Indicates if DICOM image has little endian byte order.

        :return: The is_little_endian of this DicomProperties.
        :rtype: bool
        """
        return self._is_little_endian

    @is_little_endian.setter
    def is_little_endian(self, is_little_endian):
        """Sets the is_little_endian of this DicomProperties.

        Indicates if DICOM image has little endian byte order.

        :param is_little_endian: The is_little_endian of this DicomProperties.
        :type: bool
        """
        if is_little_endian is None:
            raise ValueError("Invalid value for `is_little_endian`, must not be `None`")
        self._is_little_endian = is_little_endian

    @property
    def offset(self):
        """Gets the offset of this DicomProperties.

        Gets or sets the offset.

        :return: The offset of this DicomProperties.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this DicomProperties.

        Gets or sets the offset.

        :param offset: The offset of this DicomProperties.
        :type: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")
        self._offset = offset

    @property
    def dicom_found(self):
        """Gets the dicom_found of this DicomProperties.

        Gets or sets a value indicating whether \"DICOM\" data is found.

        :return: The dicom_found of this DicomProperties.
        :rtype: bool
        """
        return self._dicom_found

    @dicom_found.setter
    def dicom_found(self, dicom_found):
        """Sets the dicom_found of this DicomProperties.

        Gets or sets a value indicating whether \"DICOM\" data is found.

        :param dicom_found: The dicom_found of this DicomProperties.
        :type: bool
        """
        if dicom_found is None:
            raise ValueError("Invalid value for `dicom_found`, must not be `None`")
        self._dicom_found = dicom_found

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
        if not isinstance(other, DicomProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
