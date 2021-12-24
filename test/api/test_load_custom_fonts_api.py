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

import asposeimagingcloud.models.requests as requests
from test.api import ImagingApiTester


class TestLoadCustomFontsApi(ImagingApiTester):
    """ Class for testing custom fonts loading """

    self.original_data_folder = 'ImagingIntegrationTestData'
  
    def test_using_custom_fonts_for_vector_image(self):
        """
         Using custom fonts
        """       

        name = 'image.emz'
        format = 'png'
        folder = self.temp_folder
        storage = self.test_storage
      
        def request_invoker():
            return self.imaging_api.convert_image(
                requests.ConvertImageRequest(
                    name, format, folder, storage))  

        self.get_request_tester(
            'UsingCustomFontsTest',
            'Input image: {0}; Output format: {1}'.format(
                name,
                format),
            name,
            request_invoker,
            lambda x,
            y,
            z: None,
            folder,
            storage)
   