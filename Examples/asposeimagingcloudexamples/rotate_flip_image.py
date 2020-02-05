#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="rotate_flip_image.py">
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


class RotateFlipImage(ImagingBase):
    """Rotate and/or flip image example"""
    def __init__(self, imaging_api):
        ImagingBase.__init__(self, imaging_api)
        self._print_header('Rotate/flip image example:')

    def _get_sample_image_file_name(self):
        return 'RotateFlipSampleImage.psd'

    def rotate_flip_image_from_storage(self):
        """Rotate and/or flip an image"""
        print('Rotate and/or flip an image from cloud storage')

        self._upload_sample_image_to_cloud()

        # Please refer to
        # https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-RotateFlip
        # for possible output formats
        format = 'gif'  # Resulting image format
        method = 'Rotate90FlipX'  # RotateFlip method
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.RotateFlipImageRequest(self._get_sample_image_file_name(), method, format, folder, storage)

        print('Call RotateFlipImage with params: method:{0}, format:{1}'.format(method, format))

        updated_image = self._imaging_api.rotate_flip_image(request)
        self._save_updated_sample_image_to_output(updated_image, False, format)
        print()

    def rotate_flip_image_and_upload_to_storage(self):
        """Rotate and/or flip an image, and upload updated image to Cloud Storage"""
        print('Rotate/flip an image and upload to cloud storage')

        self._upload_sample_image_to_cloud()

        # Please refer to
        # https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-RotateFlip
        # for possible output formats
        format = 'gif'  # Resulting image format
        method = 'Rotate90FlipX'  # RotateFlip method
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.RotateFlipImageRequest(self._get_sample_image_file_name(), method, format, folder, storage)

        print('Call RotateFlipImage with params: method: {0}, format: {1}'.format(method, format))

        updated_image = self._imaging_api.rotate_flip_image(request)
        self._upload_image_to_cloud(self._get_modified_sample_image_file_name(False, format), updated_image)
        print()

    def create_rotate_flipped_image_from_request_body(self):
        """Rotate and/or flip an image. Image data is passed in a request stream"""
        print('Rotate/flip an image from request body')

        # Please refer to
        # https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-RotateFlip
        # for possible output formats
        format = 'gif'  # Resulting image format
        method = 'Rotate90FlipX'  # RotateFlip method
        storage = None  # We are using default Cloud Storage
        out_path = None  # Path to updated file (if this is empty, response contains streamed image)

        input_stream = os.path.join(ImagingBase.EXAMPLE_IMAGES_FOLDER, self._get_sample_image_file_name())
        request = requests.CreateRotateFlippedImageRequest(input_stream, method, format, out_path, storage)

        print('Call CreateRotateFlippedImage with params: method: {0}, format: {1}'.format(method, format))

        updated_image = self._imaging_api.create_rotate_flipped_image(request)
        self._save_updated_sample_image_to_output(updated_image, True, format)
        print()

