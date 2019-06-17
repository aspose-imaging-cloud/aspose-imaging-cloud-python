from test.api_tester import ApiTester
from test.api import ImagingApiTester


#
# Storage API tester
#
class StorageApiTester(ImagingApiTester):

    def setUp(self):
        super(StorageApiTester, self).setUp()
        ApiTester.original_data_folder += '/Storage'
        ApiTester.cloud_test_folder_prefix = 'ImagingStorageCloudTestPython'
