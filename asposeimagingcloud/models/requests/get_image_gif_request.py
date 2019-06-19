# coding: utf-8
# -----------------------------------------------------------------------------
# <copyright company="Aspose" file="get_image_gif_request.py">
#   Copyright (c) 2019 Aspose Pty Ltd. All rights reserved.
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a
#  copy  of this software and associated documentation files (the "Software"),
#  to deal  in the Software without restriction, including without limitation
#  the rights  to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell  copies of the Software, and to permit persons to whom the
#  Software is  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM,  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------

from asposeimagingcloud.models.requests.imaging_request import ImagingRequest
from asposeimagingcloud.models.requests.http_request import HttpRequest


class GetImageGifRequest(ImagingRequest):
    """
    Request model for get_image_gif operation.
    Initializes a new instance.

    :param name Filename of image.
    :param background_color_index Index of the background color.
    :param color_resolution Color resolution.
    :param has_trailer Specifies if image has trailer.
    :param interlaced Specifies if image is interlaced.
    :param is_palette_sorted Specifies if palette is sorted.
    :param pixel_aspect_ratio Pixel aspect ratio.
    :param from_scratch Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false.
    :param out_path Path to updated file (if this is empty, response contains streamed image).
    :param folder Folder with image to process.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(
            self,
            name,
            background_color_index=None,
            color_resolution=None,
            has_trailer=None,
            interlaced=None,
            is_palette_sorted=None,
            pixel_aspect_ratio=None,
            from_scratch=None,
            out_path=None,
            folder=None,
            storage=None):
        ImagingRequest.__init__(self)
        self.name = name
        self.background_color_index = background_color_index
        self.color_resolution = color_resolution
        self.has_trailer = has_trailer
        self.interlaced = interlaced
        self.is_palette_sorted = is_palette_sorted
        self.pixel_aspect_ratio = pixel_aspect_ratio
        self.from_scratch = from_scratch
        self.out_path = out_path
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
                "Missing the required parameter `name` when calling `get_image_gif`")

        collection_formats = {}
        path = '/imaging/{name}/gif'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('backgroundColorIndex') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'backgroundColorIndex' +
                    '}'),
                self.background_color_index if self.background_color_index is not None else '')
        else:
            if self.background_color_index is not None:
                query_params.append(
                    (self._lowercase_first_letter('backgroundColorIndex'),
                     self.background_color_index))
        if self._lowercase_first_letter('colorResolution') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'colorResolution' +
                    '}'),
                self.color_resolution if self.color_resolution is not None else '')
        else:
            if self.color_resolution is not None:
                query_params.append(
                    (self._lowercase_first_letter('colorResolution'),
                     self.color_resolution))
        if self._lowercase_first_letter('hasTrailer') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'hasTrailer' +
                    '}'),
                self.has_trailer if self.has_trailer is not None else '')
        else:
            if self.has_trailer is not None:
                query_params.append(
                    (self._lowercase_first_letter('hasTrailer'), self.has_trailer))
        if self._lowercase_first_letter('interlaced') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'interlaced' +
                    '}'),
                self.interlaced if self.interlaced is not None else '')
        else:
            if self.interlaced is not None:
                query_params.append(
                    (self._lowercase_first_letter('interlaced'), self.interlaced))
        if self._lowercase_first_letter('isPaletteSorted') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'isPaletteSorted' +
                    '}'),
                self.is_palette_sorted if self.is_palette_sorted is not None else '')
        else:
            if self.is_palette_sorted is not None:
                query_params.append(
                    (self._lowercase_first_letter('isPaletteSorted'),
                     self.is_palette_sorted))
        if self._lowercase_first_letter('pixelAspectRatio') in path:
            path = path.replace(
                '{' +
                self._lowercase_first_letter(
                    'pixelAspectRatio' +
                    '}'),
                self.pixel_aspect_ratio if self.pixel_aspect_ratio is not None else '')
        else:
            if self.pixel_aspect_ratio is not None:
                query_params.append((self._lowercase_first_letter(
                    'pixelAspectRatio'), self.pixel_aspect_ratio))
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
                    (self._lowercase_first_letter('fromScratch'), self.from_scratch))
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
