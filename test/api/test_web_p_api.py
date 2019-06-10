from test.api import ImagingApiTester
import asposeimagingcloud.models.requests as requests


#
# Class for testing WebPApi
#
class TestWebPApi(ImagingApiTester):

    #
    # Test get_image_web_p
    #
    def test_get_image_web_p(self):
        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'Animation.webp'
                lossless = True
                quality = 90
                anum_loop_count = 5
                anim_background_color = 'gray'
                folder = self.temp_folder
                storage = self.test_storage
                out_name = name + '_specific.webp'
                from_scratch = None

                def request_invoker(file_name, out_path):
                    return self.imaging_api.get_image_web_p(
                        requests.GetImageWebPRequest(
                            file_name,
                            lossless,
                            quality,
                            anum_loop_count,
                            anim_background_color,
                            from_scratch,
                            out_path,
                            folder,
                            storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertIsNotNone(result_properties.web_p_properties)

                    self.assertIsNotNone(original_properties.web_p_properties)
                    self.assertEqual(
                        original_properties.width,
                        result_properties.width)
                    self.assertEqual(
                        original_properties.height,
                        result_properties.height)

                self.get_request_tester(
                    'GetImageWebPTest',
                    save_result_to_storage,
                    'Input image: {0}; AnimBackgroundColor: {1}; Lossless: {2}; Quality: {3}; '
                    'AnimLoopCount: {4}'.format(
                        name,
                        anim_background_color,
                        lossless,
                        quality,
                        anum_loop_count),
                    name,
                    out_name,
                    request_invoker,
                    properties_tester,
                    folder,
                    storage)

    #
    # Test psot_image_web_p
    #
    def test_post_image_web_p(self):
        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'Animation.webp'
                lossless = True
                quality = 90
                anum_loop_count = 5
                anim_background_color = 'gray'
                folder = self.temp_folder
                storage = self.test_storage
                out_name = name + '_specific.webp'
                from_scratch = None

                def request_invoker(input_stream, out_path):
                    return self.imaging_api.post_image_web_p(
                        requests.PostImageWebPRequest(
                            input_stream,
                            lossless,
                            quality,
                            anum_loop_count,
                            anim_background_color,
                            from_scratch,
                            out_path,
                            storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertIsNotNone(result_properties.web_p_properties)

                    self.assertIsNotNone(original_properties.web_p_properties)
                    self.assertEqual(
                        original_properties.width,
                        result_properties.width)
                    self.assertEqual(
                        original_properties.height,
                        result_properties.height)

                self.post_request_tester(
                    'PostImageWebPTest',
                    save_result_to_storage,
                    'Input image: {0}; AnimBackgroundColor: {1}; Lossless: {2}; Quality: {3}; '
                    'AnimLoopCount: {4}'.format(
                        name,
                        anim_background_color,
                        lossless,
                        quality,
                        anum_loop_count),
                    name,
                    out_name,
                    request_invoker,
                    properties_tester,
                    folder,
                    storage)
