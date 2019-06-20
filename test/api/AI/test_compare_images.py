#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_compare_images.py">
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

from asposeimagingcloud import PostSearchContextCompareImagesRequest, \
    DownloadFileRequest
from test.api.AI.ai_api_tester import AiApiTester


class TestCompareImages(AiApiTester):
    COMPARABLE_IMAGE = 'ComparableImage.jpg'
    COMPARING_IMAGE_SIMILAR_LESS_15 = 'ComparingImageSimilar15.jpg'
    COMPARING_IMAGE_SIMILAR_MORE_75 = 'ComparingImageSimilar75.jpg'

    def test_compare_two_images_in_search_context(self):
        def test():
            image1 = self._get_storage_path(self.COMPARABLE_IMAGE)
            self._add_image_features_to_search_context(image1)

            image2 = self._get_storage_path(
                self.COMPARING_IMAGE_SIMILAR_MORE_75)
            self._add_image_features_to_search_context(image2)

            response = self.imaging_api.post_search_context_compare_images(
                PostSearchContextCompareImagesRequest(
                    self.search_context_id,
                    image_id1=image1,
                    image_id2=image2,
                    storage=self.test_storage))

            self.assertEqual(1, len(response.results))
            self.assertTrue(response.results[0].similarity >= 70)

        self._run_test_with_logging(
            'CompareTwoImagesInSearchContextTest', test)

    def test_compare_loaded_image_to_image_in_search_context(self):
        def test():
            image = self._get_storage_path(self.COMPARABLE_IMAGE)
            self._add_image_features_to_search_context(image)

            storage_path = self.original_data_folder + '/' + \
                           self.COMPARING_IMAGE_SIMILAR_LESS_15

            image_stream = self.imaging_api.download_file(
                DownloadFileRequest(storage_path, self.test_storage))
            self.assertIsNotNone(image_stream)

            response = self.imaging_api.post_search_context_compare_images(
                PostSearchContextCompareImagesRequest(self.search_context_id,
                                                      image_id1=image,
                                                      image_data=image_stream,
                                                      storage=self.test_storage))

            self.assertEqual(1, len(response.results))
            self.assertTrue(response.results[0].similarity <= 15)

        self._run_test_with_logging(
            'CompareLoadedImageToImageInSearchContextTest', test)
