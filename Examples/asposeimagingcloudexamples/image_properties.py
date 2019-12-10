#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="image_properties.py">
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


class ImageProperties(ImagingBase):
    """Image properties example"""

    def __init__(self, imaging_api):
        ImagingBase.__init__(self, imaging_api)
        self._print_header('Image properties example:')

    def _get_sample_image_file_name(self):
        return 'PropertiesOfSampleImage.tiff'

    def get_image_properties_from_storage(self):
        """Get properties of an image, which is store in the cloud"""
        print('Get properties of an image in cloud storage')

        self._upload_sample_image_to_cloud()

        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.GetImagePropertiesRequest(self._get_sample_image_file_name(), folder, storage)

        print('Call GetImageProperties')

        response = self._imaging_api.get_image_properties(request)

        self._output_properties_to_file('ImageProperties.txt', response)

        print()

    def extract_image_properties_from_request_body(self):
        """Get properties of an image. Image data is passed in a request stream"""
        print('Get properties of an image from request body')

        input_stream = os.path.join(ImagingBase.EXAMPLE_IMAGES_FOLDER, self._get_sample_image_file_name())
        request = requests.ExtractImagePropertiesRequest(input_stream)

        print('Call ExtractImageProperties')

        response = self._imaging_api.extract_image_properties(request)
        self._output_properties_to_file('ImagePropertiesFromRequest.txt', response)

        print()
