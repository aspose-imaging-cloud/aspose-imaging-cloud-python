#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="update_jpeg_image.py">
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


class UpdateJpegImage(ImagingBase):
    """Update JPEG image example"""
    def __init__(self, imaging_api):
        ImagingBase.__init__(self, imaging_api)
        self._print_header('Update JPEG image example:')

    def _get_sample_image_file_name(self):
        return 'UpdateJPEGSampleImage.jpg'

    def modify_jpeg_from_storage(self):
        """Update parameters of a JPEG image. The image is saved in the cloud"""
        print('Update parameters of a JPEG image from cloud storage')

        self._upload_sample_image_to_cloud()

        quality = 65
        compression_type = 'progressive'
        from_scratch = None
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.ModifyJpegRequest(self._get_sample_image_file_name(), quality, compression_type,
                                             from_scratch, folder, storage)

        print('Call ModifyJpeg with params: quality: {0}, compression type: {1}'.format(quality, compression_type))

        updated_image = self._imaging_api.modify_jpeg(request)
        self._save_updated_sample_image_to_output(updated_image, False)
        print()

    def modify_jpeg_and_upload_to_storage(self):
        """Update parameters of a JPEG image, and upload updated image to Cloud Storage"""
        print('Update parameters of a JPEG image and upload to cloud storage')

        self._upload_sample_image_to_cloud()

        quality = 65
        compression_type = 'progressive'
        from_scratch = None
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.ModifyJpegRequest(self._get_sample_image_file_name(), quality, compression_type,
                                             from_scratch, folder, storage)

        print('Call ModifyJpeg with params: quality: {0}, compression type: {1}'.format(quality, compression_type))

        updated_image = self._imaging_api.modify_jpeg(request)
        self._upload_image_to_cloud(self._get_modified_sample_image_file_name(), updated_image)
        print()

    def create_modified_jpeg_from_request_body(self):
        """Update parameters of a JPEG image. Image data is passed in a request stream"""
        print('Update parameters of a JPEG image from request body')

        quality = 65
        compression_type = 'progressive'
        from_scratch = None
        storage = None  # We are using default Cloud Storage
        out_path = None  # Path to updated file (if this is empty, response contains streamed image)

        input_stream = os.path.join(ImagingBase.EXAMPLE_IMAGES_FOLDER, self._get_sample_image_file_name())
        request = requests.CreateModifiedJpegRequest(input_stream, quality, compression_type, from_scratch, out_path,
                                                     storage)

        print('Call CreateModifiedJpeg with params: quality: {0}, compression type: {1}'.format(quality,
                                                                                                compression_type))

        updated_image = self._imaging_api.create_modified_jpeg(request)
        self._save_updated_sample_image_to_output(updated_image, True)
        print()
