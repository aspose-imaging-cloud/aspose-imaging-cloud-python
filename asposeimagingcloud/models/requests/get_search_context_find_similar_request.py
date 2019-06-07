# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="get_search_context_find_similar_request.py">
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


class GetSearchContextFindSimilarRequest(ImagingRequest):
    """
    Request model for get_search_context_find_similar operation.
    Initializes a new instance.

    :param search_context_id The search context identifier.
    :param similarity_threshold The similarity threshold.
    :param max_count The maximum count.
    :param image_data Input image
    :param image_id The search image identifier.
    :param folder The folder.
    :param storage The storage.
    """

    def __init__(self, search_context_id, similarity_threshold, max_count, image_data=None, image_id=None, folder=None, storage=None):
        ImagingRequest.__init__(self)
        self.search_context_id = search_context_id
        self.similarity_threshold = similarity_threshold
        self.max_count = max_count
        self.image_data = image_data
        self.image_id = image_id
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
            raise ValueError("Missing the required parameter `search_context_id` when calling `get_search_context_find_similar`")  # noqa: E501
        # verify the required parameter 'similarity_threshold' is set
        if self.similarity_threshold is None:
            raise ValueError("Missing the required parameter `similarity_threshold` when calling `get_search_context_find_similar`")  # noqa: E501
        # verify the required parameter 'max_count' is set
        if self.max_count is None:
            raise ValueError("Missing the required parameter `max_count` when calling `get_search_context_find_similar`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/ai/imageSearch/{searchContextId}/findSimilar'
        path_params = {}
        if self.search_context_id is not None:
            path_params[self._lowercase_first_letter('searchContextId')] = self.search_context_id  # noqa: E501

        query_params = []
        if self._lowercase_first_letter('similarityThreshold') in path:
            path = path.replace('{' + self._lowercase_first_letter('similarityThreshold' + '}'), self.similarity_threshold if self.similarity_threshold is not None else '')
        else:
            if self.similarity_threshold is not None:
                query_params.append((self._lowercase_first_letter('similarityThreshold'), self.similarity_threshold))  # noqa: E501
        if self._lowercase_first_letter('maxCount') in path:
            path = path.replace('{' + self._lowercase_first_letter('maxCount' + '}'), self.max_count if self.max_count is not None else '')
        else:
            if self.max_count is not None:
                query_params.append((self._lowercase_first_letter('maxCount'), self.max_count))  # noqa: E501
        if self._lowercase_first_letter('imageId') in path:
            path = path.replace('{' + self._lowercase_first_letter('imageId' + '}'), self.image_id if self.image_id is not None else '')
        else:
            if self.image_id is not None:
                query_params.append((self._lowercase_first_letter('imageId'), self.image_id))  # noqa: E501
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
