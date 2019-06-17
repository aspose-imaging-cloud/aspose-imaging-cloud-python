import os
import time

from asposeimagingcloud import PostCreateSearchContextRequest, \
    DeleteSearchContextRequest, ObjectExistsRequest, DeleteFolderRequest, \
    PostSearchContextExtractImageFeaturesRequest, GetSearchContextStatusRequest
from test.api_tester import ApiTester


class AiApiTester(ApiTester):

    def setUp(self):
        super(AiApiTester, self).setUp()
        self.search_context_id = self.__create_search_context()
        self.wait_timeout = 5
        ApiTester.cloud_test_folder_prefix = 'ImagingAICloudTestPython'
        ApiTester.original_data_folder += '/AI'

    def tearDown(self):
        if self.search_context_id:
            self._delete_search_context(self.search_context_id)

        if ApiTester.imaging_api.object_exists(
                ObjectExistsRequest(ApiTester.temp_folder,
                                    ApiTester.test_storage)).exists:
            ApiTester.imaging_api.delete_folder(
                DeleteFolderRequest(ApiTester.temp_folder, ApiTester.test_storage, True))

    def _get_storage_path(self, image_name, folder=None):
        return os.path.join(folder if folder else ApiTester.original_data_folder,
                            image_name)

    def _add_image_features_to_search_context(self, storage_source_path,
                                              is_folder=False):
        request = PostSearchContextExtractImageFeaturesRequest(
            self.search_context_id, images_folder=storage_source_path,
            storage=ApiTester.test_storage) if is_folder else \
            PostSearchContextExtractImageFeaturesRequest(
                self.search_context_id, image_id=storage_source_path,
                storage=ApiTester.test_storage)

        ApiTester.imaging_api.post_search_context_extract_image_features(request)

        self._wait_search_context_idle()

    def __create_search_context(self):
        return ApiTester.imaging_api.post_create_search_context(
            PostCreateSearchContextRequest(storage=ApiTester.test_storage)).id

    def _delete_search_context(self, search_contextId):
        ApiTester.imaging_api.delete_search_context(
            DeleteSearchContextRequest(self.search_context_id,
                                       storage=ApiTester.test_storage))

    def _wait_search_context_idle(self, max_time=None):
        if not max_time:
            max_time = self.wait_timeout * 60

        timeout = 10
        start_time = time.time()

        while ApiTester.imaging_api.get_search_context_status(
                GetSearchContextStatusRequest(
                    self.search_context_id,
                    storage=ApiTester.test_storage)).search_status != 'Idle' \
                and time.time() - start_time < max_time:
            time.sleep(timeout)

    @staticmethod
    def _run_test_with_logging(info, test_action_invoker):
        passed = False
        print(info)
        try:
            test_action_invoker()
            passed = True
        except Exception as e:
            print(str(e))
            raise
        finally:
            print ('Test passed: ' + str(passed))
