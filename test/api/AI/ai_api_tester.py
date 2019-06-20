#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="ai_api_tester.py">
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
        self.cloud_test_folder_prefix = 'ImagingAICloudTestPython'
        self.original_data_folder += '/AI'

    def tearDown(self):
        if self.search_context_id:
            self._delete_search_context(self.search_context_id)

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
            PostCreateSearchContextRequest(storage=self.test_storage)).id

    def _delete_search_context(self, search_contextId):
        self.imaging_api.delete_search_context(
            DeleteSearchContextRequest(self.search_context_id,
                                       storage=self.test_storage))

    def _wait_search_context_idle(self, max_time=None):
        if not max_time:
            max_time = self.wait_timeout * 60

        timeout = 10
        start_time = time.time()

        while self.imaging_api.get_search_context_status(
                GetSearchContextStatusRequest(
                    self.search_context_id,
                    storage=self.test_storage)).search_status != 'Idle' \
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
