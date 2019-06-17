from test.api.storage.storage_api_tester import StorageApiTester
from test.api_tester import ApiTester
import asposeimagingcloud.models.requests as requests


class TestFileApi(StorageApiTester):
    """ Specific file API tests for Storage """

    def test_copy_download_file(self):
        folder = ApiTester.temp_folder + '/Storage'
        file = 'Storage.txt'

        try:
            if ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, ApiTester.test_storage)).exists:
                ApiTester.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, ApiTester.test_storage, True))

            self.assertFalse(
                ApiTester.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder, ApiTester.test_storage)).exists)

            ApiTester.imaging_api.copy_file(
                requests.CopyFileRequest(
                    ApiTester.original_data_folder + '/' + file,
                    folder + '/' + file,
                    ApiTester.test_storage,
                    ApiTester.test_storage))
            exists_response = ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder + '/' + file, ApiTester.test_storage))
            self.assertIsNotNone(exists_response)
            self.assertFalse(exists_response.is_folder)
            self.assertTrue(exists_response.exists)

            original_file_info = next(
                x for x in ApiTester.imaging_api.get_files_list(
                    requests.GetFilesListRequest(
                        ApiTester.original_data_folder,
                        ApiTester.test_storage)).value if x.name == file)

            copied_file_info = next(
                x for x in ApiTester.imaging_api.get_files_list(
                    requests.GetFilesListRequest(
                        folder, ApiTester.test_storage)).value if x.name == file)

            self.assertEqual(original_file_info.size, copied_file_info.size)

            original_file = ApiTester.imaging_api.download_file(
                requests.DownloadFileRequest(
                    ApiTester.original_data_folder + '/' + file,
                    ApiTester.test_storage))
            copied_file = ApiTester.imaging_api.download_file(
                requests.DownloadFileRequest(
                    folder + '/' + file, ApiTester.test_storage))

            with open(original_file, 'r') as original_reader, open(copied_file, 'r') as copied_reader:
                original_string = original_reader.read()
                copied_string = copied_reader.read()
                self.assertEqual(len(original_string), len(copied_string))
                self.assertEqual(len(original_string), original_file_info.size)
                self.assertEqual(original_string, copied_string)
                self.assertEqual(
                    original_string,
                    original_file_info.path.strip('/'))
                self.assertEqual(
                    original_string.replace(
                        ApiTester.original_data_folder,
                        folder),
                    copied_file_info.path.strip('/'))

        finally:
            ApiTester.imaging_api.delete_file(
                requests.DeleteFileRequest(
                    folder + '/' + file,
                    ApiTester.test_storage))
            self.assertFalse(
                ApiTester.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder + '/' + file,
                        ApiTester.test_storage)).exists)

            if ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, ApiTester.test_storage)).exists:
                ApiTester.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, ApiTester.test_storage, True))

            self.assertFalse(
                ApiTester.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder, ApiTester.test_storage)).exists)

    def test_file_versions_copy(self):
        folder = ApiTester.temp_folder + '/Storage'
        file1 = 'Storage.txt'
        file2 = 'Folder1/Folder1.txt'

        try:
            if ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, ApiTester.test_storage)).exists:
                ApiTester.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, ApiTester.test_storage, True))

            self.assertFalse(
                ApiTester.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder, ApiTester.test_storage)).exists)

            ApiTester.imaging_api.copy_file(
                requests.CopyFileRequest(
                    ApiTester.original_data_folder + '/' + file1,
                    folder + '/' + file1,
                    ApiTester.test_storage,
                    ApiTester.test_storage))
            ApiTester.imaging_api.copy_file(
                requests.CopyFileRequest(
                    ApiTester.original_data_folder + '/' + file2,
                    folder + '/' + file1,
                    ApiTester.test_storage,
                    ApiTester.test_storage))
            versions = ApiTester.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(
                    folder + '/' + file1, ApiTester.test_storage)).value
            recent_version = next(x for x in versions if x.is_latest is True)
            old_version = next(x for x in versions if x.is_latest is not True)

            ApiTester.imaging_api.copy_file(
                requests.CopyFileRequest(
                    folder + '/' + file1,
                    folder + '/' + file1 + '.recent',
                    ApiTester.test_storage,
                    ApiTester.test_storage,
                    recent_version.version_id))
            copied_versions = ApiTester.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(
                    folder + '/' + file1 + '.recent',
                    ApiTester.test_storage)).value

            self.assertEqual(1, len(copied_versions))
            self.assertTrue(copied_versions[0].is_latest)
            self.assertEqual(recent_version.size, copied_versions[0].size)

            ApiTester.imaging_api.copy_file(
                requests.CopyFileRequest(
                    folder + '/' + file1,
                    folder + '/' + file1 + '.old',
                    ApiTester.test_storage,
                    ApiTester.test_storage,
                    old_version.version_id))
            copied_versions = ApiTester.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(
                    folder + '/' + file1 + '.old',
                    ApiTester.test_storage)).value

            self.assertEqual(1, len(copied_versions))
            self.assertTrue(copied_versions[0].is_latest)
            self.assertEqual(old_version.size, copied_versions[0].size)

        finally:
            if ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, ApiTester.test_storage)).exists:
                ApiTester.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, ApiTester.test_storage, True))

    def test_file_version_create(self):
        folder = ApiTester.temp_folder + '/Storage'
        file1 = 'Storage.txt'
        file2 = 'Folder1/Folder1.txt'

        file1_size = next(
            x for x in ApiTester.imaging_api.get_files_list(
                requests.GetFilesListRequest(
                    ApiTester.original_data_folder,
                    ApiTester.test_storage)).value if x.name == file1).size

        file2_size = next(
            x for x in ApiTester.imaging_api.get_files_list(
                requests.GetFilesListRequest(
                    ApiTester.original_data_folder + '/Folder1',
                    ApiTester.test_storage)).value if x.name == 'Folder1.txt').size

        try:
            if ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, ApiTester.test_storage)).exists:
                ApiTester.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, ApiTester.test_storage, True))

            self.assertFalse(
                ApiTester.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder, ApiTester.test_storage)).exists)

            ApiTester.imaging_api.copy_file(
                requests.CopyFileRequest(
                    ApiTester.original_data_folder + '/' + file1,
                    folder + '/' + file1,
                    ApiTester.test_storage,
                    ApiTester.test_storage))
            ApiTester.imaging_api.copy_file(
                requests.CopyFileRequest(
                    ApiTester.original_data_folder + '/' + file2,
                    folder + '/' + file1,
                    ApiTester.test_storage,
                    ApiTester.test_storage))
            versions = ApiTester.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(
                    folder + '/' + file1, ApiTester.test_storage)).value

            self.assertEqual(2, len(versions))
            recent_version_size = next(
                x for x in versions if x.is_latest is True).size
            old_version_size = next(
                x for x in versions if x.is_latest is not True).size
            self.assertNotEqual(recent_version_size, old_version_size)
            self.assertEqual(old_version_size, file1_size)
            self.assertEqual(recent_version_size, file2_size)

        finally:
            if ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, ApiTester.test_storage)).exists:
                ApiTester.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, ApiTester.test_storage, True))

    def test_file_version_delete(self):
        folder = ApiTester.temp_folder + '/Storage'
        file1 = 'Storage.txt'
        file2 = 'Folder1/Folder1.txt'

        try:
            if ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, ApiTester.test_storage)).exists:
                ApiTester.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, ApiTester.test_storage, True))

            self.assertFalse(
                ApiTester.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder, ApiTester.test_storage)).exists)

            ApiTester.imaging_api.copy_file(
                requests.CopyFileRequest(
                    ApiTester.original_data_folder + '/' + file1,
                    folder + '/' + file1,
                    ApiTester.test_storage,
                    ApiTester.test_storage))
            ApiTester.imaging_api.copy_file(
                requests.CopyFileRequest(
                    ApiTester.original_data_folder + '/' + file2,
                    folder + '/' + file1,
                    ApiTester.test_storage,
                    ApiTester.test_storage))
            versions = ApiTester.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(
                    folder + '/' + file1, ApiTester.test_storage)).value
            recent_version = next(x for x in versions if x.is_latest is True)
            old_version = next(x for x in versions if x.is_latest is not True)

            self.assertTrue(
                ApiTester.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder + '/' + file1,
                        ApiTester.test_storage,
                        recent_version.version_id)).exists)
            self.assertTrue(
                ApiTester.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder + '/' + file1,
                        ApiTester.test_storage,
                        old_version.version_id)).exists)

            ApiTester.imaging_api.delete_file(
                requests.DeleteFileRequest(
                    folder + '/' + file1,
                    ApiTester.test_storage,
                    recent_version.version_id))

            versions = ApiTester.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(
                    folder + '/' + file1, ApiTester.test_storage)).value
            self.assertFalse(
                ApiTester.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder + '/' + file1,
                        ApiTester.test_storage,
                        recent_version.version_id)).exists)
            self.assertTrue(
                ApiTester.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder + '/' + file1,
                        ApiTester.test_storage,
                        old_version.version_id)).exists)
            self.assertEqual(1, len(versions))
            self.assertEqual(old_version.size, versions[0].size)

            ApiTester.imaging_api.delete_file(
                requests.DeleteFileRequest(
                    folder + '/' + file1,
                    ApiTester.test_storage,
                    old_version.version_id))
            self.assertFalse(
                ApiTester.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder + '/' + file1,
                        ApiTester.test_storage)).exists)

        finally:
            if ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, ApiTester.test_storage)).exists:
                ApiTester.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, ApiTester.test_storage, True))

    def test_file_version_download(self):
        folder = ApiTester.temp_folder + '/Storage'
        file1 = 'Storage.txt'
        file2 = 'Folder1/Folder1.txt'

        try:
            if ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, ApiTester.test_storage)).exists:
                ApiTester.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, ApiTester.test_storage, True))

            self.assertFalse(
                ApiTester.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder, ApiTester.test_storage)).exists)

            ApiTester.imaging_api.copy_file(
                requests.CopyFileRequest(
                    ApiTester.original_data_folder + '/' + file1,
                    folder + '/' + file1,
                    ApiTester.test_storage,
                    ApiTester.test_storage))
            ApiTester.imaging_api.copy_file(
                requests.CopyFileRequest(
                    ApiTester.original_data_folder + '/' + file2,
                    folder + '/' + file1,
                    ApiTester.test_storage,
                    ApiTester.test_storage))
            versions = ApiTester.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(
                    folder + '/' + file1, ApiTester.test_storage)).value
            recent_version = next(x for x in versions if x.is_latest is True)
            old_version = next(x for x in versions if x.is_latest is not True)

            with open(ApiTester.imaging_api.download_file(
                    requests.DownloadFileRequest(folder + '/' + file1, ApiTester.test_storage,
                                                 old_version.version_id)), 'r') as old_file:
                self.assertEqual(old_version.size, len(old_file.read()))

            with open(ApiTester.imaging_api.download_file(
                    requests.DownloadFileRequest(folder + '/' + file1, ApiTester.test_storage,
                                                 recent_version.version_id)), 'r') as old_file:
                self.assertEqual(recent_version.size, len(old_file.read()))

        finally:
            if ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, ApiTester.test_storage)).exists:
                ApiTester.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, ApiTester.test_storage, True))

    def test_file_version_move(self):
        folder = ApiTester.temp_folder + '/Storage'
        file1 = 'Storage.txt'
        file2 = 'Folder1/Folder1.txt'

        try:
            if ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, ApiTester.test_storage)).exists:
                ApiTester.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, ApiTester.test_storage, True))

            self.assertFalse(
                ApiTester.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder, ApiTester.test_storage)).exists)

            ApiTester.imaging_api.copy_file(
                requests.CopyFileRequest(
                    ApiTester.original_data_folder + '/' + file1,
                    folder + '/' + file1,
                    ApiTester.test_storage,
                    ApiTester.test_storage))
            ApiTester.imaging_api.copy_file(
                requests.CopyFileRequest(
                    ApiTester.original_data_folder + '/' + file2,
                    folder + '/' + file1,
                    ApiTester.test_storage,
                    ApiTester.test_storage))
            versions = ApiTester.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(
                    folder + '/' + file1, ApiTester.test_storage)).value
            recent_version = next(x for x in versions if x.is_latest is True)

            ApiTester.imaging_api.move_file(
                requests.MoveFileRequest(
                    folder + '/' + file1,
                    folder + '/' + file1 + '.recent',
                    ApiTester.test_storage,
                    ApiTester.test_storage,
                    recent_version.version_id))
            copied_versions = ApiTester.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(
                    folder + '/' + file1 + '.recent',
                    ApiTester.test_storage)).value
            self.assertEqual(1, len(copied_versions))
            self.assertTrue(copied_versions[0].is_latest)
            self.assertEqual(recent_version.size, copied_versions[0].size)

            ApiTester.imaging_api.copy_file(
                requests.CopyFileRequest(
                    ApiTester.original_data_folder + '/' + file1,
                    folder + '/' + file1,
                    ApiTester.test_storage,
                    ApiTester.test_storage))
            ApiTester.imaging_api.copy_file(
                requests.CopyFileRequest(
                    ApiTester.original_data_folder + '/' + file2,
                    folder + '/' + file1,
                    ApiTester.test_storage,
                    ApiTester.test_storage))
            versions = ApiTester.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(
                    folder + '/' + file1, ApiTester.test_storage)).value
            old_version = next(x for x in versions if x.is_latest is not True)

            ApiTester.imaging_api.move_file(
                requests.MoveFileRequest(
                    folder + '/' + file1,
                    folder + '/' + file1 + '.old',
                    ApiTester.test_storage,
                    ApiTester.test_storage,
                    old_version.version_id))
            copied_versions = ApiTester.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(folder + '/' + file1 + '.old',
                                                ApiTester.test_storage)).value
            self.assertEqual(1, len(copied_versions))
            self.assertTrue(copied_versions[0].is_latest)
            self.assertEqual(old_version.size, copied_versions[0].size)

        finally:
            if ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, ApiTester.test_storage)).exists:
                ApiTester.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, ApiTester.test_storage, True))

    def test_move_file(self):
        folder = ApiTester.temp_folder + '/Storage'
        file = 'Storage.txt'

        try:
            if ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, ApiTester.test_storage)).exists:
                ApiTester.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, ApiTester.test_storage, True))

            self.assertFalse(
                ApiTester.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder, ApiTester.test_storage)).exists)

            ApiTester.imaging_api.copy_file(
                requests.CopyFileRequest(
                    ApiTester.original_data_folder + '/' + file,
                    folder + '/' + file + '.copied',
                    ApiTester.test_storage,
                    ApiTester.test_storage))
            exist_response = ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder + '/' + file + '.copied',
                    ApiTester.test_storage))
            self.assertIsNotNone(exist_response)
            self.assertFalse(exist_response.is_folder)
            self.assertTrue(exist_response.exists)

            ApiTester.imaging_api.move_file(
                requests.MoveFileRequest(
                    folder + '/' + file + '.copied',
                    folder + '/' + file,
                    ApiTester.test_storage,
                    ApiTester.test_storage))
            self.assertFalse(
                ApiTester.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder + '/' + file + '.copied',
                        ApiTester.test_storage)).exists)
            exist_response = ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder + '/' + file, ApiTester.test_storage))
            self.assertIsNotNone(exist_response)
            self.assertFalse(exist_response.is_folder)
            self.assertTrue(exist_response.exists)

            original_file_info = next(
                x for x in ApiTester.imaging_api.get_files_list(
                    requests.GetFilesListRequest(
                        ApiTester.original_data_folder,
                        ApiTester.test_storage)).value if x.name == file)
            moved_file_info = next(
                x for x in ApiTester.imaging_api.get_files_list(
                    requests.GetFilesListRequest(
                        folder, ApiTester.test_storage)).value if x.name == file)
            self.assertEqual(original_file_info.size, moved_file_info.size)

            with open(ApiTester.imaging_api.download_file(
                    requests.DownloadFileRequest(ApiTester.original_data_folder + '/' + file,
                                                 ApiTester.test_storage)), 'r') as original_file, \
                    open(ApiTester.imaging_api.download_file(requests.DownloadFileRequest(folder + '/' + file,
                                                                                     ApiTester.test_storage)),
                         'r') as moved_file:
                original_string = original_file.read()
                moved_string = moved_file.read()
                self.assertEqual(len(original_string), len(moved_string))
                self.assertEqual(len(original_string), original_file_info.size)
                self.assertEqual(original_string, moved_string)
                self.assertEqual(
                    original_string,
                    original_file_info.path.strip('/'))
                self.assertEqual(
                    original_string.replace(
                        ApiTester.original_data_folder,
                        folder),
                    moved_file_info.path.strip('/'))

        finally:
            ApiTester.imaging_api.delete_file(
                requests.DeleteFileRequest(
                    folder + '/' + file,
                    ApiTester.test_storage))
            self.assertFalse(
                ApiTester.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder + '/' + file,
                        ApiTester.test_storage)).exists)

            if ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, ApiTester.test_storage)).exists:
                ApiTester.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, ApiTester.test_storage, True))

            self.assertFalse(
                ApiTester.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder, ApiTester.test_storage)).exists)

    def test_upload_file(self):
        folder = ApiTester.temp_folder + '/Storage'
        file = 'Storage.txt'

        try:
            if ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, ApiTester.test_storage)).exists:
                ApiTester.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, ApiTester.test_storage, True))

            self.assertFalse(
                ApiTester.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder, ApiTester.test_storage)).exists)

            original_file = ApiTester.imaging_api.download_file(
                requests.DownloadFileRequest(
                    ApiTester.original_data_folder + '/' + file,
                    ApiTester.test_storage))

            result = ApiTester.imaging_api.upload_file(
                requests.UploadFileRequest(
                    folder + '/' + file,
                    original_file,
                    ApiTester.test_storage))
            self.assertIsNotNone(result)
            self.assertTrue(not result.errors or len(result) == 0)
            self.assertIsNotNone(result.uploaded)
            self.assertEqual(1, len(result.uploaded))
            self.assertEqual(file, result.uploaded[0])

            exist_response = ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder + '/' + file, ApiTester.test_storage))
            self.assertIsNotNone(exist_response)
            self.assertFalse(exist_response.is_folder)
            self.assertTrue(exist_response.exists)

            original_file_info = next(
                x for x in ApiTester.imaging_api.get_files_list(
                    requests.GetFilesListRequest(
                        ApiTester.original_data_folder,
                        ApiTester.test_storage)).value if x.name == file)

            uploaded_file_info = next(
                x for x in ApiTester.imaging_api.get_files_list(
                    requests.GetFilesListRequest(
                        folder, ApiTester.test_storage)).value if x.name == file)
            self.assertEqual(original_file_info.size, uploaded_file_info.size)

            original_file = ApiTester.imaging_api.download_file(
                requests.DownloadFileRequest(
                    ApiTester.original_data_folder + '/' + file,
                    ApiTester.test_storage))

            uploaded_file = ApiTester.imaging_api.download_file(
                requests.DownloadFileRequest(
                    folder + '/' + file, ApiTester.test_storage))

            with open(original_file, 'r') as original_reader, open(uploaded_file, 'r') as uploaded_reader:
                original_string = original_reader.read()
                copied_string = uploaded_reader.read()
                self.assertEqual(len(original_string), len(copied_string))
                self.assertEqual(len(original_string), original_file_info.size)
                self.assertEqual(original_string, copied_string)
                self.assertEqual(
                    original_string,
                    original_file_info.path.strip('/'))
                self.assertEqual(
                    original_string.replace(
                        ApiTester.original_data_folder,
                        folder),
                    uploaded_file_info.path.strip('/'))

        finally:
            ApiTester.imaging_api.delete_file(
                requests.DeleteFileRequest(
                    folder + '/' + file,
                    ApiTester.test_storage))
            self.assertFalse(
                ApiTester.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder + '/' + file,
                        ApiTester.test_storage)).exists)

            if ApiTester.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, ApiTester.test_storage)).exists:
                ApiTester.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, ApiTester.test_storage, True))

            self.assertFalse(
                ApiTester.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder, ApiTester.test_storage)).exists)
