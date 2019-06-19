import math

import asposeimagingcloud.models.requests as requests
from test.api.imaging_api_tester import ImagingApiTester


class TestBmpApi(ImagingApiTester):
    """ Class for testing BmpAPI """

    def test_get_image_bmp(self):
        """ Test get_image_bmp """

        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = "test.bmp"
                bits_per_pixel = 32
                horizontal_resolution = 300
                vertical_resolution = 300
                out_name = name + '_specific.bmp'
                folder = self.temp_folder
                storage = self.test_storage
                from_scratch = None

                def request_invoker(file_name, out_path):
                    return self.imaging_api.get_image_bmp(
                        requests.GetImageBmpRequest(
                            file_name,
                            bits_per_pixel,
                            horizontal_resolution,
                            vertical_resolution,
                            from_scratch,
                            out_path,
                            folder,
                            storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertIsNotNone(result_properties.bmp_properties)
                    self.assertEqual(
                        bits_per_pixel, result_properties.bits_per_pixel)
                    self.assertEqual(vertical_resolution, math.ceil(
                        float(result_properties.vertical_resolution)))
                    self.assertEqual(horizontal_resolution, math.ceil(
                        float(result_properties.horizontal_resolution)))

                    self.assertIsNotNone(original_properties.bmp_properties)
                    self.assertEqual(
                        original_properties.bmp_properties.compression,
                        result_properties.bmp_properties.compression)
                    self.assertEqual(
                        original_properties.width,
                        result_properties.width)
                    self.assertEqual(
                        original_properties.height,
                        result_properties.height)

                self.get_request_tester(
                    'GetImageBmpTest',
                    save_result_to_storage,
                    'Input image: {0}; Bits per pixel: {1}; Horizontal resolution: {2}; '
                    'Vertical resolution: {3}'.format(
                        name,
                        bits_per_pixel,
                        horizontal_resolution,
                        vertical_resolution),
                    name,
                    out_name,
                    request_invoker,
                    properties_tester,
                    folder,
                    storage)

    def test_post_image_bmp(self):
        """ Test post_image_bmp """

        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = "test.bmp"
                bits_per_pixel = 32
                horizontal_resolution = 300
                vertical_resolution = 300
                out_name = name + '_specific.bmp'
                folder = self.temp_folder
                storage = self.test_storage
                from_scratch = None

                def request_invoker(input_stream, out_path):
                    return self.imaging_api.post_image_bmp(
                        requests.PostImageBmpRequest(
                            input_stream,
                            bits_per_pixel,
                            horizontal_resolution,
                            vertical_resolution,
                            from_scratch,
                            out_path,
                            storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertIsNotNone(result_properties.bmp_properties)
                    self.assertEqual(
                        bits_per_pixel, result_properties.bits_per_pixel)
                    self.assertEqual(vertical_resolution, math.ceil(
                        float(result_properties.vertical_resolution)))
                    self.assertEqual(horizontal_resolution, math.ceil(
                        float(result_properties.horizontal_resolution)))

                    self.assertIsNotNone(original_properties.bmp_properties)
                    self.assertEqual(
                        original_properties.bmp_properties.compression,
                        result_properties.bmp_properties.compression)
                    self.assertEqual(
                        original_properties.width,
                        result_properties.width)
                    self.assertEqual(
                        original_properties.height,
                        result_properties.height)

                self.post_request_tester(
                    'PostImageBmpTest',
                    save_result_to_storage,
                    'Input image: {0}; Bits per pixel: {1}; Horizontal resolution: {2}; '
                    'Vertical resolution: {3}'.format(
                        name,
                        bits_per_pixel,
                        horizontal_resolution,
                        vertical_resolution),
                    name,
                    out_name,
                    request_invoker,
                    properties_tester,
                    folder,
                    storage)
