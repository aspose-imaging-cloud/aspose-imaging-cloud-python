#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="delete_file_request.py">
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


class TestJpeg2000Api(ImagingApiTester):
    """ Class for testing Jpeg2000API """

    def test_get_image_jpeg200(self):
        """ Test get_image_jpeg2000 """

        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.j2k'
                codec = 'jp2'
                comment = 'Aspose'
                out_name = name + '_specific.jp2'
                folder = self.temp_folder
                storage = self.test_storage
                from_scratch = None

                def request_invoker(file_name, out_path):
                    return self.imaging_api.get_image_jpeg2000(requests.GetImageJpeg2000Request(
                        name, comment, codec, from_scratch, out_path, folder, storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertIsNotNone(result_properties.jpeg2000_properties)

                    self.assertIsNotNone(
                        result_properties.jpeg2000_properties.codec)
                    self.assertEqual(
                        codec, result_properties.jpeg2000_properties.codec.lower())
                    self.assertIsNotNone(
                        result_properties.jpeg2000_properties.comments)
                    self.assertEqual(
                        comment, result_properties.jpeg2000_properties.comments[0])

                    self.assertIsNotNone(
                        original_properties.jpeg2000_properties)
                    self.assertEqual(
                        original_properties.width,
                        result_properties.width)
                    self.assertEqual(
                        original_properties.height,
                        result_properties.height)
                    self.assertIsNotNone(
                        original_properties.jpeg2000_properties.comments)
                    self.assertNotEqual(
                        comment, original_properties.jpeg2000_properties.comments[0])

                self.get_request_tester(
                    'GetImageJpeg2000Test',
                    save_result_to_storage,
                    'Input image: {0}; Comment: {1}; Codec: {2}'.format(
                        name,
                        comment,
                        codec),
                    name,
                    out_name,
                    request_invoker,
                    properties_tester,
                    folder,
                    storage)

    def test_post_image_jpeg2000(self):
        """ Test post_image_jpeg2000 """

        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.j2k'
                codec = 'jp2'
                comment = 'Aspose'
                out_name = name + '_specific.jp2'
                folder = self.temp_folder
                storage = self.test_storage
                from_scratch = None

                def request_invoker(input_stream, out_path):
                    return self.imaging_api.post_image_jpeg2000(
                        requests.PostImageJpeg2000Request(
                            input_stream, comment, codec, from_scratch, out_path, storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertIsNotNone(result_properties.jpeg2000_properties)

                    self.assertIsNotNone(
                        result_properties.jpeg2000_properties.codec)
                    self.assertEqual(
                        codec, result_properties.jpeg2000_properties.codec.lower())
                    self.assertIsNotNone(
                        result_properties.jpeg2000_properties.comments)
                    self.assertEqual(
                        comment, result_properties.jpeg2000_properties.comments[0])

                    self.assertIsNotNone(
                        original_properties.jpeg2000_properties)
                    self.assertEqual(
                        original_properties.width,
                        result_properties.width)
                    self.assertEqual(
                        original_properties.height,
                        result_properties.height)
                    self.assertIsNotNone(
                        original_properties.jpeg2000_properties.comments)
                    self.assertNotEqual(
                        comment, original_properties.jpeg2000_properties.comments[0])

                self.post_request_tester(
                    'PostImageJpeg2000Test',
                    save_result_to_storage,
                    'Input image: {0}; Comment: {1}; Codec: {2}'.format(
                        name,
                        comment,
                        codec),
                    name,
                    out_name,
                    request_invoker,
                    properties_tester,
                    folder,
                    storage)
