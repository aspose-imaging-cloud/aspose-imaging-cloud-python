#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="imaging_response.py">
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

from asposeimagingcloud.models.bmp_properties import BmpProperties
from asposeimagingcloud.models.dicom_properties import DicomProperties
from asposeimagingcloud.models.djvu_properties import DjvuProperties
from asposeimagingcloud.models.dng_properties import DngProperties
from asposeimagingcloud.models.gif_properties import GifProperties
from asposeimagingcloud.models.jpeg2000_properties import Jpeg2000Properties
from asposeimagingcloud.models.jpeg_properties import JpegProperties
from asposeimagingcloud.models.odg_properties import OdgProperties
from asposeimagingcloud.models.png_properties import PngProperties
from asposeimagingcloud.models.psd_properties import PsdProperties
from asposeimagingcloud.models.svg_properties import SvgProperties
from asposeimagingcloud.models.tiff_properties import TiffProperties
from asposeimagingcloud.models.web_p_properties import WebPProperties


class ImagingResponse(object):
    """Represents information about image.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'height': 'int',
        'width': 'int',
        'bits_per_pixel': 'int',
        'bmp_properties': 'BmpProperties',
        'gif_properties': 'GifProperties',
        'jpeg_properties': 'JpegProperties',
        'png_properties': 'PngProperties',
        'tiff_properties': 'TiffProperties',
        'psd_properties': 'PsdProperties',
        'djvu_properties': 'DjvuProperties',
        'web_p_properties': 'WebPProperties',
        'jpeg2000_properties': 'Jpeg2000Properties',
        'dicom_properties': 'DicomProperties',
        'dng_properties': 'DngProperties',
        'odg_properties': 'OdgProperties',
        'svg_properties': 'SvgProperties',
        'horizontal_resolution': 'float',
        'vertical_resolution': 'float',
        'is_cached': 'bool'
    }

    attribute_map = {
        'height': 'Height',
        'width': 'Width',
        'bits_per_pixel': 'BitsPerPixel',
        'bmp_properties': 'BmpProperties',
        'gif_properties': 'GifProperties',
        'jpeg_properties': 'JpegProperties',
        'png_properties': 'PngProperties',
        'tiff_properties': 'TiffProperties',
        'psd_properties': 'PsdProperties',
        'djvu_properties': 'DjvuProperties',
        'web_p_properties': 'WebPProperties',
        'jpeg2000_properties': 'Jpeg2000Properties',
        'dicom_properties': 'DicomProperties',
        'dng_properties': 'DngProperties',
        'odg_properties': 'OdgProperties',
        'svg_properties': 'SvgProperties',
        'horizontal_resolution': 'HorizontalResolution',
        'vertical_resolution': 'VerticalResolution',
        'is_cached': 'IsCached'
    }

    def __init__(self, height=None, width=None, bits_per_pixel=None, bmp_properties=None, gif_properties=None, jpeg_properties=None, png_properties=None, tiff_properties=None, psd_properties=None, djvu_properties=None, web_p_properties=None, jpeg2000_properties=None, dicom_properties=None, dng_properties=None, odg_properties=None, svg_properties=None, horizontal_resolution=None, vertical_resolution=None, is_cached=None):
        """ImagingResponse - a model defined in Swagger"""
        super(ImagingResponse, self).__init__()

        self._height = None
        self._width = None
        self._bits_per_pixel = None
        self._bmp_properties = None
        self._gif_properties = None
        self._jpeg_properties = None
        self._png_properties = None
        self._tiff_properties = None
        self._psd_properties = None
        self._djvu_properties = None
        self._web_p_properties = None
        self._jpeg2000_properties = None
        self._dicom_properties = None
        self._dng_properties = None
        self._odg_properties = None
        self._svg_properties = None
        self._horizontal_resolution = None
        self._vertical_resolution = None
        self._is_cached = None

        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if bits_per_pixel is not None:
            self.bits_per_pixel = bits_per_pixel
        if bmp_properties is not None:
            self.bmp_properties = bmp_properties
        if gif_properties is not None:
            self.gif_properties = gif_properties
        if jpeg_properties is not None:
            self.jpeg_properties = jpeg_properties
        if png_properties is not None:
            self.png_properties = png_properties
        if tiff_properties is not None:
            self.tiff_properties = tiff_properties
        if psd_properties is not None:
            self.psd_properties = psd_properties
        if djvu_properties is not None:
            self.djvu_properties = djvu_properties
        if web_p_properties is not None:
            self.web_p_properties = web_p_properties
        if jpeg2000_properties is not None:
            self.jpeg2000_properties = jpeg2000_properties
        if dicom_properties is not None:
            self.dicom_properties = dicom_properties
        if dng_properties is not None:
            self.dng_properties = dng_properties
        if odg_properties is not None:
            self.odg_properties = odg_properties
        if svg_properties is not None:
            self.svg_properties = svg_properties
        if horizontal_resolution is not None:
            self.horizontal_resolution = horizontal_resolution
        if vertical_resolution is not None:
            self.vertical_resolution = vertical_resolution
        if is_cached is not None:
            self.is_cached = is_cached

    @property
    def height(self):
        """Gets the height of this ImagingResponse.

        Gets or sets the height of image.

        :return: The height of this ImagingResponse.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ImagingResponse.

        Gets or sets the height of image.

        :param height: The height of this ImagingResponse.
        :type: int
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")
        self._height = height

    @property
    def width(self):
        """Gets the width of this ImagingResponse.

        Gets or sets the width of image.

        :return: The width of this ImagingResponse.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this ImagingResponse.

        Gets or sets the width of image.

        :param width: The width of this ImagingResponse.
        :type: int
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")
        self._width = width

    @property
    def bits_per_pixel(self):
        """Gets the bits_per_pixel of this ImagingResponse.

        Gets or sets the bits per pixel for image.

        :return: The bits_per_pixel of this ImagingResponse.
        :rtype: int
        """
        return self._bits_per_pixel

    @bits_per_pixel.setter
    def bits_per_pixel(self, bits_per_pixel):
        """Sets the bits_per_pixel of this ImagingResponse.

        Gets or sets the bits per pixel for image.

        :param bits_per_pixel: The bits_per_pixel of this ImagingResponse.
        :type: int
        """
        if bits_per_pixel is None:
            raise ValueError("Invalid value for `bits_per_pixel`, must not be `None`")
        self._bits_per_pixel = bits_per_pixel

    @property
    def bmp_properties(self):
        """Gets the bmp_properties of this ImagingResponse.

        Gets or sets the BMP properties.

        :return: The bmp_properties of this ImagingResponse.
        :rtype: BmpProperties
        """
        return self._bmp_properties

    @bmp_properties.setter
    def bmp_properties(self, bmp_properties):
        """Sets the bmp_properties of this ImagingResponse.

        Gets or sets the BMP properties.

        :param bmp_properties: The bmp_properties of this ImagingResponse.
        :type: BmpProperties
        """
        self._bmp_properties = bmp_properties

    @property
    def gif_properties(self):
        """Gets the gif_properties of this ImagingResponse.

        Gets or sets the GIF properties.

        :return: The gif_properties of this ImagingResponse.
        :rtype: GifProperties
        """
        return self._gif_properties

    @gif_properties.setter
    def gif_properties(self, gif_properties):
        """Sets the gif_properties of this ImagingResponse.

        Gets or sets the GIF properties.

        :param gif_properties: The gif_properties of this ImagingResponse.
        :type: GifProperties
        """
        self._gif_properties = gif_properties

    @property
    def jpeg_properties(self):
        """Gets the jpeg_properties of this ImagingResponse.

        Gets or sets the JPEG properties.

        :return: The jpeg_properties of this ImagingResponse.
        :rtype: JpegProperties
        """
        return self._jpeg_properties

    @jpeg_properties.setter
    def jpeg_properties(self, jpeg_properties):
        """Sets the jpeg_properties of this ImagingResponse.

        Gets or sets the JPEG properties.

        :param jpeg_properties: The jpeg_properties of this ImagingResponse.
        :type: JpegProperties
        """
        self._jpeg_properties = jpeg_properties

    @property
    def png_properties(self):
        """Gets the png_properties of this ImagingResponse.

        Gets or sets the PNG properties.

        :return: The png_properties of this ImagingResponse.
        :rtype: PngProperties
        """
        return self._png_properties

    @png_properties.setter
    def png_properties(self, png_properties):
        """Sets the png_properties of this ImagingResponse.

        Gets or sets the PNG properties.

        :param png_properties: The png_properties of this ImagingResponse.
        :type: PngProperties
        """
        self._png_properties = png_properties

    @property
    def tiff_properties(self):
        """Gets the tiff_properties of this ImagingResponse.

        Gets or sets the TIFF properties.

        :return: The tiff_properties of this ImagingResponse.
        :rtype: TiffProperties
        """
        return self._tiff_properties

    @tiff_properties.setter
    def tiff_properties(self, tiff_properties):
        """Sets the tiff_properties of this ImagingResponse.

        Gets or sets the TIFF properties.

        :param tiff_properties: The tiff_properties of this ImagingResponse.
        :type: TiffProperties
        """
        self._tiff_properties = tiff_properties

    @property
    def psd_properties(self):
        """Gets the psd_properties of this ImagingResponse.

        Gets or sets the PSD properties.

        :return: The psd_properties of this ImagingResponse.
        :rtype: PsdProperties
        """
        return self._psd_properties

    @psd_properties.setter
    def psd_properties(self, psd_properties):
        """Sets the psd_properties of this ImagingResponse.

        Gets or sets the PSD properties.

        :param psd_properties: The psd_properties of this ImagingResponse.
        :type: PsdProperties
        """
        self._psd_properties = psd_properties

    @property
    def djvu_properties(self):
        """Gets the djvu_properties of this ImagingResponse.

        Gets or sets the DJVU properties.

        :return: The djvu_properties of this ImagingResponse.
        :rtype: DjvuProperties
        """
        return self._djvu_properties

    @djvu_properties.setter
    def djvu_properties(self, djvu_properties):
        """Sets the djvu_properties of this ImagingResponse.

        Gets or sets the DJVU properties.

        :param djvu_properties: The djvu_properties of this ImagingResponse.
        :type: DjvuProperties
        """
        self._djvu_properties = djvu_properties

    @property
    def web_p_properties(self):
        """Gets the web_p_properties of this ImagingResponse.

        Gets or sets the WEBP properties.

        :return: The web_p_properties of this ImagingResponse.
        :rtype: WebPProperties
        """
        return self._web_p_properties

    @web_p_properties.setter
    def web_p_properties(self, web_p_properties):
        """Sets the web_p_properties of this ImagingResponse.

        Gets or sets the WEBP properties.

        :param web_p_properties: The web_p_properties of this ImagingResponse.
        :type: WebPProperties
        """
        self._web_p_properties = web_p_properties

    @property
    def jpeg2000_properties(self):
        """Gets the jpeg2000_properties of this ImagingResponse.

        Gets or sets the JPEG2000 properties.

        :return: The jpeg2000_properties of this ImagingResponse.
        :rtype: Jpeg2000Properties
        """
        return self._jpeg2000_properties

    @jpeg2000_properties.setter
    def jpeg2000_properties(self, jpeg2000_properties):
        """Sets the jpeg2000_properties of this ImagingResponse.

        Gets or sets the JPEG2000 properties.

        :param jpeg2000_properties: The jpeg2000_properties of this ImagingResponse.
        :type: Jpeg2000Properties
        """
        self._jpeg2000_properties = jpeg2000_properties

    @property
    def dicom_properties(self):
        """Gets the dicom_properties of this ImagingResponse.

        Gets or sets the DICOM properties.

        :return: The dicom_properties of this ImagingResponse.
        :rtype: DicomProperties
        """
        return self._dicom_properties

    @dicom_properties.setter
    def dicom_properties(self, dicom_properties):
        """Sets the dicom_properties of this ImagingResponse.

        Gets or sets the DICOM properties.

        :param dicom_properties: The dicom_properties of this ImagingResponse.
        :type: DicomProperties
        """
        self._dicom_properties = dicom_properties

    @property
    def dng_properties(self):
        """Gets the dng_properties of this ImagingResponse.

        Gets or sets the DNG properties.

        :return: The dng_properties of this ImagingResponse.
        :rtype: DngProperties
        """
        return self._dng_properties

    @dng_properties.setter
    def dng_properties(self, dng_properties):
        """Sets the dng_properties of this ImagingResponse.

        Gets or sets the DNG properties.

        :param dng_properties: The dng_properties of this ImagingResponse.
        :type: DngProperties
        """
        self._dng_properties = dng_properties

    @property
    def odg_properties(self):
        """Gets the odg_properties of this ImagingResponse.

        Gets or sets the the ODG properties.

        :return: The odg_properties of this ImagingResponse.
        :rtype: OdgProperties
        """
        return self._odg_properties

    @odg_properties.setter
    def odg_properties(self, odg_properties):
        """Sets the odg_properties of this ImagingResponse.

        Gets or sets the the ODG properties.

        :param odg_properties: The odg_properties of this ImagingResponse.
        :type: OdgProperties
        """
        self._odg_properties = odg_properties

    @property
    def svg_properties(self):
        """Gets the svg_properties of this ImagingResponse.

        Gets or sets the SVG properties.

        :return: The svg_properties of this ImagingResponse.
        :rtype: SvgProperties
        """
        return self._svg_properties

    @svg_properties.setter
    def svg_properties(self, svg_properties):
        """Sets the svg_properties of this ImagingResponse.

        Gets or sets the SVG properties.

        :param svg_properties: The svg_properties of this ImagingResponse.
        :type: SvgProperties
        """
        self._svg_properties = svg_properties

    @property
    def horizontal_resolution(self):
        """Gets the horizontal_resolution of this ImagingResponse.

        Gets or sets the horizontal resolution of an image.

        :return: The horizontal_resolution of this ImagingResponse.
        :rtype: float
        """
        return self._horizontal_resolution

    @horizontal_resolution.setter
    def horizontal_resolution(self, horizontal_resolution):
        """Sets the horizontal_resolution of this ImagingResponse.

        Gets or sets the horizontal resolution of an image.

        :param horizontal_resolution: The horizontal_resolution of this ImagingResponse.
        :type: float
        """
        if horizontal_resolution is None:
            raise ValueError("Invalid value for `horizontal_resolution`, must not be `None`")
        self._horizontal_resolution = horizontal_resolution

    @property
    def vertical_resolution(self):
        """Gets the vertical_resolution of this ImagingResponse.

        Gets or sets the vertical resolution of an image.

        :return: The vertical_resolution of this ImagingResponse.
        :rtype: float
        """
        return self._vertical_resolution

    @vertical_resolution.setter
    def vertical_resolution(self, vertical_resolution):
        """Sets the vertical_resolution of this ImagingResponse.

        Gets or sets the vertical resolution of an image.

        :param vertical_resolution: The vertical_resolution of this ImagingResponse.
        :type: float
        """
        if vertical_resolution is None:
            raise ValueError("Invalid value for `vertical_resolution`, must not be `None`")
        self._vertical_resolution = vertical_resolution

    @property
    def is_cached(self):
        """Gets the is_cached of this ImagingResponse.

        Gets or sets a value indicating whether image is cached.

        :return: The is_cached of this ImagingResponse.
        :rtype: bool
        """
        return self._is_cached

    @is_cached.setter
    def is_cached(self, is_cached):
        """Sets the is_cached of this ImagingResponse.

        Gets or sets a value indicating whether image is cached.

        :param is_cached: The is_cached of this ImagingResponse.
        :type: bool
        """
        if is_cached is None:
            raise ValueError("Invalid value for `is_cached`, must not be `None`")
        self._is_cached = is_cached

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
        if not isinstance(other, ImagingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
