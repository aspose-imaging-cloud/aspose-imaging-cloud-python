#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="detected_object.py">
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

from asposeimagingcloud.models.rectangle import Rectangle


class DetectedObject(object):
    """
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'label': 'str',
        'score': 'float',
        'bounds': 'Rectangle'
    }

    attribute_map = {
        'label': 'Label',
        'score': 'Score',
        'bounds': 'Bounds'
    }

    def __init__(self, label=None, score=None, bounds=None):
        """DetectedObject - a model defined in Swagger"""
        super(DetectedObject, self).__init__()

        self._label = None
        self._score = None
        self._bounds = None

        if label is not None:
            self.label = label
        if score is not None:
            self.score = score
        if bounds is not None:
            self.bounds = bounds

    @property
    def label(self):
        """Gets the label of this DetectedObject.


        :return: The label of this DetectedObject.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DetectedObject.


        :param label: The label of this DetectedObject.
        :type: str
        """
        self._label = label

    @property
    def score(self):
        """Gets the score of this DetectedObject.


        :return: The score of this DetectedObject.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this DetectedObject.


        :param score: The score of this DetectedObject.
        :type: float
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")
        self._score = score

    @property
    def bounds(self):
        """Gets the bounds of this DetectedObject.


        :return: The bounds of this DetectedObject.
        :rtype: Rectangle
        """
        return self._bounds

    @bounds.setter
    def bounds(self, bounds):
        """Sets the bounds of this DetectedObject.


        :param bounds: The bounds of this DetectedObject.
        :type: Rectangle
        """
        if bounds is None:
            raise ValueError("Invalid value for `bounds`, must not be `None`")
        self._bounds = bounds

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
        if not isinstance(other, DetectedObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
