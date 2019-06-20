#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_resize_api.py">
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

from itertools import product

import asposeimagingcloud.models.requests as requests
from test.api import ImagingApiTester


class TestResizeApi(ImagingApiTester):
    """ Class for testing ResizeAPI"""

    def test_get_image_resize(self):
        """  Test get_image_resize """

        additional_export_formats = set()
        if not self.EXTENDED_TEST:
            format_extension_test_cases = ['.jpg']
        else:
            format_extension_test_cases = [
                '.jpg',
                '.bmp',
                '.dicom',
                '.gif',
                '.j2k',
                '.png',
                '.psd',
                '.tiff',
                '.webp']
        save_result_to_storage_test_cases = [True, False]

        for (
                save_result_to_storage,
                format_extension) in list(
                product(
                save_result_to_storage_test_cases,
                format_extension_test_cases)):
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)) and \
                    self.subTest('format_extension: ' + str(format_extension)):

                new_width = 100
                new_height = 150
                folder = self.temp_folder
                storage = self.test_storage

                formats_to_export = set(
                    self.basic_export_formats).union(additional_export_formats)

                def request_invoker(file_name, out_path):
                    return self.imaging_api.get_image_resize(requests.GetImageResizeRequest(
                        file_name, format, new_width, new_height, out_path, folder, storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertEqual(new_width, result_properties.width)
                    self.assertEqual(new_height, result_properties.height)

                for input_file in self.input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name

                    for format in formats_to_export:
                        out_name = '{0}_crop.{1}'.format(name, format)

                        self.get_request_tester(
                            'GetImageResizeTest',
                            save_result_to_storage,
                            'Input image: {0}; Output format: {1}; New width: {2}; New height: '
                            '{3};'.format(
                                name,
                                format,
                                new_width,
                                new_height),
                            name,
                            out_name,
                            request_invoker,
                            properties_tester,
                            folder,
                            storage)

    def test_post_image_resize(self):
        """ Test post_image_resize """

        additional_export_formats = set()
        if not self.EXTENDED_TEST:
            format_extension_test_cases = ['.jpg']
        else:
            format_extension_test_cases = [
                '.jpg',
                '.bmp',
                '.dicom',
                '.gif',
                '.j2k',
                '.png',
                '.psd',
                '.tiff',
                '.webp']
        save_result_to_storage_test_cases = [True, False]

        for (
                save_result_to_storage,
                format_extension) in list(
                product(
                save_result_to_storage_test_cases,
                format_extension_test_cases)):
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)) and \
                    self.subTest('format_extension: ' + str(format_extension)):

                new_width = 100
                new_height = 150
                folder = self.temp_folder
                storage = self.test_storage

                formats_to_export = set(
                    self.basic_export_formats).union(additional_export_formats)

                def request_invoker(input_stream, out_path):
                    return self.imaging_api.post_image_resize(requests.PostImageResizeRequest(
                        input_stream, format, new_width, new_height, out_path, storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertEqual(new_width, result_properties.width)
                    self.assertEqual(new_height, result_properties.height)

                for input_file in self.input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name

                    for format in formats_to_export:
                        out_name = '{0}_crop.{1}'.format(name, format)

                        self.post_request_tester(
                            'PostImageResizeTest',
                            save_result_to_storage,
                            'Input image: {0}; Output format: {1}; New width: {2}; New height: '
                            '{3};'.format(
                                name,
                                format,
                                new_width,
                                new_height),
                            name,
                            out_name,
                            request_invoker,
                            properties_tester,
                            folder,
                            storage)
