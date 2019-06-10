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
        self.wait_timeout_in_minutes = 5
        self.cloud_test_folder_prefix = 'ImagingAICloudTestPython'
        self.original_data_folder += '/AI'

    def tearDown(self):
        if self.search_context_id:
            self.__delete_search_context(self.search_context_id)

        if self.imaging_api.object_exists(
                ObjectExistsRequest(self.temp_folder,
                                    self.test_storage)).exists:
            self.imaging_api.delete_folder(
                DeleteFolderRequest(self.temp_folder, self.test_storage, True))

    def _get_storage_path(self, image_name, folder=None):
        return os.path.join(folder if folder else self.original_data_folder,
                            image_name)

    def _add_image_features_to_search_context(self, storage_source_path,
                                              is_folder=False):
        request = PostSearchContextExtractImageFeaturesRequest(
            self.search_context_id, images_folder=storage_source_path,
            storage=self.test_storage) if is_folder else \
            PostSearchContextExtractImageFeaturesRequest(
                self.search_context_id, image_id=storage_source_path,
                storage=self.test_storage)

        self.imaging_api.post_search_context_extract_image_features(request)

        self._wait_search_context_idle()

    def __create_search_context(self):
        return self.imaging_api.post_create_search_context(
            PostCreateSearchContextRequest(storage=self.test_storage)).Id

    def __delete_search_context(self, search_contextId):
        self.imaging_api.delete_search_context(
            DeleteSearchContextRequest(self.search_context_id,
                                       storage=self.test_storage))

    def _wait_search_context_idle(self, max_time=None):
        if not max_time:
            max_time = self.wait_timeout_in_minutes * 60

        timeout = 10
        start_time = time.time()

        while self.imaging_api.get_search_context_status(
                GetSearchContextStatusRequest(
                    self.search_context_id,
                    storage=self.test_storage)).status != 'Idle' \
                and time.time() - start_time < max_time:
            time.sleep(timeout)


def logging_decorate(func):
    def wrapper_func(test_method_with_params):
        passed = False

        print(test_method_with_params)
        try:
            func()
            passed = True
        except Exception as e:
            print(str(e))
            raise

        print('Test passed: ' + str(passed))
