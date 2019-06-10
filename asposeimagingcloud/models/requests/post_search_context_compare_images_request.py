# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="post_search_context_compare_images_request.py">
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

from asposeimagingcloud.models.requests.imaging_request import ImagingRequest
from asposeimagingcloud.models.requests.http_request import HttpRequest


class PostSearchContextCompareImagesRequest(ImagingRequest):
    """
    Request model for post_search_context_compare_images operation.
    Initializes a new instance.

    :param search_context_id The search context identifier.
    :param image_id1 The first image Id in storage.
    :param image_data Input image
    :param image_id2 The second image Idin storage or null(if image loading in request).
    :param folder The folder.
    :param storage The storage.
    """

    def __init__(self, search_context_id, image_id1, image_data=None, image_id2=None, folder=None, storage=None):
        ImagingRequest.__init__(self)
        self.search_context_id = search_context_id
        self.image_id1 = image_id1
        self.image_data = image_data
        self.image_id2 = image_id2
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
        # verify the required parameter 'search_context_id' is set
        if self.search_context_id is None:
            raise ValueError("Missing the required parameter `search_context_id` when calling `post_search_context_compare_images`")  # noqa: E501
        # verify the required parameter 'image_id1' is set
        if self.image_id1 is None:
            raise ValueError("Missing the required parameter `image_id1` when calling `post_search_context_compare_images`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/ai/imageSearch/{searchContextId}/compare'
        path_params = {}
        if self.search_context_id is not None:
            path_params[self._lowercase_first_letter('searchContextId')] = self.search_context_id  # noqa: E501

        query_params = []
        if self._lowercase_first_letter('imageId1') in path:
            path = path.replace('{' + self._lowercase_first_letter('imageId1' + '}'), self.image_id1 if self.image_id1 is not None else '')
        else:
            if self.image_id1 is not None:
                query_params.append((self._lowercase_first_letter('imageId1'), self.image_id1))  # noqa: E501
        if self._lowercase_first_letter('imageId2') in path:
            path = path.replace('{' + self._lowercase_first_letter('imageId2' + '}'), self.image_id2 if self.image_id2 is not None else '')
        else:
            if self.image_id2 is not None:
                query_params.append((self._lowercase_first_letter('imageId2'), self.image_id2))  # noqa: E501
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))  # noqa: E501
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if self.image_data is not None:
            local_var_files.append((self._lowercase_first_letter('imageData'), self.image_data))  # noqa: E501

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)