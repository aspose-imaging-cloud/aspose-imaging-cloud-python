#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="create_image_tag_request.py">
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


class CreateImageTagRequest(ImagingRequest):
    """
    Request model for create_image_tag operation.
    Initializes a new instance.

    :param image_data Input image
    :param search_context_id The search context identifier.
    :param tag_name The tag.
    :param folder The folder.
    :param storage The storage.
    """

    def __init__(self, image_data, search_context_id, tag_name, folder=None, storage=None):
        ImagingRequest.__init__(self)
        self.image_data = image_data
        self.search_context_id = search_context_id
        self.tag_name = tag_name
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
        # verify the required parameter 'image_data' is set
        if self.image_data is None:
            raise ValueError("Missing the required parameter `image_data` when calling `create_image_tag`")
        # verify the required parameter 'search_context_id' is set
        if self.search_context_id is None:
            raise ValueError("Missing the required parameter `search_context_id` when calling `create_image_tag`")
        # verify the required parameter 'tag_name' is set
        if self.tag_name is None:
            raise ValueError("Missing the required parameter `tag_name` when calling `create_image_tag`")

        collection_formats = {}
        path = '/imaging/ai/imageSearch/{searchContextId}/addTag'
        path_params = {}
        if self.search_context_id is not None:
            path_params[self._lowercase_first_letter('searchContextId')] = self.search_context_id

        query_params = []
        if self._lowercase_first_letter('tagName') in path:
            path = path.replace('{' + self._lowercase_first_letter('tagName' + '}'), self.tag_name if self.tag_name is not None else '')
        else:
            if self.tag_name is not None:
                query_params.append((self._lowercase_first_letter('tagName'), self.tag_name))
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
        if self.image_data is not None:
            local_var_files.append((self._lowercase_first_letter('imageData'), self.image_data))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params else self._select_header_content_type(
            ['multipart/form-data'])

        # Authentication setting
        auth_settings = ['JWT']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
