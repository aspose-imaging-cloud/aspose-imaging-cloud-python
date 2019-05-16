from test.api import ImagingApiTester


#
# Class for testing Jpeg2000API
#
class TestJpeg2000Api(ImagingApiTester):

    #
    # Test get_image_jpeg2000
    #
    def test_get_image_jpeg200(self):
        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.j2k'
                codec = 'jp2'
                comment = 'Aspose'
                out_name = name + '_specific.jp2'
                folder = self.temp_folder
                storage = self.test_storage

                def request_invoker(file_name, out_path):
                    kwargs = {"folder": folder, "storage": storage, "codec": codec}
                    if out_path:
                        kwargs["out_path"] = out_path

                    return self.imaging_api.get_image_jpeg2000(name, comment, **kwargs)

                def properties_tester(original_properties, result_properties, result_stream):
                    self.assertIsNotNone(result_properties.jpeg2000_properties)

                    self.assertIsNotNone(result_properties.jpeg2000_properties.codec)
                    self.assertEqual(codec, result_properties.jpeg2000_properties.codec.lower())
                    self.assertIsNotNone(result_properties.jpeg2000_properties.comments)
                    self.assertEqual(comment, result_properties.jpeg2000_properties.comments[0])

                    self.assertIsNotNone(original_properties.jpeg2000_properties)
                    self.assertEqual(original_properties.width, result_properties.width)
                    self.assertEqual(original_properties.height, result_properties.height)
                    self.assertIsNotNone(original_properties.jpeg2000_properties.comments)
                    self.assertNotEqual(comment, original_properties.jpeg2000_properties.comments[0])

                self.get_request_tester('GetImageJpeg2000Test', save_result_to_storage,
                                        'Input image: {0}; Comment: {1}; Codec: {2}'.format(name, comment, codec),
                                        name, out_name, request_invoker, properties_tester, folder, storage)

    #
    # Test post_image_jpeg2000
    #
    def test_post_image_jpeg2000(self):
        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.j2k'
                codec = 'jp2'
                comment = 'Aspose'
                out_name = name + '_specific.jp2'
                folder = self.temp_folder
                storage = self.test_storage

                def request_invoker(input_stream, out_path):
                    kwargs = {"storage": storage, "codec": codec}
                    if out_path:
                        kwargs["out_path"] = out_path

                    return self.imaging_api.post_image_jpeg2000(input_stream, comment, **kwargs)

                def properties_tester(original_properties, result_properties, result_stream):
                    self.assertIsNotNone(result_properties.jpeg2000_properties)

                    self.assertIsNotNone(result_properties.jpeg2000_properties.codec)
                    self.assertEqual(codec, result_properties.jpeg2000_properties.codec.lower())
                    self.assertIsNotNone(result_properties.jpeg2000_properties.comments)
                    self.assertEqual(comment, result_properties.jpeg2000_properties.comments[0])

                    self.assertIsNotNone(original_properties.jpeg2000_properties)
                    self.assertEqual(original_properties.width, result_properties.width)
                    self.assertEqual(original_properties.height, result_properties.height)
                    self.assertIsNotNone(original_properties.jpeg2000_properties.comments)
                    self.assertNotEqual(comment, original_properties.jpeg2000_properties.comments[0])

                self.post_request_tester('PostImageJpeg2000Test', save_result_to_storage,
                                         'Input image: {0}; Comment: {1}; Codec: {2}'.format(name, comment, codec),
                                         name, out_name, request_invoker, properties_tester, folder, storage)
