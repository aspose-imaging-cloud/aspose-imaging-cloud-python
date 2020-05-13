#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="multiframe_image.py">
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


class MultiframeImage(ImagingBase):
    """Multiframe example"""

    def __init__(self, imaging_api):
        ImagingBase.__init__(self, imaging_api)
        self._print_header('Multiframe example:')

    def _get_sample_image_file_name(self):
        return 'MultipageSampleImage.djvu'

    def get_image_frame_from_storage(self):
        """Get separate frame from existing image"""
        print('Get separate frame from existing image in cloud storage')

        self._upload_sample_image_to_cloud()

        frame_id = 1  # Index of the frame
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.GetImageFrameRequest(self._get_sample_image_file_name(), frame_id, folder=folder,
                                                storage=storage)

        print("Call GetImageFrame with params: frame Id: {0}".format(frame_id))

        image_frame = self._imaging_api.get_image_frame(request)
        self._save_updated_image_to_output('SingleFrame.djvu', image_frame)
        print()

    def get_image_frame_and_upload_to_storage(self):
        """Get separate frame from existing image and upload to cloud storage"""
        print('Get separate frame from existing image and upload to cloud storage')

        self._upload_sample_image_to_cloud()

        frame_id = 1  # Index of the frame
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.GetImageFrameRequest(self._get_sample_image_file_name(), frame_id, folder=folder,
                                                storage=storage)

        print("Call GetImageFrame with params: frame Id: {0}".format(frame_id))

        image_frame = self._imaging_api.get_image_frame(request)
        self._upload_image_to_cloud('SingleFrame.djvu', image_frame)
        print()

    def create_image_frame_from_request_body(self):
        """Get separate frame from request body"""
        print('Get separate frame from existing image from request body')

        frame_id = 1  # Index of the frame
        storage = None  # We are using default Cloud Storage
        out_path = None

        input_stream = os.path.join(ImagingBase.EXAMPLE_IMAGES_FOLDER, self._get_sample_image_file_name())
        request = requests.CreateImageFrameRequest(input_stream, frame_id, out_path=out_path,
                                                   storage=storage)

        print("Call CreateImageFrame with params: frame Id: {0}".format(frame_id))

        image_frame = self._imaging_api.create_image_frame(request)
        self._save_updated_image_to_output('SingleFrameFromRequest.djvu', image_frame)
        print()

    def get_image_frame_range_from_storage(self):
        """Get frame range from existing image"""
        print('Get frame range from existing image')

        self._upload_sample_image_to_cloud()

        start_frame_id = 1  # Index of the first frame in range
        end_frame_id = 4  # Index of the last frame in range
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.GetImageFrameRangeRequest(self._get_sample_image_file_name(), start_frame_id,
                                                     end_frame_id, folder=folder, storage=storage)

        print("Call CreateImageFrameRangeRequest with params: start frame Id: {0}, end frame i: {1}"
              .format(start_frame_id, end_frame_id))

        image_frames = self._imaging_api.get_image_frame(request)
        self._save_updated_image_to_output('FrameRange.djvu', image_frames)
        print()

    def get_image_frame_range_and_upload_to_storage(self):
        """Get frame range from existing image and upload to cloud storage"""
        print('Get frame range from existing image and upload to cloud storage')

        self._upload_sample_image_to_cloud()

        start_frame_id = 1  # Index of the first frame in range
        end_frame_id = 4  # Index of the last frame in range
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.GetImageFrameRangeRequest(self._get_sample_image_file_name(), start_frame_id,
                                                     end_frame_id, folder=folder, storage=storage)

        print("Call CreateImageFrameRangeRequest with params: start frame Id: {0}, end frame i: {1}"
              .format(start_frame_id, end_frame_id))

        image_frames = self._imaging_api.get_image_frame(request)
        self._save_updated_image_to_output('FrameRange.djvu', image_frames)
        print()

    def create_image_frame_range_from_request_body(self):
        """Get frame range from existing image from request body"""
        print('Get frame range from existing image from request body')

        start_frame_id = 1  # Index of the first frame in range
        end_frame_id = 4  # Index of the last frame in range
        out_path = None  # Path to updated file (if this is empty, response contains streamed image)
        storage = None  # We are using default Cloud Storage

        input_stream = os.path.join(ImagingBase.EXAMPLE_IMAGES_FOLDER, self._get_sample_image_file_name())
        request = requests.CreateImageFrameRangeRequest(input_stream, start_frame_id, end_frame_id, out_path=out_path,
                                                        storage=storage)

        print("Call CreateImageFrameRangeRequest with params: start frame Id: {0}, end frame i: {1}"
              .format(start_frame_id, end_frame_id))

        updated_image = self._imaging_api.create_image_frame_range(request)
        self._save_updated_image_to_output('FrameRangeFromRequest.djvu', updated_image)
        print()

    def get_image_frame_properties_from_storage(self):
        """Get separate frame properties of a image"""
        print('Gets separate frame properties of existing image from cloud storage')

        self._upload_sample_image_to_cloud()

        frame_id = 1  # Number of a frame
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.GetImageFramePropertiesRequest(self._get_sample_image_file_name(), frame_id, folder, storage)

        print("Call GetImageFrameProperties with params: frame Id: {0}".format(frame_id))

        response = self._imaging_api.get_image_frame_properties(request)
        self._output_properties_to_file('TiffFrameProperties.txt', response)
        print()

    def extract_image_frame_properties_from_request_body(self):
        """Get separate frame properties of a image. Image data is passed in a request stream."""
        print('Get separate frame properties of existing image from request body')

        frame_id = 1  # Number of a frame

        input_stream = os.path.join(ImagingBase.EXAMPLE_IMAGES_FOLDER, self._get_sample_image_file_name())
        request = requests.ExtractImageFramePropertiesRequest(input_stream, frame_id)

        print("Call ExtractImageFrameProperties with params: frame Id: {0}".format(frame_id))

        response = self._imaging_api.extract_image_frame_properties(request)
        self._output_properties_to_file('TiffFramePropertiesFromRequest.txt', response)
        print()
