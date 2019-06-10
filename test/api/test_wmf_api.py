from test.api import ImagingApiTester
import asposeimagingcloud.models.requests as requests


#
# Class for testing WmfApi
#
class TestWmfApi(ImagingApiTester):

    #
    # Test get_image_wmf
    #
    def test_get_image_wmf(self):
        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.wmf'
                bk_color = 'gray'
                page_width = 300
                page_height = 300
                border_x = 50
                border_y = 50
                out_name = name + '_specific.png'
                folder = self.temp_folder
                storage = self.test_storage
                from_scratch = None

                def request_invoker(file_name, out_path):
                    return self.imaging_api.get_image_wmf(
                        requests.GetImageWmfRequest(
                            name,
                            bk_color,
                            page_width,
                            page_height,
                            border_x,
                            border_y,
                            from_scratch,
                            out_path,
                            folder,
                            storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertIsNotNone(result_properties.png_properties)
                    self.assertEqual(
                        page_width + border_x * 2,
                        result_properties.width)
                    self.assertEqual(
                        page_height + border_y * 2,
                        result_properties.height)

                self.get_request_tester(
                    'GetImageWmfTest',
                    save_result_to_storage,
                    'Input image: {0}; BackColor: {1}; Page width: {2}; Page height: {3}; '
                    'BorderX: {4}; BorderY: {5}'.format(
                        name,
                        bk_color,
                        page_width,
                        page_height,
                        border_x,
                        border_y),
                    name,
                    out_name,
                    request_invoker,
                    properties_tester,
                    folder,
                    storage)

    #
    # Test post_image_wmf
    #
    def test_post_image_wmf(self):
        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.wmf'
                bk_color = 'gray'
                page_width = 300
                page_height = 300
                border_x = 50
                border_y = 50
                out_name = name + '_specific.png'
                folder = self.temp_folder
                storage = self.test_storage
                from_scratch = None

                def request_invoker(input_stream, out_path):
                    return self.imaging_api.post_image_wmf(
                        requests.PostImageWmfRequest(
                            input_stream,
                            bk_color,
                            page_width,
                            page_height,
                            border_x,
                            border_y,
                            from_scratch,
                            out_path,
                            storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertIsNotNone(result_properties.png_properties)
                    self.assertEqual(
                        page_width + border_x * 2,
                        result_properties.width)
                    self.assertEqual(
                        page_height + border_y * 2,
                        result_properties.height)

                self.post_request_tester(
                    'PostImageWmfTest',
                    save_result_to_storage,
                    'Input image: {0}; BackColor: {1}; Page width: {2}; Page height: {3}; '
                    'BorderX: {4}; BorderY: {5}'.format(
                        name,
                        bk_color,
                        page_width,
                        page_height,
                        border_x,
                        border_y),
                    name,
                    out_name,
                    request_invoker,
                    properties_tester,
                    folder,
                    storage)
