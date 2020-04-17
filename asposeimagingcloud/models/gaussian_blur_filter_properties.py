#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="gaussian_blur_filter_properties.py">
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

from asposeimagingcloud.models.convolution_filter_properties import ConvolutionFilterProperties


class GaussianBlurFilterProperties(ConvolutionFilterProperties):
    """The Gaussian blur
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'radius': 'int',
        'sigma': 'float'
    }

    attribute_map = {
        'radius': 'Radius',
        'sigma': 'Sigma'
    }

    def __init__(self, radius=None, sigma=None):
        """GaussianBlurFilterProperties - a model defined in Swagger"""
        super(GaussianBlurFilterProperties, self).__init__()

        self._radius = None
        self._sigma = None

        if radius is not None:
            self.radius = radius
        if sigma is not None:
            self.sigma = sigma

    @property
    def radius(self):
        """Gets the radius of this GaussianBlurFilterProperties.

        Gets or sets the radius.

        :return: The radius of this GaussianBlurFilterProperties.
        :rtype: int
        """
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Sets the radius of this GaussianBlurFilterProperties.

        Gets or sets the radius.

        :param radius: The radius of this GaussianBlurFilterProperties.
        :type: int
        """
        if radius is None:
            raise ValueError("Invalid value for `radius`, must not be `None`")
        self._radius = radius

    @property
    def sigma(self):
        """Gets the sigma of this GaussianBlurFilterProperties.

        Gets or sets the sigma.

        :return: The sigma of this GaussianBlurFilterProperties.
        :rtype: float
        """
        return self._sigma

    @sigma.setter
    def sigma(self, sigma):
        """Sets the sigma of this GaussianBlurFilterProperties.

        Gets or sets the sigma.

        :param sigma: The sigma of this GaussianBlurFilterProperties.
        :type: float
        """
        if sigma is None:
            raise ValueError("Invalid value for `sigma`, must not be `None`")
        self._sigma = sigma

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
        if not isinstance(other, GaussianBlurFilterProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
