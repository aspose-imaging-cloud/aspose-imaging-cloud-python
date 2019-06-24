#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_frames_get_api.py">
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


class TestFramesGetApi(ImagingApiTester):
    """ Class for testing FramesApi """

    def test_get_image_single_frame(self):
        """ Test get_image_frame """

        name = 'test.tiff'
        frame_id = 2
        new_width = 300
        new_height = 450
        x = 10
        y = 10
        rect_width = 200
        rect_height = 300
        rotate_flip_method = 'Rotate90FlipX'
        save_other_frames = False
        folder = self.temp_folder
        storage = self.test_storage
        out_name = name + '_singleFrame.tiff'

        def request_invoker():
            return self.imaging_api.get_image_frame(
                requests.GetImageFrameRequest(
                    name,
                    frame_id,
                    new_width,
                    new_height,
                    x,
                    y,
                    rect_width,
                    rect_height,
                    rotate_flip_method,
                    save_other_frames,
                    folder,
                    storage))

        def properties_tester(
                original_properties,
                result_properties,
                result_stream):
            self.assertIsNotNone(result_properties)
            self.assertIsNotNone(result_properties.tiff_properties)
            self.assertIsNotNone(
                result_properties.tiff_properties.frames)
            self.assertEqual(
                1, len(
                    result_properties.tiff_properties.frames))

            # please note that rotation was performed, so switching of
            # width and height comparison is valid

            self.assertEqual(
                rect_height, result_properties.tiff_properties.frames[0].width)
            self.assertEqual(
                rect_width, result_properties.tiff_properties.frames[0].height)
            self.assertEqual(
                result_properties.tiff_properties.frames[
                    0].frame_options.image_width,
                rect_height)
            self.assertEqual(
                rect_width,
                result_properties.tiff_properties.frames[
                    0].frame_options.image_length)
            self.assertEqual(rect_height, result_properties.width)
            self.assertEqual(rect_width, result_properties.height)

        self.get_request_tester(
            'GetImageSingleFrameTest',
            'Input image: {0}; Frame ID: {1}; New width: {2}; New height: {3}; '
            'Rotate/flip method: {4}; Save other frames: {5}; X: {6}; Y: {7}; Rect width: '
            '{8}; Rect height: {9}'.format(
                name,
                frame_id,
                new_width,
                new_height,
                rotate_flip_method,
                save_other_frames,
                x,
                y,
                rect_width,
                rect_height),
            name,
            request_invoker,
            properties_tester,
            folder,
            storage)

    def test_get_image_all_frames(self):
        """ Test get_image_frame """

        name = 'test.tiff'
        frame_id = 2
        new_width = 300
        new_height = 450
        x = 10
        y = 10
        rect_width = 200
        rect_height = 300
        rotate_flip_method = 'Rotate90FlipX'
        save_other_frames = True
        folder = self.temp_folder
        storage = self.test_storage

        def request_invoker():
            return self.imaging_api.get_image_frame(
                requests.GetImageFrameRequest(
                    name,
                    frame_id,
                    new_width,
                    new_height,
                    x,
                    y,
                    rect_width,
                    rect_height,
                    rotate_flip_method,
                    save_other_frames,
                    folder,
                    storage))

        def properties_tester(
                original_properties,
                result_properties,
                result_stream):
            self.assertIsNotNone(original_properties)
            self.assertIsNotNone(original_properties.tiff_properties)
            self.assertIsNotNone(
                original_properties.tiff_properties.frames)

            self.assertIsNotNone(result_properties.tiff_properties)
            self.assertIsNotNone(
                result_properties.tiff_properties.frames)
            self.assertEqual(len(original_properties.tiff_properties.frames),
                             len(result_properties.tiff_properties.frames))
            self.assertEqual(
                original_properties.width,
                result_properties.width)
            self.assertEqual(
                original_properties.height,
                result_properties.height)

            # please note that rotation was performed, so switching of
            # width and height comparison is valid

            self.assertEqual(
                rect_height,
                result_properties.tiff_properties.frames[frame_id].width)
            self.assertEqual(
                rect_width,
                result_properties.tiff_properties.frames[frame_id].height)
            self.assertEqual(
                rect_height,
                result_properties.tiff_properties.frames[
                    frame_id].frame_options.image_width)
            self.assertEqual(
                rect_width,
                result_properties.tiff_properties.frames[
                    frame_id].frame_options.image_length)

        self.get_request_tester(
            'GetImageAllFramesTest',
            'Input image: {0}; Frame ID: {1}; New width: {2}; New height: {3}; '
            'Rotate/flip method: {4}; Save other frames: {5}; X: {6}; Y: {7}; Rect width: '
            '{8}; Rect height: {9}'.format(
                name,
                frame_id,
                new_width,
                new_height,
                rotate_flip_method,
                save_other_frames,
                x,
                y,
                rect_width,
                rect_height),
            name,
            request_invoker,
            properties_tester,
            folder,
            storage)
