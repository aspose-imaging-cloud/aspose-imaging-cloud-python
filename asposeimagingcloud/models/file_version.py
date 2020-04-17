#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="file_version.py">
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

from asposeimagingcloud.models.storage_file import StorageFile


class FileVersion(StorageFile):
    """File Version
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'version_id': 'str',
        'is_latest': 'bool'
    }

    attribute_map = {
        'version_id': 'VersionId',
        'is_latest': 'IsLatest'
    }

    def __init__(self, version_id=None, is_latest=None):
        """FileVersion - a model defined in Swagger"""
        super(FileVersion, self).__init__()

        self._version_id = None
        self._is_latest = None

        if version_id is not None:
            self.version_id = version_id
        if is_latest is not None:
            self.is_latest = is_latest

    @property
    def version_id(self):
        """Gets the version_id of this FileVersion.

        File Version ID.

        :return: The version_id of this FileVersion.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this FileVersion.

        File Version ID.

        :param version_id: The version_id of this FileVersion.
        :type: str
        """
        self._version_id = version_id

    @property
    def is_latest(self):
        """Gets the is_latest of this FileVersion.

        Specifies whether the file is (true) or is not (false) the latest version of an file.

        :return: The is_latest of this FileVersion.
        :rtype: bool
        """
        return self._is_latest

    @is_latest.setter
    def is_latest(self, is_latest):
        """Sets the is_latest of this FileVersion.

        Specifies whether the file is (true) or is not (false) the latest version of an file.

        :param is_latest: The is_latest of this FileVersion.
        :type: bool
        """
        if is_latest is None:
            raise ValueError("Invalid value for `is_latest`, must not be `None`")
        self._is_latest = is_latest

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
        if not isinstance(other, FileVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
