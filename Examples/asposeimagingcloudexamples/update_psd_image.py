#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="update_psd_image.py">
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


class UpdatePsdImage(ImagingBase):
    """Update PSD image example"""
    def __init__(self, imaging_api):
        ImagingBase.__init__(self, imaging_api)
        self._print_header('Update PSD image example:')

    def _get_sample_image_file_name(self):
        return 'UpdatePSDSampleImage.psd'

    def modify_psd_from_storage(self):
        """Update parameters of a PSD image. The image is saved in the cloud"""
        print('Update parameters of a PSD image from cloud storage')

        self._upload_sample_image_to_cloud()

        channels_count = 3
        compression_method = 'raw'
        from_scratch = None
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.ModifyPsdRequest(self._get_sample_image_file_name(), channels_count, compression_method,
                                            from_scratch, folder, storage)

        print('Call ModifyPsd with params: channels count: {0}, compression method: {1}'.format(channels_count,
                                                                                                compression_method))

        updated_image = self._imaging_api.modify_psd(request)
        self._save_updated_sample_image_to_output(updated_image, False)
        print()

    def modify_psd_and_upload_to_storage(self):
        """Update parameters of a PSD image, and upload updated image to Cloud Storage"""
        print('Update parameters of a PSD image and upload to cloud storage')

        self._upload_sample_image_to_cloud()

        channels_count = 3
        compression_method = 'raw'
        from_scratch = None
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.ModifyPsdRequest(self._get_sample_image_file_name(), channels_count, compression_method,
                                            from_scratch, folder, storage)

        print('Call ModifyPsd with params: channels count: {0}, compression method: {1}'.format(channels_count,
                                                                                                compression_method))

        updated_image = self._imaging_api.modify_psd(request)
        self._upload_image_to_cloud(self._get_modified_sample_image_file_name(), updated_image)
        print()

    def create_modified_psd_from_request_body(self):
        """Update parameters of a PSD image. Image data is passed in a request stream"""
        print('Update parameters of a PSD image from request body')

        channels_count = 3
        compression_method = 'raw'
        from_scratch = None
        storage = None  # We are using default Cloud Storage
        out_path = None  # Path to updated file (if this is empty, response contains streamed image)

        input_stream = os.path.join(ImagingBase.EXAMPLE_IMAGES_FOLDER, self._get_sample_image_file_name())
        request = requests.CreateModifiedPsdRequest(input_stream, channels_count, compression_method, from_scratch,
                                                    out_path, storage)

        print('Call CreateModifiedPsd with params: channels count: {0}, compression method: {1}'.format(
            channels_count, compression_method))

        updated_image = self._imaging_api.create_modified_psd(request)
        self._save_updated_sample_image_to_output(updated_image, True)
        print()
