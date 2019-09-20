#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="tiff_properties.py">
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

from asposeimagingcloud.models.exif_data import ExifData
from asposeimagingcloud.models.tiff_frame import TiffFrame


class TiffProperties(object):
    """Represents properties of TIFF image.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'frames': 'list[TiffFrame]',
        'byte_order': 'str',
        'exif_data': 'ExifData'
    }

    attribute_map = {
        'frames': 'Frames',
        'byte_order': 'ByteOrder',
        'exif_data': 'ExifData'
    }

    def __init__(self, frames=None, byte_order=None, exif_data=None):
        """TiffProperties - a model defined in Swagger"""
        super(TiffProperties, self).__init__()

        self._frames = None
        self._byte_order = None
        self._exif_data = None

        if frames is not None:
            self.frames = frames
        if byte_order is not None:
            self.byte_order = byte_order
        if exif_data is not None:
            self.exif_data = exif_data

    @property
    def frames(self):
        """Gets the frames of this TiffProperties.

        Frames information.

        :return: The frames of this TiffProperties.
        :rtype: list[TiffFrame]
        """
        return self._frames

    @frames.setter
    def frames(self, frames):
        """Sets the frames of this TiffProperties.

        Frames information.

        :param frames: The frames of this TiffProperties.
        :type: list[TiffFrame]
        """
        self._frames = frames

    @property
    def byte_order(self):
        """Gets the byte_order of this TiffProperties.

        Gets or sets the byte order.

        :return: The byte_order of this TiffProperties.
        :rtype: str
        """
        return self._byte_order

    @byte_order.setter
    def byte_order(self, byte_order):
        """Sets the byte_order of this TiffProperties.

        Gets or sets the byte order.

        :param byte_order: The byte_order of this TiffProperties.
        :type: str
        """
        self._byte_order = byte_order

    @property
    def exif_data(self):
        """Gets the exif_data of this TiffProperties.

        Gets or sets the EXIF data.

        :return: The exif_data of this TiffProperties.
        :rtype: ExifData
        """
        return self._exif_data

    @exif_data.setter
    def exif_data(self, exif_data):
        """Sets the exif_data of this TiffProperties.

        Gets or sets the EXIF data.

        :param exif_data: The exif_data of this TiffProperties.
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
        if not isinstance(other, TiffProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
