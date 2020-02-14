#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="imaging_base.py">
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
import shutil

import asposeimagingcloud.models.requests as requests


class ImagingBase:
    """Base class for examples"""

    # The example images folder path
    EXAMPLE_IMAGES_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'Images')

    # The output folder path
    OUTPUT_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'Output')

    # The cloud path
    CLOUD_PATH = 'Examples'

    def __init__(self, imaging_api):
        self._imaging_api = imaging_api

    def _get_sample_image_file_name(self):
        raise NotImplementedError('get_sample_image_file_name must be implemented')

    def _get_modified_sample_image_file_name(self, from_request=False, new_format_extension=None):
        """Gets the name of the modified sample image file"""
        if new_format_extension:
            filename_part, extension = os.path.splitext(self._get_sample_image_file_name())
            filename = filename_part + '.' + new_format_extension
        else:
            filename = self._get_sample_image_file_name()

        return 'ModifiedFromRequest' + filename if from_request \
            else 'Modified' + filename

    def _upload_sample_image_to_cloud(self):
        """Uploads the example image to cloud"""
        local_input_image = os.path.join(ImagingBase.EXAMPLE_IMAGES_FOLDER, self._get_sample_image_file_name())
        self._upload_image_to_cloud(self._get_sample_image_file_name(), local_input_image)

    def _upload_image_to_cloud(self, image_name, image):
        """Uploads the image to cloud"""
        upload_file_request = requests.UploadFileRequest(os.path.join(ImagingBase.CLOUD_PATH, image_name), image)
        result = self._imaging_api.upload_file(upload_file_request)
        if result.errors:
            print('Uploading errors count: ' + str(len(result.errors)))
        else:
            print('Image ' + image_name + ' is uploaded to cloud storage')

    def _save_updated_sample_image_to_output(self, updated_image, from_request, new_format_extension=None):
        """Saves the updated image to local output folder"""
        new_file_name = self._get_modified_sample_image_file_name(from_request, new_format_extension)

        self._save_updated_image_to_output(new_file_name, updated_image)

    def _save_updated_image_to_output(self, image_name, updated_image):
        """Saves the updated image to output folder"""
        path = os.path.abspath(os.path.join(ImagingBase.OUTPUT_FOLDER, image_name))
        shutil.copy(updated_image, path)
        print('Image ' + image_name + ' is saved to ' + os.path.dirname(path))

    def _output_properties_to_file(self, file_name, imaging_response):
        """Outputs the properties to file"""
        path = os.path.abspath(os.path.join(ImagingBase.OUTPUT_FOLDER, file_name))
        with open(path, 'w') as output_file:
            output_file.write('Width: ' + str(imaging_response.width))
            output_file.write('Height: ' + str(imaging_response.height))
            output_file.write('Horizontal resolution: ' + str(imaging_response.horizontal_resolution))
            output_file.write('Vertical resolution: ' + str(imaging_response.vertical_resolution))
            output_file.write('Bits per pixel: ' + str(imaging_response.bits_per_pixel))

            if imaging_response.tiff_properties:
                output_file.write('Tiff properties:')
                output_file.write('Frames count: ' + str(len(imaging_response.tiff_properties.frames)))
                output_file.write('Camera owner name: ' +
                                  imaging_response.tiff_properties.exif_data.camera_owner_name if imaging_response.tiff_properties.exif_data else '')
                output_file.write('Byte order: ' + str(imaging_response.tiff_properties.byte_order))

        print('File ' + file_name + ' is saved to ' + os.path.dirname(path))

    def _print_header(self, header):
        print(header)
        print()
