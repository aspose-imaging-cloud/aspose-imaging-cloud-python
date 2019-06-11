from asposeimagingcloud import GetSearchContextFindDuplicatesRequest
from test.api.AI.ai_api_tester import AiApiTester


class TestFindDuplicates(AiApiTester):
    COMPARABLE_IMAGE = 'ComparableImage.jpg'
    COMPARING_IMAGE_SIMILAR_LESS_15 = 'ComparingImageSimilar15.jpg'
    COMPARING_IMAGE_SIMILAR_MORE_75 = 'ComparingImageSimilar75.jpg'

    def test_find_duplicates(self):
        def test():
            self._add_image_features_to_search_context(
                self.original_data_folder + '/FindSimilar', is_folder=True)

            image = self._get_storage_path(self.COMPARABLE_IMAGE)
            self._add_image_features_to_search_context(image)

            image = self._get_storage_path(
                self.COMPARING_IMAGE_SIMILAR_LESS_15)
            self._add_image_features_to_search_context(image)

            image = self._get_storage_path(
                self.COMPARING_IMAGE_SIMILAR_MORE_75)
            self._add_image_features_to_search_context(image)

            response = self.imaging_api.get_search_context_find_duplicates(
                GetSearchContextFindDuplicatesRequest(self.search_context_id,
                                                      similarity_threshold=80,
                                                      storage=self.test_storage))
            self.assertEqual(1, response.duplicates.count)

        self._run_test_with_logging('FindDuplicatesTest', test)
