#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="eps_properties.py">
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


class EpsProperties(object):
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
        'bounding_box_string': 'str',
        'creation_date_string': 'str',
        'creator': 'str',
        'post_script_version': 'str',
        'title': 'str'
    }

    attribute_map = {
        'bounding_box_string': 'BoundingBoxString',
        'creation_date_string': 'CreationDateString',
        'creator': 'Creator',
        'post_script_version': 'PostScriptVersion',
        'title': 'Title'
    }

    def __init__(self, bounding_box_string=None, creation_date_string=None, creator=None, post_script_version=None, title=None):
        """EpsProperties - a model defined in Swagger"""
        super(EpsProperties, self).__init__()

        self._bounding_box_string = None
        self._creation_date_string = None
        self._creator = None
        self._post_script_version = None
        self._title = None

        if bounding_box_string is not None:
            self.bounding_box_string = bounding_box_string
        if creation_date_string is not None:
            self.creation_date_string = creation_date_string
        if creator is not None:
            self.creator = creator
        if post_script_version is not None:
            self.post_script_version = post_script_version
        if title is not None:
            self.title = title

    @property
    def bounding_box_string(self):
        """Gets the bounding_box_string of this EpsProperties.

        Gets the BoundingBox.

        :return: The bounding_box_string of this EpsProperties.
        :rtype: str
        """
        return self._bounding_box_string

    @bounding_box_string.setter
    def bounding_box_string(self, bounding_box_string):
        """Sets the bounding_box_string of this EpsProperties.

        Gets the BoundingBox.

        :param bounding_box_string: The bounding_box_string of this EpsProperties.
        :type: str
        """
        self._bounding_box_string = bounding_box_string

    @property
    def creation_date_string(self):
        """Gets the creation_date_string of this EpsProperties.

        Gets the CreationDate.

        :return: The creation_date_string of this EpsProperties.
        :rtype: str
        """
        return self._creation_date_string

    @creation_date_string.setter
    def creation_date_string(self, creation_date_string):
        """Sets the creation_date_string of this EpsProperties.

        Gets the CreationDate.

        :param creation_date_string: The creation_date_string of this EpsProperties.
        :type: str
        """
        self._creation_date_string = creation_date_string

    @property
    def creator(self):
        """Gets the creator of this EpsProperties.

        Gets the Creator.

        :return: The creator of this EpsProperties.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this EpsProperties.

        Gets the Creator.

        :param creator: The creator of this EpsProperties.
        :type: str
        """
        self._creator = creator

    @property
    def post_script_version(self):
        """Gets the post_script_version of this EpsProperties.

        Gets the PostScript version.

        :return: The post_script_version of this EpsProperties.
        :rtype: str
        """
        return self._post_script_version

    @post_script_version.setter
    def post_script_version(self, post_script_version):
        """Sets the post_script_version of this EpsProperties.

        Gets the PostScript version.

        :param post_script_version: The post_script_version of this EpsProperties.
        :type: str
        """
        self._post_script_version = post_script_version

    @property
    def title(self):
        """Gets the title of this EpsProperties.

        Gets the Title.

        :return: The title of this EpsProperties.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this EpsProperties.

        Gets the Title.

        :param title: The title of this EpsProperties.
        :type: str
        """
        self._title = title

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
        if not isinstance(other, EpsProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
