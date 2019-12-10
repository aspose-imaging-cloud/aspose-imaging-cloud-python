#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="update_tiff_image.py">
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


class UpdateTiffImage(ImagingBase):
    """Update TIFF image example"""
    def __init__(self, imaging_api):
        ImagingBase.__init__(self, imaging_api)
        self._print_header('Update TIFF image example:')

    def _get_sample_image_file_name(self):
        return 'TiffSampleImage.tiff'

    def modify_tiff_from_storage(self):
        """Update parameters of a TIFF image. The image is saved in the cloud"""
        print('Update parameters of a TIFF image from cloud storage')

        self._upload_sample_image_to_cloud()

        compression = 'adobedeflate'
        resolution_unit = 'inch'
        bit_depth = 1
        horizontal_resolution = 150
        vertical_resolution = 150
        from_scratch = None
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.ModifyTiffRequest(self._get_sample_image_file_name(), bit_depth, compression,
                                             resolution_unit, horizontal_resolution, vertical_resolution, from_scratch,
                                             folder, storage)

        print('Call ModifyTiff with params: compression: {0}, resolution unit: {1}, bit depth: {2}, horizontal '
              'resolution: {3}, vertical resolution: {4}'.format(compression, resolution_unit, bit_depth,
                                                                 horizontal_resolution, vertical_resolution))

        updated_image = self._imaging_api.modify_tiff(request)
        self._save_updated_sample_image_to_output(updated_image, False)
        print()

    def modify_tiff_and_upload_to_storage(self):
        """Update parameters of a TIFF image, and upload updated image to Cloud Storage"""
        print('Update parameters of a TIFF image and upload to cloud storage')

        self._upload_sample_image_to_cloud()

        compression = 'adobedeflate'
        resolution_unit = 'inch'
        bit_depth = 1
        horizontal_resolution = 150
        vertical_resolution = 150
        from_scratch = None
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.ModifyTiffRequest(
            self._get_sample_image_file_name(), bit_depth, compression,
            resolution_unit, horizontal_resolution, vertical_resolution,
            from_scratch, folder, storage)

        print(
            'Call ModifyTiff with params: compression: {0}, resolution unit: {1}, bit depth: {2}, '
            'horizontal resolution: {3}, vertical resolution: {4}'
                .format(compression, resolution_unit, bit_depth, horizontal_resolution, vertical_resolution))

        updated_image = self._imaging_api.modify_tiff(request)
        self._upload_image_to_cloud(self._get_modified_sample_image_file_name(), updated_image)
        print()

    def create_modified_tiff_from_request_body(self):
        """Update parameters of a TIFF image. Image data is passed in a request stream"""
        print('Update parameters of a TIFF image from request body')

        compression = 'adobedeflate'
        resolution_unit = 'inch'
        bit_depth = 1
        horizontal_resolution = 150
        vertical_resolution = 150
        from_scratch = None
        storage = None  # We are using default Cloud Storage
        out_path = None  # Path to updated file (if this is empty, response contains streamed image)

        input_stream = os.path.join(ImagingBase.EXAMPLE_IMAGES_FOLDER, self._get_sample_image_file_name())
        request = requests.CreateModifiedTiffRequest(input_stream, bit_depth, compression, resolution_unit,
                                                     horizontal_resolution, vertical_resolution, from_scratch, out_path,
                                                     storage)

        print(
            'Call CreateModifiedTiff with params: compression: {0}, resolution unit: {1}, bit depth: {2}, '
            'horizontal resolution: {3}, vertical resolution: {4}'
                .format(compression, resolution_unit, bit_depth, horizontal_resolution, vertical_resolution))

        updated_image = self._imaging_api.create_modified_tiff(request)
        self._save_updated_sample_image_to_output(updated_image, True)
        print()

    def update_tiff_to_fax_from_storage(self):
        """Update parameters of TIFF image according to fax parameters"""
        print('Update parameters of TIFF image according to fax parameters')

        self._upload_sample_image_to_cloud()

        # Update TIFF Image parameters according to fax parameters
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.ConvertTiffToFaxRequest(self._get_sample_image_file_name(), storage, folder)

        print('Call ConvertTiffToFax')

        updated_image = self._imaging_api.convert_tiff_to_fax(request)
        self._save_updated_image_to_output('ConvertTiffToFax.tiff', updated_image)
        print()

    def append_tiff_from_storage(self):
        """Appends existing TIFF image to another existing TIFF image (i.e. merges TIFF images)"""
        print('Appends existing TIFF image to another existing TIFF image')

        append_file_name = 'Append.tiff'  # Image file name to be appended to original one

        self._upload_sample_image_to_cloud()
        self._upload_image_to_cloud(append_file_name, os.path.join(ImagingBase.EXAMPLE_IMAGES_FOLDER, append_file_name))

        # Update TIFF Image parameters according to fax parameters
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        append_request = requests.AppendTiffRequest(self._get_sample_image_file_name(), append_file_name, storage,
                                                    folder)

        print('Call AppendTiff')

        self._imaging_api.append_tiff(append_request)

        # Download updated file to local storage
        download_request = requests.DownloadFileRequest(os.path.join(ImagingBase.CLOUD_PATH,
                                                                     self._get_sample_image_file_name()), storage)
        updated_image = self._imaging_api.download_file(download_request)
        self._save_updated_image_to_output('AppendToTiff.tiff', updated_image)
        print()
