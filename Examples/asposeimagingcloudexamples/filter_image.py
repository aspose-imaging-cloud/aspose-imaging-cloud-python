#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="imaging_examples.py">
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

from asposeimagingcloud.models.big_rectangular_filter_properties import BigRectangularFilterProperties
from asposeimagingcloud.models.requests.filter_effect_image_request import FilterEffectImageRequest

from asposeimagingcloudexamples.imaging_base import ImagingBase


class FilterImage(ImagingBase):
    """Applying a filtering effect to an image example"""

    def __init__(self, imaging_api):
        ImagingBase.__init__(self, imaging_api)
        self._print_header('Filter image example:')

    def _get_sample_image_file_name(self):
        return 'FilterEffectSampleImage.psd'

    def filter_image_from_storage(self):
        """Applies filtering effect to an image from cloud storage"""
        print('Apply filtering effect to an image from cloud storage')

        self._upload_sample_image_to_cloud()

        filter_type = 'BigRectangular'
        filter_properties = BigRectangularFilterProperties()
        format = 'bmp'
        folder = ImagingBase.CLOUD_PATH
        storage = None

        request = FilterEffectImageRequest(self._get_sample_image_file_name(), filter_type, filter_properties,
                                           format, folder, storage)

        print('Call FilterEffectImage with params: filter type: {0}, format: {1}'.format(filter_type, format))

        updated_image = self._imaging_api.filter_effect_image(request)
        self._save_updated_sample_image_to_output(updated_image, False, format)
        print()

    def filter_image_and_upload_to_storage(self):
        """Applies filtering effect to an image and upload to Cloud Storage"""
        print('Apply filtering effect to an image and upload to cloud storage')

        self._upload_sample_image_to_cloud()

        filter_type = 'BigRectangular'
        filter_properties = BigRectangularFilterProperties()
        format = 'bmp'
        folder = ImagingBase.CLOUD_PATH
        storage = None

        request = FilterEffectImageRequest(self._get_sample_image_file_name(), filter_type, filter_properties,
                                           format, folder, storage)

        print('Call FilterEffectImage with params: filter type: {0}, format: {1}'.format(filter_type, format))

        updated_image = self._imaging_api.filter_effect_image(request)
        self._save_updated_image_to_output(self._get_modified_sample_image_file_name(False, format), updated_image)
        print()
