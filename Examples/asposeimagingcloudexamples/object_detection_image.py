#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="object_detection_image.py">
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
        includeClass = True
        includeScore = True

        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.ObjectBoundsRequest(self._get_sample_image_file_name(), method, threshold,
                                               includeClass, includeScore, folder, storage)

        print('Call ObjectBoundsRequest with params: method: {0}, threshold: {1}, includeClass: {2}, includeScore: {3}'.format(method, threshold, includeClass, includeScore))

        detectedObjectsList = self._imaging_api.objectBounds(request)
        print('objects detected: {0}'.format(detectedObjectsList.detectedObjects.len()))
        #self._save_updated_sample_image_to_output(updated_image, False, "bmp")
        print()

    def visualize_detected_objects_image_from_storage(self):
        """Get visualized detected objects and upload it to the cloud storage"""
        print('Get visualized detected objects and upload it to the cloud storage')

        self._upload_sample_image_to_cloud()

        method = 'ssd'
        threshold = 50
        includeClass = True
        includeScore = True

        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.VisualObjectBoundsRequest(self._get_sample_image_file_name(), method, threshold,
                                               includeClass, includeScore, folder, storage)

        print('Call VisualObjectBoundsRequest with params: method: {0}, threshold: {1}, includeClass: {2}, includeScore: {3}'.format(method, threshold, includeClass, includeScore))

        updated_image = self._imaging_api.objectBounds(request)
        #print('objects detected: {0}'.format(detectedObjectsList.detectedObjects.len()))
        self._save_updated_sample_image_to_output(updated_image, False, "jpg")
        print()


    def detect_objects_image_from_request_body(self):
        """detected object on an image that is passed in a request stream"""
        print('detected object on an image that is passed in a request stream')


        method = 'ssd'
        threshold = 50
        includeClass = True
        includeScore = True
        input_stream = os.path.join(ImagingBase.EXAMPLE_IMAGES_FOLDER, self._get_sample_image_file_name())
        outPath = None
        storage = None  # We are using default Cloud Storage

        request = requests.CreateObjectBoundsRequest(input_stream, method, threshold,
                                               includeClass, includeScore, outPath, storage)

        print('Call CreateObjectBoundsRequest with params: method: {0}, threshold: {1}, includeClass: {2}, includeScore: {3}'.format(method, threshold, includeClass, includeScore))

        detectedObjectsList = self._imaging_api.createObjectBounds(request)
        print('objects detected: {0}'.format(detectedObjectsList.detectedObjects.len()))
        #self._save_updated_sample_image_to_output(updated_image, False, "bmp")
        print()

    def visualize_detect_objects_image_from_request_body(self):
        """Visualize detected object on an image that is passed in a request stream."""
        print('Visualize detected object on an image that is passed in a request stream')


        method = 'ssd'
        threshold = 50
        includeClass = True
        includeScore = True
        input_stream = os.path.join(ImagingBase.EXAMPLE_IMAGES_FOLDER, self._get_sample_image_file_name())
        outPath = None
        storage = None  # We are using default Cloud Storage

        request = requests.CreateVisualObjectBoundsRequest(input_stream, method, threshold,
                                               includeClass, includeScore, outPath, storage)

        print('Call CreateVisualObjectBoundsRequest with params: method: {0}, threshold: {1}, includeClass: {2}, includeScore: {3}'.format(method, threshold, includeClass, includeScore))

        updated_image = self._imaging_api.CreateVisualObjectBounds(request)
        self._save_updated_sample_image_to_output(updated_image, False, "jpg")
        print()















    def detect_objects_image_from_storage(self):
        """Detect objects on an image from a cloud storage"""
        print('Detect objects on an image from a cloud storage')

        self._upload_sample_image_to_cloud()

        method = 'ssd'
        threshold = 50
        includeClass = True
        includeScore = True

        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.ObjectBoundsRequest(self._get_sample_image_file_name(), method, threshold,
                                               includeClass, includeScore, folder, storage)

        print('Call ObjectBoundsRequest with params: method: {0}, threshold: {1}, includeClass: {2}, includeScore: {3}'.format(method, threshold, includeClass, includeScore))

        detectedObjectsList = self._imaging_api.objectBounds(request)
        print('objects detected: {0}'.format(detectedObjectsList.detectedObjects.len()))
        #self._save_updated_sample_image_to_output(updated_image, False, "bmp")
        print()





    def deskew_image_and_upload_to_storage(self):
        """Deskew an existing image, and upload updated image to Cloud Storage"""
        print('Deskews the image and upload to cloud storage')

        self._upload_sample_image_to_cloud()

        resize_proportionally = True
        bk_color = 'white'
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.DeskewImageRequest(self._get_sample_image_file_name(), resize_proportionally, bk_color, folder,
                                            storage)

        print('Call DeskewImage with params: resize_proportionally: {0}, bk_color: {1}'.format(resize_proportionally, bk_color))

        updated_image = self._imaging_api.deskew_image(request)
        self._upload_image_to_cloud(self._get_modified_sample_image_file_name(False, "bmp"), updated_image)
        print()

    def create_deskewed_image_from_request_body(self):
        """Deskew an image. Image data is passed in a request stream"""
        print('Deskews the image from request body')

        resize_proportionally = True
        bk_color = 'white'
        storage = None  # We are using default Cloud Storage
        out_path = None  # Path to updated file (if this is empty, response contains streamed image)

        input_stream = os.path.join(ImagingBase.EXAMPLE_IMAGES_FOLDER, self._get_sample_image_file_name())
        request = requests.CreateDeskewedImageRequest(input_stream, resize_proportionally, bk_color, out_path, storage)

        print('Call CreateDeskewedImage with params: resize_proportionally: {0}, bk_color: {1}'.format(resize_proportionally, bk_color))

        updated_image = self._imaging_api.create_deskewed_image(request)
        self._save_updated_sample_image_to_output(updated_image, True, "bmp")
        print()
