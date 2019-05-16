from test.api import ImagingApiTester


#
# Class for testing GifAPI
#
class TestGifApi(ImagingApiTester):

    #
    # Test get_image_gif
    #
    def test_get_image_gif(self):
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

                def request_invoker(file_name, out_path):
                    kwargs = {"background_color_index": background_color_index, "color_resolution": color_resolution,
                              "has_trailer": has_trailer, "interlaced": interlaced,
                              "is_palette_sorted": is_palette_sorted, "pixel_aspect_ratio": pixel_aspect_ratio,
                              "folder": folder, "storage": storage}
                    if out_path:
                        kwargs["out_path"] = out_path

                    return self.imaging_api.get_image_gif(name, **kwargs)

                def properties_tester(original_properties, result_properties, result_stream):
                    self.assertIsNotNone(result_properties.gif_properties)

                    # TODO: enable when IMAGINGCLOUD-51 is done
                    # self.assertEqual(has_trailer, result_properties.gif_properties.has_trailer)
                    self.assertEqual(pixel_aspect_ratio, result_properties.gif_properties.pixel_aspect_ratio)

                    self.assertIsNotNone(original_properties.gif_properties)
                    self.assertEqual(original_properties.width, result_properties.width)
                    self.assertEqual(original_properties.height, result_properties.height)

                self.get_request_tester('GetImageGifTest', save_result_to_storage,
                                        'Input image: {0}; Back color index: {1}; Color resolution: {2}; Has trailer: '
                                        '{3}; Interlaced: {4}; Is palette sorted: {5}; Pixel aspect ratio: {6}'.format(
                                            name, background_color_index, color_resolution, has_trailer, interlaced,
                                            is_palette_sorted, pixel_aspect_ratio),
                                        name, out_name, request_invoker, properties_tester, folder, storage)

    #
    # Test post_image_gif
    #
    def test_post_image_gif(self):
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

                def request_invoker(input_stream, out_path):
                    kwargs = {"background_color_index": background_color_index, "color_resolution": color_resolution,
                              "has_trailer": has_trailer, "interlaced": interlaced,
                              "is_palette_sorted": is_palette_sorted, "pixel_aspect_ratio": pixel_aspect_ratio,
                              "storage": storage}
                    if out_path:
                        kwargs["out_path"] = out_path

                    return self.imaging_api.post_image_gif(input_stream, **kwargs)

                def properties_tester(original_properties, result_properties, result_stream):
                    self.assertIsNotNone(result_properties.gif_properties)

                    # TODO: enable when IMAGINGCLOUD-51 is done
                    # self.assertEqual(has_trailer, result_properties.gif_properties.has_trailer)
                    self.assertEqual(pixel_aspect_ratio, result_properties.gif_properties.pixel_aspect_ratio)

                    self.assertIsNotNone(original_properties.gif_properties)
                    self.assertEqual(original_properties.width, result_properties.width)
                    self.assertEqual(original_properties.height, result_properties.height)

                self.post_request_tester('PostImageGifTest', save_result_to_storage,
                                         'Input image: {0}; Back color index: {1}; Color resolution: {2}; Has trailer: '
                                         '{3}; Interlaced: {4}; Is palette sorted: {5}; Pixel aspect ratio: {6}'.format(
                                             name, background_color_index, color_resolution, has_trailer, interlaced,
                                             is_palette_sorted, pixel_aspect_ratio),
                                         name, out_name, request_invoker, properties_tester, folder, storage)
