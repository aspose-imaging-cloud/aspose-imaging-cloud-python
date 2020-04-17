#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_update_image_api.py">
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


class TestUpdateImageApi(ImagingApiTester):
    """ Class for testing UpdateImageAPI """

    def test_update_image(self):
        """ Test update_image """

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

        for format_extension in format_extension_test_cases:
            with self.subTest('format_extension: ' + str(format_extension)):
                new_width = 300
                new_height = 450
                x = 10
                y = 10
                rect_width = 200
                rect_height = 300
                rotate_flip_method = 'Rotate90FlipX'
                folder = self.temp_folder
                storage = self.test_storage

                formats_to_export = set(
                    self.basic_export_formats).union(additional_export_formats)

                def request_invoker():
                    return self.imaging_api.update_image(
                        requests.UpdateImageRequest(
                            name,
                            new_width,
                            new_height,
                            x,
                            y,
                            rect_width,
                            rect_height,
                            rotate_flip_method,
                            format,
                            folder,
                            storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertEqual(rect_height, result_properties.width)
                    self.assertEqual(rect_width, result_properties.height)

                for input_file in self.basic_input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name

                    for format in formats_to_export:
                        out_name = '{0}_crop.{1}'.format(name, format)

                        self.get_request_tester(
                            'UpdateImageTest',
                            'Input image: {0}; Output format: {1}; New width: {2}; New height: {3}; '
                            'Rotate/flip method: {4}; X: {5}; Y: {6}; Rect width: {7}; Rect height: '
                            '{8}'.format(
                                name,
                                format,
                                new_width,
                                new_height,
                                rotate_flip_method,
                                x,
                                y,
                                rect_width,
                                rect_height),
                            name,
                            request_invoker,
                            properties_tester,
                            folder,
                            storage)

    def test_create_updated_image(self):
        """ Test create_updated_image """

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
                new_width = 300
                new_height = 450
                x = 10
                y = 10
                rect_width = 200
                rect_height = 300
                rotate_flip_method = 'Rotate90FlipX'
                folder = self.temp_folder
                storage = self.test_storage

                formats_to_export = set(
                    self.basic_export_formats).union(additional_export_formats)

                def request_invoker(input_stream, out_path):
                    return self.imaging_api.create_updated_image(
                        requests.CreateUpdatedImageRequest(
                            input_stream,
                            new_width,
                            new_height,
                            x,
                            y,
                            rect_width,
                            rect_height,
                            rotate_flip_method,
                            format,
                            out_path,
                            storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertEqual(rect_height, result_properties.width)
                    self.assertEqual(rect_width, result_properties.height)

                for input_file in self.basic_input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name

                    for format in formats_to_export:
                        out_name = '{0}_crop.{1}'.format(name, format)

                        self.post_request_tester(
                            'CreateUpdatedImageTest',
                            save_result_to_storage,
                            'Input image: {0}; Output format: {1}; New width: {2}; '
                            'New height: {3}; Rotate/flip method: {4}; X: {5}; Y: {6}; '
                            'Rect width: {7}; Rect height: '
                            '{8}'.format(
                                name,
                                format,
                                new_width,
                                new_height,
                                rotate_flip_method,
                                x,
                                y,
                                rect_width,
                                rect_height),
                            name,
                            out_name,
                            request_invoker,
                            properties_tester,
                            folder,
                            storage)
