#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="get_object_bounds_request.py">
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

from asposeimagingcloud.models.requests.imaging_request import ImagingRequest
from asposeimagingcloud.models.requests.http_request import HttpRequest


class GetObjectBoundsRequest(ImagingRequest):
    """
    Request model for get_object_bounds operation.
    Initializes a new instance.

    :param name Image file name.
    :param method Object detection method
    :param threshold Object detection probability threshold in percents
    :param include_label Return detected objects labels
    :param include_score Return detected objects score
    :param folder Folder
    :param storage Storage
    """

    def __init__(self, name, method=None, threshold=None, include_label=None, include_score=None, folder=None, storage=None):
        ImagingRequest.__init__(self)
        self.name = name
        self.method = method
        self.threshold = threshold
        self.include_label = include_label
        self.include_score = include_score
        self.folder = folder
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: Imaging API configuration
        :type: asposeimagingcloud.Configuration
        :return: http_request configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_object_bounds`")

        collection_formats = {}
        path = '/imaging/ai/objectdetection/{name}/bounds'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('method') in path:
            path = path.replace('{' + self._lowercase_first_letter('method' + '}'), self.method if self.method is not None else '')
        else:
            if self.method is not None:
                query_params.append((self._lowercase_first_letter('method'), self.method))
        if self._lowercase_first_letter('threshold') in path:
            path = path.replace('{' + self._lowercase_first_letter('threshold' + '}'), self.threshold if self.threshold is not None else '')
        else:
            if self.threshold is not None:
                query_params.append((self._lowercase_first_letter('threshold'), self.threshold))
        if self._lowercase_first_letter('includeLabel') in path:
            path = path.replace('{' + self._lowercase_first_letter('includeLabel' + '}'), self.include_label if self.include_label is not None else '')
        else:
            if self.include_label is not None:
                query_params.append((self._lowercase_first_letter('includeLabel'), self.include_label))
        if self._lowercase_first_letter('includeScore') in path:
            path = path.replace('{' + self._lowercase_first_letter('includeScore' + '}'), self.include_score if self.include_score is not None else '')
        else:
            if self.include_score is not None:
                query_params.append((self._lowercase_first_letter('includeScore'), self.include_score))
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params else self._select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['JWT']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
