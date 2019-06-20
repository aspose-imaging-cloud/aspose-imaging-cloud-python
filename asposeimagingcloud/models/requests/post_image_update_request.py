#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="post_image_update_request.py">
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


class PostImageUpdateRequest(ImagingRequest):
    """
    Request model for post_image_update operation.
    Initializes a new instance.

    :param image_data Input image
    :param format Resulting image format. Please, refer to https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases.
    :param new_width New width of the scaled image.
    :param new_height New height of the scaled image.
    :param x X position of start point for cropping rectangle.
    :param y Y position of start point for cropping rectangle.
    :param rect_width Width of cropping rectangle.
    :param rect_height Height of cropping rectangle.
    :param rotate_flip_method RotateFlip method (Rotate180FlipNone, Rotate180FlipX, Rotate180FlipXY, Rotate180FlipY, Rotate270FlipNone, Rotate270FlipX, Rotate270FlipXY, Rotate270FlipY, Rotate90FlipNone, Rotate90FlipX, Rotate90FlipXY, Rotate90FlipY, RotateNoneFlipNone, RotateNoneFlipX, RotateNoneFlipXY, RotateNoneFlipY). Default is RotateNoneFlipNone.
    :param out_path Path to updated file (if this is empty, response contains streamed image).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(
            self,
            image_data,
            format,
            new_width,
            new_height,
            x,
            y,
            rect_width,
            rect_height,
            rotate_flip_method,
            out_path=None,
            storage=None):
        ImagingRequest.__init__(self)
        self.image_data = image_data
        self.format = format
        self.new_width = new_width
        self.new_height = new_height
        self.x = x
        self.y = y
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.rotate_flip_method = rotate_flip_method
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
            raise ValueError(
                "Missing the required parameter `image_data` when calling `post_image_update`")
        # verify the required parameter 'format' is set
        if self.format is None:
            raise ValueError(
                "Missing the required parameter `format` when calling `post_image_update`")
        # verify the required parameter 'new_width' is set
        if self.new_width is None:
            raise ValueError(
                "Missing the required parameter `new_width` when calling `post_image_update`")
        # verify the required parameter 'new_height' is set
        if self.new_height is None:
            raise ValueError(
                "Missing the required parameter `new_height` when calling `post_image_update`")
        # verify the required parameter 'x' is set
        if self.x is None:
            raise ValueError(
                "Missing the required parameter `x` when calling `post_image_update`")
        # verify the required parameter 'y' is set
        if self.y is None:
            raise ValueError(
                "Missing the required parameter `y` when calling `post_image_update`")
        # verify the required parameter 'rect_width' is set
        if self.rect_width is None:
            raise ValueError(
                "Missing the required parameter `rect_width` when calling `post_image_update`")
        # verify the required parameter 'rect_height' is set
        if self.rect_height is None:
            raise ValueError(
                "Missing the required parameter `rect_height` when calling `post_image_update`")
        # verify the required parameter 'rotate_flip_method' is set
        if self.rotate_flip_method is None:
            raise ValueError(
                "Missing the required parameter `rotate_flip_method` when calling `post_image_update`")

        collection_formats = {}
        path = '/imaging/updateImage'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('format') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'format' +
                    '}'),
                self.format if self.format is not None else '')
        else:
            if self.format is not None:
                query_params.append(
                    (self._lowercase_first_letter('format'), self.format))
        if self._lowercase_first_letter('newWidth') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'newWidth' +
                    '}'),
                self.new_width if self.new_width is not None else '')
        else:
            if self.new_width is not None:
                query_params.append(
                    (self._lowercase_first_letter('newWidth'), self.new_width))
        if self._lowercase_first_letter('newHeight') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'newHeight' +
                    '}'),
                self.new_height if self.new_height is not None else '')
        else:
            if self.new_height is not None:
                query_params.append(
                    (self._lowercase_first_letter('newHeight'), self.new_height))
        if self._lowercase_first_letter('x') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'x' +
                    '}'),
                self.x if self.x is not None else '')
        else:
            if self.x is not None:
                query_params.append(
                    (self._lowercase_first_letter('x'), self.x))
        if self._lowercase_first_letter('y') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'y' +
                    '}'),
                self.y if self.y is not None else '')
        else:
            if self.y is not None:
                query_params.append(
                    (self._lowercase_first_letter('y'), self.y))
        if self._lowercase_first_letter('rectWidth') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'rectWidth' +
                    '}'),
                self.rect_width if self.rect_width is not None else '')
        else:
            if self.rect_width is not None:
                query_params.append(
                    (self._lowercase_first_letter('rectWidth'), self.rect_width))
        if self._lowercase_first_letter('rectHeight') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'rectHeight' +
                    '}'),
                self.rect_height if self.rect_height is not None else '')
        else:
            if self.rect_height is not None:
                query_params.append(
                    (self._lowercase_first_letter('rectHeight'), self.rect_height))
        if self._lowercase_first_letter('rotateFlipMethod') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'rotateFlipMethod' +
                    '}'),
                self.rotate_flip_method if self.rotate_flip_method is not None else '')
        else:
            if self.rotate_flip_method is not None:
                query_params.append((self._lowercase_first_letter(
                    'rotateFlipMethod'), self.rotate_flip_method))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'outPath' +
                    '}'),
                self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append(
                    (self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'storage' +
                    '}'),
                self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append(
                    (self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.image_data is not None:
            local_var_files.append(
                (self._lowercase_first_letter('imageData'), self.image_data))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(
            ['multipart/form-data'])

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
