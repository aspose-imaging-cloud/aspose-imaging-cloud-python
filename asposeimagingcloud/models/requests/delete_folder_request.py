#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="delete_folder_request.py">
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

from asposeimagingcloud.models.requests.imaging_request import ImagingRequest
from asposeimagingcloud.models.requests.http_request import HttpRequest


class DeleteFolderRequest(ImagingRequest):
    """
    Request model for delete_folder operation.
    Initializes a new instance.

    :param path Folder path e.g. '/folder'
    :param storage_name Storage name
    :param recursive Enable to delete folders, subfolders and files
    """

    def __init__(self, path, storage_name=None, recursive=None):
        ImagingRequest.__init__(self)
        self.path = path
        self.storage_name = storage_name
        self.recursive = recursive

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: Imaging API configuration
        :type: asposeimagingcloud.Configuration
        :return: http_request configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'path' is set
        if self.path is None:
            raise ValueError(
                "Missing the required parameter `path` when calling `delete_folder`")

        collection_formats = {}
        path = '/imaging/storage/folder/{path}'
        path_params = {}
        if self.path is not None:
            path_params[self._lowercase_first_letter('path')] = self.path

        query_params = []
        if self._lowercase_first_letter('storageName') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'storageName' +
                    '}'),
                self.storage_name if self.storage_name is not None else '')
        else:
            if self.storage_name is not None:
                query_params.append(
                    (self._lowercase_first_letter('storageName'), self.storage_name))
        if self._lowercase_first_letter('recursive') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'recursive' +
                    '}'),
                self.recursive if self.recursive is not None else '')
        else:
            if self.recursive is not None:
                query_params.append(
                    (self._lowercase_first_letter('recursive'), self.recursive))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['JWT']

        return HttpRequest(
            path,
            path_params,
            query_params,
            header_params,
            form_params,
            body_params,
            local_var_files,
            collection_formats,
            auth_settings)
