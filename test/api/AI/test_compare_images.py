from asposeimagingcloud import PostSearchContextCompareImagesRequest, \
    DownloadFileRequest
from test.api.AI.ai_api_tester import AiApiTester, logging_decorate


class TestCompareImages(AiApiTester):
    comparable_image = 'ComparableImage.jpg'
    comparing_image_similar_less_15 = 'ComparingImageSimilar15.jpg'
    comparing_image_similar_more_75 = 'ComparingImageSimilar75.jpg'

    def test_compare_two_images_in_search_context(self):
        image1 = self._get_storage_path(self.comparable_image)
        self._add_image_features_to_search_context(image1)

        image2 = self._get_storage_path(self.comparing_image_similar_more_75)
        self._add_image_features_to_search_context(image2)

        response = self.imaging_api.post_search_context_compare_images(
            PostSearchContextCompareImagesRequest(self.search_context_id,
                                                  image_id1=image1,
                                                  image_id2=image2,
                                                  storage=self.test_storage))

        self.assertEqual(1, len(response.results))
        self.assertTrue(response.results[0].similarity >= 70)

    def test_compare_loaded_image_to_image_in_search_context(self):
        image = self._get_storage_path(self.comparable_image)
        self._add_image_features_to_search_context(image)

        storage_path = self.original_data_folder + '/' + self.comparing_image_similar_less_15

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
