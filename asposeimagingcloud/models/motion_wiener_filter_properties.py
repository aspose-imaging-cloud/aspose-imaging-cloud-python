#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="motion_wiener_filter_properties.py">
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

from asposeimagingcloud.models.deconvolution_filter_properties import DeconvolutionFilterProperties


class MotionWienerFilterProperties(DeconvolutionFilterProperties):
    """Deconvolution filter options deblur motion             
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'length': 'int',
        'smooth': 'float',
        'angle': 'float'
    }

    attribute_map = {
        'length': 'Length',
        'smooth': 'Smooth',
        'angle': 'Angle'
    }

    def __init__(self, length=None, smooth=None, angle=None):
        """MotionWienerFilterProperties - a model defined in Swagger"""
        super(MotionWienerFilterProperties, self).__init__()

        self._length = None
        self._smooth = None
        self._angle = None

        if length is not None:
            self.length = length
        if smooth is not None:
            self.smooth = smooth
        if angle is not None:
            self.angle = angle

    @property
    def length(self):
        """Gets the length of this MotionWienerFilterProperties.

        Gets or sets the length.             

        :return: The length of this MotionWienerFilterProperties.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this MotionWienerFilterProperties.

        Gets or sets the length.             

        :param length: The length of this MotionWienerFilterProperties.
        :type: int
        """
        if length is None:
            raise ValueError("Invalid value for `length`, must not be `None`")
        self._length = length

    @property
    def smooth(self):
        """Gets the smooth of this MotionWienerFilterProperties.

        Gets or sets the smooth.             

        :return: The smooth of this MotionWienerFilterProperties.
        :rtype: float
        """
        return self._smooth

    @smooth.setter
    def smooth(self, smooth):
        """Sets the smooth of this MotionWienerFilterProperties.

        Gets or sets the smooth.             

        :param smooth: The smooth of this MotionWienerFilterProperties.
        :type: float
        """
        if smooth is None:
            raise ValueError("Invalid value for `smooth`, must not be `None`")
        self._smooth = smooth

    @property
    def angle(self):
        """Gets the angle of this MotionWienerFilterProperties.

        Gets or sets the angle in gradus.             

        :return: The angle of this MotionWienerFilterProperties.
        :rtype: float
        """
        return self._angle

    @angle.setter
    def angle(self, angle):
        """Sets the angle of this MotionWienerFilterProperties.

        Gets or sets the angle in gradus.             

        :param angle: The angle of this MotionWienerFilterProperties.
        :type: float
        """
        if angle is None:
            raise ValueError("Invalid value for `angle`, must not be `None`")
        self._angle = angle

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
        if not isinstance(other, MotionWienerFilterProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
