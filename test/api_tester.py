import unittest
import getpass
import os
import json

from asposeimagingcloud import ImagingApi, ApiClient


class ApiTester(unittest.TestCase):
    def setUp(self):
        # TODO: Move some of parameters to something like OneTimeSetUp?
        self.failed_any_test = False
        self.default_storage = 'Imaging-CI'
        self.cloud_test_folder_prefix = 'ImagingCloudTestDotNet'
        self.original_data_folder = 'ImagingIntegrationTestData'
        self._server_access_file = 'serverAccess.json'
        self._api_version = 'v3.0'
        self._app_key = 'xxx'
        self._app_sid = 'xxx'
        self._base_url = 'http://api.aspose.cloud/'
        self._local_test_folder = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'TestData/')
        self.test_storage = None
        self.remove_result = True

        self.temp_folder = '{0}_{1}'.format(self.cloud_test_folder_prefix,
                                            os.environ.get('BUILD_NUMBER') or getpass.getuser())

        self.test_storage = os.environ.get('StorageName')
        if not self.test_storage:
            print('Storage name is not set by environment variable. Using the default one.')
            self.test_storage = self.default_storage

        self._create_api_instance()

        if not self.failed_any_test and self.remove_result and self.imaging_api.object_exists(
                self.temp_folder, **{"storage_name": self.test_storage}).exists:
            self.imaging_api.delete_folder(self.temp_folder, **{"storage_name": self.test_storage, "recursive": True})
            self.imaging_api.create_folder(self.temp_folder, **{"storage_name": self.test_storage})

    def tearDown(self):
        if not self.failed_any_test and self.remove_result and self.imaging_api.object_exists(
                self.temp_folder, **{"storage_name": self.test_storage}).exists:
            self.imaging_api.delete_folder(self.temp_folder, **{"storage_name": self.test_storage, "recursive": True})

    def _create_api_instance(self, app_key=None, app_sid=None, base_url=None,
                             api_version=None, debug=False):
        if not app_key:
            app_key = self._app_key

        if not app_sid:
            app_sid = self._app_sid

        if not base_url:
            base_url = self._base_url

        if not api_version:
            api_version = self._api_version

        if app_key == self._app_key or app_sid == self._app_sid:
            print("Access data isn't set explicitly. Trying to obtain it from environment variables.")

            app_key = os.environ.get('AppKey')
            app_sid = os.environ.get('AppSid')
            base_url = os.environ.get('ApiEndpoint')
            api_version = os.environ.get('ApiVersion')

        if not (app_key and app_sid and base_url and api_version):
            print(
                "Access data isn't set completely by environment variables. Filling unset data with default values.")

        if not api_version:
            api_version = self._api_version
            print('Set default API version')

        server_access_info = os.path.join(self._local_test_folder, self._server_access_file)
        with open(server_access_info) as f:
            server_file_info = json.load(f)

        if not server_file_info:
            raise ValueError('Please, specify valid access data (AppKey, AppSid, Base URL)')

        if not app_key:
            app_key = server_file_info['AppKey']
            print('Set default App key')

        if not app_sid:
            app_sid = server_file_info['AppSid']
            print('Set default App SID')

        if not base_url:
            base_url = server_file_info['BaseURL']
            print('Set default Base URL')

        print('App key: ' + app_key)
        print('App SID: ' + app_sid)
        print('Storage: ' + self.test_storage)
        print('Base URL: ' + base_url)
        print('API version: ' + api_version)

        api_client = ApiClient()
        api_client.configuration.host = base_url
        api_client.configuration.api_key['api_key'] = app_key
        api_client.configuration.api_key['app_sid'] = app_sid
        api_client.configuration.api_version = api_version

        self.imaging_api = ImagingApi(api_client)
        self.imaging_api.request_token()

        self.input_test_files = self.imaging_api.get_files_list(self.original_data_folder,
                                                                **{"storage_name": self.test_storage}).value

    def _test_request(self, test_method_name, save_result_to_storage, parameters_line, input_file_name,
                      result_file_name, invoke_request_action, properties_tester, folder, storage=None):
        if not storage:
            storage = self.default_storage

        if not self._check_input_file_exists(input_file_name):
            raise ValueError(
                "Input file {0} doesn't exist in the specified storage folder: {1}. Please, upload it first.".format(
                    input_file_name, folder))

        if not self.imaging_api.object_exists(os.path.join(folder, input_file_name),
                                              **{"storage_name": storage}).exists:
            self.imaging_api.copy_file(os.path.join(self.original_data_folder, input_file_name),
                                       os.path.join(folder, input_file_name), **{"src_storage_name": storage,
                                                                                 "dest_storage_name": storage}
                                       )
        passed = False
        out_path = str(None)

        try:
            print(parameters_line)

            if save_result_to_storage:
                out_path = os.path.join(folder, result_file_name)

                if self.imaging_api.object_exists(out_path, **{"storage_name": storage}).exists:
                    self.imaging_api.delete_file(out_path, **{"storage_name": storage})

            response = invoke_request_action()
            if save_result_to_storage:

                result_info = self._get_storage_file_info(folder, result_file_name, storage)
                if not result_info:
                    raise ValueError(
                        "Result file {0} doesn't exist in the specified storage folder: {1}. "
                        "Result isn't present in the storage by an unknown reason.".format(
                            result_file_name, folder))

                if not str(result_file_name).endswith('.pdf'):
                    result_properties = self.imaging_api.get_image_properties(result_file_name, **{"folder": folder,
                                                                                                   "storage":
                                                                                                       storage})
                self.assertIsNotNone(result_properties)
            elif "v1." not in self.imaging_api.api_client.configuration.host and not str(result_file_name).endswith(
                    'pdf'):
                result_properties = self.imaging_api.post_image_properties(response)
                self.assertIsNotNone(result_properties)

            original_properties = self.imaging_api.get_image_properties(input_file_name,
                                                                        **{"folder": folder, "storage": storage})
            self.assertIsNotNone(original_properties)

            if result_properties:
                properties_tester(original_properties, result_properties, response)

            passed = True

        except Exception as e:
            self.failed_any_test = True
            print(str(e))
            raise
        finally:
            if passed and save_result_to_storage and self.remove_result \
                    and self.imaging_api.object_exists(out_path, **{"storage_name": storage}).exists:
                self.imaging_api.delete_file(out_path, **{"storage_name": storage})
            print("Test passed: " + str(passed))

    def test_get_request(self, test_method_name, save_result_to_storage, parameters_line, input_file_name,
                         result_file_name, request_invoker, properties_tester, folder, storage=None):
        if not storage:
            storage = self.default_storage

        self._test_request(test_method_name, save_result_to_storage, parameters_line, input_file_name, result_file_name,
                           lambda: self._obtain_get_response(input_file_name, os.path.join(folder, result_file_name) if save_result_to_storage else None,
                                                             request_invoker), properties_tester, folder, storage)

    def _check_input_file_exists(self, input_file_name):
        return any(input_file_name == storage_file_info.name for storage_file_info in self.input_test_files)

    def _get_storage_file_info(self, folder, file_name, storage):
        file_list_response = self.imaging_api.get_files_list(folder, **{"storage_name": storage}).value

        for storage_file_info in file_list_response:
            if storage_file_info.name == file_name:
                return storage_file_info
        return None

    def _obtain_get_response(self, input_file_name, out_path, request_invoker):
        response = request_invoker(input_file_name, out_path)
        if not out_path: return None

        self.assertIsNotNone(response)
        # TODO: assert response length?
        return response
