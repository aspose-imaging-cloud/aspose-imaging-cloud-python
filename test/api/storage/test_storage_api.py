import unittest

from asposeimagingcloud.rest import ApiException
from test.api.storage.storage_api_tester import StorageApiTester
import asposeimagingcloud.models.requests as requests


#
#  Specific Storage API tests
#
class TestStorageApi(StorageApiTester):

    @unittest.skip('IMAGINGCLOUD-292')
    def test_get_disc_usage(self):
        try:
            disk_usage = self.imaging_api.get_disc_usage(requests.GetDiscUsageRequest(self.test_storage))
            self.assertLess(disk_usage.used_size, disk_usage.total_size)
        except ApiException as ex:
            self.assertEqual(501, ex.status)

    def test_storage_exists(self):
        storage_exists = self.imaging_api.storage_exists(requests.StorageExistsRequest(self.test_storage))
        self.assertTrue(storage_exists.exists)

    def test_storage_does_not_exist(self):
        storage_exists = self.imaging_api.storage_exists(requests.StorageExistsRequest('NonExistingStorage'))
        self.assertFalse(storage_exists.exists)
