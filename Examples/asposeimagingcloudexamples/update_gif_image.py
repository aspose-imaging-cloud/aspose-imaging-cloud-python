#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="update_gif_image.py">
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

import os

import asposeimagingcloud.models.requests as requests

from asposeimagingcloudexamples.imaging_base import ImagingBase


class UpdateGifImage(ImagingBase):
    """Update GIF image example"""
    def __init__(self, imaging_api):
        ImagingBase.__init__(self, imaging_api)
        self._print_header('Update GIF image example:')

    def _get_sample_image_file_name(self):
        return 'UpdateGIFSampleImage.gif'

    def modify_gif_from_storage(self):
        """Update parameters of a GIF image. The image is saved in the cloud"""
        print('Update parameters of a GIF image from cloud storage')

        self._upload_sample_image_to_cloud()

        background_color_index = 5
        color_resolution = 4
        has_trailer = True
        interlaced = False
        is_palette_sorted = True
        pixel_aspect_ratio = 4
        from_scratch = None
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.ModifyGifRequest(self._get_sample_image_file_name(), background_color_index,
                                            color_resolution, has_trailer, interlaced, is_palette_sorted,
                                            pixel_aspect_ratio, from_scratch, folder, storage)

        print('Call ModifyGif with params: background color index: {0}, color resolution: {1}, has trailer: {2}, '
              'interlaced: {3}, is palette sorted: {4}, pixel aspect ratio: {5}'
              .format(background_color_index, color_resolution, has_trailer, interlaced, is_palette_sorted,
                      pixel_aspect_ratio))

        updated_image = self._imaging_api.modify_gif(request)
        self._save_updated_sample_image_to_output(updated_image, False)
        print()

    def modify_gif_and_upload_to_storage(self):
        """Update parameters of a GIF image, and upload updated image to Cloud Storage"""
        print('Update parameters of a GIF image and upload to cloud storage')

        self._upload_sample_image_to_cloud()

        background_color_index = 5
        color_resolution = 4
        has_trailer = True
        interlaced = False
        is_palette_sorted = True
        pixel_aspect_ratio = 4
        from_scratch = None
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.ModifyGifRequest(self._get_sample_image_file_name(), background_color_index,
                                            color_resolution, has_trailer, interlaced, is_palette_sorted,
                                            pixel_aspect_ratio, from_scratch, folder, storage)

        print('Call ModifyGif with params: background color index: {0}, color resolution: {1}, has trailer: {2}, '
              'interlaced: {3}, is palette sorted: {4}, pixel aspect ratio: {5}'
              .format(background_color_index, color_resolution, has_trailer, interlaced, is_palette_sorted,
                      pixel_aspect_ratio))

        updated_image = self._imaging_api.modify_gif(request)
        self._upload_image_to_cloud(self._get_modified_sample_image_file_name(), updated_image)
        print()

    def create_modified_gif_from_request_body(self):
        """Update parameters of a GIF image. Image data is passed in a request stream"""
        print('Update parameters of a GIF image from request body')

        background_color_index = 5
        color_resolution = 4
        has_trailer = True
        interlaced = False
        is_palette_sorted = True
        pixel_aspect_ratio = 4
        from_scratch = None
        storage = None  # We are using default Cloud Storage
        out_path = None  # Path to updated file (if this is empty, response contains streamed image)

        input_stream = os.path.join(ImagingBase.EXAMPLE_IMAGES_FOLDER, self._get_sample_image_file_name())
        request = requests.CreateModifiedGifRequest(input_stream, background_color_index, color_resolution,
                                                    has_trailer, interlaced, is_palette_sorted, pixel_aspect_ratio,
                                                    from_scratch, out_path, storage)

        print(
            'Call CreateModifiedGif with params: background color index: {0}, color resolution: {1}, has trailer: {2},'
            ' interlaced: {3}, is palette sorted: {4}, pixel aspect ratio: {5}'
                .format(background_color_index, color_resolution, has_trailer, interlaced, is_palette_sorted,
                        pixel_aspect_ratio))

        updated_image = self._imaging_api.create_modified_gif(request)
        self._save_updated_sample_image_to_output(updated_image, True)
        print()
