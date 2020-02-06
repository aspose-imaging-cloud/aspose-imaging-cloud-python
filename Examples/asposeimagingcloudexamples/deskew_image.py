#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="deskew_image.py">
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


class DeskewImage(ImagingBase):
    """Deskew image example"""
    def __init__(self, imaging_api):
        ImagingBase.__init__(self, imaging_api)
        self._print_header('Deskew image example:')

    def _get_sample_image_file_name(self):
        return 'DeskewSampleImage.bmp'

    def deskew_image_from_storage(self):
        """Deskews the image from cloud storage"""
        print('Deskews the image from cloud storage')

        self._upload_sample_image_to_cloud()

        resize_proportionally = True
        bk_color = 'green'
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.DeskewImageRequest(self._get_sample_image_file_name(), resize_proportionally, bk_color, folder,
                                            storage)

        print('Call DeskewImage with params: resize_proportionally: {0}, bk_color: {1}'.format(resize_proportionally, bk_color))

        updated_image = self._imaging_api.deskew_image(request)
        self._save_updated_sample_image_to_output(updated_image, False, "bmp")
        print()

    def deskew_image_and_upload_to_storage(self):
        """Deskew an existing image, and upload updated image to Cloud Storage"""
        print('Deskews the image and upload to cloud storage')

        self._upload_sample_image_to_cloud()

        resize_proportionally = True
        bk_color = 'green'
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.DeskewImageRequest(self._get_sample_image_file_name(), resize_proportionally, bk_color, folder,
                                            storage)

        print('Call DeskewImage with params: resize_proportionally: {0}, bk_color: {1}'.format(resize_proportionally, bk_color))

        updated_image = self._imaging_api.deskew_image(request)
        self._upload_image_to_cloud(self._get_modified_sample_image_file_name(False, "bmp"), updated_image)
        print()

    def create_deskewed_image_from_request_body(self):
        """Deskew an image. Image data is passed in a request stream"""
        print('Deskews the image from request body')

        resize_proportionally = True
        bk_color = 'green'
        storage = None  # We are using default Cloud Storage
        out_path = None  # Path to updated file (if this is empty, response contains streamed image)

        input_stream = os.path.join(ImagingBase.EXAMPLE_IMAGES_FOLDER, self._get_sample_image_file_name())
        request = requests.CreateDeskewedImageRequest(input_stream, resize_proportionally, bk_color, out_path, storage)

        print('Call CreateDeskewedImage with params: resize_proportionally: {0}, bk_color: {1}'.format(resize_proportionally, bk_color))

        updated_image = self._imaging_api.create_deskewed_image(request)
        self._save_updated_sample_image_to_output(updated_image, True, "bmp")
        print()
