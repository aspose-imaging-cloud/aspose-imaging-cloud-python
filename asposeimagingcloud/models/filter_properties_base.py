#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="filter_properties_base.py">
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


class FilterPropertiesBase(object):
    """Filter Options Base, abstract class
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'discriminator': 'str'
    }

    attribute_map = {
        'discriminator': 'discriminator'
    }

    discriminator_value_class_map = {
        'BigRectangularFilterProperties': 'BigRectangularFilterProperties',
        'MotionWienerFilterProperties': 'MotionWienerFilterProperties',
        'SmallRectangularFilterProperties': 'SmallRectangularFilterProperties',
        'MedianFilterProperties': 'MedianFilterProperties',
        'DeconvolutionFilterProperties': 'DeconvolutionFilterProperties',
        'BilateralSmoothingFilterProperties': 'BilateralSmoothingFilterProperties',
        'ConvolutionFilterProperties': 'ConvolutionFilterProperties',
        'GaussWienerFilterProperties': 'GaussWienerFilterProperties',
        'GaussianBlurFilterProperties': 'GaussianBlurFilterProperties',
        'SharpenFilterProperties': 'SharpenFilterProperties'
    }

    def __init__(self, discriminator=None):
        """FilterPropertiesBase - a model defined in Swagger"""
        super(FilterPropertiesBase, self).__init__()

        self._discriminator = None

        if discriminator is not None:
            self.discriminator = discriminator

    @property
    def discriminator(self):
        """Gets the discriminator of this FilterPropertiesBase.


        :return: The discriminator of this FilterPropertiesBase.
        :rtype: str
        """
        return self._discriminator

    @discriminator.setter
    def discriminator(self, discriminator):
        """Sets the discriminator of this FilterPropertiesBase.


        :param discriminator: The discriminator of this FilterPropertiesBase.
        :type: str
        """
        if discriminator is None:
            raise ValueError("Invalid value for `discriminator`, must not be `None`")
        self._discriminator = discriminator

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data.get(self.discriminator)
        return self.discriminator_value_class_map.get(discriminator_value.lower()) if discriminator_value else None

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
        if not isinstance(other, FilterPropertiesBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
