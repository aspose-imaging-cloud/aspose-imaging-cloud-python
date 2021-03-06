#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="create_object_bounds_request.py">
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


class CreateObjectBoundsRequest(ImagingRequest):
    """
    Request model for create_object_bounds operation.
    Initializes a new instance.

    :param image_data Input image
    :param method Object detection method
    :param threshold Object detection probability threshold in percents
    :param include_label Draw detected objects labels
    :param include_score Draw detected objects scores
    :param allowed_labels Comma-separated list of allowed labels
    :param blocked_labels Comma-separated list of blocked labels
    :param out_path Path to updated file (if this is empty, response contains streamed image)
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, image_data, method=None, threshold=None, include_label=None, include_score=None, allowed_labels=None, blocked_labels=None, out_path=None, storage=None):
        ImagingRequest.__init__(self)
        self.image_data = image_data
        self.method = method
        self.threshold = threshold
        self.include_label = include_label
        self.include_score = include_score
        self.allowed_labels = allowed_labels
        self.blocked_labels = blocked_labels
        self.out_path = out_path
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
            raise ValueError("Missing the required parameter `image_data` when calling `create_object_bounds`")

        collection_formats = {}
        path = '/imaging/ai/objectdetection/bounds'
        path_params = {}

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
        if self._lowercase_first_letter('allowedLabels') in path:
            path = path.replace('{' + self._lowercase_first_letter('allowedLabels' + '}'), self.allowed_labels if self.allowed_labels is not None else '')
        else:
            if self.allowed_labels is not None:
                query_params.append((self._lowercase_first_letter('allowedLabels'), self.allowed_labels))
        if self._lowercase_first_letter('blockedLabels') in path:
            path = path.replace('{' + self._lowercase_first_letter('blockedLabels' + '}'), self.blocked_labels if self.blocked_labels is not None else '')
        else:
            if self.blocked_labels is not None:
                query_params.append((self._lowercase_first_letter('blockedLabels'), self.blocked_labels))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
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
