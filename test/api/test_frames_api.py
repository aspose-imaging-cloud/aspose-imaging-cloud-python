#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_frames_api.py">
#    Copyright (c) 2019-2020 Aspose Pty Ltd. All rights reserved.
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
from itertools import product

import asposeimagingcloud.models.requests as requests
from test.api.imaging_api_tester import ImagingApiTester


class TestFramesApi(ImagingApiTester):
    """ Class for testing Frames API """

    def setUp(self):
        super(ImagingApiTester, self).setUp()
        self.__formats_without_properties = [
            '.cdr',
            '.cmx',
            '.otg'
        ]

    def test_get_single_frame(self):
        """ Test get_image_frame"""

        if not self.EXTENDED_TEST:
            format_extension_test_cases = ['.tiff']
        else:
            format_extension_test_cases = [
                '.cdr',
                '.cmx',
                '.dicom',
                '.djvu',
                '.gif',
                '.odg',
                '.otg',
                '.psd',
                '.webp']

        for format_extension in format_extension_test_cases:
            with self.subTest('format_extension: ' + str(format_extension)):

                frame_id = 1
                folder = self.temp_folder
                storage = self.test_storage
                export_format = TestFramesApi.__get_export_format(format_extension, False)

                def request_invoker():
                    return self.imaging_api.get_image_frame(requests.GetImageFrameRequest(
                        name, frame_id, folder=folder, storage=storage))

                def properties_tester(original_properties, result_properties, result_stream):
                    self.assertIsNotNone(result_properties)
                    if export_format in self.__formats_without_properties or export_format == '.pdf':
                        return

                    properties_name = TestFramesApi.__get_properties_name(export_format)
                    result_format_properties = getattr(result_properties, properties_name)
                    self.assertIsNotNone(result_format_properties)

                for input_file in self.multipage_input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name

                    self.get_request_tester(
                        'GetImageFrame',
                        'Input image: {0}; Frame id: {1}'.format(name, frame_id),
                        name,
                        request_invoker,
                        properties_tester,
                        folder,
                        storage)

    def test_create_single_frame(self):
        """ Test create_image_frame"""

        save_result_to_storage_test_cases = [True, False]

        if not self.EXTENDED_TEST:
            format_extension_test_cases = ['.tiff']
        else:
            format_extension_test_cases = [
                '.cdr',
                '.cmx',
                '.dicom',
                '.djvu',
                '.gif',
                '.odg',
                '.otg',
                '.psd',
                '.webp']

            for (
                    save_result_to_storage,
                    format_extension) in list(
                product(
                    save_result_to_storage_test_cases,
                    format_extension_test_cases)):
                with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)) and \
                     self.subTest('format_extension: ' + str(format_extension)):

                    frame_id = 1
                    export_format = TestFramesApi.__get_export_format(format_extension, False)
                    folder = self.temp_folder
                    storage = self.test_storage

                    def request_invoker(input_stream, out_path):
                        return self.imaging_api.create_image_frame(requests.CreateImageFrameRequest(
                            input_stream, frame_id, out_path=out_path, storage=storage))

                    def properties_tester(original_properties, result_properties, result_stream):
                        self.assertIsNotNone(result_properties)
                        if export_format in self.__formats_without_properties or export_format == '.pdf':
                            return

                        properties_name = TestFramesApi.__get_properties_name(export_format)
                        result_format_properties = getattr(result_properties, properties_name)
                        self.assertIsNotNone(result_format_properties)

                    for input_file in self.multipage_input_test_files:
                        if not str(input_file.name).endswith(format_extension):
                            continue

                        name = input_file.name

                        out_name = '{0}_single_frame{1}'.format(name, export_format)

                        self.post_request_tester(
                            'CreateImageFrame',
                            save_result_to_storage,
                            'Input image: {0}; Frame id: {1}'.format(name, frame_id),
                            name,
                            out_name,
                            request_invoker,
                            properties_tester,
                            folder,
                            storage)

    def test_get_frame_range(self):
        """Test get_image_frame_range"""

        if not self.EXTENDED_TEST:
            format_extension_test_cases = ['.tiff']
        else:
            format_extension_test_cases = [
                '.cdr',
                '.cmx',
                '.dicom',
                '.djvu',
                '.gif',
                '.odg',
                '.otg',
                '.psd',
                '.webp']

        for format_extension in format_extension_test_cases:
            with self.subTest('format_extension: ' + str(format_extension)):

                start_frame_id = 0
                end_frame_id = 1
                folder = self.temp_folder
                storage = self.test_storage
                export_format = TestFramesApi.__get_export_format(format_extension, False)

                def request_invoker():
                    request = requests.GetImageFrameRangeRequest(
                        name, start_frame_id, end_frame_id, folder=folder, storage=storage)
                    return self.imaging_api.get_image_frame_range(request)

                def properties_tester(original_properties, result_properties, result_stream):
                    self.assertIsNotNone(result_properties)
                    if export_format in self.__formats_without_properties:
                        return

                    properties_name = TestFramesApi.__get_properties_name(export_format)
                    result_format_properties = getattr(result_properties, properties_name)
                    self.assertIsNotNone(result_format_properties)

                for input_file in self.multipage_input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name

                    self.get_request_tester(
                        'GetImageFrameRange',
                        'Input image: {0}; Start frame id: {1}; End frame id: {2}'.format(
                            name, start_frame_id, end_frame_id),
                        name,
                        request_invoker,
                        properties_tester,
                        folder,
                        storage)

    def test_create_frame_range(self):
        """ Test create_image_frame_range"""

        save_result_to_storage_test_cases = [True, False]

        if not self.EXTENDED_TEST:
            format_extension_test_cases = ['.tiff']
        else:
            format_extension_test_cases = [
                '.cdr',
                '.cmx',
                '.dicom',
                '.djvu',
                '.gif',
                '.odg',
                '.otg',
                '.psd',
                '.webp']

            for (
                    save_result_to_storage,
                    format_extension) in list(
                product(
                    save_result_to_storage_test_cases,
                    format_extension_test_cases)):
                with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)) and \
                     self.subTest('format_extension: ' + str(format_extension)):

                    start_frame_id = 0
                    end_frame_id = 1
                    folder = self.temp_folder
                    storage = self.test_storage
                    export_format = TestFramesApi.__get_export_format(format_extension, False)

                    def request_invoker(input_stream, out_path):
                        return self.imaging_api.create_image_frame_range(requests.CreateImageFrameRangeRequest(
                            input_stream, start_frame_id, end_frame_id, out_path=out_path, storage=storage))

                    def properties_tester(original_properties, result_properties, result_stream):
                        self.assertIsNotNone(result_properties)
                        if export_format in self.__formats_without_properties:
                            return

                        properties_name = TestFramesApi.__get_properties_name(export_format)
                        result_format_properties = getattr(result_properties, properties_name)
                        self.assertIsNotNone(result_format_properties)

                    for input_file in self.multipage_input_test_files:
                        if not str(input_file.name).endswith(format_extension):
                            continue

                        name = input_file.name
                        out_name = '{0}_frame_range{1}'.format(name, export_format)

                        self.post_request_tester(
                            'CreateImageFrameRange',
                            save_result_to_storage,
                            'Input image: {0}; Start frame id: {1}; End frame id: {2}'.format(
                                name, start_frame_id, end_frame_id),
                            name,
                            out_name,
                            request_invoker,
                            properties_tester,
                            folder,
                            storage)

    def test_get_frame_properties(self):
        """Test get_image_frame_properties"""

        if not self.EXTENDED_TEST:
            format_extension_test_cases = ['.tiff']
        else:
            format_extension_test_cases = [
                '.cdr',
                '.cmx',
                '.dicom',
                '.djvu',
                '.gif',
                '.odg',
                '.otg',
                '.psd',
                '.webp']

        for format_extension in format_extension_test_cases:
            with self.subTest('format_extension: ' + str(format_extension)):

                frame_id = 1
                folder = self.temp_folder
                storage = self.test_storage

                for input_file in self.multipage_input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name
                    self._copy_input_file_to_test_folder(name, folder, storage)

                    print('GetImageFrameProperties')
                    print('Input image: {0}; Frame id: {1}'.format(name, frame_id))

                    response_message = self.imaging_api.get_image_frame_properties(
                        requests.GetImageFramePropertiesRequest(name, frame_id, folder, storage))

                    self.assertIsNotNone(response_message)
                    if format_extension in self.__formats_without_properties:
                        continue

                    properties_name = TestFramesApi.__get_properties_name(format_extension)
                    result_format_properties = getattr(response_message, properties_name)
                    self.assertIsNotNone(result_format_properties)

    def test_extract_frame_properties(self):
        """Test extract_image_frame_properties"""

        if not self.EXTENDED_TEST:
            format_extension_test_cases = ['.tiff']
        else:
            format_extension_test_cases = [
                '.cdr',
                '.cmx',
                '.dicom',
                '.djvu',
                '.gif',
                '.odg',
                '.otg',
                '.psd',
                '.webp']

        for format_extension in format_extension_test_cases:
            with self.subTest('format_extension: ' + str(format_extension)):
                frame_id = 1
                folder = self.temp_folder
                storage = self.test_storage

                for input_file in self.multipage_input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name
                    self._copy_input_file_to_test_folder(name, folder, storage)
                    image_data = self.imaging_api.download_file(requests.DownloadFileRequest(
                        os.path.join(folder, name), storage))

                    print('ExtractImageFrameProperties')
                    print('Input image: {0}; Frame id: {1}'.format(name, frame_id))

                    response_message = self.imaging_api.extract_image_frame_properties(
                        requests.ExtractImageFramePropertiesRequest(image_data, frame_id))

                    self.assertIsNotNone(response_message)
                    if format_extension in self.__formats_without_properties:
                        continue

                    properties_name = TestFramesApi.__get_properties_name(format_extension)
                    result_format_properties = getattr(response_message, properties_name)
                    self.assertIsNotNone(result_format_properties)

    @staticmethod
    def __get_properties_name(format):
        """Returns field name containing properties for specified format"""
        if not format:
            raise ValueError('Invalid format')

        if format == '.jpg':
            format = '.jpeg'
        elif format == '.j2k':
            format = '.jpeg2000'
        elif format == '.webp':
            format = '.web_p'

        return format.lstrip('.') + '_properties'

    @staticmethod
    def __get_export_format(format, is_single_frame):
        """Returns default export format for specified image format and single or range frame mode"""

        if format in [".dicom", ".dng", ".djvu", ".cdr", ".cmx", ".odg", ".otg", ".svg"]:
            return ".psd" if is_single_frame else ".pdf"
        return format
