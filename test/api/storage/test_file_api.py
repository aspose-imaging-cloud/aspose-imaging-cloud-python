from test.api.storage.storage_api_tester import StorageApiTester


#
# Specific file API tests for Storage
#
class TestFileApi(StorageApiTester):

    def test_copy_download_file(self):
        folder = self.temp_folder + '/Storage'
        file = 'Storage.txt'

        try:
            if self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists:
                self.imaging_api.delete_folder(folder, storage_name=self.test_storage, recursive=True)

            self.assertFalse(self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists)

            self.imaging_api.copy_file(self.original_data_folder + '/' + file, folder + '/' + file,
                                       src_storage_name=self.test_storage, dest_storage_name=self.test_storage)
            exists_response = self.imaging_api.object_exists(folder + '/' + file, storage_name=self.test_storage)
            self.assertIsNotNone(exists_response)
            self.assertFalse(exists_response.is_folder)
            self.assertTrue(exists_response.exists)

            original_file_info = next(x for x in self.imaging_api.get_files_list(
                self.original_data_folder, storage_name=self.test_storage).value if x.name == file)

            copied_file_info = next(x for x in self.imaging_api.get_files_list(
                folder, storage_name=self.test_storage).value if x.name == file)

            self.assertEqual(original_file_info.size, copied_file_info.size)

            original_file = self.imaging_api.download_file(self.original_data_folder + '/' + file,
                                                           storage_name=self.test_storage)
            copied_file = self.imaging_api.download_file(folder + '/' + file, storage_name=self.test_storage)

            with open(original_file, 'r') as original_reader, open(copied_file, 'r') as copied_reader:
                original_string = original_reader.read()
                copied_string = copied_reader.read()
                self.assertEqual(len(original_string), len(copied_string))
                self.assertEqual(len(original_string), original_file_info.size)
                self.assertEqual(original_string, copied_string)
                self.assertEqual(original_string, original_file_info.path.strip('/'))
                self.assertEqual(original_string.replace(self.original_data_folder, folder),
                                 copied_file_info.path.strip('/'))

        finally:
            self.imaging_api.delete_file(folder + '/' + file, storage_name=self.test_storage)
            self.assertFalse(
                self.imaging_api.object_exists(folder + '/' + file, storage_name=self.test_storage).exists)

            if self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists:
                self.imaging_api.delete_folder(folder, storage_name=self.test_storage, recursive=True)

            self.assertFalse(self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists)

    def test_file_versions_copy(self):
        folder = self.temp_folder + '/Storage'
        file1 = 'Storage.txt'
        file2 = 'Folder1/Folder1.txt'

        try:
            if self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists:
                self.imaging_api.delete_folder(folder, storage_name=self.test_storage, recursive=True)

            self.assertFalse(self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists)

            self.imaging_api.copy_file(self.original_data_folder + '/' + file1, folder + '/' + file1,
                                       src_storage_name=self.test_storage, dest_storage_name=self.test_storage)
            self.imaging_api.copy_file(self.original_data_folder + '/' + file2, folder + '/' + file1,
                                       src_storage_name=self.test_storage, dest_storage_name=self.test_storage)
            versions = self.imaging_api.get_file_versions(folder + '/' + file1, storage_name=self.test_storage).value
            recent_version = next(x for x in versions if x.is_latest is True)
            old_version = next(x for x in versions if x.is_latest is not True)

            self.imaging_api.copy_file(folder + '/' + file1, folder + '/' + file1 + '.recent',
                                       src_storage_name=self.test_storage, dest_storage_name=self.test_storage,
                                       version_id=recent_version.version_id)
            copied_versions = self.imaging_api.get_file_versions(folder + '/' + file1 + '.recent',
                                                                 storage_name=self.test_storage).value

            self.assertEqual(1, len(copied_versions))
            self.assertTrue(copied_versions[0].is_latest)
            self.assertEqual(recent_version.size, copied_versions[0].size)

            self.imaging_api.copy_file(folder + '/' + file1, folder + '/' + file1 + '.old',
                                       src_storage_name=self.test_storage, dest_storage_name=self.test_storage,
                                       version_id=old_version.version_id)
            copied_versions = self.imaging_api.get_file_versions(folder + '/' + file1 + '.old',
                                                                 storage_name=self.test_storage).value

            self.assertEqual(1, len(copied_versions))
            self.assertTrue(copied_versions[0].is_latest)
            self.assertEqual(old_version.size, copied_versions[0].size)

        finally:
            if self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists:
                self.imaging_api.delete_folder(folder, storage_name=self.test_storage, recursive=True)

    def test_file_version_create(self):
        folder = self.temp_folder + '/Storage'
        file1 = 'Storage.txt'
        file2 = 'Folder1/Folder1.txt'

        file1_size = next(x for x in self.imaging_api.get_files_list(
            self.original_data_folder, storage_name=self.test_storage).value if x.name == file1).size

        file2_size = next(x for x in self.imaging_api.get_files_list(
            self.original_data_folder + '/Folder1', storage_name=self.test_storage).value if
                          x.name == 'Folder1.txt').size

        try:
            if self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists:
                self.imaging_api.delete_folder(folder, storage_name=self.test_storage, recursive=True)

            self.assertFalse(self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists)

            self.imaging_api.copy_file(self.original_data_folder + '/' + file1, folder + '/' + file1,
                                       src_storage_name=self.test_storage, dest_storage_name=self.test_storage)
            self.imaging_api.copy_file(self.original_data_folder + '/' + file2, folder + '/' + file1,
                                       src_storage_name=self.test_storage, dest_storage_name=self.test_storage)
            versions = self.imaging_api.get_file_versions(folder + '/' + file1, storage_name=self.test_storage).value

            self.assertEqual(2, len(versions))
            recent_version_size = next(x for x in versions if x.is_latest is True).size
            old_version_size = next(x for x in versions if x.is_latest is not True).size
            self.assertNotEqual(recent_version_size, old_version_size)
            self.assertEqual(old_version_size, file1_size)
            self.assertEqual(recent_version_size, file2_size)

        finally:
            if self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists:
                self.imaging_api.delete_folder(folder, storage_name=self.test_storage, recursive=True)

    def test_file_version_delete(self):
        folder = self.temp_folder + '/Storage'
        file1 = 'Storage.txt'
        file2 = 'Folder1/Folder1.txt'

        try:
            if self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists:
                self.imaging_api.delete_folder(folder, storage_name=self.test_storage, recursive=True)

            self.assertFalse(self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists)

            self.imaging_api.copy_file(self.original_data_folder + '/' + file1, folder + '/' + file1,
                                       src_storage_name=self.test_storage, dest_storage_name=self.test_storage)
            self.imaging_api.copy_file(self.original_data_folder + '/' + file2, folder + '/' + file1,
                                       src_storage_name=self.test_storage, dest_storage_name=self.test_storage)
            versions = self.imaging_api.get_file_versions(folder + '/' + file1, storage_name=self.test_storage).value
            recent_version = next(x for x in versions if x.is_latest is True)
            old_version = next(x for x in versions if x.is_latest is not True)

            self.assertTrue(self.imaging_api.object_exists(folder + '/' + file1, storage_name=self.test_storage,
                                                           version_id=recent_version.version_id).exists)
            self.assertTrue(self.imaging_api.object_exists(folder + '/' + file1, storage_name=self.test_storage,
                                                           version_id=old_version.version_id).exists)

            self.imaging_api.delete_file(folder + '/' + file1, storage_name=self.test_storage,
                                         version_id=recent_version.version_id)

            versions = self.imaging_api.get_file_versions(folder + '/' + file1, storage_name=self.test_storage).value
            self.assertFalse(self.imaging_api.object_exists(folder + '/' + file1, storage_name=self.test_storage,
                                                            version_id=recent_version.version_id).exists)
            self.assertTrue(self.imaging_api.object_exists(folder + '/' + file1, storage_name=self.test_storage,
                                                           version_id=old_version.version_id).exists)
            self.assertEqual(1, len(versions))
            self.assertEqual(old_version.size, versions[0].size)

            self.imaging_api.delete_file(folder + '/' + file1, storage_name=self.test_storage,
                                         version_id=old_version.version_id)
            self.assertFalse(self.imaging_api.object_exists(folder + '/' + file1,
                                                            storage_name=self.test_storage).exists)

        finally:
            if self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists:
                self.imaging_api.delete_folder(folder, storage_name=self.test_storage, recursive=True)

    def test_file_version_download(self):
        folder = self.temp_folder + '/Storage'
        file1 = 'Storage.txt'
        file2 = 'Folder1/Folder1.txt'

        try:
            if self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists:
                self.imaging_api.delete_folder(folder, storage_name=self.test_storage, recursive=True)

            self.assertFalse(self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists)

            self.imaging_api.copy_file(self.original_data_folder + '/' + file1, folder + '/' + file1,
                                       src_storage_name=self.test_storage, dest_storage_name=self.test_storage)
            self.imaging_api.copy_file(self.original_data_folder + '/' + file2, folder + '/' + file1,
                                       src_storage_name=self.test_storage, dest_storage_name=self.test_storage)
            versions = self.imaging_api.get_file_versions(folder + '/' + file1, storage_name=self.test_storage).value
            recent_version = next(x for x in versions if x.is_latest is True)
            old_version = next(x for x in versions if x.is_latest is not True)

            with open(self.imaging_api.download_file(folder + '/' + file1, storage_name=self.test_storage,
                                                     version_id=old_version.version_id), 'r') as old_file:
                self.assertEqual(old_version.size, len(old_file.read()))

            with open(self.imaging_api.download_file(folder + '/' + file1, storage_name=self.test_storage,
                                                     version_id=recent_version.version_id), 'r') as old_file:
                self.assertEqual(recent_version.size, len(old_file.read()))

        finally:
            if self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists:
                self.imaging_api.delete_folder(folder, storage_name=self.test_storage, recursive=True)

    def test_file_version_move(self):
        folder = self.temp_folder + '/Storage'
        file1 = 'Storage.txt'
        file2 = 'Folder1/Folder1.txt'

        try:
            if self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists:
                self.imaging_api.delete_folder(folder, storage_name=self.test_storage, recursive=True)

            self.assertFalse(self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists)

            self.imaging_api.copy_file(self.original_data_folder + '/' + file1, folder + '/' + file1,
                                       src_storage_name=self.test_storage, dest_storage_name=self.test_storage)
            self.imaging_api.copy_file(self.original_data_folder + '/' + file2, folder + '/' + file1,
                                       src_storage_name=self.test_storage, dest_storage_name=self.test_storage)
            versions = self.imaging_api.get_file_versions(folder + '/' + file1, storage_name=self.test_storage).value
            recent_version = next(x for x in versions if x.is_latest is True)

            self.imaging_api.move_file(folder + '/' + file1, folder + '/' + file1 + '.recent',
                                       src_storage_name=self.test_storage, dest_storage_name=self.test_storage,
                                       version_id=recent_version.version_id)
            copied_versions = self.imaging_api.get_file_versions(folder + '/' + file1 + '.recent',
                                                                 storage_name=self.test_storage).value
            self.assertEqual(1, len(copied_versions))
            self.assertTrue(copied_versions[0].is_latest)
            self.assertEqual(recent_version.size, copied_versions[0].size)

            self.imaging_api.copy_file(self.original_data_folder + '/' + file1, folder + '/' + file1,
                                       src_storage_name=self.test_storage, dest_storage_name=self.test_storage)
            self.imaging_api.copy_file(self.original_data_folder + '/' + file2, folder + '/' + file1,
                                       src_storage_name=self.test_storage, dest_storage_name=self.test_storage)
            versions = self.imaging_api.get_file_versions(folder + '/' + file1, storage_name=self.test_storage).value
            old_version = next(x for x in versions if x.is_latest is not True)

            self.imaging_api.move_file(folder + '/' + file1, folder + '/' + file1 + '.old',
                                       src_storage_name=self.test_storage, dest_storage_name=self.test_storage,
                                       version_id=old_version.version_id)
            copied_versions = self.imaging_api.get_file_versions(folder + '/' + file1 + '.old',
                                                                 storage_name=self.test_storage).value
            self.assertEqual(1, len(copied_versions))
            self.assertTrue(copied_versions[0].is_latest)
            self.assertEqual(old_version.size, copied_versions[0].size)

        finally:
            if self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists:
                self.imaging_api.delete_folder(folder, storage_name=self.test_storage, recursive=True)

    def test_move_file(self):
        folder = self.temp_folder + '/Storage'
        file = 'Storage.txt'

        try:
            if self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists:
                self.imaging_api.delete_folder(folder, storage_name=self.test_storage, recursive=True)

            self.assertFalse(self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists)

            self.imaging_api.copy_file(self.original_data_folder + '/' + file, folder + '/' + file + '.copied',
                                       src_storage_name=self.test_storage, dest_storage_name=self.test_storage)
            exist_response = self.imaging_api.object_exists(folder + '/' + file + '.copied',
                                                            storage_name=self.test_storage)
            self.assertIsNotNone(exist_response)
            self.assertFalse(exist_response.is_folder)
            self.assertTrue(exist_response.exists)

            self.imaging_api.move_file(folder + '/' + file + '.copied', folder + '/' + file,
                                       src_storage_name=self.test_storage, dest_storage_name=self.test_storage)
            self.assertFalse(
                self.imaging_api.object_exists(folder + '/' + file + '.copied', storage_name=self.test_storage).exists)
            exist_response = self.imaging_api.object_exists(folder + '/' + file,
                                                            storage_name=self.test_storage)
            self.assertIsNotNone(exist_response)
            self.assertFalse(exist_response.is_folder)
            self.assertTrue(exist_response.exists)

            original_file_info = next(x for x in self.imaging_api.get_files_list(
                self.original_data_folder, storage_name=self.test_storage).value if x.name == file)
            moved_file_info = next(x for x in self.imaging_api.get_files_list(
                folder, storage_name=self.test_storage).value if x.name == file)
            self.assertEqual(original_file_info.size, moved_file_info.size)

            with open(self.imaging_api.download_file(self.original_data_folder + '/' + file,
                                                     storage_name=self.test_storage), 'r') as original_file, \
                    open(self.imaging_api.download_file(folder + '/' + file,
                                                        storage_name=self.test_storage), 'r') as moved_file:
                original_string = original_file.read()
                moved_string = moved_file.read()
                self.assertEqual(len(original_string), len(moved_string))
                self.assertEqual(len(original_string), original_file_info.size)
                self.assertEqual(original_string, moved_string)
                self.assertEqual(original_string, original_file_info.path.strip('/'))
                self.assertEqual(original_string.replace(self.original_data_folder, folder),
                                 moved_file_info.path.strip('/'))

        finally:
            self.imaging_api.delete_file(folder + '/' + file, storage_name=self.test_storage)
            self.assertFalse(
                self.imaging_api.object_exists(folder + '/' + file, storage_name=self.test_storage).exists)

            if self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists:
                self.imaging_api.delete_folder(folder, storage_name=self.test_storage, recursive=True)

            self.assertFalse(self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists)

    def test_upload_file(self):
        folder = self.temp_folder + '/Storage'
        file = 'Storage.txt'

        try:
            if self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists:
                self.imaging_api.delete_folder(folder, storage_name=self.test_storage, recursive=True)

            self.assertFalse(self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists)

            original_file = self.imaging_api.download_file(self.original_data_folder + '/' + file,
                                                           storage_name=self.test_storage)

            result = self.imaging_api.upload_file(folder + '/' + file, original_file, storage_name=self.test_storage)
            self.assertIsNotNone(result)
            self.assertTrue(not result.errors or len(result) == 0)
            self.assertIsNotNone(result.uploaded)
            self.assertEqual(1, len(result.uploaded))
            self.assertEqual(file, result.uploaded[0])

            exist_response = self.imaging_api.object_exists(folder + '/' + file,
                                                            storage_name=self.test_storage)
            self.assertIsNotNone(exist_response)
            self.assertFalse(exist_response.is_folder)
            self.assertTrue(exist_response.exists)

            original_file_info = next(x for x in self.imaging_api.get_files_list(
                self.original_data_folder, storage_name=self.test_storage).value if x.name == file)

            uploaded_file_info = next(x for x in self.imaging_api.get_files_list(
                folder, storage_name=self.test_storage).value if x.name == file)
            self.assertEqual(original_file_info.size, uploaded_file_info.size)

            original_file = self.imaging_api.download_file(self.original_data_folder + '/' + file,
                                                           storage_name=self.test_storage)

            uploaded_file = self.imaging_api.download_file(folder + '/' + file, storage_name=self.test_storage)

            with open(original_file, 'r') as original_reader, open(uploaded_file, 'r') as uploaded_reader:
                original_string = original_reader.read()
                copied_string = uploaded_reader.read()
                self.assertEqual(len(original_string), len(copied_string))
                self.assertEqual(len(original_string), original_file_info.size)
                self.assertEqual(original_string, copied_string)
                self.assertEqual(original_string, original_file_info.path.strip('/'))
                self.assertEqual(original_string.replace(self.original_data_folder, folder),
                                 uploaded_file_info.path.strip('/'))

        finally:
            self.imaging_api.delete_file(folder + '/' + file, storage_name=self.test_storage)
            self.assertFalse(
                self.imaging_api.object_exists(folder + '/' + file, storage_name=self.test_storage).exists)

            if self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists:
                self.imaging_api.delete_folder(folder, storage_name=self.test_storage, recursive=True)

            self.assertFalse(self.imaging_api.object_exists(folder, storage_name=self.test_storage).exists)
