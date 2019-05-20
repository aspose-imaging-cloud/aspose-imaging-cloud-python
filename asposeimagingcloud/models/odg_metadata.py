# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="OdgMetadata.py">
#   Copyright (c) 2019 Aspose Pty Ltd. All rights reserved.
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
# 
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
# 
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------
import pprint
import re  # noqa: F401

import six


class OdgMetadata(object):
    """ODG format metadata
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'generator': 'str',
        'title': 'str',
        'description': 'str',
        'subject': 'str',
        'keywords': 'str',
        'initial_creator': 'str',
        'creator': 'str',
        'printed_by': 'str',
        'creation_date_time': 'str',
        'modification_date_time': 'str',
        'print_date_time': 'str',
        'document_template': 'str',
        'automatic_reload': 'str',
        'hyperlink_behavior': 'str',
        'language': 'str',
        'editing_cycles': 'str',
        'editing_duration': 'str',
        'document_statistics': 'str'
    }

    attribute_map = {
        'generator': 'Generator',
        'title': 'Title',
        'description': 'Description',
        'subject': 'Subject',
        'keywords': 'Keywords',
        'initial_creator': 'InitialCreator',
        'creator': 'Creator',
        'printed_by': 'PrintedBy',
        'creation_date_time': 'CreationDateTime',
        'modification_date_time': 'ModificationDateTime',
        'print_date_time': 'PrintDateTime',
        'document_template': 'DocumentTemplate',
        'automatic_reload': 'AutomaticReload',
        'hyperlink_behavior': 'HyperlinkBehavior',
        'language': 'Language',
        'editing_cycles': 'EditingCycles',
        'editing_duration': 'EditingDuration',
        'document_statistics': 'DocumentStatistics'
    }

    def __init__(self, generator=None, title=None, description=None, subject=None, keywords=None, initial_creator=None, creator=None, printed_by=None, creation_date_time=None, modification_date_time=None, print_date_time=None, document_template=None, automatic_reload=None, hyperlink_behavior=None, language=None, editing_cycles=None, editing_duration=None, document_statistics=None):  # noqa: E501
        """OdgMetadata - a model defined in Swagger"""  # noqa: E501

        self._generator = None
        self._title = None
        self._description = None
        self._subject = None
        self._keywords = None
        self._initial_creator = None
        self._creator = None
        self._printed_by = None
        self._creation_date_time = None
        self._modification_date_time = None
        self._print_date_time = None
        self._document_template = None
        self._automatic_reload = None
        self._hyperlink_behavior = None
        self._language = None
        self._editing_cycles = None
        self._editing_duration = None
        self._document_statistics = None
        self.discriminator = None

        if generator is not None:
            self.generator = generator
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if subject is not None:
            self.subject = subject
        if keywords is not None:
            self.keywords = keywords
        if initial_creator is not None:
            self.initial_creator = initial_creator
        if creator is not None:
            self.creator = creator
        if printed_by is not None:
            self.printed_by = printed_by
        if creation_date_time is not None:
            self.creation_date_time = creation_date_time
        if modification_date_time is not None:
            self.modification_date_time = modification_date_time
        if print_date_time is not None:
            self.print_date_time = print_date_time
        if document_template is not None:
            self.document_template = document_template
        if automatic_reload is not None:
            self.automatic_reload = automatic_reload
        if hyperlink_behavior is not None:
            self.hyperlink_behavior = hyperlink_behavior
        if language is not None:
            self.language = language
        if editing_cycles is not None:
            self.editing_cycles = editing_cycles
        if editing_duration is not None:
            self.editing_duration = editing_duration
        if document_statistics is not None:
            self.document_statistics = document_statistics

    @property
    def generator(self):
        """Gets the generator of this OdgMetadata.  # noqa: E501

        Gets or sets the generator.  # noqa: E501

        :return: The generator of this OdgMetadata.  # noqa: E501
        :rtype: str
        """
        return self._generator

    @generator.setter
    def generator(self, generator):
        """Sets the generator of this OdgMetadata.

        Gets or sets the generator.  # noqa: E501

        :param generator: The generator of this OdgMetadata.  # noqa: E501
        :type: str
        """
        self._generator = generator

    @property
    def title(self):
        """Gets the title of this OdgMetadata.  # noqa: E501

        Gets or sets the title.  # noqa: E501

        :return: The title of this OdgMetadata.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this OdgMetadata.

        Gets or sets the title.  # noqa: E501

        :param title: The title of this OdgMetadata.  # noqa: E501
        :type: str
        """
        self._title = title

    @property
    def description(self):
        """Gets the description of this OdgMetadata.  # noqa: E501

        Gets or sets the description.  # noqa: E501

        :return: The description of this OdgMetadata.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OdgMetadata.

        Gets or sets the description.  # noqa: E501

        :param description: The description of this OdgMetadata.  # noqa: E501
        :type: str
        """
        self._description = description

    @property
    def subject(self):
        """Gets the subject of this OdgMetadata.  # noqa: E501

        Gets or sets the subject.  # noqa: E501

        :return: The subject of this OdgMetadata.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this OdgMetadata.

        Gets or sets the subject.  # noqa: E501

        :param subject: The subject of this OdgMetadata.  # noqa: E501
        :type: str
        """
        self._subject = subject

    @property
    def keywords(self):
        """Gets the keywords of this OdgMetadata.  # noqa: E501

        Gets or sets the keywords.  # noqa: E501

        :return: The keywords of this OdgMetadata.  # noqa: E501
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this OdgMetadata.

        Gets or sets the keywords.  # noqa: E501

        :param keywords: The keywords of this OdgMetadata.  # noqa: E501
        :type: str
        """
        self._keywords = keywords

    @property
    def initial_creator(self):
        """Gets the initial_creator of this OdgMetadata.  # noqa: E501

        Gets or sets the initial creator.  # noqa: E501

        :return: The initial_creator of this OdgMetadata.  # noqa: E501
        :rtype: str
        """
        return self._initial_creator

    @initial_creator.setter
    def initial_creator(self, initial_creator):
        """Sets the initial_creator of this OdgMetadata.

        Gets or sets the initial creator.  # noqa: E501

        :param initial_creator: The initial_creator of this OdgMetadata.  # noqa: E501
        :type: str
        """
        self._initial_creator = initial_creator

    @property
    def creator(self):
        """Gets the creator of this OdgMetadata.  # noqa: E501

        Gets or sets the creator.  # noqa: E501

        :return: The creator of this OdgMetadata.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this OdgMetadata.

        Gets or sets the creator.  # noqa: E501

        :param creator: The creator of this OdgMetadata.  # noqa: E501
        :type: str
        """
        self._creator = creator

    @property
    def printed_by(self):
        """Gets the printed_by of this OdgMetadata.  # noqa: E501

        Gets or sets the \"PrintedBy\" record.  # noqa: E501

        :return: The printed_by of this OdgMetadata.  # noqa: E501
        :rtype: str
        """
        return self._printed_by

    @printed_by.setter
    def printed_by(self, printed_by):
        """Sets the printed_by of this OdgMetadata.

        Gets or sets the \"PrintedBy\" record.  # noqa: E501

        :param printed_by: The printed_by of this OdgMetadata.  # noqa: E501
        :type: str
        """
        self._printed_by = printed_by

    @property
    def creation_date_time(self):
        """Gets the creation_date_time of this OdgMetadata.  # noqa: E501

        Gets or sets the creation date and time.  # noqa: E501

        :return: The creation_date_time of this OdgMetadata.  # noqa: E501
        :rtype: str
        """
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, creation_date_time):
        """Sets the creation_date_time of this OdgMetadata.

        Gets or sets the creation date and time.  # noqa: E501

        :param creation_date_time: The creation_date_time of this OdgMetadata.  # noqa: E501
        :type: str
        """
        self._creation_date_time = creation_date_time

    @property
    def modification_date_time(self):
        """Gets the modification_date_time of this OdgMetadata.  # noqa: E501

        Gets or sets the modification date and time.  # noqa: E501

        :return: The modification_date_time of this OdgMetadata.  # noqa: E501
        :rtype: str
        """
        return self._modification_date_time

    @modification_date_time.setter
    def modification_date_time(self, modification_date_time):
        """Sets the modification_date_time of this OdgMetadata.

        Gets or sets the modification date and time.  # noqa: E501

        :param modification_date_time: The modification_date_time of this OdgMetadata.  # noqa: E501
        :type: str
        """
        self._modification_date_time = modification_date_time

    @property
    def print_date_time(self):
        """Gets the print_date_time of this OdgMetadata.  # noqa: E501

        Gets or sets the print date and time.  # noqa: E501

        :return: The print_date_time of this OdgMetadata.  # noqa: E501
        :rtype: str
        """
        return self._print_date_time

    @print_date_time.setter
    def print_date_time(self, print_date_time):
        """Sets the print_date_time of this OdgMetadata.

        Gets or sets the print date and time.  # noqa: E501

        :param print_date_time: The print_date_time of this OdgMetadata.  # noqa: E501
        :type: str
        """
        self._print_date_time = print_date_time

    @property
    def document_template(self):
        """Gets the document_template of this OdgMetadata.  # noqa: E501

        Gets or sets the document template.  # noqa: E501

        :return: The document_template of this OdgMetadata.  # noqa: E501
        :rtype: str
        """
        return self._document_template

    @document_template.setter
    def document_template(self, document_template):
        """Sets the document_template of this OdgMetadata.

        Gets or sets the document template.  # noqa: E501

        :param document_template: The document_template of this OdgMetadata.  # noqa: E501
        :type: str
        """
        self._document_template = document_template

    @property
    def automatic_reload(self):
        """Gets the automatic_reload of this OdgMetadata.  # noqa: E501

        Gets or sets the automatic reload.  # noqa: E501

        :return: The automatic_reload of this OdgMetadata.  # noqa: E501
        :rtype: str
        """
        return self._automatic_reload

    @automatic_reload.setter
    def automatic_reload(self, automatic_reload):
        """Sets the automatic_reload of this OdgMetadata.

        Gets or sets the automatic reload.  # noqa: E501

        :param automatic_reload: The automatic_reload of this OdgMetadata.  # noqa: E501
        :type: str
        """
        self._automatic_reload = automatic_reload

    @property
    def hyperlink_behavior(self):
        """Gets the hyperlink_behavior of this OdgMetadata.  # noqa: E501

        Gets or sets the hyperlink behavior.  # noqa: E501

        :return: The hyperlink_behavior of this OdgMetadata.  # noqa: E501
        :rtype: str
        """
        return self._hyperlink_behavior

    @hyperlink_behavior.setter
    def hyperlink_behavior(self, hyperlink_behavior):
        """Sets the hyperlink_behavior of this OdgMetadata.

        Gets or sets the hyperlink behavior.  # noqa: E501

        :param hyperlink_behavior: The hyperlink_behavior of this OdgMetadata.  # noqa: E501
        :type: str
        """
        self._hyperlink_behavior = hyperlink_behavior

    @property
    def language(self):
        """Gets the language of this OdgMetadata.  # noqa: E501

        Gets or sets the language.  # noqa: E501

        :return: The language of this OdgMetadata.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this OdgMetadata.

        Gets or sets the language.  # noqa: E501

        :param language: The language of this OdgMetadata.  # noqa: E501
        :type: str
        """
        self._language = language

    @property
    def editing_cycles(self):
        """Gets the editing_cycles of this OdgMetadata.  # noqa: E501

        Gets or sets the editing cycles.  # noqa: E501

        :return: The editing_cycles of this OdgMetadata.  # noqa: E501
        :rtype: str
        """
        return self._editing_cycles

    @editing_cycles.setter
    def editing_cycles(self, editing_cycles):
        """Sets the editing_cycles of this OdgMetadata.

        Gets or sets the editing cycles.  # noqa: E501

        :param editing_cycles: The editing_cycles of this OdgMetadata.  # noqa: E501
        :type: str
        """
        self._editing_cycles = editing_cycles

    @property
    def editing_duration(self):
        """Gets the editing_duration of this OdgMetadata.  # noqa: E501

        Gets or sets the duration of the editing.  # noqa: E501

        :return: The editing_duration of this OdgMetadata.  # noqa: E501
        :rtype: str
        """
        return self._editing_duration

    @editing_duration.setter
    def editing_duration(self, editing_duration):
        """Sets the editing_duration of this OdgMetadata.

        Gets or sets the duration of the editing.  # noqa: E501

        :param editing_duration: The editing_duration of this OdgMetadata.  # noqa: E501
        :type: str
        """
        self._editing_duration = editing_duration

    @property
    def document_statistics(self):
        """Gets the document_statistics of this OdgMetadata.  # noqa: E501

        Gets or sets the document statistics.  # noqa: E501

        :return: The document_statistics of this OdgMetadata.  # noqa: E501
        :rtype: str
        """
        return self._document_statistics

    @document_statistics.setter
    def document_statistics(self, document_statistics):
        """Sets the document_statistics of this OdgMetadata.

        Gets or sets the document statistics.  # noqa: E501

        :param document_statistics: The document_statistics of this OdgMetadata.  # noqa: E501
        :type: str
        """
        self._document_statistics = document_statistics

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
        if not isinstance(other, OdgMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
