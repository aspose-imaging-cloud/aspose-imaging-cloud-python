#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_filter_effect_api.py">
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

import asposeimagingcloud.models as models
import asposeimagingcloud.models.requests as requests
from test.api import ImagingApiTester


class TestFilterEffectApi(ImagingApiTester):
    """ Class for testing FilterEffectAPI """

    def test_filter_effect(self):
        """ Test filter_effect_image """

        additional_export_formats = set()
        if not self.EXTENDED_TEST:
            format_extension_test_cases = ['.psd']
        else:
            format_extension_test_cases = [
                '.dicom',
                '.djvu',
                '.gif',
                '.psd',
                '.tiff',
                '.webp']

        for format_extension in format_extension_test_cases:
            with self.subTest('format_extension: ' + str(format_extension)):

                folder = self.temp_folder
                storage = self. test_storage

                formats_to_export = set(
                    self.basic_export_formats).union(additional_export_formats)

                def request_invoker():
                    return self.imaging_api.filter_effect_image(requests.FilterEffectImageRequest(name,
                                                                                                  filter.filter_type,
                                                                                                  filter.filter_properties, format, folder, storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    pass

                for input_file in self.input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name

                    for filter in self.__filters:
                        for format in formats_to_export:
                            out_name = '{0}_crop.{1}'.format(name, format)

                            self.get_request_tester(
                                'FilterEffectTest',
                                'Input image: {0}; Output format: {1}; Filter type:'
                                ' {2}'.format(
                                    name,
                                    format,
                                    filter.filter_type
                                ),
                                name,
                                request_invoker,
                                properties_tester,
                                folder,
                                storage
                            )

    class __Filter:
        """ Wrapper for filter type and filter properties """

        def __init__(self, filter_type, filter_properties):
            """ Creates Filter instance """
            self.filter_type = filter_type
            self.filter_properties = filter_properties

    # Filters to test
    __filters = [
        __Filter('BigRectangular', models.BigRectangularFilterProperties()),
        __Filter('SmallRectangular', models.SmallRectangularFilterProperties),
        __Filter('Median',  models.MedianFilterProperties(3)),
        __Filter('GaussWiener', models.GaussWienerFilterProperties(2, 2)),
        __Filter('MotionWiener', models.MotionWienerFilterProperties(2, 2, 12)),
        __Filter('GaussianBlur', models.GaussianBlurFilterProperties(2, 2)),
        __Filter('Sharpen', models.SharpenFilterProperties(2, 0.5)),
        __Filter('BilateralSmoothing', models.BilateralSmoothingFilterProperties(2, 2, 2, 2, 2)),
    ]
