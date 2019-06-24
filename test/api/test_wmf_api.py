#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_wmf_api.py">
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


class TestWmfApi(ImagingApiTester):
    """ Class for testing WmfApi """

    def test_modify_wmf(self):
        """ Test modify_wmf """

        name = 'test.wmf'
        bk_color = 'gray'
        page_width = 300
        page_height = 300
        border_x = 50
        border_y = 50
        out_name = name + '_specific.png'
        folder = self.temp_folder
        storage = self.test_storage
        from_scratch = None

        def request_invoker():
            return self.imaging_api.modify_wmf(
                requests.ModifyWmfRequest(
                    name,
                    bk_color,
                    page_width,
                    page_height,
                    border_x,
                    border_y,
                    from_scratch,
                    folder,
                    storage))

        def properties_tester(
                original_properties,
                result_properties,
                result_stream):
            self.assertIsNotNone(result_properties.png_properties)
            self.assertEqual(
                page_width + border_x * 2,
                result_properties.width)
            self.assertEqual(
                page_height + border_y * 2,
                result_properties.height)

        self.get_request_tester(
            'ModifyWmfTest',
            'Input image: {0}; BackColor: {1}; Page width: {2}; Page height: {3}; '
            'BorderX: {4}; BorderY: {5}'.format(
                name,
                bk_color,
                page_width,
                page_height,
                border_x,
                border_y),
            name,
            request_invoker,
            properties_tester,
            folder,
            storage)

    def test_create_modified_wmf(self):
        """ Test create_modified_wmf """

        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.wmf'
                bk_color = 'gray'
                page_width = 300
                page_height = 300
                border_x = 50
                border_y = 50
                out_name = name + '_specific.png'
                folder = self.temp_folder
                storage = self.test_storage
                from_scratch = None

                def request_invoker(input_stream, out_path):
                    return self.imaging_api.create_modified_wmf(
                        requests.CreateModifiedWmfRequest(
                            input_stream,
                            bk_color,
                            page_width,
                            page_height,
                            border_x,
                            border_y,
                            from_scratch,
                            out_path,
                            storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertIsNotNone(result_properties.png_properties)
                    self.assertEqual(
                        page_width + border_x * 2,
                        result_properties.width)
                    self.assertEqual(
                        page_height + border_y * 2,
                        result_properties.height)

                self.post_request_tester(
                    'CreateModifiedWmfTest',
                    save_result_to_storage,
                    'Input image: {0}; BackColor: {1}; Page width: {2}; Page height: {3}; '
                    'BorderX: {4}; BorderY: {5}'.format(
                        name,
                        bk_color,
                        page_width,
                        page_height,
                        border_x,
                        border_y),
                    name,
                    out_name,
                    request_invoker,
                    properties_tester,
                    folder,
                    storage)
