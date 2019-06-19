from test.api.storage.storage_api_tester import StorageApiTester
from test.api_tester import ApiTester
import asposeimagingcloud.models.requests as requests


class TestFolderApi(StorageApiTester):
    """ Specific folder API tests for Storage """

    def test_create_folder(self):
        folder = self.temp_folder + '/DummyFolder'

        try:
            if self.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, self.test_storage)).exists:
                self.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, self.test_storage, True))

            self.assertFalse(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder, self.test_storage)).exists)

            self.imaging_api.create_folder(
                requests.CreateFolderRequest(
                    folder, self.test_storage))
            self.assertTrue(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder, self.test_storage)).exists)

        finally:
            if self.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, self.test_storage)).exists:
                self.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, self.test_storage, True))

            self.assertFalse(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder, self.test_storage)).exists)

    def test_copy_folder(self):
        folder = self.temp_folder + '/Storage'

        try:
            if self.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, self.test_storage)).exists:
                self.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, self.test_storage, True))

            self.assertFalse(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder, self.test_storage)).exists)

            self.imaging_api.copy_folder(
                requests.CopyFolderRequest(
                    self.original_data_folder,
                    folder,
                    self.test_storage,
                    self.test_storage))
            self.assertTrue(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder, self.test_storage)).exists)

            original_files = self.imaging_api.get_files_list(
                requests.GetFilesListRequest(
                    self.original_data_folder,
                    self.test_storage)).value
            copied_files = self.imaging_api.get_files_list(
                requests.GetFilesListRequest(folder, self.test_storage)).value
            self.assertGreater(len(original_files), 0)
            self.assertGreater(len(copied_files), 0)
            self.assertEqual(len(original_files), len(copied_files))
            for i in range(len(original_files)):
                self.assertEqual(
                    original_files[i].is_folder,
                    copied_files[i].is_folder)
                self.assertEqual(original_files[i].name, copied_files[i].name)
                self.assertEqual(original_files[i].size, copied_files[i].size)

        finally:
            if self.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, self.test_storage)).exists:
                self.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, self.test_storage, True))

            self.assertFalse(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder, self.test_storage)).exists)

    def test_move_folder(self):
        tmp_folder = self.temp_folder + '/Temp'
        folder = self.temp_folder + '/Storage'

        try:
            if self.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, self.test_storage)).exists:
                self.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, self.test_storage, True))

            self.assertFalse(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder, self.test_storage)).exists)

            if self.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    tmp_folder,
                    self.test_storage)).exists:
                self.imaging_api.delete_tmp_folder(
                    requests.DeleteFolderRequest(
                        tmp_folder, self.test_storage, True))

            self.assertFalse(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        tmp_folder,
                        self.test_storage)).exists)

            self.imaging_api.copy_folder(
                requests.CopyFolderRequest(
                    self.original_data_folder,
                    tmp_folder,
                    self.test_storage,
                    self.test_storage))
            self.assertTrue(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        tmp_folder,
                        self.test_storage)).exists)

            self.imaging_api.move_folder(
                requests.MoveFolderRequest(
                    tmp_folder,
                    folder,
                    self.test_storage,
                    self.test_storage))
            self.assertFalse(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        tmp_folder,
                        self.test_storage)).exists)
            self.assertTrue(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder, self.test_storage)).exists)

            original_files = self.imaging_api.get_files_list(
                requests.GetFilesListRequest(
                    self.original_data_folder,
                    self.test_storage)).value
            copied_files = self.imaging_api.get_files_list(
                requests.GetFilesListRequest(folder, self.test_storage)).value
            self.assertGreater(len(original_files), 0)
            self.assertGreater(len(copied_files), 0)
            self.assertEqual(len(original_files), len(copied_files))
            for i in range(len(original_files)):
                self.assertEqual(
                    original_files[i].is_folder,
                    copied_files[i].is_folder)
                self.assertEqual(original_files[i].name, copied_files[i].name)
                self.assertEqual(original_files[i].size, copied_files[i].size)

        finally:
            if self.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, self.test_storage)).exists:
                self.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, self.test_storage, True))

            self.assertFalse(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder, self.test_storage)).exists)

    def test_files_list(self):
        files = self.imaging_api.get_files_list(
            requests.GetFilesListRequest(
                self.original_data_folder,
                self.test_storage)).value
        self.assertEqual(3, len(files))
        folder1 = next(x for x in files if x.name == 'Folder1')
        self.assertIsNotNone(folder1)
        self.assertTrue(folder1.is_folder)
        self.assertTrue(folder1.path.strip('/').endswith(folder1.name))
        folder2 = next(x for x in files if x.name == 'Folder2')
        self.assertIsNotNone(folder2)
        self.assertTrue(folder2.is_folder)
        self.assertTrue(folder2.path.strip('/').endswith(folder2.name))
        storage_file = next(x for x in files if x.name == 'Storage.txt')
        self.assertIsNotNone(storage_file)
        self.assertFalse(storage_file.is_folder)
        self.assertTrue(storage_file.path.strip(
            '/').endswith(storage_file.name))
        self.assertEqual(storage_file.size, len(storage_file.path.strip('/')))

        files = self.imaging_api.get_files_list(
            requests.GetFilesListRequest(
                self.original_data_folder + '/' + folder1.name,
                self.test_storage)).value
        self.assertEqual(1, len(files))
        folder1_file = next(x for x in files if x.name == 'Folder1.txt')
        self.assertIsNotNone(folder1_file)
        self.assertFalse(folder1_file.is_folder)
        self.assertTrue(folder1_file.path.strip(
            '/').endswith(folder1_file.name))
        self.assertEqual(folder1_file.size, len(folder1_file.path.strip('/')))

        files = self.imaging_api.get_files_list(
            requests.GetFilesListRequest(
                self.original_data_folder + '/' + folder2.name,
                self.test_storage)).value
        self.assertEqual(2, len(files))
        folder2_file = next(x for x in files if x.name == 'Folder2.txt')
        self.assertIsNotNone(folder2_file)
        self.assertFalse(folder2_file.is_folder)
        self.assertTrue(folder2_file.path.strip(
            '/').endswith(folder2_file.name))
        self.assertEqual(folder2_file.size, len(folder2_file.path.strip('/')))
        folder3 = next(x for x in files if x.name == 'Folder3')
        self.assertIsNotNone(folder3)
        self.assertTrue(folder3.is_folder)
        self.assertTrue(folder3.path.strip('/').endswith(folder3.name))

        files = self.imaging_api.get_files_list(
            requests.GetFilesListRequest(
                self.original_data_folder +
                '/' +
                folder2.name +
                '/' +
                folder3.name,
                self.test_storage)).value
        self.assertEqual(1, len(files))
        folder3_file = next(x for x in files if x.name == 'Folder3.txt')
        self.assertIsNotNone(folder3_file)
        self.assertFalse(folder3_file.is_folder)
        self.assertTrue(folder3_file.path.strip(
            '/').endswith(folder3_file.name))
        self.assertEqual(folder3_file.size, len(folder3_file.path.strip('/')))
