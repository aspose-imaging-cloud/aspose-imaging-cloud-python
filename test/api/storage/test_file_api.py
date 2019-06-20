#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="delete_file_request.py">
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

import asposeimagingcloud.models.requests as requests
from test.api.storage.storage_api_tester import StorageApiTester


class TestFileApi(StorageApiTester):
    """ Specific file API tests for Storage """

    def test_copy_download_file(self):
        folder = self.temp_folder + '/Storage'
        file = 'Storage.txt'

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

            self.imaging_api.copy_file(
                requests.CopyFileRequest(
                    self.original_data_folder + '/' + file,
                    folder + '/' + file,
                    self.test_storage,
                    self.test_storage))
            exists_response = self.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder + '/' + file, self.test_storage))
            self.assertIsNotNone(exists_response)
            self.assertFalse(exists_response.is_folder)
            self.assertTrue(exists_response.exists)

            original_file_info = next(
                x for x in self.imaging_api.get_files_list(
                    requests.GetFilesListRequest(
                        self.original_data_folder,
                        self.test_storage)).value if x.name == file)

            copied_file_info = next(
                x for x in self.imaging_api.get_files_list(
                    requests.GetFilesListRequest(
                        folder, self.test_storage)).value if x.name == file)

            self.assertEqual(original_file_info.size, copied_file_info.size)

            original_file = self.imaging_api.download_file(
                requests.DownloadFileRequest(
                    self.original_data_folder + '/' + file,
                    self.test_storage))
            copied_file = self.imaging_api.download_file(
                requests.DownloadFileRequest(
                    folder + '/' + file, self.test_storage))

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
                        self.original_data_folder,
                        folder),
                    copied_file_info.path.strip('/'))

        finally:
            self.imaging_api.delete_file(
                requests.DeleteFileRequest(
                    folder + '/' + file,
                    self.test_storage))
            self.assertFalse(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder + '/' + file,
                        self.test_storage)).exists)

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

    def test_file_versions_copy(self):
        folder = self.temp_folder + '/Storage'
        file1 = 'Storage.txt'
        file2 = 'Folder1/Folder1.txt'

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

            self.imaging_api.copy_file(
                requests.CopyFileRequest(
                    self.original_data_folder + '/' + file1,
                    folder + '/' + file1,
                    self.test_storage,
                    self.test_storage))
            self.imaging_api.copy_file(
                requests.CopyFileRequest(
                    self.original_data_folder + '/' + file2,
                    folder + '/' + file1,
                    self.test_storage,
                    self.test_storage))
            versions = self.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(
                    folder + '/' + file1, self.test_storage)).value
            recent_version = next(x for x in versions if x.is_latest is True)
            old_version = next(x for x in versions if x.is_latest is not True)

            self.imaging_api.copy_file(
                requests.CopyFileRequest(
                    folder + '/' + file1,
                    folder + '/' + file1 + '.recent',
                    self.test_storage,
                    self.test_storage,
                    recent_version.version_id))
            copied_versions = self.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(
                    folder + '/' + file1 + '.recent',
                    self.test_storage)).value

            self.assertEqual(1, len(copied_versions))
            self.assertTrue(copied_versions[0].is_latest)
            self.assertEqual(recent_version.size, copied_versions[0].size)

            self.imaging_api.copy_file(
                requests.CopyFileRequest(
                    folder + '/' + file1,
                    folder + '/' + file1 + '.old',
                    self.test_storage,
                    self.test_storage,
                    old_version.version_id))
            copied_versions = self.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(
                    folder + '/' + file1 + '.old',
                    self.test_storage)).value

            self.assertEqual(1, len(copied_versions))
            self.assertTrue(copied_versions[0].is_latest)
            self.assertEqual(old_version.size, copied_versions[0].size)

        finally:
            if self.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, self.test_storage)).exists:
                self.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, self.test_storage, True))

    def test_file_version_create(self):
        folder = self.temp_folder + '/Storage'
        file1 = 'Storage.txt'
        file2 = 'Folder1/Folder1.txt'

        file1_size = next(
            x for x in self.imaging_api.get_files_list(
                requests.GetFilesListRequest(
                    self.original_data_folder,
                    self.test_storage)).value if x.name == file1).size

        file2_size = next(
            x for x in self.imaging_api.get_files_list(
                requests.GetFilesListRequest(
                    self.original_data_folder + '/Folder1',
                    self.test_storage)).value if x.name == 'Folder1.txt').size

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

            self.imaging_api.copy_file(
                requests.CopyFileRequest(
                    self.original_data_folder + '/' + file1,
                    folder + '/' + file1,
                    self.test_storage,
                    self.test_storage))
            self.imaging_api.copy_file(
                requests.CopyFileRequest(
                    self.original_data_folder + '/' + file2,
                    folder + '/' + file1,
                    self.test_storage,
                    self.test_storage))
            versions = self.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(
                    folder + '/' + file1, self.test_storage)).value

            self.assertEqual(2, len(versions))
            recent_version_size = next(
                x for x in versions if x.is_latest is True).size
            old_version_size = next(
                x for x in versions if x.is_latest is not True).size
            self.assertNotEqual(recent_version_size, old_version_size)
            self.assertEqual(old_version_size, file1_size)
            self.assertEqual(recent_version_size, file2_size)

        finally:
            if self.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, self.test_storage)).exists:
                self.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, self.test_storage, True))

    def test_file_version_delete(self):
        folder = self.temp_folder + '/Storage'
        file1 = 'Storage.txt'
        file2 = 'Folder1/Folder1.txt'

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

            self.imaging_api.copy_file(
                requests.CopyFileRequest(
                    self.original_data_folder + '/' + file1,
                    folder + '/' + file1,
                    self.test_storage,
                    self.test_storage))
            self.imaging_api.copy_file(
                requests.CopyFileRequest(
                    self.original_data_folder + '/' + file2,
                    folder + '/' + file1,
                    self.test_storage,
                    self.test_storage))
            versions = self.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(
                    folder + '/' + file1, self.test_storage)).value
            recent_version = next(x for x in versions if x.is_latest is True)
            old_version = next(x for x in versions if x.is_latest is not True)

            self.assertTrue(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder + '/' + file1,
                        self.test_storage,
                        recent_version.version_id)).exists)
            self.assertTrue(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder + '/' + file1,
                        self.test_storage,
                        old_version.version_id)).exists)

            self.imaging_api.delete_file(
                requests.DeleteFileRequest(
                    folder + '/' + file1,
                    self.test_storage,
                    recent_version.version_id))

            versions = self.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(
                    folder + '/' + file1, self.test_storage)).value
            self.assertFalse(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder + '/' + file1,
                        self.test_storage,
                        recent_version.version_id)).exists)
            self.assertTrue(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder + '/' + file1,
                        self.test_storage,
                        old_version.version_id)).exists)
            self.assertEqual(1, len(versions))
            self.assertEqual(old_version.size, versions[0].size)

            self.imaging_api.delete_file(
                requests.DeleteFileRequest(
                    folder + '/' + file1,
                    self.test_storage,
                    old_version.version_id))
            self.assertFalse(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder + '/' + file1,
                        self.test_storage)).exists)

        finally:
            if self.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, self.test_storage)).exists:
                self.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, self.test_storage, True))

    def test_file_version_download(self):
        folder = self.temp_folder + '/Storage'
        file1 = 'Storage.txt'
        file2 = 'Folder1/Folder1.txt'

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

            self.imaging_api.copy_file(
                requests.CopyFileRequest(
                    self.original_data_folder + '/' + file1,
                    folder + '/' + file1,
                    self.test_storage,
                    self.test_storage))
            self.imaging_api.copy_file(
                requests.CopyFileRequest(
                    self.original_data_folder + '/' + file2,
                    folder + '/' + file1,
                    self.test_storage,
                    self.test_storage))
            versions = self.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(
                    folder + '/' + file1, self.test_storage)).value
            recent_version = next(x for x in versions if x.is_latest is True)
            old_version = next(x for x in versions if x.is_latest is not True)

            with open(self.imaging_api.download_file(
                    requests.DownloadFileRequest(folder + '/' + file1, self.test_storage,
                                                 old_version.version_id)), 'r') as old_file:
                self.assertEqual(old_version.size, len(old_file.read()))

            with open(self.imaging_api.download_file(
                    requests.DownloadFileRequest(folder + '/' + file1, self.test_storage,
                                                 recent_version.version_id)), 'r') as old_file:
                self.assertEqual(recent_version.size, len(old_file.read()))

        finally:
            if self.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, self.test_storage)).exists:
                self.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, self.test_storage, True))

    def test_file_version_move(self):
        folder = self.temp_folder + '/Storage'
        file1 = 'Storage.txt'
        file2 = 'Folder1/Folder1.txt'

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

            self.imaging_api.copy_file(
                requests.CopyFileRequest(
                    self.original_data_folder + '/' + file1,
                    folder + '/' + file1,
                    self.test_storage,
                    self.test_storage))
            self.imaging_api.copy_file(
                requests.CopyFileRequest(
                    self.original_data_folder + '/' + file2,
                    folder + '/' + file1,
                    self.test_storage,
                    self.test_storage))
            versions = self.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(
                    folder + '/' + file1, self.test_storage)).value
            recent_version = next(x for x in versions if x.is_latest is True)

            self.imaging_api.move_file(
                requests.MoveFileRequest(
                    folder + '/' + file1,
                    folder + '/' + file1 + '.recent',
                    self.test_storage,
                    self.test_storage,
                    recent_version.version_id))
            copied_versions = self.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(
                    folder + '/' + file1 + '.recent',
                    self.test_storage)).value
            self.assertEqual(1, len(copied_versions))
            self.assertTrue(copied_versions[0].is_latest)
            self.assertEqual(recent_version.size, copied_versions[0].size)

            self.imaging_api.copy_file(
                requests.CopyFileRequest(
                    self.original_data_folder + '/' + file1,
                    folder + '/' + file1,
                    self.test_storage,
                    self.test_storage))
            self.imaging_api.copy_file(
                requests.CopyFileRequest(
                    self.original_data_folder + '/' + file2,
                    folder + '/' + file1,
                    self.test_storage,
                    self.test_storage))
            versions = self.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(
                    folder + '/' + file1, self.test_storage)).value
            old_version = next(x for x in versions if x.is_latest is not True)

            self.imaging_api.move_file(
                requests.MoveFileRequest(
                    folder + '/' + file1,
                    folder + '/' + file1 + '.old',
                    self.test_storage,
                    self.test_storage,
                    old_version.version_id))
            copied_versions = self.imaging_api.get_file_versions(
                requests.GetFileVersionsRequest(folder + '/' + file1 + '.old',
                                                self.test_storage)).value
            self.assertEqual(1, len(copied_versions))
            self.assertTrue(copied_versions[0].is_latest)
            self.assertEqual(old_version.size, copied_versions[0].size)

        finally:
            if self.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder, self.test_storage)).exists:
                self.imaging_api.delete_folder(
                    requests.DeleteFolderRequest(
                        folder, self.test_storage, True))

    def test_move_file(self):
        folder = self.temp_folder + '/Storage'
        file = 'Storage.txt'

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

            self.imaging_api.copy_file(
                requests.CopyFileRequest(
                    self.original_data_folder + '/' + file,
                    folder + '/' + file + '.copied',
                    self.test_storage,
                    self.test_storage))
            exist_response = self.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder + '/' + file + '.copied',
                    self.test_storage))
            self.assertIsNotNone(exist_response)
            self.assertFalse(exist_response.is_folder)
            self.assertTrue(exist_response.exists)

            self.imaging_api.move_file(
                requests.MoveFileRequest(
                    folder + '/' + file + '.copied',
                    folder + '/' + file,
                    self.test_storage,
                    self.test_storage))
            self.assertFalse(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder + '/' + file + '.copied',
                        self.test_storage)).exists)
            exist_response = self.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder + '/' + file, self.test_storage))
            self.assertIsNotNone(exist_response)
            self.assertFalse(exist_response.is_folder)
            self.assertTrue(exist_response.exists)

            original_file_info = next(
                x for x in self.imaging_api.get_files_list(
                    requests.GetFilesListRequest(
                        self.original_data_folder,
                        self.test_storage)).value if x.name == file)
            moved_file_info = next(
                x for x in self.imaging_api.get_files_list(
                    requests.GetFilesListRequest(
                        folder, self.test_storage)).value if x.name == file)
            self.assertEqual(original_file_info.size, moved_file_info.size)

            with open(self.imaging_api.download_file(
                    requests.DownloadFileRequest(self.original_data_folder + '/' + file,
                                                 self.test_storage)), 'r') as original_file, \
                    open(self.imaging_api.download_file(requests.DownloadFileRequest(folder + '/' + file,
                                                                                     self.test_storage)),
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
                        self.original_data_folder,
                        folder),
                    moved_file_info.path.strip('/'))

        finally:
            self.imaging_api.delete_file(
                requests.DeleteFileRequest(
                    folder + '/' + file,
                    self.test_storage))
            self.assertFalse(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder + '/' + file,
                        self.test_storage)).exists)

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

    def test_upload_file(self):
        folder = self.temp_folder + '/Storage'
        file = 'Storage.txt'

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

            original_file = self.imaging_api.download_file(
                requests.DownloadFileRequest(
                    self.original_data_folder + '/' + file,
                    self.test_storage))

            result = self.imaging_api.upload_file(
                requests.UploadFileRequest(
                    folder + '/' + file,
                    original_file,
                    self.test_storage))
            self.assertIsNotNone(result)
            self.assertTrue(not result.errors or len(result) == 0)
            self.assertIsNotNone(result.uploaded)
            self.assertEqual(1, len(result.uploaded))
            self.assertEqual(file, result.uploaded[0])

            exist_response = self.imaging_api.object_exists(
                requests.ObjectExistsRequest(
                    folder + '/' + file, self.test_storage))
            self.assertIsNotNone(exist_response)
            self.assertFalse(exist_response.is_folder)
            self.assertTrue(exist_response.exists)

            original_file_info = next(
                x for x in self.imaging_api.get_files_list(
                    requests.GetFilesListRequest(
                        self.original_data_folder,
                        self.test_storage)).value if x.name == file)

            uploaded_file_info = next(
                x for x in self.imaging_api.get_files_list(
                    requests.GetFilesListRequest(
                        folder, self.test_storage)).value if x.name == file)
            self.assertEqual(original_file_info.size, uploaded_file_info.size)

            original_file = self.imaging_api.download_file(
                requests.DownloadFileRequest(
                    self.original_data_folder + '/' + file,
                    self.test_storage))

            uploaded_file = self.imaging_api.download_file(
                requests.DownloadFileRequest(
                    folder + '/' + file, self.test_storage))

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
                        self.original_data_folder,
                        folder),
                    uploaded_file_info.path.strip('/'))

        finally:
            self.imaging_api.delete_file(
                requests.DeleteFileRequest(
                    folder + '/' + file,
                    self.test_storage))
            self.assertFalse(
                self.imaging_api.object_exists(
                    requests.ObjectExistsRequest(
                        folder + '/' + file,
                        self.test_storage)).exists)

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
