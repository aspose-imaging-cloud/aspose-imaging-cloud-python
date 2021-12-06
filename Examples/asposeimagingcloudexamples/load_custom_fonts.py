#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="export_image.py">
#    Copyright (c) 2019-2021 Aspose Pty Ltd. All rights reserved.
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


class LoadCustomFonts(ImagingBase):
    """Load custom fonts example"""

    def __init__(self, imaging_api):
        ImagingBase.__init__(self, imaging_api)
        self._print_header('Load custom fonts example:')

    def _get_sample_image_file_name(self):
        return 'ImageWithCustomFonts.emz'

    def using_custom_fonts_for_vector_image_conversion(self):
        """Using custom fonts for vector image conversion example"""
        print('Using custom fonts for vector image conversion')

        self._upload_sample_image_to_cloud()
        
        # custom fonts should be loaded to storage to 'Fonts' folder
        # 'Fonts' folder should be placed to the root of the cloud storage
        self._upload_fonts_to_cloud();

        # Please refer to
        # https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-Export(SaveAs)
        # for possible output formats
        format = 'png'  # Resulting image format
        folder = ImagingBase.CLOUD_PATH  # Input file is saved at the Examples folder in the storage
        storage = None  # We are using default Cloud Storage

        request = requests.ConvertImageRequest(self._get_sample_image_file_name(), format, folder, storage)

        print('Call Convert with params: format: {0}'.format(format))

        updated_image = self._imaging_api.convert_image(request)
        self._save_updated_sample_image_to_output(updated_image, False, format)

        print()
        
    def _upload_fonts_to_cloud(self):
        """Uploads the font files to cloud"""
        fontsFolder = os.path.join(ImagingBase.EXAMPLE_IMAGES_FOLDER, "Fonts");  
        for fontFile in glob.glob(glob(fontsFolder + "/*.ttf")):           
            self._upload_image_to_cloud(os.path.join("Fonts", fontFile), os.path.join(fontsFolder, fontFile))    

    def _upload_file_to_cloud(self, file_name, file):
        """Uploads the file to cloud"""
        upload_file_request = requests.UploadFileRequest(file_name, file)
        result = self._imaging_api.upload_file(upload_file_request)
        if result.errors:
            print('Uploading errors count: ' + str(len(result.errors)))
        else:
            print('File ' + file_name + ' is uploaded to cloud storage')
