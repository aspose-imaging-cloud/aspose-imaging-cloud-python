from test.api_tester import ApiTester
from test.api import ImagingApiTester
import asposeimagingcloud.models.requests as requests


class TestJpgApi(ImagingApiTester):
    """ Class for testing JpgAPI """

    def test_get_image_jpg(self):
        """ Test get_image_jpg """

        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.jpg'
                quality = 65
                compression_type = 'progressive'
                out_name = name + '_specific.jpg'
                folder = ApiTester.temp_folder
                storage = ApiTester.test_storage
                from_scratch = None

            def request_invoker(file_name, out_path):
                return ApiTester.imaging_api.get_image_jpg(
                    requests.GetImageJpgRequest(
                        name,
                        quality,
                        compression_type,
                        from_scratch,
                        out_path,
                        folder,
                        storage))

            def properties_tester(
                    original_properties,
                    result_properties,
                    result_stream):
                self.assertIsNotNone(result_properties.jpeg_properties)

                self.assertIsNotNone(original_properties.jpeg_properties)
                self.assertEqual(
                    original_properties.width,
                    result_properties.width)
                self.assertEqual(
                    original_properties.height,
                    result_properties.height)

            self.get_request_tester(
                'GetImageJpgTest',
                save_result_to_storage,
                'Input image: {0}; Quality: {1}; Compression type: {2}'.format(
                    name,
                    quality,
                    compression_type),
                name,
                out_name,
                request_invoker,
                properties_tester,
                folder,
                storage)

    def test_post_image_jpg(self):
        """ Test post_image_jpg """

        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.jpg'
                quality = 65
                compression_type = 'progressive'
                out_name = name + '_specific.jpg'
                folder = ApiTester.temp_folder
                storage = ApiTester.test_storage
                from_scratch = None

            def request_invoker(input_stream, out_path):
                return ApiTester.imaging_api.post_image_jpg(requests.PostImageJpgRequest(
                    input_stream, quality, compression_type, from_scratch, out_path, storage))

            def properties_tester(
                    original_properties,
                    result_properties,
                    result_stream):
                self.assertIsNotNone(result_properties.jpeg_properties)

                self.assertIsNotNone(original_properties.jpeg_properties)
                self.assertEqual(
                    original_properties.width,
                    result_properties.width)
                self.assertEqual(
                    original_properties.height,
                    result_properties.height)

            self.post_request_tester(
                'PostImageJpgTest',
                save_result_to_storage,
                'Input image: {0}; Quality: {1}; Compression type: {2}'.format(
                    name,
                    quality,
                    compression_type),
                name,
                out_name,
                request_invoker,
                properties_tester,
                folder,
                storage)
