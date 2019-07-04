#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="tiff_frame.py">
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
from asposeimagingcloud.models.tiff_options import TiffOptions


class TiffFrame(object):
    """Represents information about TIFF frame.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'frame_options': 'TiffOptions',
        'height': 'int',
        'width': 'int',
        'exif_data': 'ExifData'
    }

    attribute_map = {
        'frame_options': 'FrameOptions',
        'height': 'Height',
        'width': 'Width',
        'exif_data': 'ExifData'
    }

    def __init__(self, frame_options=None, height=None, width=None, exif_data=None):
        """TiffFrame - a model defined in Swagger"""

        self._frame_options = None
        self._height = None
        self._width = None
        self._exif_data = None
        self.discriminator = None

        if frame_options is not None:
            self.frame_options = frame_options
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if exif_data is not None:
            self.exif_data = exif_data

    @property
    def frame_options(self):
        """Gets the frame_options of this TiffFrame.

        Gets or sets options for the frame.

        :return: The frame_options of this TiffFrame.
        :rtype: TiffOptions
        """
        return self._frame_options

    @frame_options.setter
    def frame_options(self, frame_options):
        """Sets the frame_options of this TiffFrame.

        Gets or sets options for the frame.

        :param frame_options: The frame_options of this TiffFrame.
        :type: TiffOptions
        """
        self._frame_options = frame_options

    @property
    def height(self):
        """Gets the height of this TiffFrame.

        Gets or sets the frame height.

        :return: The height of this TiffFrame.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this TiffFrame.

        Gets or sets the frame height.

        :param height: The height of this TiffFrame.
        :type: int
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")
        self._height = height

    @property
    def width(self):
        """Gets the width of this TiffFrame.

        Gets or sets the frame width.

        :return: The width of this TiffFrame.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this TiffFrame.

        Gets or sets the frame width.

        :param width: The width of this TiffFrame.
        :type: int
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")
        self._width = width

    @property
    def exif_data(self):
        """Gets the exif_data of this TiffFrame.

        Gets or sets the EXIF data.

        :return: The exif_data of this TiffFrame.
        :rtype: ExifData
        """
        return self._exif_data

    @exif_data.setter
    def exif_data(self, exif_data):
        """Sets the exif_data of this TiffFrame.

        Gets or sets the EXIF data.

        :param exif_data: The exif_data of this TiffFrame.
        :type: ExifData
        """
        self._exif_data = exif_data

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
        if not isinstance(other, TiffFrame):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
