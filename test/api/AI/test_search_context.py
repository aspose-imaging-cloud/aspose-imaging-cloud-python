import os

import six

from asposeimagingcloud import GetSearchContextStatusRequest, \
    DownloadFileRequest, PostSearchContextAddImageRequest, ObjectExistsRequest, \
    GetSearchContextImageRequest, PostSearchContextExtractImageFeaturesRequest, \
    GetSearchContextImageFeaturesRequest, DeleteSearchContextImageRequest, \
    PutSearchContextImageRequest, GetSearchContextExtractImageFeaturesRequest, \
    PutSearchContextImageFeaturesRequest
from asposeimagingcloud.rest import ApiException
from test.api.AI.ai_api_tester import AiApiTester

if six.PY2:
    import unittest2 as unittest
else:
    import unittest


class TestSearchContext(AiApiTester):
    SMALL_TEST_IMAGE = 'ComparableImage.jpg'
    TEST_IMAGE = 'ComparingImageSimilar15.jpg'

    def test_create_search_context(self):
        self._run_test_with_logging('CreateSearchContextTest',
                                    lambda: self.assertIsNotNone(
                                        self.search_context_id))

    def test_delete_search_context(self):
        def test():
            self._delete_search_context(self.search_context_id)

            self.assertRaises(ApiException,
                              self.imaging_api.get_search_context_status,
                              GetSearchContextStatusRequest(
                                  self.search_context_id,
                                  storage=self.test_storage))

        self._run_test_with_logging('DeleteSearchContextTest', test)

    def test_add_image(self):
        self._run_test_with_logging('AddImageTest',
                                    lambda: self.__add_image(self.TEST_IMAGE))

    def test_delete_image(self):
        def test():
            image = self.TEST_IMAGE
            self.__add_image(image)

            dest_server_path = self.temp_folder + '/' + image

            self.imaging_api.delete_search_context_image(
                DeleteSearchContextImageRequest(self.search_context_id,
                                                dest_server_path,
                                                storage=self.test_storage))

            self.assertRaises(ApiException,
                              self.imaging_api.get_search_context_image,
                              GetSearchContextImageRequest(
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

            self.imaging_api.put_search_context_image(
                PutSearchContextImageRequest(self.search_context_id,
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
                self.imaging_api.get_search_context_extract_image_features(
                    GetSearchContextExtractImageFeaturesRequest(
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
            self.imaging_api.post_search_context_extract_image_features(
                PostSearchContextExtractImageFeaturesRequest(
                    self.search_context_id,
                    images_folder=self.original_data_folder + '/FindSimilar',
                    storage=self.test_storage))

            self.wait_timeout()

            response = self.imaging_api.get_search_context_image_features(
                GetSearchContextImageFeaturesRequest(
                    self.search_context_id,
                    self.original_data_folder + '/FindSimilar/3.jpg',
                    storage=self.test_storage))

            self.assertTrue('3.jpg' in response.image_id)
            self.assertGreater(len(response.features), 0)

        self._run_test_with_logging('ExtractAndAddImageFeaturesFromFolderTest',
                                    test)

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

            self.imaging_api.delete_search_context_image(
                DeleteSearchContextImageRequest(self.search_context_id,
                                                dest_server_path,
                                                storage=self.test_storage))

            self.assertRaises(ApiException,
                              self.imaging_api.get_search_context_image,
                              GetSearchContextImageRequest(
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

            self.imaging_api.put_search_context_image_features(
                PutSearchContextImageFeaturesRequest(
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

        self.imaging_api.post_search_context_add_image(
            PostSearchContextAddImageRequest(self.search_context_id,
                                             dest_server_path, image_stream,
                                             storage=self.test_storage))

        exist_response = self.imaging_api.object_exists(
            ObjectExistsRequest(dest_server_path, self.test_storage))

        self.assertIsNotNone(exist_response)
        self.assertTrue(exist_response.exists)

    def __get_image(self, image):
        dest_server_path = self.temp_folder + '/' + image
        response = self.imaging_api.get_search_context_image(
            GetSearchContextImageRequest(self.search_context_id,
                                         dest_server_path,
                                         storage=self.test_storage))

        return response

    def __add_image_features(self, image):
        dest_server_path = self.original_data_folder + '/' + image

        self.imaging_api.post_search_context_extract_image_features(
            PostSearchContextExtractImageFeaturesRequest(
                self.search_context_id, image_id=dest_server_path,
                storage=self.test_storage))

    def __get_image_features(self, image):
        dest_server_path = self.original_data_folder + '/' + image
        response = self.imaging_api.get_search_context_image_features(
            GetSearchContextImageFeaturesRequest(self.search_context_id,
                                                 image_id=dest_server_path,
                                                 storage=self.test_storage))

        return response
