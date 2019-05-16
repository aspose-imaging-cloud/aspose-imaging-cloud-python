from test.api import ImagingApiTester


#
# Class for testing PsdApi
#
class TestPsdApi(ImagingApiTester):

    #
    # Test get_image_psd
    #
    def test_get_image_psd(self):
        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.psd'
                channels_count = 3
                compression_method = 'raw'
                out_name = name + '_specific.psd'
                folder = self.temp_folder
                storage = self.test_storage

                def request_invoker(file_name, out_path):
                    kwargs = {"channels_count": channels_count, "compression_method": compression_method,
                              "folder": folder, "storage": storage}
                    if out_path:
                        kwargs["out_path"] = out_path

                    return self.imaging_api.get_image_psd(name, **kwargs)

                def properties_tester(original_properties, result_properties, result_stream):
                    self.assertIsNotNone(result_properties.psd_properties)
                    self.assertEqual(compression_method, result_properties.psd_properties.compression.lower())
                    self.assertEqual(channels_count, result_properties.psd_properties.channels_count)

                    self.assertIsNotNone(original_properties.psd_properties)
                    self.assertEqual(original_properties.width, result_properties.width)
                    self.assertEqual(original_properties.height, result_properties.height)
                    self.assertEqual(original_properties.psd_properties.bits_per_channel,
                                     result_properties.psd_properties.bits_per_channel)

                self.get_request_tester('GetImagePsdTest', save_result_to_storage,
                                        'Input image: {0}; Channel count: {1}, Compression method: '
                                        '{2}'.format(name, channels_count, compression_method),
                                        name, out_name, request_invoker, properties_tester, folder, storage)

    #
    # Test post_image_psd
    #
    def test_post_image_psd(self):
        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.psd'
                channels_count = 3
                compression_method = 'raw'
                out_name = name + '_specific.psd'
                folder = self.temp_folder
                storage = self.test_storage

                def request_invoker(input_stream, out_path):
                    kwargs = {"channels_count": channels_count, "compression_method": compression_method,
                              "storage": storage}
                    if out_path:
                        kwargs["out_path"] = out_path

                    return self.imaging_api.post_image_psd(input_stream, **kwargs)

                def properties_tester(original_properties, result_properties, result_stream):
                    self.assertIsNotNone(result_properties.psd_properties)
                    self.assertEqual(compression_method, result_properties.psd_properties.compression.lower())
                    self.assertEqual(channels_count, result_properties.psd_properties.channels_count)

                    self.assertIsNotNone(original_properties.psd_properties)
                    self.assertEqual(original_properties.width, result_properties.width)
                    self.assertEqual(original_properties.height, result_properties.height)
                    self.assertEqual(original_properties.psd_properties.bits_per_channel,
                                     result_properties.psd_properties.bits_per_channel)

                self.post_request_tester('PostImagePsdTest', save_result_to_storage,
                                         'Input image: {0}; Channel count: {1}, Compression method: '
                                         '{2}'.format(name, channels_count, compression_method),
                                         name, out_name, request_invoker, properties_tester, folder, storage)