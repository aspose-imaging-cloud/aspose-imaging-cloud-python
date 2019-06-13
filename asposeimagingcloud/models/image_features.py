# coding: utf-8
# -----------------------------------------------------------------------------
# <copyright company="Aspose" file="ImageFeatures.py">
#   Copyright (c) 2019 Aspose Pty Ltd. All rights reserved.
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a
#  copy  of this software and associated documentation files (the "Software"),
#  to deal  in the Software without restriction, including without limitation
#  the rights  to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell  copies of the Software, and to permit persons to whom the
#  Software is  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM,  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------
import pprint

import six


class ImageFeatures(object):
    """Image features.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'image_id': 'str',
        'features_count': 'int',
        'feature_length_in_bits': 'int',
        'features': 'str'
    }

    attribute_map = {
        'image_id': 'ImageId',
        'features_count': 'FeaturesCount',
        'feature_length_in_bits': 'FeatureLengthInBits',
        'features': 'Features'
    }

    def __init__(self, image_id=None, features_count=None, feature_length_in_bits=None, features=None):
        """ImageFeatures - a model defined in Swagger"""

        self._image_id = None
        self._features_count = None
        self._feature_length_in_bits = None
        self._features = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if features_count is not None:
            self.features_count = features_count
        if feature_length_in_bits is not None:
            self.feature_length_in_bits = feature_length_in_bits
        if features is not None:
            self.features = features

    @property
    def image_id(self):
        """Gets the image_id of this ImageFeatures.

        Gets the image identifier.

        :return: The image_id of this ImageFeatures.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ImageFeatures.

        Gets the image identifier.

        :param image_id: The image_id of this ImageFeatures.
        :type: str
        """
        self._image_id = image_id

    @property
    def features_count(self):
        """Gets the features_count of this ImageFeatures.

        Gets the features count.

        :return: The features_count of this ImageFeatures.
        :rtype: int
        """
        return self._features_count

    @features_count.setter
    def features_count(self, features_count):
        """Sets the features_count of this ImageFeatures.

        Gets the features count.

        :param features_count: The features_count of this ImageFeatures.
        :type: int
        """
        if features_count is None:
            raise ValueError("Invalid value for `features_count`, must not be `None`")
        self._features_count = features_count

    @property
    def feature_length_in_bits(self):
        """Gets the feature_length_in_bits of this ImageFeatures.

        Gets the feature length in bits.

        :return: The feature_length_in_bits of this ImageFeatures.
        :rtype: int
        """
        return self._feature_length_in_bits

    @feature_length_in_bits.setter
    def feature_length_in_bits(self, feature_length_in_bits):
        """Sets the feature_length_in_bits of this ImageFeatures.

        Gets the feature length in bits.

        :param feature_length_in_bits: The feature_length_in_bits of this ImageFeatures.
        :type: int
        """
        if feature_length_in_bits is None:
            raise ValueError("Invalid value for `feature_length_in_bits`, must not be `None`")
        self._feature_length_in_bits = feature_length_in_bits

    @property
    def features(self):
        """Gets the features of this ImageFeatures.

        Gets the features.

        :return: The features of this ImageFeatures.
        :rtype: str
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this ImageFeatures.

        Gets the features.

        :param features: The features of this ImageFeatures.
        :type: str
        """
        if features is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', features):
            raise ValueError("Invalid value for `features`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")
        self._features = features

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
        if not isinstance(other, ImageFeatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
