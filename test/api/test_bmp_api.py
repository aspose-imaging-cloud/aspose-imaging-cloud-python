#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_bmp_api.py">
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

import math

import asposeimagingcloud.models.requests as requests
from test.api.imaging_api_tester import ImagingApiTester


class TestBmpApi(ImagingApiTester):
    """ Class for testing BmpAPI """

    def test_modify_bmp(self):
        """ Test modify_bmp """

        name = "test.bmp"
        bits_per_pixel = 32
        horizontal_resolution = 300
        vertical_resolution = 300
        folder = self.temp_folder
        storage = self.test_storage
        from_scratch = None

        def request_invoker():
            return self.imaging_api.modify_bmp(
                requests.ModifyBmpRequest(
                    name,
                    bits_per_pixel,
                    horizontal_resolution,
                    vertical_resolution,
                    from_scratch,
                    folder,
                    storage))

        def properties_tester(
                original_properties,
                result_properties,
                result_stream):
            self.assertIsNotNone(result_properties.bmp_properties)
            self.assertEqual(
                bits_per_pixel, result_properties.bits_per_pixel)
            self.assertEqual(vertical_resolution, math.ceil(
                float(result_properties.vertical_resolution)))
            self.assertEqual(horizontal_resolution, math.ceil(
                float(result_properties.horizontal_resolution)))

            self.assertIsNotNone(original_properties.bmp_properties)
            self.assertEqual(
                original_properties.bmp_properties.compression,
                result_properties.bmp_properties.compression)
            self.assertEqual(
                original_properties.width,
                result_properties.width)
            self.assertEqual(
                original_properties.height,
                result_properties.height)

        self.get_request_tester(
            'ModifyBmpTest',
            'Input image: {0}; Bits per pixel: {1}; Horizontal resolution: {2}; '
            'Vertical resolution: {3}'.format(
                name,
                bits_per_pixel,
                horizontal_resolution,
                vertical_resolution),
            name,
            request_invoker,
            properties_tester,
            folder,
            storage)

    def test_create_modified_bmp(self):
        """ Test create_modified_bmp """

        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = "test.bmp"
                bits_per_pixel = 32
                horizontal_resolution = 300
                vertical_resolution = 300
                out_name = name + '_specific.bmp'
                folder = self.temp_folder
                storage = self.test_storage
                from_scratch = None

                def request_invoker(input_stream, out_path):
                    return self.imaging_api.create_modified_bmp(
                        requests.CreateModifiedBmpRequest(
                            input_stream,
                            bits_per_pixel,
                            horizontal_resolution,
                            vertical_resolution,
                            from_scratch,
                            out_path,
                            storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertIsNotNone(result_properties.bmp_properties)
                    self.assertEqual(
                        bits_per_pixel, result_properties.bits_per_pixel)
                    self.assertEqual(vertical_resolution, math.ceil(
                        float(result_properties.vertical_resolution)))
                    self.assertEqual(horizontal_resolution, math.ceil(
                        float(result_properties.horizontal_resolution)))

                    self.assertIsNotNone(original_properties.bmp_properties)
                    self.assertEqual(
                        original_properties.bmp_properties.compression,
                        result_properties.bmp_properties.compression)
                    self.assertEqual(
                        original_properties.width,
                        result_properties.width)
                    self.assertEqual(
                        original_properties.height,
                        result_properties.height)

                self.post_request_tester(
                    'CreateModifiedBmpTest',
                    save_result_to_storage,
                    'Input image: {0}; Bits per pixel: {1}; Horizontal resolution: {2}; '
                    'Vertical resolution: {3}'.format(
                        name,
                        bits_per_pixel,
                        horizontal_resolution,
                        vertical_resolution),
                    name,
                    out_name,
                    request_invoker,
                    properties_tester,
                    folder,
                    storage)
