# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="post_image_wmf_request.py">
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


class PostImageWmfRequest(ImagingRequest):
    """
    Request model for post_image_wmf operation.
    Initializes a new instance.

    :param image_data Input image
    :param bk_color Color of the background.
    :param page_width Width of the page.
    :param page_height Height of the page.
    :param border_x Border width.
    :param border_y Border height.
    :param from_scratch Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false.
    :param out_path Path to updated file (if this is empty, response contains streamed image).
    :param storage Your Aspose Cloud Storage name.
    :param format Export format (PNG is the default one). Please, refer to the export table from https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases.
    """

    def __init__(self, image_data, bk_color, page_width, page_height, border_x, border_y, from_scratch=None, out_path=None, storage=None, format=None):
        ImagingRequest.__init__(self)
        self.image_data = image_data
        self.bk_color = bk_color
        self.page_width = page_width
        self.page_height = page_height
        self.border_x = border_x
        self.border_y = border_y
        self.from_scratch = from_scratch
        self.out_path = out_path
        self.storage = storage
        self.format = format

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
            raise ValueError("Missing the required parameter `image_data` when calling `post_image_wmf`")  # noqa: E501
        # verify the required parameter 'bk_color' is set
        if self.bk_color is None:
            raise ValueError("Missing the required parameter `bk_color` when calling `post_image_wmf`")  # noqa: E501
        # verify the required parameter 'page_width' is set
        if self.page_width is None:
            raise ValueError("Missing the required parameter `page_width` when calling `post_image_wmf`")  # noqa: E501
        # verify the required parameter 'page_height' is set
        if self.page_height is None:
            raise ValueError("Missing the required parameter `page_height` when calling `post_image_wmf`")  # noqa: E501
        # verify the required parameter 'border_x' is set
        if self.border_x is None:
            raise ValueError("Missing the required parameter `border_x` when calling `post_image_wmf`")  # noqa: E501
        # verify the required parameter 'border_y' is set
        if self.border_y is None:
            raise ValueError("Missing the required parameter `border_y` when calling `post_image_wmf`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/wmf'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('bkColor') in path:
            path = path.replace('{' + self._lowercase_first_letter('bkColor' + '}'), self.bk_color if self.bk_color is not None else '')
        else:
            if self.bk_color is not None:
                query_params.append((self._lowercase_first_letter('bkColor'), self.bk_color))  # noqa: E501
        if self._lowercase_first_letter('pageWidth') in path:
            path = path.replace('{' + self._lowercase_first_letter('pageWidth' + '}'), self.page_width if self.page_width is not None else '')
        else:
            if self.page_width is not None:
                query_params.append((self._lowercase_first_letter('pageWidth'), self.page_width))  # noqa: E501
        if self._lowercase_first_letter('pageHeight') in path:
            path = path.replace('{' + self._lowercase_first_letter('pageHeight' + '}'), self.page_height if self.page_height is not None else '')
        else:
            if self.page_height is not None:
                query_params.append((self._lowercase_first_letter('pageHeight'), self.page_height))  # noqa: E501
        if self._lowercase_first_letter('borderX') in path:
            path = path.replace('{' + self._lowercase_first_letter('borderX' + '}'), self.border_x if self.border_x is not None else '')
        else:
            if self.border_x is not None:
                query_params.append((self._lowercase_first_letter('borderX'), self.border_x))  # noqa: E501
        if self._lowercase_first_letter('borderY') in path:
            path = path.replace('{' + self._lowercase_first_letter('borderY' + '}'), self.border_y if self.border_y is not None else '')
        else:
            if self.border_y is not None:
                query_params.append((self._lowercase_first_letter('borderY'), self.border_y))  # noqa: E501
        if self._lowercase_first_letter('fromScratch') in path:
            path = path.replace('{' + self._lowercase_first_letter('fromScratch' + '}'), self.from_scratch if self.from_scratch is not None else '')
        else:
            if self.from_scratch is not None:
                query_params.append((self._lowercase_first_letter('fromScratch'), self.from_scratch))  # noqa: E501
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))  # noqa: E501
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))  # noqa: E501
        if self._lowercase_first_letter('format') in path:
            path = path.replace('{' + self._lowercase_first_letter('format' + '}'), self.format if self.format is not None else '')
        else:
            if self.format is not None:
                query_params.append((self._lowercase_first_letter('format'), self.format))  # noqa: E501

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
