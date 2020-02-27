#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="tiff_frames.py">
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


class TiffFrames(ImagingBase):
    """TIFF frames example"""
    def __init__(self, imaging_api):
        ImagingBase.__init__(self, imaging_api)
        self._print_header('TIFF frames example:')

    def _get_sample_image_file_name(self):
        return 'TiffFrameSampleImage.tiff'

    def get_image_frame_from_storage(self):
        """Get separate frame from existing TIFF image"""
        print('Get separate frame from existing TIFF image in cloud storage')

        self._upload_sample_image_to_cloud()

        frame_id = 1  # Number of a frame
        new_width = 300
        new_height = 450
        x = 10
        y = 10
        rect_width = 200
        rect_height = 300
        rotate_flip_method = 'Rotate90FlipX'
        save_other_frames = False  # Result will include just the specified frame
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.GetImageFrameRequest(self._get_sample_image_file_name(), frame_id, new_width, new_height,
                                                x, y, rect_width, rect_height, rotate_flip_method, save_other_frames,
                                                folder, storage)

        print("Call GetImageFrame with params: frame Id: {0}, new width: {1}, new height: {2}, x: {3}, y: {4}, "
              "rect width: {5}, rect height: {6}, rotate/flip method: {7}, save other frames: {8}"
              .format(frame_id, new_width, new_height, x, y, rect_width, rect_height, rotate_flip_method,
                      save_other_frames))

        updated_image = self._imaging_api.get_image_frame(request)
        self._save_updated_image_to_output('SingleFrame.tiff', updated_image)
        print()

    def get_image_frame_and_upload_to_storage(self):
        """Get separate frame from existing TIFF image, and upload the frame to Cloud Storage"""
        print('Get separate frame from existing TIFF image and upload to cloud storage')

        self._upload_sample_image_to_cloud()

        frame_id = 1  # Number of a frame
        new_width = 300
        new_height = 450
        x = 10
        y = 10
        rect_width = 200
        rect_height = 300
        rotate_flip_method = 'Rotate90FlipX'
        save_other_frames = False  # Result will include just the specified frame
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.GetImageFrameRequest(self._get_sample_image_file_name(), frame_id, new_width, new_height,
                                                x, y, rect_width, rect_height, rotate_flip_method, save_other_frames,
                                                folder, storage)

        print("Call GetImageFrame with params: frame Id: {0}, new width: {1}, new height: {2}, x: {3}, y: {4}, "
              "rect width: {5}, rect height: {6}, rotate/flip method: {7}, save other frames: {8}"
              .format(frame_id, new_width, new_height, x, y, rect_width, rect_height, rotate_flip_method,
                      save_other_frames))

        updated_image = self._imaging_api.get_image_frame(request)
        self._upload_image_to_cloud('SingleFrame.tiff', updated_image)
        print()

    def resize_image_frame_from_storage(self):
        """Resize a TIFF frame"""
        print('Resize frame from existing TIFF image from cloud storage')

        self._upload_sample_image_to_cloud()

        frame_id = 1  # Number of a frame
        new_width = 300
        new_heigth = 300
        save_other_frames = False  # Result will include just the specified frame
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.GetImageFrameRequest(self._get_sample_image_file_name(), frame_id, new_width, new_heigth,
                                                save_other_frames=save_other_frames, folder=folder, storage=storage)

        print("Call GetImageFrame with params: frame Id: {0}, new width: {1}, new height: {2}, save other frames: {2}"
              .format(frame_id, new_width, save_other_frames))

        updated_image = self._imaging_api.get_image_frame(request)
        self._save_updated_image_to_output('ResizeFrame.tiff', updated_image)
        print()

    def crop_image_frame_from_storage(self):
        """Crop a TIFF frame"""
        print('Crop frame from existing TIFF image from cloud storage')

        self.get_image_frame_and_upload_to_storage()

        frame_id = 0  # Number of a frame
        x = 10
        y = 10
        rect_width = 200
        rect_height = 300
        save_other_frames = False  # Result will include just the specified frame
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.GetImageFrameRequest(self._get_sample_image_file_name(), frame_id, x=x, y=y,
                                                rect_width=rect_width, rect_height=rect_height,
                                                save_other_frames=save_other_frames, folder=folder, storage=storage)

        print("Call GetImageFrame with params: frame Id: {0}, x: {1}, y: {2}, rect width: {3}, rect height: {4}, "
              "save other frames: {5}".format(frame_id, x, y, rect_width, rect_height, save_other_frames))

        updated_image = self._imaging_api.get_image_frame(request)
        self._save_updated_image_to_output('CropFrame.tiff', updated_image)
        print()

    def rotate_flip_image_frame_from_storage(self):
        """Rotate/Flip a TIFF frame"""
        print('Rotate/flip frame from existing TIFF image from cloud storage')

        self.get_image_frame_and_upload_to_storage()

        frame_id = 0  # Number of a frame
        rotate_flip_method = 'Rotate90FlipX'
        save_other_frames = False  # Result will include just the specified frame
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.GetImageFrameRequest(
            self._get_sample_image_file_name(), frame_id, rotate_flip_method=rotate_flip_method,
            save_other_frames=save_other_frames, folder=folder,
            storage=storage)

        print("Call GetImageFrame with params: frame Id: {0}, rrotate/flip method: {1}, save other frames: {2}"
              .format(frame_id, rotate_flip_method, save_other_frames))

        updated_image = self._imaging_api.get_image_frame(request)
        self._save_updated_image_to_output('RotateFlipFrame.tiff', updated_image)
        print()

    def get_all_image_frames_from_storage(self):
        """Gets all image frames from storage"""
        print('Gets all image frames from existing TIFF image from cloud storage')

        self._upload_sample_image_to_cloud()

        frame_id = 1  # Number of a frame
        new_width = 300
        new_height = 450
        x = 10
        y = 10
        rect_width = 200
        rect_height = 300
        rotate_flip_method = 'Rotate90FlipX'
        save_other_frames = True  # Result will include just the specified frame
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.GetImageFrameRequest(self._get_sample_image_file_name(), frame_id, new_width, new_height,
                                                x, y, rect_width, rect_height, rotate_flip_method, save_other_frames,
                                                folder, storage)

        print("Call GetImageFrame with params: frame Id: {0}, new width: {1}, new height: {2}, x: {3}, y: {4}, "
              "rect width: {5}, rect height: {6}, rotate/flip method: {7}, save other frames: {8}"
              .format(frame_id, new_width, new_height, x, y, rect_width, rect_height, rotate_flip_method,
                      save_other_frames))

        updated_image = self._imaging_api.get_image_frame(request)
        self._save_updated_image_to_output('OtherFrames.tiff', updated_image)
        print()

    def create_image_frame_from_request_body(self):
        """Get separate frame from existing TIFF image. Image data is passed in a request stream."""
        print('Get separate frame from existing TIFF image in cloud storage')

        self._upload_sample_image_to_cloud()

        frame_id = 1  # Number of a frame
        new_width = 300
        new_height = 450
        x = 10
        y = 10
        rect_width = 200
        rect_height = 300
        rotate_flip_method = 'Rotate90FlipX'
        save_other_frames = False  # Result will include just the specified frame
        out_path = None  # Path to updated file (if this is empty, response contains streamed image)
        storage = None  # We are using default Cloud Storage

        input_stream = os.path.join(ImagingBase.EXAMPLE_IMAGES_FOLDER, self._get_sample_image_file_name())
        request = requests.CreateImageFrameRequest(input_stream, frame_id, new_width, new_height, x, y, rect_width,
                                                   rect_height, rotate_flip_method, save_other_frames, out_path,
                                                   storage)

        print("Call CreateImageFrame with params: frame Id: {0}, new width: {1}, new height: {2}, x: {3}, y: {4}, "
              "rect width: {5}, rect height: {6}, rotate/flip method: {7}, save other frames: {8}"
              .format(frame_id, new_width, new_height, x, y, rect_width, rect_height, rotate_flip_method,
                      save_other_frames))

        updated_image = self._imaging_api.create_image_frame(request)
        self._save_updated_image_to_output('SingleFrameFromRequest.tiff', updated_image)
        print()

    def get_image_frame_properties_from_storage(self):
        """Get separate frame properties of a TIFF image"""
        print('Gets separate frame properties of existing TIFF image from cloud storage')

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
        """Get separate frame properties of a TIFF image. Image data is passed in a request stream."""
        print('Get separate frame properties of existing TIFF image from request body')

        frame_id = 1  # Number of a frame

        input_stream = os.path.join(ImagingBase.EXAMPLE_IMAGES_FOLDER, self._get_sample_image_file_name())
        request = requests.ExtractImageFramePropertiesRequest(input_stream, frame_id)

        print("Call ExtractImageFrameProperties with params: frame Id: {0}".format(frame_id))

        response = self._imaging_api.extract_image_frame_properties(request)
        self._output_properties_to_file('TiffFramePropertiesFromRequest.txt', response)
        print()
