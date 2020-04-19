#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="convolution_filter_properties.py">
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

from asposeimagingcloud.models.filter_properties_base import FilterPropertiesBase


class ConvolutionFilterProperties(FilterPropertiesBase):
    """The convolution filter.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'factor': 'float',
        'bias': 'int'
    }

    attribute_map = {
        'factor': 'Factor',
        'bias': 'Bias'
    }

    def __init__(self, factor=None, bias=None):
        """ConvolutionFilterProperties - a model defined in Swagger"""
        super(ConvolutionFilterProperties, self).__init__()

        self._factor = None
        self._bias = None

        if factor is not None:
            self.factor = factor
        if bias is not None:
            self.bias = bias

    @property
    def factor(self):
        """Gets the factor of this ConvolutionFilterProperties.

        Gets or sets the factor.

        :return: The factor of this ConvolutionFilterProperties.
        :rtype: float
        """
        return self._factor

    @factor.setter
    def factor(self, factor):
        """Sets the factor of this ConvolutionFilterProperties.

        Gets or sets the factor.

        :param factor: The factor of this ConvolutionFilterProperties.
        :type: float
        """
        if factor is None:
            raise ValueError("Invalid value for `factor`, must not be `None`")
        self._factor = factor

    @property
    def bias(self):
        """Gets the bias of this ConvolutionFilterProperties.

        Gets or sets the bias.

        :return: The bias of this ConvolutionFilterProperties.
        :rtype: int
        """
        return self._bias

    @bias.setter
    def bias(self, bias):
        """Sets the bias of this ConvolutionFilterProperties.

        Gets or sets the bias.

        :param bias: The bias of this ConvolutionFilterProperties.
        :type: int
        """
        if bias is None:
            raise ValueError("Invalid value for `bias`, must not be `None`")
        self._bias = bias

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
        if not isinstance(other, ConvolutionFilterProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
