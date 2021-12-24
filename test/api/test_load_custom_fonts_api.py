#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_load_custom_fonts_api.py">
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

from itertools import product

import os
import asposeimagingcloud.models.requests as requests
from test.api import ImagingApiTester


class TestLoadCustomFontsApi(ImagingApiTester):
    """ Class for testing custom fonts loading """
 
    def test_using_custom_fonts_for_vector_image(self):
        """
         Using custom fonts
        """       

        name = 'image.emz'
        format = 'png'
        folder = self.temp_folder
        storage = self.test_storage
        
        self.copy_input_file_to_test_folder(name, folder, storage)
      
        def request_invoker():
            return self.imaging_api.convert_image(
                requests.ConvertImageRequest(
                    name, format, folder, storage))  
        
        def properties_tester(
                    original_properties,
                    result_properties,
                    result_stream):
            self.assertTrue(abs(result_stream.length - 11454) < 100)                   

        self.get_request_tester(
            'UsingCustomFontsTest',
            'Input image: {0}; Output format: {1}'.format(
                name,
                format),
            name,
            request_invoker,
            properties_tester,
            folder,
            storage)
            
    def copy_input_file_to_test_folder(self, input_file_name, folder, storage):       
        if not self.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    os.path.join(
                        folder,
                        input_file_name),
                    storage)).exists:
            self.imaging_api.copy_file(
                requests.CopyFileRequest(
                    os.path.join(
                        self.original_data_folder + '/UseCases',
                        input_file_name),
                    os.path.join(
                        folder,
                        input_file_name),
                    storage,
                    storage))
   
   
        