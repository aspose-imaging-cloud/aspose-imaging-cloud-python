#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_examples.py">
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
from asposeimagingcloud import ImagingApi
from test.api import ImagingApiTester


class TestExamples(ImagingApiTester):
    """ Tests that correspond with examples code """

    def test_convert_from_storage(self):
        """ Convert from storage example test """

        config = self.imaging_api.api_client.configuration
        imaging_api = ImagingApi(
            config.api_key['api_key'], config.api_key['app_sid'], config.host,
            config.api_version)

        try:
            # upload local image to storage
            result = imaging_api.upload_file(requests.UploadFileRequest(
                'ExampleFolderPython/inputImage.png',
                os.path.join(self._local_test_folder, 'test.png'),
                storage_name=self.test_storage))

            # inspect result.Errors list if there were any
            # inspect result.Uploaded list for uploaded file names

            # convert image from storage to JPEG
            converted_image = imaging_api.convert_image(
                requests.ConvertImageRequest('inputImage.png', 'jpg',
                                            'ExampleFolderPython',
                                            storage=self.test_storage))
            # process resulting image
            # for example, save it to storage

            result = imaging_api.upload_file(requests.UploadFileRequest(
                'ExampleFolderPython/resultImage.jpg', converted_image,
                storage_name=self.test_storage))

            # inspect result.Errors list if there were any
            # inspect result.Uploaded list for uploaded file names

        finally:
            # remove files from storage
            imaging_api.delete_file(
                requests.DeleteFileRequest(
                    'ExampleFolderPython/inputImage.png',
                    storage_name=self.test_storage))
            imaging_api.delete_file(
                requests.DeleteFileRequest(
                    'ExampleFolderPython/resultImage.jpg',
                    storage_name=self.test_storage))

    def test_convert_from_stream_example(self):
        """ Convert from stream example """

        config = self.imaging_api.api_client.configuration
        imaging_api = ImagingApi(
            config.api_key['api_key'], config.api_key['app_sid'], config.host,
            config.api_version)
        remote_result_image = 'ExampleFolderPython' + '/' + 'resultImage.jpg'

        try:
            # get local image stream
            local_input_image = os.path.join(
                self._local_test_folder, 'test.png')
            # convert image from request stream to JPEG and save it to storage
            # please, use outPath parameter for saving the result to storage
            imaging_api.create_converted_image(
                requests.CreateConvertedImageRequest(
                    local_input_image, 'jpg', remote_result_image,
                    storage=self.test_storage))

            #  download saved image from storage
            saved_file = imaging_api.download_file(
                requests.DownloadFileRequest(remote_result_image,
                                             storage_name=self.test_storage))
            # TODO: process resulting image from storage

            # convert image from request stream to JPEG and read it from
            # resulting stream
            image_stream = imaging_api.create_converted_image(
                requests.CreateConvertedImageRequest(local_input_image, "jpg",
                                                   storage=self.test_storage))
            # TODO: process resulting image from response stream

        finally:
            imaging_api.delete_file(
                requests.DeleteFileRequest(remote_result_image,
                                           storage_name=self.test_storage))
