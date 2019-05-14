from test.api import ImagingApiTester


#
# Class for testing JpgAPI
#
class TestJpgApi(ImagingApiTester):

    #
    # Test get_image_jpg
    #
    def test_get_image_jpg(self):
        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.jpg'
                quality = 65
                compression_type = 'progressive'
                out_name = name + '_specific.jpg'
                folder = self.temp_folder
                storage = self.test_storage

            def request_invoker(file_name, out_path):
                kwargs = {"quality": quality, "compression_type": compression_type, "folder": folder,
                          "storage": storage}
                if out_path:
                    kwargs["out_path"] = out_path

                return self.imaging_api.get_image_jpg(name, **kwargs)

            def properties_tester(original_properties, result_properties, result_stream):
                self.assertIsNotNone(result_properties.jpeg_properties)

                self.assertIsNotNone(original_properties.jpeg_properties)
                self.assertEqual(original_properties.width, result_properties.width)
                self.assertEqual(original_properties.height, result_properties.height)

            self.test_get_request('GetImageJpgTest', save_result_to_storage,
                                  'Input image: {0}; Quality: {1}; Compression type: {2}'.format(name, quality,
                                                                                                 compression_type),
                                  name, out_name, request_invoker, properties_tester, folder, storage)

    #
    # Test post_image_jpg
    #
    def test_post_image_jpg(self):
        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.jpg'
                quality = 65
                compression_type = 'progressive'
                out_name = name + '_specific.jpg'
                folder = self.temp_folder
                storage = self.test_storage

            def request_invoker(input_stream, out_path):
                kwargs = {"quality": quality, "compression_type": compression_type, "storage": storage}
                if out_path:
                    kwargs["out_path"] = out_path

                return self.imaging_api.post_image_jpg(input_stream, **kwargs)

            def properties_tester(original_properties, result_properties, result_stream):
                self.assertIsNotNone(result_properties.jpeg_properties)

                self.assertIsNotNone(original_properties.jpeg_properties)
                self.assertEqual(original_properties.width, result_properties.width)
                self.assertEqual(original_properties.height, result_properties.height)

            self.test_post_request('PostImageJpgTest', save_result_to_storage,
                                  'Input image: {0}; Quality: {1}; Compression type: {2}'.format(name, quality,
                                                                                                 compression_type),
                                  name, out_name, request_invoker, properties_tester, folder, storage)
