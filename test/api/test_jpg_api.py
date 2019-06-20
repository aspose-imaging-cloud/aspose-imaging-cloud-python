#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_jpg_api.py">
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

import asposeimagingcloud.models.requests as requests
from test.api import ImagingApiTester


class TestJpgApi(ImagingApiTester):
    """ Class for testing JpgAPI """

    def test_get_image_jpg(self):
        """ Test get_image_jpg """

        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.jpg'
                quality = 65
                compression_type = 'progressive'
                out_name = name + '_specific.jpg'
                folder = self.temp_folder
                storage = self.test_storage
                from_scratch = None

            def request_invoker(file_name, out_path):
                return self.imaging_api.get_image_jpg(
                    requests.GetImageJpgRequest(
                        name,
                        quality,
                        compression_type,
                        from_scratch,
                        out_path,
                        folder,
                        storage))

            def properties_tester(
                    original_properties,
                    result_properties,
                    result_stream):
                self.assertIsNotNone(result_properties.jpeg_properties)

                self.assertIsNotNone(original_properties.jpeg_properties)
                self.assertEqual(
                    original_properties.width,
                    result_properties.width)
                self.assertEqual(
                    original_properties.height,
                    result_properties.height)

            self.get_request_tester(
                'GetImageJpgTest',
                save_result_to_storage,
                'Input image: {0}; Quality: {1}; Compression type: {2}'.format(
                    name,
                    quality,
                    compression_type),
                name,
                out_name,
                request_invoker,
                properties_tester,
                folder,
                storage)

    def test_post_image_jpg(self):
        """ Test post_image_jpg """

        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.jpg'
                quality = 65
                compression_type = 'progressive'
                out_name = name + '_specific.jpg'
                folder = self.temp_folder
                storage = self.test_storage
                from_scratch = None

            def request_invoker(input_stream, out_path):
                return self.imaging_api.post_image_jpg(requests.PostImageJpgRequest(
                    input_stream, quality, compression_type, from_scratch, out_path, storage))

            def properties_tester(
                    original_properties,
                    result_properties,
                    result_stream):
                self.assertIsNotNone(result_properties.jpeg_properties)

                self.assertIsNotNone(original_properties.jpeg_properties)
                self.assertEqual(
                    original_properties.width,
                    result_properties.width)
                self.assertEqual(
                    original_properties.height,
                    result_properties.height)

            self.post_request_tester(
                'PostImageJpgTest',
                save_result_to_storage,
                'Input image: {0}; Quality: {1}; Compression type: {2}'.format(
                    name,
                    quality,
                    compression_type),
                name,
                out_name,
                request_invoker,
                properties_tester,
                folder,
                storage)
