from asposeimagingcloud import GetSearchContextFindSimilarRequest, \
    DownloadFileRequest, PostSearchContextAddTagRequest, \
    PostSearchContextFindByTagsRequest
from test.api.AI.ai_api_tester import AiApiTester


class TestFindImages(AiApiTester):
    IMAGE_TO_FIND = '4.jpg'
    IMAGE_TO_FIND_BY_TAG = 'ComparingImageSimilar75.jpg'

    def test_find_similar(self):
        def test():
            self._add_image_features_to_search_context(
                self.original_data_folder + '/FindSimilar', is_folder=True)
            find_image_id = self.original_data_folder + '/FindSimilar/' + self.IMAGE_TO_FIND
            response = self.imaging_api.get_search_context_find_similar(
                GetSearchContextFindSimilarRequest(self.search_context_id,
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
            self.imaging_api.post_search_context_add_tag(
                PostSearchContextAddTagRequest(tag_image_stream,
                                               self.search_context_id, tag,
                                               storage=self.test_storage))

            response = self.imaging_api.post_search_context_find_by_tags(
                PostSearchContextFindByTagsRequest([tag],
                                                   self.search_context_id,
                                                   similarity_threshold=60,
                                                   max_count=5,
                                                   storage=self.test_storage))

            self.assertEqual(1, len(response.result))
            self.assertTrue('2.jpg' in response.results[0].image_id)
