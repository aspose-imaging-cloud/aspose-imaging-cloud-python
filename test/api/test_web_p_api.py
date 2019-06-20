#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_web_p_api.py">
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


class TestWebPApi(ImagingApiTester):
    """ Class for testing WebPApi """

    def test_get_image_web_p(self):
        """ Test get_image_web_p """

        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'Animation.webp'
                lossless = True
                quality = 90
                anum_loop_count = 5
                anim_background_color = 'gray'
                folder = self.temp_folder
                storage = self.test_storage
                out_name = name + '_specific.webp'
                from_scratch = None

                def request_invoker(file_name, out_path):
                    return self.imaging_api.get_image_web_p(
                        requests.GetImageWebPRequest(
                            file_name,
                            lossless,
                            quality,
                            anum_loop_count,
                            anim_background_color,
                            from_scratch,
                            out_path,
                            folder,
                            storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertIsNotNone(result_properties.web_p_properties)

                    self.assertIsNotNone(original_properties.web_p_properties)
                    self.assertEqual(
                        original_properties.width,
                        result_properties.width)
                    self.assertEqual(
                        original_properties.height,
                        result_properties.height)

                self.get_request_tester(
                    'GetImageWebPTest',
                    save_result_to_storage,
                    'Input image: {0}; AnimBackgroundColor: {1}; Lossless: {2}; Quality: {3}; '
                    'AnimLoopCount: {4}'.format(
                        name,
                        anim_background_color,
                        lossless,
                        quality,
                        anum_loop_count),
                    name,
                    out_name,
                    request_invoker,
                    properties_tester,
                    folder,
                    storage)

    def test_post_image_web_p(self):
        """ Test post_image_web_p """
        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'Animation.webp'
                lossless = True
                quality = 90
                anum_loop_count = 5
                anim_background_color = 'gray'
                folder = self.temp_folder
                storage = self.test_storage
                out_name = name + '_specific.webp'
                from_scratch = None

                def request_invoker(input_stream, out_path):
                    return self.imaging_api.post_image_web_p(
                        requests.PostImageWebPRequest(
                            input_stream,
                            lossless,
                            quality,
                            anum_loop_count,
                            anim_background_color,
                            from_scratch,
                            out_path,
                            storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertIsNotNone(result_properties.web_p_properties)

                    self.assertIsNotNone(original_properties.web_p_properties)
                    self.assertEqual(
                        original_properties.width,
                        result_properties.width)
                    self.assertEqual(
                        original_properties.height,
                        result_properties.height)

                self.post_request_tester(
                    'PostImageWebPTest',
                    save_result_to_storage,
                    'Input image: {0}; AnimBackgroundColor: {1}; Lossless: {2}; Quality: {3}; '
                    'AnimLoopCount: {4}'.format(
                        name,
                        anim_background_color,
                        lossless,
                        quality,
                        anum_loop_count),
                    name,
                    out_name,
                    request_invoker,
                    properties_tester,
                    folder,
                    storage)
