# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="JpegProperties.py">
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

from asposeimagingcloud.models.jfif_data import JfifData  # noqa: F401,E501
from asposeimagingcloud.models.jpeg_exif_data import JpegExifData  # noqa: F401,E501


class JpegProperties(object):
    """Represents information about image in JPEG format.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'comment': 'str',
        'jpeg_exif_data': 'JpegExifData',
        'jpeg_jfif_data': 'JfifData'
    }

    attribute_map = {
        'comment': 'Comment',
        'jpeg_exif_data': 'JpegExifData',
        'jpeg_jfif_data': 'JpegJfifData'
    }

    def __init__(self, comment=None, jpeg_exif_data=None, jpeg_jfif_data=None):  # noqa: E501
        """JpegProperties - a model defined in Swagger"""  # noqa: E501

        self._comment = None
        self._jpeg_exif_data = None
        self._jpeg_jfif_data = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if jpeg_exif_data is not None:
            self.jpeg_exif_data = jpeg_exif_data
        if jpeg_jfif_data is not None:
            self.jpeg_jfif_data = jpeg_jfif_data

    @property
    def comment(self):
        """Gets the comment of this JpegProperties.  # noqa: E501

        Gets or sets the comment.  # noqa: E501

        :return: The comment of this JpegProperties.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this JpegProperties.

        Gets or sets the comment.  # noqa: E501

        :param comment: The comment of this JpegProperties.  # noqa: E501
        :type: str
        """
        self._comment = comment

    @property
    def jpeg_exif_data(self):
        """Gets the jpeg_exif_data of this JpegProperties.  # noqa: E501

        Gets or sets the JPEG EXIF data.  # noqa: E501

        :return: The jpeg_exif_data of this JpegProperties.  # noqa: E501
        :rtype: JpegExifData
        """
        return self._jpeg_exif_data

    @jpeg_exif_data.setter
    def jpeg_exif_data(self, jpeg_exif_data):
        """Sets the jpeg_exif_data of this JpegProperties.

        Gets or sets the JPEG EXIF data.  # noqa: E501

        :param jpeg_exif_data: The jpeg_exif_data of this JpegProperties.  # noqa: E501
        :type: JpegExifData
        """
        self._jpeg_exif_data = jpeg_exif_data

    @property
    def jpeg_jfif_data(self):
        """Gets the jpeg_jfif_data of this JpegProperties.  # noqa: E501

        Gets or sets the JPEG JFIF data.  # noqa: E501

        :return: The jpeg_jfif_data of this JpegProperties.  # noqa: E501
        :rtype: JfifData
        """
        return self._jpeg_jfif_data

    @jpeg_jfif_data.setter
    def jpeg_jfif_data(self, jpeg_jfif_data):
        """Sets the jpeg_jfif_data of this JpegProperties.

        Gets or sets the JPEG JFIF data.  # noqa: E501

        :param jpeg_jfif_data: The jpeg_jfif_data of this JpegProperties.  # noqa: E501
        :type: JfifData
        """
        self._jpeg_jfif_data = jpeg_jfif_data

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
        if not isinstance(other, JpegProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
