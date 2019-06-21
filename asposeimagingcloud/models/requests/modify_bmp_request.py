#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="modify_bmp_request.py">
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

from asposeimagingcloud.models.requests.http_request import HttpRequest
from asposeimagingcloud.models.requests.imaging_request import ImagingRequest


class ModifyBmpRequest(ImagingRequest):
    """
    Request model for modify_bmp operation.
    Initializes a new instance.

    :param name Filename of image.
    :param bits_per_pixel Color depth.
    :param horizontal_resolution New horizontal resolution.
    :param vertical_resolution New vertical resolution.
    :param from_scratch Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false.
    :param folder Folder with image to process.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(
            self,
            name,
            bits_per_pixel,
            horizontal_resolution,
            vertical_resolution,
            from_scratch=None,
            folder=None,
            storage=None):
        ImagingRequest.__init__(self)
        self.name = name
        self.bits_per_pixel = bits_per_pixel
        self.horizontal_resolution = horizontal_resolution
        self.vertical_resolution = vertical_resolution
        self.from_scratch = from_scratch
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
            raise ValueError(
                "Missing the required parameter `name` when calling `modify_bmp`")
        # verify the required parameter 'bits_per_pixel' is set
        if self.bits_per_pixel is None:
            raise ValueError(
                "Missing the required parameter `bits_per_pixel` when calling `modify_bmp`")
        # verify the required parameter 'horizontal_resolution' is set
        if self.horizontal_resolution is None:
            raise ValueError(
                "Missing the required parameter `horizontal_resolution` when calling `modify_bmp`")
        # verify the required parameter 'vertical_resolution' is set
        if self.vertical_resolution is None:
            raise ValueError(
                "Missing the required parameter `vertical_resolution` when calling `modify_bmp`")

        collection_formats = {}
        path = '/imaging/{name}/bmp'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('bitsPerPixel') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'bitsPerPixel' +
                    '}'),
                self.bits_per_pixel if self.bits_per_pixel is not None else '')
        else:
            if self.bits_per_pixel is not None:
                query_params.append(
                    (self._lowercase_first_letter('bitsPerPixel'),
                     self.bits_per_pixel))
        if self._lowercase_first_letter('horizontalResolution') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'horizontalResolution' +
                    '}'),
                self.horizontal_resolution if self.horizontal_resolution is not None else '')
        else:
            if self.horizontal_resolution is not None:
                query_params.append(
                    (self._lowercase_first_letter('horizontalResolution'),
                     self.horizontal_resolution))
        if self._lowercase_first_letter('verticalResolution') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'verticalResolution' +
                    '}'),
                self.vertical_resolution if self.vertical_resolution is not None else '')
        else:
            if self.vertical_resolution is not None:
                query_params.append(
                    (self._lowercase_first_letter('verticalResolution'),
                     self.vertical_resolution))
        if self._lowercase_first_letter('fromScratch') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'fromScratch' +
                    '}'),
                self.from_scratch if self.from_scratch is not None else '')
        else:
            if self.from_scratch is not None:
                query_params.append(
                    (self._lowercase_first_letter('fromScratch'),
                     self.from_scratch))
        if self._lowercase_first_letter('folder') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'folder' +
                    '}'),
                self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append(
                    (self._lowercase_first_letter('folder'), self.folder))
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
