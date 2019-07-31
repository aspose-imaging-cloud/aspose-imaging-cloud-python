#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_psd_api.py">
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


class TestPsdApi(ImagingApiTester):
    """ Class for testing PsdApi """

    def test_modify_psd(self):
        """ Test modify_psd """

        name = 'test.psd'
        channels_count = 3
        compression_method = 'raw'
        folder = self.temp_folder
        storage = self.test_storage
        from_scratch = None

        def request_invoker():
            return self.imaging_api.modify_psd(
                requests.ModifyPsdRequest(
                    name,
                    channels_count,
                    compression_method,
                    from_scratch,
                    folder,
                    storage))

        def properties_tester(
                original_properties,
                result_properties,
                result_stream):
            self.assertIsNotNone(result_properties.psd_properties)
            self.assertEqual(
                compression_method,
                result_properties.psd_properties.compression.lower())
            self.assertEqual(
                channels_count,
                result_properties.psd_properties.channels_count)

            self.assertIsNotNone(original_properties.psd_properties)
            self.assertEqual(
                original_properties.width,
                result_properties.width)
            self.assertEqual(
                original_properties.height,
                result_properties.height)
            self.assertEqual(
                original_properties.psd_properties.bits_per_channel,
                result_properties.psd_properties.bits_per_channel)

        self.get_request_tester(
            'ModifyPsdTest',
            'Input image: {0}; Channel count: {1}, Compression method: '
            '{2}'.format(
                name,
                channels_count,
                compression_method),
            name,
            request_invoker,
            properties_tester,
            folder,
            storage)

    def test_create_modified_psd(self):
        """ Test create_modified_psd """

        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest(
                    'save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.psd'
                channels_count = 3
                compression_method = 'raw'
                out_name = name + '_specific.psd'
                folder = self.temp_folder
                storage = self.test_storage
                from_scratch = None

                def request_invoker(input_stream, out_path):
                    return self.imaging_api.create_modified_psd(
                        requests.CreateModifiedPsdRequest(
                            input_stream,
                            channels_count,
                            compression_method,
                            from_scratch,
                            out_path,
                            storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertIsNotNone(result_properties.psd_properties)
                    self.assertEqual(
                        compression_method,
                        result_properties.psd_properties.compression.lower())
                    self.assertEqual(
                        channels_count,
                        result_properties.psd_properties.channels_count)

                    self.assertIsNotNone(original_properties.psd_properties)
                    self.assertEqual(
                        original_properties.width,
                        result_properties.width)
                    self.assertEqual(
                        original_properties.height,
                        result_properties.height)
                    self.assertEqual(
                        original_properties.psd_properties.bits_per_channel,
                        result_properties.psd_properties.bits_per_channel)

                self.post_request_tester(
                    'CreateModifiedPsdTest',
                    save_result_to_storage,
                    'Input image: {0}; Channel count: {1}, Compression method: '
                    '{2}'.format(
                        name,
                        channels_count,
                        compression_method),
                    name,
                    out_name,
                    request_invoker,
                    properties_tester,
                    folder,
                    storage)
