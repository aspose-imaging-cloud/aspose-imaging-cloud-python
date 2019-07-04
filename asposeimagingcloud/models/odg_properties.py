#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="odg_properties.py">
#    Copyright (c) 2019 Aspose Pty Ltd. All rights reserved.
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

from asposeimagingcloud.models.odg_metadata import OdgMetadata
from asposeimagingcloud.models.odg_page import OdgPage


class OdgProperties(object):
    """ODG format specific properties
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'page_count': 'int',
        'metadata': 'OdgMetadata',
        'pages': 'list[OdgPage]'
    }

    attribute_map = {
        'page_count': 'PageCount',
        'metadata': 'Metadata',
        'pages': 'Pages'
    }

    def __init__(self, page_count=None, metadata=None, pages=None):
        """OdgProperties - a model defined in Swagger"""

        self._page_count = None
        self._metadata = None
        self._pages = None
        self.discriminator = None

        if page_count is not None:
            self.page_count = page_count
        if metadata is not None:
            self.metadata = metadata
        if pages is not None:
            self.pages = pages

    @property
    def page_count(self):
        """Gets the page_count of this OdgProperties.

        Gets or sets the page count.

        :return: The page_count of this OdgProperties.
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this OdgProperties.

        Gets or sets the page count.

        :param page_count: The page_count of this OdgProperties.
        :type: int
        """
        if page_count is None:
            raise ValueError("Invalid value for `page_count`, must not be `None`")
        self._page_count = page_count

    @property
    def metadata(self):
        """Gets the metadata of this OdgProperties.

        Gets or sets the metadata.

        :return: The metadata of this OdgProperties.
        :rtype: OdgMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this OdgProperties.

        Gets or sets the metadata.

        :param metadata: The metadata of this OdgProperties.
        :type: OdgMetadata
        """
        self._metadata = metadata

    @property
    def pages(self):
        """Gets the pages of this OdgProperties.

        Gets or sets the pages.

        :return: The pages of this OdgProperties.
        :rtype: list[OdgPage]
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this OdgProperties.

        Gets or sets the pages.

        :param pages: The pages of this OdgProperties.
        :type: list[OdgPage]
        """
        self._pages = pages

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
        if not isinstance(other, OdgProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
