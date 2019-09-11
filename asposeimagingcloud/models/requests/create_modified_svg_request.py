#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="create_modified_svg_request.py">
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


class CreateModifiedSvgRequest(ImagingRequest):
    """
    Request model for create_modified_svg operation.
    Initializes a new instance.

    :param image_data Input image
    :param color_type Color type for SVG image. Only RGB is supported for now.
    :param text_as_shapes Whether text must be converted as shapes. true if all text is turned into SVG shapes in the convertion; otherwise, false
    :param scale_x Scale X.
    :param scale_y Scale Y.
    :param page_width Width of the page.
    :param page_height Height of the page.
    :param border_x Border width. Only 0 is supported for now.
    :param border_y Border height. Only 0 is supported for now.
    :param bk_color Background color (Default is white).
    :param from_scratch Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false.
    :param out_path Path to updated file (if this is empty, response contains streamed image).
    :param storage Your Aspose Cloud Storage name.
    :param format Export format (PNG is the default one). Please, refer to the export table from https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases.
    """

    def __init__(self, image_data, color_type=None, text_as_shapes=None, scale_x=None, scale_y=None, page_width=None, page_height=None, border_x=None, border_y=None, bk_color=None, from_scratch=None, out_path=None, storage=None, format=None):
        ImagingRequest.__init__(self)
        self.image_data = image_data
        self.color_type = color_type
        self.text_as_shapes = text_as_shapes
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.page_width = page_width
        self.page_height = page_height
        self.border_x = border_x
        self.border_y = border_y
        self.bk_color = bk_color
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
            raise ValueError("Missing the required parameter `image_data` when calling `create_modified_svg`")

        collection_formats = {}
        path = '/imaging/svg'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('colorType') in path:
            path = path.replace('{' + self._lowercase_first_letter('colorType' + '}'), self.color_type if self.color_type is not None else '')
        else:
            if self.color_type is not None:
                query_params.append((self._lowercase_first_letter('colorType'), self.color_type))
        if self._lowercase_first_letter('textAsShapes') in path:
            path = path.replace('{' + self._lowercase_first_letter('textAsShapes' + '}'), self.text_as_shapes if self.text_as_shapes is not None else '')
        else:
            if self.text_as_shapes is not None:
                query_params.append((self._lowercase_first_letter('textAsShapes'), self.text_as_shapes))
        if self._lowercase_first_letter('scaleX') in path:
            path = path.replace('{' + self._lowercase_first_letter('scaleX' + '}'), self.scale_x if self.scale_x is not None else '')
        else:
            if self.scale_x is not None:
                query_params.append((self._lowercase_first_letter('scaleX'), self.scale_x))
        if self._lowercase_first_letter('scaleY') in path:
            path = path.replace('{' + self._lowercase_first_letter('scaleY' + '}'), self.scale_y if self.scale_y is not None else '')
        else:
            if self.scale_y is not None:
                query_params.append((self._lowercase_first_letter('scaleY'), self.scale_y))
        if self._lowercase_first_letter('pageWidth') in path:
            path = path.replace('{' + self._lowercase_first_letter('pageWidth' + '}'), self.page_width if self.page_width is not None else '')
        else:
            if self.page_width is not None:
                query_params.append((self._lowercase_first_letter('pageWidth'), self.page_width))
        if self._lowercase_first_letter('pageHeight') in path:
            path = path.replace('{' + self._lowercase_first_letter('pageHeight' + '}'), self.page_height if self.page_height is not None else '')
        else:
            if self.page_height is not None:
                query_params.append((self._lowercase_first_letter('pageHeight'), self.page_height))
        if self._lowercase_first_letter('borderX') in path:
            path = path.replace('{' + self._lowercase_first_letter('borderX' + '}'), self.border_x if self.border_x is not None else '')
        else:
            if self.border_x is not None:
                query_params.append((self._lowercase_first_letter('borderX'), self.border_x))
        if self._lowercase_first_letter('borderY') in path:
            path = path.replace('{' + self._lowercase_first_letter('borderY' + '}'), self.border_y if self.border_y is not None else '')
        else:
            if self.border_y is not None:
                query_params.append((self._lowercase_first_letter('borderY'), self.border_y))
        if self._lowercase_first_letter('bkColor') in path:
            path = path.replace('{' + self._lowercase_first_letter('bkColor' + '}'), self.bk_color if self.bk_color is not None else '')
        else:
            if self.bk_color is not None:
                query_params.append((self._lowercase_first_letter('bkColor'), self.bk_color))
        if self._lowercase_first_letter('fromScratch') in path:
            path = path.replace('{' + self._lowercase_first_letter('fromScratch' + '}'), self.from_scratch if self.from_scratch is not None else '')
        else:
            if self.from_scratch is not None:
                query_params.append((self._lowercase_first_letter('fromScratch'), self.from_scratch))
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
        if self._lowercase_first_letter('format') in path:
            path = path.replace('{' + self._lowercase_first_letter('format' + '}'), self.format if self.format is not None else '')
        else:
            if self.format is not None:
                query_params.append((self._lowercase_first_letter('format'), self.format))

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
        header_params['Content-Type'] = self._select_header_content_type(
            ['multipart/form-data'])

        # Authentication setting
        auth_settings = ['JWT']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
