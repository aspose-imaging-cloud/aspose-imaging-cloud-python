import getpass
import os
import json
import six
from asposeimagingcloud import ImagingApi, ApiClient
import asposeimagingcloud.models.requests as requests
if six.PY2:
    import unittest2 as unittest
else:
    import unittest


class ApiTester(unittest.TestCase):
    EXTENDED_TEST = False
    imaging_api = None  # type: ImagingApi
    failed_any_test = False
    default_storage = 'Imaging-CI'
    cloud_test_folder_prefix = 'ImagingCloudTestPython'
    original_data_folder = 'ImagingIntegrationTestData'
    _server_access_file = 'serverAccess.json'
    _api_version = 'v3.0'
    _app_key = 'xxx'
    _app_sid = 'xxx'
    _base_url = 'http://api.aspose.cloud/'
    _local_test_folder = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'TestData/')
    remove_result = True

    temp_folder = '{0}_{1}'.format(cloud_test_folder_prefix,
                                        os.environ.get(
                                            'BUILD_NUMBER') or getpass.getuser())

    test_storage = None  # type: str

    basic_export_formats = ['bmp',
                                 'gif',
                                 'jpg',
                                 'png',
                                 'psd',
                                 'tiff',
                                 'webp',
                                 'pdf']

    input_test_files = None  # type: list

    def setUp(self):
        print(os.linesep + self._testMethodName)

        ApiTester.failed_any_test = False
        ApiTester.default_storage = 'Imaging-CI'
        ApiTester.cloud_test_folder_prefix = 'ImagingCloudTestPython'
        ApiTester.original_data_folder = 'ImagingIntegrationTestData'
        ApiTester._server_access_file = 'serverAccess.json'
        ApiTester._api_version = 'v3.0'
        ApiTester._app_key = 'xxx'
        ApiTester._app_sid = 'xxx'
        ApiTester._base_url = 'http://api.aspose.cloud/'
        ApiTester._local_test_folder = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'TestData/')
        ApiTester.remove_result = True

        ApiTester.temp_folder = '{0}_{1}'.format(ApiTester.cloud_test_folder_prefix,
                                            os.environ.get('BUILD_NUMBER') or getpass.getuser())

        if not ApiTester.test_storage:
            ApiTester.test_storage = os.environ.get('StorageName')
        if not ApiTester.test_storage:
            print('Storage name is not set by environment variable. Using the default one.')
            ApiTester.test_storage = ApiTester.default_storage

        if not ApiTester.imaging_api:
            self.__create_api_instance()

        if not ApiTester.failed_any_test and ApiTester.remove_result and ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(ApiTester.temp_folder, ApiTester.test_storage)).exists:
            ApiTester.imaging_api.delete_folder(requests.DeleteFolderRequest(ApiTester.temp_folder, ApiTester.test_storage, True))
            ApiTester.imaging_api.create_folder(requests.CreateFolderRequest(ApiTester.temp_folder, ApiTester.test_storage))

    def tearDown(self):
        if not ApiTester.failed_any_test and ApiTester.remove_result and ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(ApiTester.temp_folder, ApiTester.test_storage)).exists:
            ApiTester.imaging_api.delete_folder(requests.DeleteFolderRequest(ApiTester.temp_folder, ApiTester.test_storage, True))

    def __create_api_instance(self, app_key=None, app_sid=None, base_url=None,
                              api_version=None, debug=False):
        if not app_key:
            app_key = ApiTester._app_key

        if not app_sid:
            app_sid = ApiTester._app_sid

        if not base_url:
            base_url = ApiTester._base_url

        if not api_version:
            api_version = ApiTester._api_version

        if app_key == ApiTester._app_key or app_sid == ApiTester._app_sid:
            print("Access data isn't set explicitly. Trying to obtain it from environment variables.")

            app_key = os.environ.get('AppKey')
            app_sid = os.environ.get('AppSid')
            base_url = os.environ.get('ApiEndpoint')
            api_version = os.environ.get('ApiVersion')

        if not (app_key and app_sid and base_url and api_version):
            print(
                "Access data isn't set completely by environment variables. Filling unset data with default values.")

        if not api_version:
            api_version = ApiTester._api_version
            print('Set default API version')

        server_access_info = os.path.join(ApiTester._local_test_folder, ApiTester._server_access_file)
        with open(server_access_info) as f:
            server_file_info = json.load(f)

        if server_file_info:
            if not app_key:
                app_key = server_file_info['AppKey']
                print('Set default App key')

            if not app_sid:
                app_sid = server_file_info['AppSid']
                print('Set default App SID')

            if not base_url:
                base_url = server_file_info['BaseURL']
                print('Set default Base URL')

        if not (app_key and app_sid and base_url and api_version):
            raise ValueError('Please, specify valid access data (AppKey, AppSid, Base URL)')

        print('App key: ' + app_key)
        print('App SID: ' + app_sid)
        print('Storage: ' + ApiTester.test_storage)
        print('Base URL: ' + base_url)
        print('API version: ' + api_version)

        api_client = ApiClient()
        api_client.configuration.host = base_url
        api_client.configuration.api_key['api_key'] = app_key
        api_client.configuration.api_key['app_sid'] = app_sid
        api_client.configuration.api_version = api_version

        ApiTester.imaging_api = ImagingApi(api_client)

        ApiTester.input_test_files = ApiTester.imaging_api.get_files_list(
            requests.GetFilesListRequest(ApiTester.original_data_folder, ApiTester.test_storage)).value

    def __request_tester(self, test_method_name, save_result_to_storage, parameters_line, input_file_name,
                         result_file_name, invoke_request_action, properties_tester, folder, storage=None):
        if not storage:
            storage = ApiTester.default_storage

        if not self._check_input_file_exists(input_file_name):
            raise ValueError(
                "Input file {0} doesn't exist in the specified storage folder: {1}. Please, upload it first.".format(
                    input_file_name, folder))

        if not ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(os.path.join(folder, input_file_name), storage)).exists:
            ApiTester.imaging_api.copy_file(
                requests.CopyFileRequest(os.path.join(ApiTester.original_data_folder, input_file_name),
                                         os.path.join(folder, input_file_name), storage, storage))
        passed = False
        out_path = str(None)

        try:
            print(parameters_line)

            if save_result_to_storage:
                out_path = os.path.join(folder, result_file_name)

                if ApiTester.imaging_api.object_exists(requests.ObjectExistsRequest(out_path, storage)).exists:
                    ApiTester.imaging_api.delete_file(requests.DeleteFileRequest(out_path, storage))

            result_properties = None
            response = invoke_request_action()
            if save_result_to_storage:

                result_info = self._get_storage_file_info(folder, result_file_name, storage)
                if not result_info:
                    raise ValueError(
                        "Result file {0} doesn't exist in the specified storage folder: {1}. "
                        "Result isn't present in the storage by an unknown reason.".format(
                            result_file_name, folder))

                if not str(result_file_name).endswith('.pdf'):
                    result_properties = ApiTester.imaging_api.get_image_properties(
                        requests.GetImagePropertiesRequest(result_file_name, folder, storage))
                    self.assertIsNotNone(result_properties)
            elif "v1." not in ApiTester.imaging_api.api_client.configuration.host and not str(result_file_name).endswith(
                    'pdf'):
                result_properties = ApiTester.imaging_api.post_image_properties(
                    requests.PostImagePropertiesRequest(response))
                self.assertIsNotNone(result_properties)

            original_properties = ApiTester.imaging_api.get_image_properties(
                requests.GetImagePropertiesRequest(input_file_name, folder, storage))
            self.assertIsNotNone(original_properties)

            if result_properties:
                properties_tester(original_properties, result_properties, response)

            passed = True

        except Exception as e:
            ApiTester.failed_any_test = True
            print(str(e))
            raise
        finally:
            if passed and save_result_to_storage and ApiTester.remove_result \
                    and ApiTester.imaging_api.object_exists(requests.ObjectExistsRequest(out_path, storage)).exists:
                ApiTester.imaging_api.delete_file(requests.DeleteFileRequest(out_path, storage))
            print("Test passed: " + str(passed) + os.linesep)

    def get_request_tester(self, test_method_name, save_result_to_storage, parameters_line, input_file_name,
                           result_file_name, request_invoker, properties_tester, folder, storage=None):
        if not storage:
            storage = ApiTester.default_storage

        self.__request_tester(test_method_name, save_result_to_storage, parameters_line, input_file_name,
                              result_file_name,
                              lambda: self._obtain_get_response(
                                  input_file_name,
                                  os.path.join(folder, result_file_name) if save_result_to_storage else None,
                                  request_invoker), properties_tester, folder, storage)

    def post_request_tester(self, test_method_name, save_result_to_storage, parameters_line, input_file_name,
                            result_file_name, request_invoker, properties_tester, folder, storage=None):
        if not storage:
            storage = ApiTester.default_storage

        self.__request_tester(test_method_name, save_result_to_storage, parameters_line, input_file_name,
                              result_file_name,
                              lambda: self._obtain_post_response(os.path.join(folder, input_file_name),
                                                                 os.path.join(folder, result_file_name)
                                                                 if save_result_to_storage else None, storage,
                                                                 request_invoker), properties_tester, folder, storage)

    def _check_input_file_exists(self, input_file_name):
        return any(input_file_name == storage_file_info.name for storage_file_info in ApiTester.input_test_files)

    def _get_storage_file_info(self, folder, file_name, storage):
        file_list_response = ApiTester.imaging_api.get_files_list(requests.GetFilesListRequest(folder, storage)).value

        for storage_file_info in file_list_response:
            if storage_file_info.name == file_name:
                return storage_file_info
        return None

    def _obtain_get_response(self, input_file_name, out_path, request_invoker):
        response = request_invoker(input_file_name, out_path)
        if out_path:
            return None

        self.assertIsNotNone(response)
        self.assertGreater(os.path.getsize(response), 0)
        return response

    def _obtain_post_response(self, input_path, out_path, storage, request_invoker):
        res = ApiTester.imaging_api.download_file(requests.DownloadFileRequest(input_path, storage))

        response = request_invoker(res, out_path)

        if out_path:
            return None

        self.assertIsNotNone(response)
        return response

