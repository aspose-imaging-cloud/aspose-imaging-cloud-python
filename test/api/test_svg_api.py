#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_svg_api.py">
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


class TestSvgApi(ImagingApiTester):
    """ Class for testing svgAPI """

    def test_modify_svg_size_rasterization(self):
        """ Test modify_svg performing rasterization of image using page size parameters """

        name = 'test.svg'
        bk_color = 'gray'
        page_width = 300
        page_height = 300
        # borderX and borderY are not supported right now, see IMAGINGNET-3543
        border_x = 0
        border_y = 0
        format = 'png'
        folder = self.temp_folder
        storage = self.test_storage
        from_scratch = None

        def request_invoker():
            return self.imaging_api.modify_svg(
                requests.ModifySvgRequest(
                    name,
                    bk_color=bk_color,
                    page_width=page_width,
                    page_height=page_height,
                    border_x=border_x,
                    border_y=border_y,
                    from_scratch=from_scratch,
                    folder=folder,
                    storage=storage,
                    format=format))

        def properties_tester(
                original_properties,
                result_properties,
                result_stream):
            width = page_width + border_x * 2
            height = page_height + border_y * 2

            self.assertIsNotNone(result_properties.png_properties)
            self.assertEqual(width, result_properties.width)
            self.assertEqual(height, result_properties.height)

        self.get_request_tester(
            'ModifySvgSizeRasterizationTest',
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

    def test_modify_svg_scale_rasterization(self):
        """ Test modify_svg performing rasterization of image using page scale parameters """

        name = 'test.svg'
        bk_color = 'gray'
        scale_x = 2
        scale_y = 2
        format = 'png'
        folder = self.temp_folder
        storage = self.test_storage
        from_scratch = None

        def request_invoker():
            return self.imaging_api.modify_svg(
                requests.ModifySvgRequest(
                    name,
                    bk_color=bk_color,
                    scale_x=scale_x,
                    scale_y=scale_y,
                    from_scratch=from_scratch,
                    folder=folder,
                    storage=storage,
                    format=format))

        def properties_tester(
                original_properties,
                result_properties,
                result_stream):
            width = original_properties.width * scale_x
            height = original_properties.height * scale_y

            self.assertIsNotNone(result_properties.png_properties)
            self.assertEqual(width, result_properties.width)
            self.assertEqual(height, result_properties.height)

        self.get_request_tester(
            'ModifySvgScaleRasterizationTest',
            'Input image: {0}; BackColor: {1}; Scale X: {2}; Scale Y: {3}'
            .format(
                name,
                bk_color,
                scale_x,
                scale_y),
            name,
            request_invoker,
            properties_tester,
            folder,
            storage)

    def test_modify_svg_update_properties(self):
        """ Test modify_svg performing update of image properties """

        name = 'test.svg'
        # Only RGB color type is supported right now, see IMAGINGNET-3543
        color_type = "rgb"
        text_as_shapes = False
        format = 'svg'
        folder = self.temp_folder
        storage = self.test_storage
        from_scratch = None

        def request_invoker():
            return self.imaging_api.modify_svg(
                requests.ModifySvgRequest(
                    name,
                    text_as_shapes=text_as_shapes,
                    color_type=color_type,
                    from_scratch=from_scratch,
                    folder=folder,
                    storage=storage,
                    format=format))

        def properties_tester(
                original_properties,
                result_properties,
                result_stream):
            self.assertIsNotNone(result_properties.svg_properties)
            self.assertEqual(color_type, result_properties.svg_properties.color_type)

        self.get_request_tester(
            'ModifySvgUpdatePropertiesTest',
            'Input image: {0}; Color type: {1}; Text as shapes: {2}'
            .format(
                name,
                color_type,
                text_as_shapes),
            name,
            request_invoker,
            properties_tester,
            folder,
            storage)

    def test_create_modified_svg_size_rasterization(self):
        """ Test create_modified_svg performing rasterization of image using page size parameters """

        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest(
                    'save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.svg'
                bk_color = 'gray'
                page_width = 300
                page_height = 300
                # borderX and borderY are not supported right now, see IMAGINGNET-3543
                border_x = 0
                border_y = 0
                format = 'png'
                out_name = name + '_specific.svg'
                folder = self.temp_folder
                storage = self.test_storage
                from_scratch = None

                def request_invoker(input_stream, out_path):
                    kwargs = ({"out_path": out_path, "storage": storage}
                    ) if out_path else ({"storage": storage})

                    return self.imaging_api.create_modified_svg(
                        requests.CreateModifiedSvgRequest(
                            input_stream,
                            bk_color=bk_color,
                            page_width=page_width,
                            page_height=page_height,
                            border_x=border_x,
                            border_y=border_y,
                            from_scratch=from_scratch,
                            out_path=out_path,
                            storage=storage,
                            format=format))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    width = page_width + border_x * 2
                    height = page_height + border_y * 2

                    self.assertIsNotNone(result_properties.png_properties)
                    self.assertEqual(width, result_properties.width)
                    self.assertEqual(height, result_properties.height)

                self.post_request_tester(
                    'CreateModifiedSvgSizeRasterizationTest',
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

    def test_create_modified_svg_scale_rasterization(self):
        """ Test create_modified_svg performing rasterization of image using page scale parameters """

        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest(
                    'save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.svg'
                bk_color = 'gray'
                scale_x = 2
                scale_y = 2
                format = 'png'
                out_name = name + '_specific.svg'
                folder = self.temp_folder
                storage = self.test_storage
                from_scratch = None

                def request_invoker(input_stream, out_path):
                    kwargs = ({"out_path": out_path, "storage": storage}
                    ) if out_path else ({"storage": storage})

                    return self.imaging_api.create_modified_svg(
                        requests.CreateModifiedSvgRequest(
                            input_stream,
                            bk_color=bk_color,
                            scale_x=scale_x,
                            scale_y=scale_y,
                            from_scratch=from_scratch,
                            out_path=out_path,
                            storage=storage,
                            format=format))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    width = original_properties.width * scale_x
                    height = original_properties.height * scale_y

                    self.assertIsNotNone(result_properties.png_properties)
                    self.assertEqual(width, result_properties.width)
                    self.assertEqual(height, result_properties.height)

                self.post_request_tester(
                    'CreateModifiedSvgScaleRasterizationTest',
                    save_result_to_storage,
                    'Input image: {0}; BackColor: {1}; Scale X: {2}; Scale Y: {3}'
                        .format(
                        name,
                        bk_color,
                        scale_x,
                        scale_y),
                    name,
                    out_name,
                    request_invoker,
                    properties_tester,
                    folder,
                    storage)

    def test_create_modified_svg_update_properties(self):
        """ Test create_modified_svg performing update of image properties """

        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest(
                    'save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.svg'
                # Only RGB color type is supported right now, see IMAGINGNET-3543
                color_type = "rgb"
                text_as_shapes = False
                format = 'svg'
                out_name = name + '_specific.svg'
                folder = self.temp_folder
                storage = self.test_storage
                from_scratch = None

                def request_invoker(input_stream, out_path):
                    kwargs = ({"out_path": out_path, "storage": storage}
                    ) if out_path else ({"storage": storage})

                    return self.imaging_api.create_modified_svg(
                        requests.CreateModifiedSvgRequest(
                            input_stream,
                            text_as_shapes=text_as_shapes,
                            color_type=color_type,
                            from_scratch=from_scratch,
                            out_path=out_path,
                            storage=storage,
                            format=format))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertIsNotNone(result_properties.svg_properties)
                    self.assertEqual(color_type, result_properties.svg_properties.color_type)

                self.post_request_tester(
                    'CreateModifiedSvgTest',
                    save_result_to_storage,
                    'Input image: {0}; Color type: {1}; Text as shapes: {2}'
                        .format(
                        name,
                        color_type,
                        text_as_shapes),
                    name,
                    out_name,
                    request_invoker,
                    properties_tester,
                    folder,
                    storage)
