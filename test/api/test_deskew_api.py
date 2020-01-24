#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_deskew_api.py">
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
from test.api.imaging_api_tester import ImagingApiTester


class TestDeskewApi(ImagingApiTester):
    """ Class for testing DeskewAPI """

    def test_deskew_image(self):
        """ Test deskew_image """

        if not self.EXTENDED_TEST:
            format_extension_test_cases = [".jpg"]
        else:
            format_extension_test_cases = [
                ".jpg",
                ".bmp",
                ".gif",
                ".j2k",
                ".png",
                ".psd",
                ".tiff",
                ".webp"
                # the following tests should be uncommented once export method is implemented for them (see https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap)
                #'.dicom',
                #'.dng',
                #'.djvu'
            ]

        for format_extension in format_extension_test_cases:
            with self.subTest("format_extension: " + str(format_extension)):
                folder = self.temp_folder
                storage = self.test_storage
                resize_proportinoally = True
                bk_color = "green"

                def request_invoker():
                    return self.imaging_api.deskew_image(
                        requests.DeskewImageRequest(
                            name, resize_proportinoally, bk_color, folder, storage
                        )
                    )

                def properties_tester(
                    original_properties, result_properties, result_stream
                ):
                    self.assertIsNotNone(result_stream)

                for input_file in self.input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name

                    self.get_request_tester(
                        "DeskewImageTest",
                        "Input image: {0}; Output format: {1}; Resize proportionally: {2}; BkColor: {3};".format(
                            name, format_extension, resize_proportinoally, bk_color
                        ),
                        name,
                        request_invoker,
                        properties_tester,
                        folder,
                        storage,
                    )

    def test_create_deskewed_image(self):
        """ Test create_deskewed_image"""

        if not self.EXTENDED_TEST:
            format_extension_test_cases = [".jpg"]
        else:
            format_extension_test_cases = [
                ".jpg",
                ".bmp",
                ".gif",
                ".j2k",
                ".png",
                ".psd",
                ".tiff",
                ".webp"
                # the following tests should be uncommented once export method is implemented for them (see https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap)
                #'.dicom',
                #'.dng',
                #'.djvu'
            ]

        save_result_to_storage_test_cases = [True, False]

        for (save_result_to_storage, format_extension) in list(
            product(save_result_to_storage_test_cases, format_extension_test_cases)
        ):
            with self.subTest(
                "save_result_to_storage: " + str(save_result_to_storage)
            ) and self.subTest("format_extension: " + str(format_extension)):
                resize_proportionally = True
                bk_color = "green"
                folder = self.temp_folder
                storage = self.test_storage

                def request_invoker(input_stream, out_path):
                    return self.imaging_api.create_deskewed_image(
                        requests.CreateDeskewedImageRequest(
                            input_stream,
                            resize_proportionally,
                            bk_color,
                            out_path,
                            storage,
                        )
                    )

                def properties_tester(
                    original_properties, result_properties, result_stream
                ):
                    self.assertNotEqual(
                        original_properties.width, result_properties.width
                    )

                for input_file in self.input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name

                    out_name = "{0}_deskew.{1}".format(name, format_extension)

                    self.post_request_tester(
                        "CreateDeskewedImageTest",
                        save_result_to_storage,
                        "Input image: {0}; Output format: {1}; Resize Proportionally: {2}; Background color: {3};".format(
                            name, format_extension, resize_proportionally, bk_color
                        ),
                        name,
                        out_name,
                        request_invoker,
                        properties_tester,
                        folder,
                        storage,
                    )
