#  coding: utf-8

#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_objectdetection_api.py">
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

#
#
from itertools import product

import asposeimagingcloud.models.requests as requests
from asposeimagingcloud import DetectedObjectList
from test.api.imaging_api_tester import ImagingApiTester


class TestObjectDetectionApi(ImagingApiTester):

    def test_visualobjectbounds(self):

        folder = self.temp_folder
        storage = self.test_storage

        def request_invoker():
            return self.imaging_api.visual_object_bounds(
                requests.VisualObjectBoundsRequest(name, None, 20, True, True,  folder,
                    storage))

        def properties_tester(
                original_properties,
                result_properties,
                result_stream):
            self.assertIsNotNone(result_stream)
            self.assertGreater(len(result_stream), 0)

        for input_file in self.basic_input_test_files:
            if str(input_file.name) != "test.bmp":
                continue

            name = input_file.name
            self.get_request_tester(
                'objectDetection_visualobjectbounds_test',
                'Input image: {0};'.format(name),
                name,
                request_invoker,
                properties_tester,
                folder,
                storage)

    def test_objectbounds(self):

        folder = self.temp_folder
        storage = self.test_storage

        def request_invoker():
            return self.imaging_api.object_bounds(
                requests.ObjectBoundsRequest(name, None, 20, True, True,  folder,
                    storage))

        def response_tester(bounds: DetectedObjectList):
            self.assertIsNotNone(bounds)
            self.assertIsNotNone(bounds.detected_objects);
            self.assertGreater(len(bounds.detected_objects), 0);
            self.assertIsNotNone(bounds.detected_objects[0].score);
            self.assertIsNotNone(bounds.detected_objects[0].label);
            self.assertIsNotNone(bounds.detected_objects[0].bounds);

        for input_file in self.basic_input_test_files:
            if str(input_file.name) != "test.bmp":
                continue

            name = input_file.name
            self.get_object_detection_request_tester(
                'objectDetection_objectbounds_test',
                'Input image: {0};'.format(name),
                name,
                request_invoker,
                response_tester,
                folder,
                storage)

    def test_createvisualobjectbounds(self):
        """ Test create_object_detection_image"""

        save_result_to_storage_test_cases = [True, False]

        for (save_result_to_storage) in list(
                product(
                save_result_to_storage_test_cases)):
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):

                folder = self.temp_folder
                storage = self.test_storage

                def request_invoker(input_stream, out_path):
                    req = requests.CreateVisualObjectBoundsRequest(
                        input_stream, None, 20, True, True, out_path, storage)
                    resp = self.imaging_api.create_visual_object_bounds(req)
                    return resp

                def properties_tester(result_stream):
                    self.assertIsNotNone(result_stream)
                    self.assertGreater(len(result_stream), 0)

                for input_file in self.basic_input_test_files:
                    if str(input_file.name) != "test.bmp":
                        continue

                    name = input_file.name

                    out_name = 'object_detection_test_saved.bmp'

                    self.post_request_object_detection_tester(
                        'objectDetection_createvisualobjectbounds_test',
                        save_result_to_storage,
                        'Input image: {0}; save_result_to_storage: {1}'.format(name, str(save_result_to_storage)),
                        name,
                        out_name,
                        request_invoker,
                        properties_tester,
                        folder,
                        storage)

    def test_createobjectbounds(self):
        """ Test test_create_object_bounds"""

        save_result_to_storage_test_cases = [True, False]

        for (save_result_to_storage) in list(
                product(
                save_result_to_storage_test_cases)):
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):

                folder = self.temp_folder
                storage = self.test_storage

                def request_invoker(input_stream, out_path):
                    req = requests.CreateObjectBoundsRequest(
                        input_stream, None, 20, True, True, out_path, storage)
                    resp = self.imaging_api.create_object_bounds(req)
                    return resp

                def properties_tester(bounds):
                    self.assertIsNotNone(bounds)
                    self.assertIsNotNone(bounds.detected_objects);
                    self.assertGreater(len(bounds.detected_objects), 0);
                    self.assertIsNotNone(bounds.detected_objects[0].score);
                    self.assertIsNotNone(bounds.detected_objects[0].label);
                    self.assertIsNotNone(bounds.detected_objects[0].bounds);

                for input_file in self.basic_input_test_files:
                    if str(input_file.name) != "test.bmp":
                        continue

                    name = input_file.name

                    out_name = 'object_detection_test_saved.bmp'

                    self.post_request_object_detection_tester(
                        'objectDetection_createobjectbounds_test',
                        save_result_to_storage,
                        'Input image: {0}; save_result_to_storage'.format(name, str(save_result_to_storage)),
                        name,
                        out_name,
                        request_invoker,
                        properties_tester,
                        folder,
                        storage)
