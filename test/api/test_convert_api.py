#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_convert_api.py">
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


class TestConvertApi(ImagingApiTester):
    """ Class for testing ConvertAPI """

    def test_convert_image(self):
        """
        Performs Convert (export to another format) operation test with GET
        method, taking input data from storage
        """

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

                folder = self.temp_folder
                storage = self.test_storage

                formats_to_export = set(
                    self.basic_export_formats).union(additional_export_formats)

                def request_invoker():
                    return self.imaging_api.convert_image(
                        requests.ConvertImageRequest(
                            name, format, folder, storage))

                for input_file in self.basic_input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name

                    for format in formats_to_export:

                        self.get_request_tester(
                            'ConvertImageTest',
                            'Input image: {0}; Output format: {1}'.format(
                                name,
                                format),
                            name,
                            request_invoker,
                            lambda x,
                            y,
                            z: None,
                            folder,
                            storage)

    def test_create_converted_image(self):
        """
        Performs Convert (export to another format) operation test with POST
        method, sending input data in request stream.
        """

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

                folder = self.temp_folder
                storage = self.test_storage

                formats_to_export = set(
                    self.basic_export_formats).union(additional_export_formats)

                def request_invoker(input_stream, out_path):
                    kwargs = {"storage": storage}
                    if out_path:
                        kwargs["out_path"] = out_path

                    return self.imaging_api.create_converted_image(
                        requests.CreateConvertedImageRequest(
                            input_stream, format, out_path, storage))

                for input_file in self.basic_input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name

                    for format in formats_to_export:
                        out_name = '{0}.{1}'.format(name, format)

                        self.post_request_tester(
                            'CreateConvertedImageTest',
                            save_result_to_storage,
                            'Input image: {0}; Output format: {1}'.format(
                                name,
                                format),
                            name,
                            out_name,
                            request_invoker,
                            lambda x,
                            y,
                            z: None,
                            folder,
                            storage)
