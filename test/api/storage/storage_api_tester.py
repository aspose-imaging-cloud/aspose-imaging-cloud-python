from test.api import ImagingApiTester


#
# Storage API tester
#
class StorageApiTester(ImagingApiTester):

    def setUp(self):
        super(StorageApiTester, self).setUp()
        self.original_data_folder += '/Storage'
        self.cloud_test_folder_prefix = 'ImagingStorageCloudTestDotNet'
