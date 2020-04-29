#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_tiff_api.py">
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


class TestTiffApi(ImagingApiTester):
    """ Class for testing TiffApi """

    def test_convert_tiff_to_fax(self):
        """ Test convert_tiff_to_fax """

        name = 'test.tiff'
        folder = self.temp_folder
        storage = self.test_storage

        def request_invoker():
            return self.imaging_api.convert_tiff_to_fax(
                requests.ConvertTiffToFaxRequest(
                    name, storage, folder))

        def properties_tester(
                original_properties,
                result_properties,
                result_stream):
            self.assertIsNotNone(result_properties.tiff_properties)
            self.assertEqual(1, result_properties.bits_per_pixel)
            self.assertEqual(196, result_properties.vertical_resolution)
            self.assertEqual(204, result_properties.horizontal_resolution)
            self.assertEqual(1728, result_properties.width)
            self.assertEqual(2200, result_properties.height)

        self.get_request_tester('ConvertTiffToFaxTest',
                                'Input image: {0}'.format(
                                    name), name, request_invoker,
                                properties_tester, folder, storage)

    def test_create_fax_tiff(self):
        """ Test create_fax_tiff """

        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.tiff'
                folder = self.temp_folder
                storage = self.test_storage
                out_name = name + '_specific.tiff'

                def request_invoker(input_stream, out_path):
                    return self.imaging_api.create_fax_tiff(
                        requests.CreateFaxTiffRequest(input_stream, out_path, storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertIsNotNone(result_properties.tiff_properties)
                    self.assertEqual(1, result_properties.bits_per_pixel)
                    self.assertEqual(196, result_properties.vertical_resolution)
                    self.assertEqual(204, result_properties.horizontal_resolution)
                    self.assertEqual(1728, result_properties.width)
                    self.assertEqual(2200, result_properties.height)

                self.post_request_tester('CreateFaxTiff',
                                         save_result_to_storage,
                                         'Input image: {0}'.format(name),
                                         name,
                                         out_name,
                                         request_invoker,
                                         properties_tester,
                                         folder,
                                         storage)

    def test_create_modified_tiff(self):
        """ Test create_modified_tiff """

        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.tiff'
                compression = 'adobedeflate'
                resolution_unit = 'inch'
                bit_depth = 1
                horizontal_resolution = 150
                vertical_resolution = 150
                out_name = name + '_specific.tiff'
                folder = self.temp_folder
                storage = self.test_storage
                from_scratch = None

                def request_invoker(input_stream, out_path):
                    kwargs = {
                        "horizontal_resolution": horizontal_resolution,
                        "vertical_resolution": vertical_resolution,
                        "storage": storage}
                    if out_path:
                        kwargs["out_path"] = out_path

                    return self.imaging_api.create_modified_tiff(
                        requests.CreateModifiedTiffRequest(
                            input_stream,
                            bit_depth,
                            compression,
                            resolution_unit,
                            horizontal_resolution,
                            vertical_resolution,
                            from_scratch,
                            out_path,
                            storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertIsNotNone(result_properties.tiff_properties)
                    self.assertEqual(
                        bit_depth * 4 if bit_depth > 1 else bit_depth,
                        result_properties.bits_per_pixel)
                    self.assertEqual(
                        vertical_resolution,
                        result_properties.vertical_resolution)
                    self.assertEqual(
                        horizontal_resolution,
                        result_properties.horizontal_resolution)

                    self.assertIsNotNone(original_properties.tiff_properties)
                    self.assertEqual(len(original_properties.tiff_properties.frames),
                                     len(result_properties.tiff_properties.frames))
                    self.assertEqual(
                        original_properties.width,
                        result_properties.width)
                    self.assertEqual(
                        original_properties.height,
                        result_properties.height)

                self.post_request_tester(
                    'CreateModifiedTiffTest',
                    save_result_to_storage,
                    'Input image: {0}; Compression: {1}; Bit depth: {2}; Horizontal resolution: '
                    '{3}; Vertical resolution: {4}'.format(
                        name,
                        compression,
                        bit_depth,
                        horizontal_resolution,
                        vertical_resolution),
                    name,
                    out_name,
                    request_invoker,
                    properties_tester,
                    folder,
                    storage)

    def test_append_tiff(self):
        """ Test append_tiff """

        passed = False
        print('AppendTiffTest')

        input_file_name = 'test.tiff'
        folder = self.temp_folder

        if not self._check_input_file_exists(input_file_name):
            raise ValueError(
                'Input file {0} doesn\'t exist in the specified storage folder: {1}. Please, upload it first.'.format(
                    input_file_name, folder))

        result_file_name = input_file_name + '_merged.tiff'

        input_path = self.temp_folder + '/' + input_file_name
        storage = self.test_storage

        try:
            print('Input image: ' + input_file_name)

            out_path = self.temp_folder + '/' + result_file_name

            # remove output file from the storage (if exists)
            if self.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    out_path, storage)).exists:
                self.imaging_api.delete_file(
                    requests.DeleteFileRequest(
                        out_path, storage))

            if not self.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    input_path,
                    storage)).exists:
                self.imaging_api.copy_file(
                    requests.CopyFileRequest(
                        self.original_data_folder +
                        '/' +
                        input_file_name,
                        folder +
                        '/' +
                        input_file_name,
                        storage,
                        storage))

            self.imaging_api.copy_file(
                requests.CopyFileRequest(
                    input_path, out_path, storage, storage))
            self.assertTrue(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        out_path, storage)))

            self.imaging_api.append_tiff(
                requests.AppendTiffRequest(
                    result_file_name, input_file_name, storage, folder))

            result_info = self._get_storage_file_info(
                folder, result_file_name, storage)
            if not result_info:
                raise ValueError(
                    'Result file {0} doesn\'t exist in the specified storage folder: {1}. Result isn\'t '
                    'present in the storage by an unknown reason.'.format(
                        result_file_name, folder))

            result_properties = self.imaging_api.get_image_properties(
                requests.GetImagePropertiesRequest(result_file_name, folder, storage))
            self.assertIsNotNone(result_properties)

            original_properties = self.imaging_api.get_image_properties(
                requests.GetImagePropertiesRequest(input_file_name, folder, storage))
            self.assertIsNotNone(original_properties)

            self.assertIsNotNone(result_properties.tiff_properties)
            self.assertIsNotNone(original_properties.tiff_properties)
            self.assertEqual(len(original_properties.tiff_properties.frames)
                             * 2, len(result_properties.tiff_properties.frames))
            self.assertEqual(
                original_properties.width,
                result_properties.width)
            self.assertEqual(
                original_properties.height,
                result_properties.height)

            passed = True

        except Exception as e:
            self.failed_any_test = True
            print(e)

        finally:
            if self.remove_result and self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(out_path, storage)).exists:
                self.imaging_api.delete_file(
                    requests.DeleteFileRequest(
                        out_path, storage))

                print('Test passed: ' + str(passed))
