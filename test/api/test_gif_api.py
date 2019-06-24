#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_gif_api.py">
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


class TestGifApi(ImagingApiTester):
    """ Class for testing GifAPI """

    def test_modify_gif(self):
        """ Test modify_gif """

        name = 'test.gif'
        background_color_index = 5
        color_resolution = 4
        has_trailer = True
        interlaced = False
        is_palette_sorted = True
        pixel_aspect_ratio = 4
        folder = self.temp_folder
        storage = self.test_storage
        from_scratch = None

        def request_invoker():
            return self.imaging_api.modify_gif(
                requests.ModifyGifRequest(
                    name,
                    background_color_index,
                    color_resolution,
                    has_trailer,
                    interlaced,
                    is_palette_sorted,
                    pixel_aspect_ratio,
                    from_scratch,
                    folder,
                    storage))

        def properties_tester(
                original_properties,
                result_properties,
                result_stream):
            self.assertIsNotNone(result_properties.gif_properties)

            # TODO: enable when IMAGINGCLOUD-51 is done
            # self.assertEqual(has_trailer, result_properties.gif_properties.has_trailer)
            self.assertEqual(
                pixel_aspect_ratio,
                result_properties.gif_properties.pixel_aspect_ratio)

            self.assertIsNotNone(original_properties.gif_properties)
            self.assertEqual(
                original_properties.width,
                result_properties.width)
            self.assertEqual(
                original_properties.height,
                result_properties.height)

        self.get_request_tester(
            'ModifyGifTest',
            'Input image: {0}; Back color index: {1}; Color resolution: {2}; Has trailer: '
            '{3}; Interlaced: {4}; Is palette sorted: {5}; Pixel aspect ratio: {6}'.format(
                name,
                background_color_index,
                color_resolution,
                has_trailer,
                interlaced,
                is_palette_sorted,
                pixel_aspect_ratio),
            name,
            request_invoker,
            properties_tester,
            folder,
            storage)

    def test_create_modified_gif(self):
        """ Test create_modified_gif """

        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.gif'
                background_color_index = 5
                color_resolution = 4
                has_trailer = True
                interlaced = False
                is_palette_sorted = True
                pixel_aspect_ratio = 4
                out_name = name + '_specific.gif'
                folder = self.temp_folder
                storage = self.test_storage
                from_scratch = None

                def request_invoker(input_stream, out_path):
                    return self.imaging_api.create_modified_gif(
                        requests.CreateModifiedGifRequest(
                            input_stream,
                            background_color_index,
                            color_resolution,
                            has_trailer,
                            interlaced,
                            is_palette_sorted,
                            pixel_aspect_ratio,
                            from_scratch,
                            out_path,
                            storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertIsNotNone(result_properties.gif_properties)

                    # TODO: enable when IMAGINGCLOUD-51 is done
                    # self.assertEqual(has_trailer, result_properties.gif_properties.has_trailer)
                    self.assertEqual(
                        pixel_aspect_ratio,
                        result_properties.gif_properties.pixel_aspect_ratio)

                    self.assertIsNotNone(original_properties.gif_properties)
                    self.assertEqual(
                        original_properties.width,
                        result_properties.width)
                    self.assertEqual(
                        original_properties.height,
                        result_properties.height)

                self.post_request_tester(
                    'CreateModifiedGifTest',
                    save_result_to_storage,
                    'Input image: {0}; Back color index: {1}; Color resolution: {2}; Has trailer: '
                    '{3}; Interlaced: {4}; Is palette sorted: {5}; Pixel aspect ratio: {6}'.format(
                        name,
                        background_color_index,
                        color_resolution,
                        has_trailer,
                        interlaced,
                        is_palette_sorted,
                        pixel_aspect_ratio),
                    name,
                    out_name,
                    request_invoker,
                    properties_tester,
                    folder,
                    storage)
