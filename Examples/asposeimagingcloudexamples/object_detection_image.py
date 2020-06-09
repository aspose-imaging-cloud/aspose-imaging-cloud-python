#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="object_detection_image.py">
#    Copyright (c) 2020 Aspose Pty Ltd. All rights reserved.
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

import asposeimagingcloud.models.requests as requests

from asposeimagingcloudexamples.imaging_base import ImagingBase


class ObjectDetectionImage(ImagingBase):
    """ObjectDetection image example"""
    def __init__(self, imaging_api):
        ImagingBase.__init__(self, imaging_api)
        self._print_header('Object detection image example:')

    def _get_sample_image_file_name(self):
        return 'object_detection_example.jpg'

    def detect_objects_image_from_storage(self):
        """Detect objects on an image from a cloud storage"""
        print('Detect objects on an image from a cloud storage')

        self._upload_sample_image_to_cloud()

        method = 'ssd'
        threshold = 50
        includeLabel = True
        includeScore = True

        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.GetObjectBoundsRequest(self._get_sample_image_file_name(), method, threshold,
                                               includeLabel, includeScore, folder, storage)

        print('Call ObjectBoundsRequest with params: method: {0}, threshold: {1}, includeLabel: {2}, includeScore: {3}'.format(method, threshold, includeLabel, includeScore))

        detectedObjectsList = self._imaging_api.get_object_bounds(request)
        print('objects detected: {0}'.format(len(detectedObjectsList.detected_objects)))
        print()

    def visualize_detected_objects_image_from_storage(self):
        """Get visualized detected objects and upload it to the cloud storage"""
        print('Get visualized detected objects and upload it to the cloud storage')

        self._upload_sample_image_to_cloud()

        method = 'ssd'
        threshold = 50
        includeLabel = True
        color = 'blue'
        includeScore = True

        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.GetVisualObjectBoundsRequest(self._get_sample_image_file_name(), method, threshold,
                                               includeLabel, includeScore, color, folder, storage)

        print('Call VisualObjectBoundsRequest with params: method: {0}, threshold: {1}, includeLabel: {2}, includeScore: {3}, color: {4}'.format(method, threshold, includeLabel, includeScore, color))

        updated_image = self._imaging_api.get_visual_object_bounds(request)
        self._save_updated_sample_image_to_output(updated_image, False, "jpg")
        print()


    def detect_objects_image_from_request_body(self):
        """detected object on an image that is passed in a request stream"""
        print('detected object on an image that is passed in a request stream')

        method = 'ssd'
        threshold = 50
        includeLabel = True
        includeScore = True
        input_stream = os.path.join(ImagingBase.EXAMPLE_IMAGES_FOLDER, self._get_sample_image_file_name())
        outPath = None
        storage = None  # We are using default Cloud Storage

        request = requests.CreateObjectBoundsRequest(input_stream, method, threshold,
                                               includeLabel, includeScore, outPath, storage)

        print('Call CreateObjectBoundsRequest with params: method: {0}, threshold: {1}, includeLabel: {2}, includeScore: {3}'.format(method, threshold, includeLabel, includeScore))

        detectedObjectsList = self._imaging_api.create_object_bounds(request)
        print('objects detected: {0}'.format(len(detectedObjectsList.detected_objects)))
        print()

    def visualize_detect_objects_image_from_request_body(self):
        """Visualize detected object on an image that is passed in a request stream."""
        print('Visualize detected object on an image that is passed in a request stream')


        method = 'ssd'
        threshold = 50
        includeLabel = True
        includeScore = True
        color = None
        input_stream = os.path.join(ImagingBase.EXAMPLE_IMAGES_FOLDER, self._get_sample_image_file_name())
        outPath = None
        storage = None  # We are using default Cloud Storage

        request = requests.CreateVisualObjectBoundsRequest(input_stream, method, threshold,
                                               includeLabel, includeScore, color, outPath, storage)

        print('Call CreateVisualObjectBoundsRequest with params: method: {0}, threshold: {1}, includeLabel: {2}, includeScore: {3}, color: {4}'.format(method, threshold, includeLabel, includeScore, color))

        updated_image = self._imaging_api.create_visual_object_bounds(request)
        self._save_updated_sample_image_to_output(updated_image, False, "jpg")
        print()