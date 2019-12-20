#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_search_context.py">
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
import six

from asposeimagingcloud import GetImageSearchStatusRequest, \
    DownloadFileRequest, AddSearchImageRequest, ObjectExistsRequest, \
    GetSearchImageRequest, CreateImageFeaturesRequest, \
    GetImageFeaturesRequest, UpdateSearchImageRequest, \
    ExtractImageFeaturesRequest, UpdateImageFeaturesRequest, \
    DeleteSearchImageRequest, CreateWebSiteImageFeaturesRequest
from asposeimagingcloud.rest import ApiException
from test.api.AI.ai_api_tester import AiApiTester

if six.PY2:
    import unittest2 as unittest
    import urllib as urllib
else:
    import unittest
    import urllib.parse as urllib


class TestSearchContext(AiApiTester):
    SMALL_TEST_IMAGE = 'ComparableImage.jpg'
    TEST_IMAGE = 'ComparingImageSimilar15.jpg'

    def test_create_search_context(self):
        self._run_test_with_logging('CreateSearchContextTest',
                                    lambda: self.assertIsNotNone(
                                        self.search_context_id))

    def test_delete_image_search(self):
        def test():
            self._delete_image_search(self.search_context_id)

            self.assertRaises(ApiException,
                              self.imaging_api.get_image_search_status,
                              GetImageSearchStatusRequest(
                                  self.search_context_id,
                                  storage=self.test_storage))
			
			self.search_context_id = None

        self._run_test_with_logging('DeleteImageSearchTest', test)

    def test_add_image(self):
        self._run_test_with_logging('AddImageTest',
                                    lambda: self.__add_image(self.TEST_IMAGE))

    def test_delete_image(self):
        def test():
            image = self.TEST_IMAGE
            self.__add_image(image)

            dest_server_path = self.temp_folder + '/' + image

            self.imaging_api.delete_image_search(
                DeleteSearchImageRequest(self.search_context_id,
                                         dest_server_path,
                                         storage=self.test_storage))

            self.assertRaises(ApiException,
                              self.imaging_api.get_search_image,
                              GetSearchImageRequest(
                                  self.search_context_id, dest_server_path,
                                  storage=self.test_storage))

        self._run_test_with_logging('DeleteImageTest', test)

    def test_get_image(self):
        def test():
            image = self.TEST_IMAGE
            self.__add_image(image)

            response_file = self.__get_image(image)

            self.assertGreater(os.path.getsize(response_file), 50000)

        self._run_test_with_logging('GetImageTest', test)

    def test_update_image(self):
        def test():
            image = self.TEST_IMAGE
            self.__add_image(image)
            response_file = self.__get_image(image)
            self.assertGreater(os.path.getsize(response_file), 50000)

            image = self.SMALL_TEST_IMAGE
            dest_server_path = self.temp_folder + '/' + image

            storage_path = self.original_data_folder + '/' + image
            image_stream = self.imaging_api.download_file(
                DownloadFileRequest(storage_path, self.test_storage))
            self.assertIsNotNone(image_stream)

            self.imaging_api.update_search_image(
                UpdateSearchImageRequest(self.search_context_id,
                                             dest_server_path, image_stream,
                                             storage=self.test_storage))

            response_file = self.__get_image(image)
            self.assertLess(os.path.getsize(response_file), 40000)

        self._run_test_with_logging('UpdateImageTest', test)

    def test_extract_image_features(self):
        def test():
            image = self.TEST_IMAGE
            self.__add_image(image)
            dest_server_path = self.temp_folder + '/' + image

            response = \
                self.imaging_api.extract_image_features(
                    ExtractImageFeaturesRequest(
                        self.search_context_id, dest_server_path,
                        storage=self.test_storage))

            self.assertTrue(image in response.image_id)
            self.assertGreater(len(response.features), 0)

        self._run_test_with_logging('ExtractImageFeaturesTest', test)

    def test_extract_and_add_image_features(self):
        self._run_test_with_logging('ExtractAndAddImageFeaturesTest',
                                    lambda: self.__add_image_features(
                                        self.TEST_IMAGE))

    @unittest.skip('IMAGINGNET-107')
    def test_extract_and_add_image_features_from_folder_test(self):
        def test():
            self.imaging_api.create_image_features(
                CreateImageFeaturesRequest(
                    self.search_context_id,
                    images_folder=self.original_data_folder + '/FindSimilar',
                    storage=self.test_storage))

            self.wait_timeout()

            response = self.imaging_api.get_image_features(
                GetImageFeaturesRequest(
                    self.search_context_id,
                    self.original_data_folder + '/FindSimilar/3.jpg',
                    storage=self.test_storage))

            self.assertTrue('3.jpg' in response.image_id)
            self.assertGreater(len(response.features), 0)

        self._run_test_with_logging('ExtractAndAddImageFeaturesFromFolderTest',
                                    test)

    def test_extract_and_add_image_features_from_website_test(self):
        def test():
            image_source_url = urllib.quote_plus('https://www.f1news.ru/interview/hamilton/140909.shtml')
            self.imaging_api.create_web_site_image_features(CreateWebSiteImageFeaturesRequest(self.search_context_id, image_source_url, storage=self.test_storage))

            self._wait_search_context_idle()

            image_url = urllib.quote_plus('https://cdn.f1ne.ws/userfiles/hamilton/140909.jpg')
            response = self.imaging_api.get_image_features(GetImageFeaturesRequest(self.search_context_id, image_url, storage=self.test_storage))

            self.assertGreater(len(response.features), 0)

        self._run_test_with_logging('ExtractAndAddImageFeaturesFromWebsiteTest', test)

    def test_get_image_feature(self):
        def test():
            self.__add_image_features(self.TEST_IMAGE)

            response = self.__get_image_features(self.TEST_IMAGE)

            self.assertTrue(self.TEST_IMAGE in response.image_id)
            self.assertGreater(len(response.features), 0)

        self._run_test_with_logging('GetImageFeaturesTest', test)

    def test_delete_image_features(self):
        def test():
            image = self.TEST_IMAGE
            self.__add_image_features(image)
            dest_server_path = self.temp_folder + '/' + image

            self.imaging_api.delete_image_search(
                DeleteSearchImageRequest(self.search_context_id,
                                         dest_server_path,
                                         storage=self.test_storage))

            self.assertRaises(ApiException,
                              self.imaging_api.get_search_image,
                              GetSearchImageRequest(
                                  self.search_context_id, dest_server_path,
                                  storage=self.test_storage))

        self._run_test_with_logging('DeleteImageFeaturesTest', test)

    def test_update_image_features(self):
        def test():
            image = self.TEST_IMAGE
            self.__add_image_features(image)
            response = self.__get_image_features(image)
            self.assertTrue(self.TEST_IMAGE in response.image_id)
            features_length = len(response.features)

            dest_server_path = self.original_data_folder + '/' + image
            storage_path = self.original_data_folder + '/' + \
                           self.SMALL_TEST_IMAGE
            image_stream = self.imaging_api.download_file(
                DownloadFileRequest(storage_path, self.test_storage))
            self.assertIsNotNone(image_stream)

            self.imaging_api.update_image_features(
                UpdateImageFeaturesRequest(
                    self.search_context_id,
                    dest_server_path,
                    image_stream,
                    storage=self.test_storage))

            response = self.__get_image_features(image)
            self.assertTrue(self.TEST_IMAGE in response.image_id)
            self.assertNotEqual(features_length, len(response.features))

        self._run_test_with_logging('ExtractImageFeaturesTest', test)

    def __add_image(self, image):
        dest_server_path = self.temp_folder + '/' + image
        storage_path = self.original_data_folder + '/' + image
        image_stream = self.imaging_api.download_file(
            DownloadFileRequest(storage_path, self.test_storage))
        self.assertIsNotNone(image_stream)

        self.imaging_api.add_search_image(
            AddSearchImageRequest(self.search_context_id,
                                             dest_server_path, image_stream,
                                             storage=self.test_storage))

        exist_response = self.imaging_api.object_exists(
            ObjectExistsRequest(dest_server_path, self.test_storage))

        self.assertIsNotNone(exist_response)
        self.assertTrue(exist_response.exists)

    def __get_image(self, image):
        dest_server_path = self.temp_folder + '/' + image
        response = self.imaging_api.get_search_image(
            GetSearchImageRequest(self.search_context_id,
                                         dest_server_path,
                                         storage=self.test_storage))

        return response

    def __add_image_features(self, image):
        dest_server_path = self.original_data_folder + '/' + image

        self.imaging_api.create_image_features(
            CreateImageFeaturesRequest(
                self.search_context_id, image_id=dest_server_path,
                storage=self.test_storage))

    def __get_image_features(self, image):
        dest_server_path = self.original_data_folder + '/' + image
        response = self.imaging_api.get_image_features(
            GetImageFeaturesRequest(self.search_context_id,
                                                 image_id=dest_server_path,
                                                 storage=self.test_storage))

        return response
