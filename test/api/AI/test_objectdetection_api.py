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
from test.api.imaging_api_tester import ImagingApiTester


class TestObjectDetectionApi(ImagingApiTester):

    def test_visualobjectdetection(self):

        folder = self.temp_folder
        storage = self.test_storage

        def request_invoker():
            return self.imaging_api.visual_object_bounds(
                requests.VisualObjectBoundsRequest(name, None, 60, True, True,  folder,
                    storage))

        def properties_tester(
                original_properties,
                result_properties,
                result_stream):
            self.assertIsNotNone(result_stream)

        for input_file in self.basic_input_test_files:
            if str(input_file.name) != "object_detection_example.jpg":
                continue

            name = input_file.name
            self.get_request_tester(
                'VisualObjectBoundsTest',
                'Input image: {0};'.format(name),
                name,
                request_invoker,
                properties_tester,
                folder,
                storage)

    def test_objectdetection(self):

        folder = self.temp_folder
        storage = self.test_storage

        def request_invoker():
            return self.imaging_api.object_bounds(
                requests.ObjectBoundsRequest(name, None, 60, True, True,  folder,
                    storage))

        def response_tester(bounds):
            self.assertIsNotNone(bounds)

        for input_file in self.basic_input_test_files:
            if str(input_file.name) != "object_detection_example.jpg":
                continue

            name = input_file.name
            self.get_object_detection_request_tester(
                'ObjectBoundsTest',
                'Input image: {0};'.format(name),
                name,
                request_invoker,
                response_tester,
                folder,
                storage)

    def test_create_visual_object_bounds(self):
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
                        input_stream, None, 60, True, True, out_path, storage)
                    resp = self.imaging_api.create_visual_object_bounds(req)
                    return resp

                def properties_tester(result_stream):
                    self.assertIsNotNone(result_stream)

                for input_file in self.basic_input_test_files:
                    if str(input_file.name) != "object_detection_example.jpg":
                        continue

                    name = input_file.name

                    out_name = 'object_detection_example_saved.jpg'

                    self.post_request_object_detection_tester(
                        'CreateVisualObjectBoundsTest',
                        save_result_to_storage,
                        'Input image: {0};'.format(name),
                        name,
                        out_name,
                        request_invoker,
                        properties_tester,
                        folder,
                        storage)

    def test_create_object_bounds(self):
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
                        input_stream, None, 60, True, True, out_path, storage)
                    resp = self.imaging_api.create_object_bounds(req)
                    return resp

                def properties_tester(bounds):
                    self.assertIsNotNone(bounds)

                for input_file in self.basic_input_test_files:
                    if str(input_file.name) != "object_detection_example.jpg":
                        continue

                    name = input_file.name

                    out_name = 'object_detection_example_saved.jpg'

                    self.post_request_object_detection_tester(
                        'CreateObjectBoundsTest',
                        save_result_to_storage,
                        'Input image: {0};'.format(name),
                        name,
                        out_name,
                        request_invoker,
                        properties_tester,
                        folder,
                        storage)
