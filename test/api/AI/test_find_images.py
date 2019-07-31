#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_find_images.py">
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

from asposeimagingcloud import FindSimilarImagesRequest, \
    DownloadFileRequest, CreateImageTagRequest, \
    FindImagesByTagsRequest
from test.api.AI.ai_api_tester import AiApiTester


class TestFindImages(AiApiTester):
    IMAGE_TO_FIND = '4.jpg'
    IMAGE_TO_FIND_BY_TAG = 'ComparingImageSimilar75.jpg'

    def test_find_similar(self):
        def test():
            self._add_image_features_to_search_context(
                self.original_data_folder + '/FindSimilar', is_folder=True)
            find_image_id = self.original_data_folder + '/FindSimilar/' + self.IMAGE_TO_FIND
            response = self.imaging_api.find_similar_images(
                FindSimilarImagesRequest(self.search_context_id,
                                                   similarity_threshold=3,
                                                   max_count=3,
                                                   image_id=find_image_id,
                                                   storage=self.test_storage))

            self.assertTrue(len(response.results) >= 1)

        self._run_test_with_logging('FindSimilarImagesTest', test)

    def test_find_similar_images_by_tag(self):
        def test():
            self._add_image_features_to_search_context(
                self.original_data_folder + '/FindSimilar', is_folder=True)

            tag = 'TestTag'
            storage_path = self.original_data_folder + '/' + self.IMAGE_TO_FIND_BY_TAG

            tag_image_stream = self.imaging_api.download_file(
                DownloadFileRequest(storage_path, self.test_storage))
            self.assertIsNotNone(tag_image_stream)
            self.imaging_api.create_image_tag(
                CreateImageTagRequest(tag_image_stream,
                                               self.search_context_id, tag,
                                               storage=self.test_storage))

            response = self.imaging_api.find_images_by_tags(
                FindImagesByTagsRequest([tag],
                                                   self.search_context_id,
                                                   similarity_threshold=60,
                                                   max_count=5,
                                                   storage=self.test_storage))

            self.assertEqual(1, len(response.result))
            self.assertTrue('2.jpg' in response.results[0].image_id)
