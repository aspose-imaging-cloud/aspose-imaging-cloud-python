#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="update_image.py">
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


class UpdateImage(ImagingBase):
    """Update image example"""
    def __init__(self, imaging_api):
        ImagingBase.__init__(self, imaging_api)
        self._print_header('Update image example:')

    def _get_sample_image_file_name(self):
        return 'UpdateSampleImage.gif'

    def update_image_from_storage(self):
        """Updates the image"""
        print('Update an image from cloud storage')

        self._upload_sample_image_to_cloud()

        # Please refer to
        # https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-Update
        # for possible output formats
        format = 'pdf'  # Resulting image format
        new_width = 300
        new_height = 450
        x = 10
        y = 10
        rect_width = 200
        rect_height = 300
        rotate_flip_method = 'Rotate90FlipX'
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.UpdateImageRequest(self._get_sample_image_file_name(), format, new_width, new_height, x,
                                              y, rect_width, rect_height, rotate_flip_method, folder, storage)

        print('Call UpdateImage with params: new width: {0}, new height: {1}, x: {2}, y: {3}, rect width: {4}, '
              'rectHeight: {5}, rotate/flip method: {6}, format: {7}'
              .format(new_width, new_height, x, y, rect_width, rect_height, rotate_flip_method, format))

        updated_image = self._imaging_api.update_image(request)
        self._save_updated_sample_image_to_output(updated_image, False)
        print()

    def update_image_and_upload_to_storage(self):
        """Updates the sample image and upload to Cloud Storage"""
        print('Update an image and upload to cloud storage')

        self._upload_sample_image_to_cloud()

        # Please refer to
        # https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-Update
        # for possible output formats
        format = 'pdf'  # Resulting image format
        new_width = 300
        new_height = 450
        x = 10
        y = 10
        rect_width = 200
        rect_height = 300
        rotate_flip_method = 'Rotate90FlipX'
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.UpdateImageRequest(self._get_sample_image_file_name(), format, new_width, new_height, x, y,
                                              rect_width, rect_height, rotate_flip_method, folder, storage)

        print('Call UpdateImage with params: new width: {0}, new height: {1}, x: {2}, y: {3}, rect width: {4}, '
              'rectHeight: {5}, rotate/flip method: {6}, format: {7}'
              .format(new_width, new_height, x, y, rect_width, rect_height, rotate_flip_method, format))

        updated_image = self._imaging_api.update_image(request)
        self._upload_image_to_cloud(self._get_modified_sample_image_file_name(), updated_image)
        print()

    def create_updated_image_from_request_body(self):
        """Update an image. Image data is passed in a request stream"""
        print('Update an image from request body')

        # Please refer to
        # https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-Update
        # for possible output formats
        format = 'pdf'  # Resulting image format
        new_width = 300
        new_height = 450
        x = 10
        y = 10
        rect_width = 200
        rect_height = 300
        rotate_flip_method = 'Rotate90FlipX'
        storage = None  # We are using default Cloud Storage
        out_path = None  # Path to updated file (if this is empty, response contains streamed image)

        input_stream = os.path.join(ImagingBase.EXAMPLE_IMAGES_FOLDER, self._get_sample_image_file_name())
        request = requests.CreateUpdatedImageRequest(input_stream, format, new_width, new_height, x, y, rect_width,
                                                     rect_height, rotate_flip_method, out_path, storage)

        print('Call CreateUpdatedImage with params: new width: {0}, new height: {1}, x: {2}, y: {3}, rect width: {4}, '
              'rectHeight: {5}, rotate/flip method: {6}, format: {7}'
              .format(new_width, new_height, x, y, rect_width, rect_height, rotate_flip_method, format))

        updated_image = self._imaging_api.create_updated_image(request)
        self._save_updated_sample_image_to_output(updated_image, True, format)
        print()
