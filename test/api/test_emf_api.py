from test.api import ImagingApiTester


#
# Class for testing EmfAPI
#
class TestEmfApi(ImagingApiTester):

    #
    # Test get_image_emf
    #
    def test_get_image_emf(self):
        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.emf'
                bk_color = 'gray'
                page_width = 300
                page_height = 300
                border_x = 50
                border_y = 50
                out_name = name + '_specific.bmp'
                folder = self.temp_folder
                storage = self.test_storage

                def request_invoker(file_name, out_path):
                    kwargs = ({"out_path": out_path, "folder": folder, "storage": storage}) if out_path else (
                        {"folder": folder, "storage": storage})

                    return self.imaging_api.get_image_emf(name, bk_color, page_width, page_height, border_x, border_y,
                                                          **kwargs)

                def properties_tester(original_properties, result_properties, result_stream):
                    width = page_width + border_x * 2
                    height = page_height + border_y * 2

                    self.assertIsNotNone(result_properties.png_properties)
                    self.assertEqual(width, result_properties.width)
                    self.assertEqual(height, result_properties.height)

                self.get_request_tester('GetImageEmfTest', save_result_to_storage,
                                        'Input image: {0}; BackColor: {1}; Page width: {2}; Page height: {3}; '
                                        'BorderX: {4}; BorderY: {5}'.format(name, bk_color, page_width, page_height,
                                                                            border_x, border_y),
                                        name, out_name, request_invoker, properties_tester, folder, storage)

    #
    # Test post_image_emf
    #
    def test_post_image_emf(self):
        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.emf'
                bk_color = 'gray'
                page_width = 300
                page_height = 300
                border_x = 50
                border_y = 50
                out_name = name + '_specific.bmp'
                folder = self.temp_folder
                storage = self.test_storage

                def request_invoker(input_stream, out_path):
                    kwargs = ({"out_path": out_path, "storage": storage}) if out_path else ({"storage": storage})

                    return self.imaging_api.post_image_emf(input_stream, bk_color, page_width, page_height, border_x,
                                                           border_y, **kwargs)

                def properties_tester(original_properties, result_properties, result_stream):
                    width = page_width + border_x * 2
                    height = page_height + border_y * 2

                    self.assertIsNotNone(result_properties.png_properties)
                    self.assertEqual(width, result_properties.width)
                    self.assertEqual(height, result_properties.height)

                self.post_request_tester('PostImageEmfTest', save_result_to_storage,
                                         'Input image: {0}; BackColor: {1}; Page width: {2}; Page height: {3}; '
                                         'BorderX: {4}; BorderY: {5}'.format(name, bk_color, page_width, page_height,
                                                                             border_x, border_y),
                                         name, out_name, request_invoker, properties_tester, folder, storage)
