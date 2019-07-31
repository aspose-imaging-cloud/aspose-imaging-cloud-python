#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="crop_image_request.py">
#    Copyright (c) 2018-2019 Aspose Pty Ltd. All rights reserved.
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


class CropImageRequest(ImagingRequest):
    """
    Request model for crop_image operation.
    Initializes a new instance.

    :param name Filename of an image.
    :param format Resulting image format. Please, refer to https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases.
    :param x X position of start point for cropping rectangle.
    :param y Y position of start point for cropping rectangle.
    :param width Width of cropping rectangle
    :param height Height of cropping rectangle.
    :param folder Folder with image to process.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, format, x, y, width, height, folder=None, storage=None):
        ImagingRequest.__init__(self)
        self.name = name
        self.format = format
        self.x = x
        self.y = y
        self.width = width
        self.height = height
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
            raise ValueError("Missing the required parameter `name` when calling `crop_image`")
        # verify the required parameter 'format' is set
        if self.format is None:
            raise ValueError("Missing the required parameter `format` when calling `crop_image`")
        # verify the required parameter 'x' is set
        if self.x is None:
            raise ValueError("Missing the required parameter `x` when calling `crop_image`")
        # verify the required parameter 'y' is set
        if self.y is None:
            raise ValueError("Missing the required parameter `y` when calling `crop_image`")
        # verify the required parameter 'width' is set
        if self.width is None:
            raise ValueError("Missing the required parameter `width` when calling `crop_image`")
        # verify the required parameter 'height' is set
        if self.height is None:
            raise ValueError("Missing the required parameter `height` when calling `crop_image`")

        collection_formats = {}
        path = '/imaging/{name}/crop'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('format') in path:
            path = path.replace('{' + self._lowercase_first_letter('format' + '}'), self.format if self.format is not None else '')
        else:
            if self.format is not None:
                query_params.append((self._lowercase_first_letter('format'), self.format))
        if self._lowercase_first_letter('x') in path:
            path = path.replace('{' + self._lowercase_first_letter('x' + '}'), self.x if self.x is not None else '')
        else:
            if self.x is not None:
                query_params.append((self._lowercase_first_letter('x'), self.x))
        if self._lowercase_first_letter('y') in path:
            path = path.replace('{' + self._lowercase_first_letter('y' + '}'), self.y if self.y is not None else '')
        else:
            if self.y is not None:
                query_params.append((self._lowercase_first_letter('y'), self.y))
        if self._lowercase_first_letter('width') in path:
            path = path.replace('{' + self._lowercase_first_letter('width' + '}'), self.width if self.width is not None else '')
        else:
            if self.width is not None:
                query_params.append((self._lowercase_first_letter('width'), self.width))
        if self._lowercase_first_letter('height') in path:
            path = path.replace('{' + self._lowercase_first_letter('height' + '}'), self.height if self.height is not None else '')
        else:
            if self.height is not None:
                query_params.append((self._lowercase_first_letter('height'), self.height))
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
        header_params['Content-Type'] = self._select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['JWT']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
