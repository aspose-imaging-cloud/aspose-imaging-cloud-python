#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="deconvolution_filter_properties.py">
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


class DeconvolutionFilterProperties(FilterPropertiesBase):
    """Deconvolution Filter Options, abstract class
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'snr': 'float',
        'brightness': 'float',
        'grayscale': 'bool',
        'is_partial_loaded': 'bool'
    }

    attribute_map = {
        'snr': 'Snr',
        'brightness': 'Brightness',
        'grayscale': 'Grayscale',
        'is_partial_loaded': 'IsPartialLoaded'
    }

    def __init__(self, snr=None, brightness=None, grayscale=None, is_partial_loaded=None):
        """DeconvolutionFilterProperties - a model defined in Swagger"""
        super(DeconvolutionFilterProperties, self).__init__()

        self._snr = None
        self._brightness = None
        self._grayscale = None
        self._is_partial_loaded = None

        if snr is not None:
            self.snr = snr
        if brightness is not None:
            self.brightness = brightness
        if grayscale is not None:
            self.grayscale = grayscale
        if is_partial_loaded is not None:
            self.is_partial_loaded = is_partial_loaded

    @property
    def snr(self):
        """Gets the snr of this DeconvolutionFilterProperties.

        Gets or sets the SNR(signal-to-noise ratio) recommended range 0.002 - 0.009, default value = 0.007

        :return: The snr of this DeconvolutionFilterProperties.
        :rtype: float
        """
        return self._snr

    @snr.setter
    def snr(self, snr):
        """Sets the snr of this DeconvolutionFilterProperties.

        Gets or sets the SNR(signal-to-noise ratio) recommended range 0.002 - 0.009, default value = 0.007

        :param snr: The snr of this DeconvolutionFilterProperties.
        :type: float
        """
        if snr is None:
            raise ValueError("Invalid value for `snr`, must not be `None`")
        self._snr = snr

    @property
    def brightness(self):
        """Gets the brightness of this DeconvolutionFilterProperties.

        Gets or sets the brightness. recommended range 1 - 1.5 default value = 1.15

        :return: The brightness of this DeconvolutionFilterProperties.
        :rtype: float
        """
        return self._brightness

    @brightness.setter
    def brightness(self, brightness):
        """Sets the brightness of this DeconvolutionFilterProperties.

        Gets or sets the brightness. recommended range 1 - 1.5 default value = 1.15

        :param brightness: The brightness of this DeconvolutionFilterProperties.
        :type: float
        """
        if brightness is None:
            raise ValueError("Invalid value for `brightness`, must not be `None`")
        self._brightness = brightness

    @property
    def grayscale(self):
        """Gets the grayscale of this DeconvolutionFilterProperties.

        Gets or sets a value indicating whether this DeconvolutionFilterProperties is grayscale. Return grayscale mode or RGB mode.

        :return: The grayscale of this DeconvolutionFilterProperties.
        :rtype: bool
        """
        return self._grayscale

    @grayscale.setter
    def grayscale(self, grayscale):
        """Sets the grayscale of this DeconvolutionFilterProperties.

        Gets or sets a value indicating whether this DeconvolutionFilterProperties is grayscale. Return grayscale mode or RGB mode.

        :param grayscale: The grayscale of this DeconvolutionFilterProperties.
        :type: bool
        """
        if grayscale is None:
            raise ValueError("Invalid value for `grayscale`, must not be `None`")
        self._grayscale = grayscale

    @property
    def is_partial_loaded(self):
        """Gets the is_partial_loaded of this DeconvolutionFilterProperties.

        Gets a value indicating whether this instance is partial loaded.

        :return: The is_partial_loaded of this DeconvolutionFilterProperties.
        :rtype: bool
        """
        return self._is_partial_loaded

    @is_partial_loaded.setter
    def is_partial_loaded(self, is_partial_loaded):
        """Sets the is_partial_loaded of this DeconvolutionFilterProperties.

        Gets a value indicating whether this instance is partial loaded.

        :param is_partial_loaded: The is_partial_loaded of this DeconvolutionFilterProperties.
        :type: bool
        """
        if is_partial_loaded is None:
            raise ValueError("Invalid value for `is_partial_loaded`, must not be `None`")
        self._is_partial_loaded = is_partial_loaded

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
        if not isinstance(other, DeconvolutionFilterProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
