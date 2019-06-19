import asposeimagingcloud.models.requests as requests
from test.api import ImagingApiTester


class TestGifApi(ImagingApiTester):
    """ Class for testing GifAPI """

    def test_get_image_gif(self):
        """ Test get_image_gif """

        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.gif'
                background_color_index = 5
                color_resolution = 4
                has_trailer = True
                interlaced = False
                is_palette_sorted = True
                pixel_aspect_ratio = 4
                out_name = name + '_specific.gif'
                folder = self.temp_folder
                storage = self.test_storage
                from_scratch = None

                def request_invoker(file_name, out_path):
                    return self.imaging_api.get_image_gif(
                        requests.GetImageGifRequest(
                            name,
                            background_color_index,
                            color_resolution,
                            has_trailer,
                            interlaced,
                            is_palette_sorted,
                            pixel_aspect_ratio,
                            from_scratch,
                            out_path,
                            folder,
                            storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertIsNotNone(result_properties.gif_properties)

                    # TODO: enable when IMAGINGCLOUD-51 is done
                    # self.assertEqual(has_trailer, result_properties.gif_properties.has_trailer)
                    self.assertEqual(
                        pixel_aspect_ratio,
                        result_properties.gif_properties.pixel_aspect_ratio)

                    self.assertIsNotNone(original_properties.gif_properties)
                    self.assertEqual(
                        original_properties.width,
                        result_properties.width)
                    self.assertEqual(
                        original_properties.height,
                        result_properties.height)

                self.get_request_tester(
                    'GetImageGifTest',
                    save_result_to_storage,
                    'Input image: {0}; Back color index: {1}; Color resolution: {2}; Has trailer: '
                    '{3}; Interlaced: {4}; Is palette sorted: {5}; Pixel aspect ratio: {6}'.format(
                        name,
                        background_color_index,
                        color_resolution,
                        has_trailer,
                        interlaced,
                        is_palette_sorted,
                        pixel_aspect_ratio),
                    name,
                    out_name,
                    request_invoker,
                    properties_tester,
                    folder,
                    storage)

    def test_post_image_gif(self):
        """ Test post_image_gif """

        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.gif'
                background_color_index = 5
                color_resolution = 4
                has_trailer = True
                interlaced = False
                is_palette_sorted = True
                pixel_aspect_ratio = 4
                out_name = name + '_specific.gif'
                folder = self.temp_folder
                storage = self.test_storage
                from_scratch = None

                def request_invoker(input_stream, out_path):
                    return self.imaging_api.post_image_gif(
                        requests.PostImageGifRequest(
                            input_stream,
                            background_color_index,
                            color_resolution,
                            has_trailer,
                            interlaced,
                            is_palette_sorted,
                            pixel_aspect_ratio,
                            from_scratch,
                            out_path,
                            storage))

                def properties_tester(
                        original_properties,
                        result_properties,
                        result_stream):
                    self.assertIsNotNone(result_properties.gif_properties)

                    # TODO: enable when IMAGINGCLOUD-51 is done
                    # self.assertEqual(has_trailer, result_properties.gif_properties.has_trailer)
                    self.assertEqual(
                        pixel_aspect_ratio,
                        result_properties.gif_properties.pixel_aspect_ratio)

                    self.assertIsNotNone(original_properties.gif_properties)
                    self.assertEqual(
                        original_properties.width,
                        result_properties.width)
                    self.assertEqual(
                        original_properties.height,
                        result_properties.height)

                self.post_request_tester(
                    'PostImageGifTest',
                    save_result_to_storage,
                    'Input image: {0}; Back color index: {1}; Color resolution: {2}; Has trailer: '
                    '{3}; Interlaced: {4}; Is palette sorted: {5}; Pixel aspect ratio: {6}'.format(
                        name,
                        background_color_index,
                        color_resolution,
                        has_trailer,
                        interlaced,
                        is_palette_sorted,
                        pixel_aspect_ratio),
                    name,
                    out_name,
                    request_invoker,
                    properties_tester,
                    folder,
                    storage)
