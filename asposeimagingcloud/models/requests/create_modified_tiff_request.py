#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="create_modified_tiff_request.py">
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


class CreateModifiedTiffRequest(ImagingRequest):
    """
    Request model for create_modified_tiff operation.
    Initializes a new instance.

    :param image_data Input image
    :param bit_depth Bit depth.
    :param compression Compression (none is default). Please, refer to https://apireference.aspose.com/net/imaging/aspose.imaging.fileformats.tiff.enums/tiffcompressions for all possible values.
    :param resolution_unit New resolution unit (none - the default one, inch or centimeter).
    :param horizontal_resolution New horizontal resolution.
    :param vertical_resolution New vertical resolution.
    :param from_scratch Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false.
    :param out_path Path to updated file (if this is empty, response contains streamed image).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, image_data, bit_depth, compression=None, resolution_unit=None, horizontal_resolution=None, vertical_resolution=None, from_scratch=None, out_path=None, storage=None):
        ImagingRequest.__init__(self)
        self.image_data = image_data
        self.bit_depth = bit_depth
        self.compression = compression
        self.resolution_unit = resolution_unit
        self.horizontal_resolution = horizontal_resolution
        self.vertical_resolution = vertical_resolution
        self.from_scratch = from_scratch
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
            raise ValueError("Missing the required parameter `image_data` when calling `create_modified_tiff`")
        # verify the required parameter 'bit_depth' is set
        if self.bit_depth is None:
            raise ValueError("Missing the required parameter `bit_depth` when calling `create_modified_tiff`")

        collection_formats = {}
        path = '/imaging/tiff'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('bitDepth') in path:
            path = path.replace('{' + self._lowercase_first_letter('bitDepth' + '}'), self.bit_depth if self.bit_depth is not None else '')
        else:
            if self.bit_depth is not None:
                query_params.append((self._lowercase_first_letter('bitDepth'), self.bit_depth))
        if self._lowercase_first_letter('compression') in path:
            path = path.replace('{' + self._lowercase_first_letter('compression' + '}'), self.compression if self.compression is not None else '')
        else:
            if self.compression is not None:
                query_params.append((self._lowercase_first_letter('compression'), self.compression))
        if self._lowercase_first_letter('resolutionUnit') in path:
            path = path.replace('{' + self._lowercase_first_letter('resolutionUnit' + '}'), self.resolution_unit if self.resolution_unit is not None else '')
        else:
            if self.resolution_unit is not None:
                query_params.append((self._lowercase_first_letter('resolutionUnit'), self.resolution_unit))
        if self._lowercase_first_letter('horizontalResolution') in path:
            path = path.replace('{' + self._lowercase_first_letter('horizontalResolution' + '}'), self.horizontal_resolution if self.horizontal_resolution is not None else '')
        else:
            if self.horizontal_resolution is not None:
                query_params.append((self._lowercase_first_letter('horizontalResolution'), self.horizontal_resolution))
        if self._lowercase_first_letter('verticalResolution') in path:
            path = path.replace('{' + self._lowercase_first_letter('verticalResolution' + '}'), self.vertical_resolution if self.vertical_resolution is not None else '')
        else:
            if self.vertical_resolution is not None:
                query_params.append((self._lowercase_first_letter('verticalResolution'), self.vertical_resolution))
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
