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

import six

import asposeimagingcloud.models.requests as requests
from asposeimagingcloud.rest import ApiException
from test.api.storage.storage_api_tester import StorageApiTester

if six.PY2:
    import unittest2 as unittest
else:
    import unittest


class TestStorageApi(StorageApiTester):
    """ Specific Storage API tests """

    @unittest.skip('IMAGINGCLOUD-292')
    def test_get_disc_usage(self):
        try:
            disk_usage = self.imaging_api.get_disc_usage(
                requests.GetDiscUsageRequest(self.test_storage))
            self.assertLess(disk_usage.used_size, disk_usage.total_size)
        except ApiException as ex:
            self.assertEqual(501, ex.status)

    def test_storage_exists(self):
        storage_exists = self.imaging_api.storage_exists(
            requests.StorageExistsRequest(self.test_storage))
        self.assertTrue(storage_exists.exists)

    def test_storage_does_not_exist(self):
        storage_exists = self.imaging_api.storage_exists(
            requests.StorageExistsRequest('NonExistingStorage'))
        self.assertFalse(storage_exists.exists)
