from test.api import ImagingApiTester
from itertools import product


#
# Class for testing RotateFlipApi
#
class TestRotateFlipApi(ImagingApiTester):

    #
    # Test get_image_rotate_flip
    #
    def test_get_image_rotate_flip(self):
        additional_export_formats = set()
        if not self.EXTENDED_TEST:
            format_extension_test_cases = ['.jpg']
        else:
            format_extension_test_cases = ['.jpg', '.bmp', '.dicom', '.gif', '.j2k', '.png', '.psd', '.tiff', '.webp']
        save_result_to_storage_test_cases = [True, False]

        for (save_result_to_storage, format_extension) in list(
                product(save_result_to_storage_test_cases, format_extension_test_cases)):
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)) and \
                 self.subTest('format_extension: ' + str(format_extension)):

                method = 'Rotate90FlipX'
                folder = self.temp_folder
                storage = self.test_storage

                formats_to_export = set(self.basic_export_formats).union(additional_export_formats)

                def request_invoker(file_name, out_path):
                    kwargs = {"folder": folder, "storage": storage}
                    if out_path:
                        kwargs["out_path"] = out_path

                    return self.imaging_api.get_image_rotate_flip(file_name, format, method, **kwargs)

                def properties_tester(original_properties, result_properties, result_stream):
                    try:
                        self.assertEqual(original_properties.height, result_properties.width)
                    except:
                        self.assertEqual(original_properties.height - 1, result_properties.width)

                    try:
                        self.assertEqual(original_properties.width, result_properties.height)
                    except:
                        self.assertEqual(original_properties.width - 1, result_properties.height)

                for input_file in self.input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name

                    for format in formats_to_export:
                        out_name = '{0}_crop.{1}'.format(name, format)

                        self.get_request_tester('GetImageRotateFlipTest', save_result_to_storage,
                                                'Input image: {0}; Output format: {1}; Method: '
                                                '{2}'.format(name, format, method),
                                                name, out_name, request_invoker, properties_tester, folder, storage)

    #
    # Test post_image_rotate_flip
    #
    def test_post_image_rotate_flip(self):
        additional_export_formats = set()
        if not self.EXTENDED_TEST:
            format_extension_test_cases = ['.jpg']
        else:
            format_extension_test_cases = ['.jpg', '.bmp', '.dicom', '.gif', '.j2k', '.png', '.psd', '.tiff', '.webp']
        save_result_to_storage_test_cases = [True, False]

        for (save_result_to_storage, format_extension) in list(
                product(save_result_to_storage_test_cases, format_extension_test_cases)):
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)) and \
                 self.subTest('format_extension: ' + str(format_extension)):

                method = 'Rotate90FlipX'
                folder = self.temp_folder
                storage = self.test_storage

                formats_to_export = set(self.basic_export_formats).union(additional_export_formats)

                def request_invoker(input_stream, out_path):
                    kwargs = {"storage": storage}
                    if out_path:
                        kwargs["out_path"] = out_path

                    return self.imaging_api.post_image_rotate_flip(input_stream, format, method, **kwargs)

                def properties_tester(original_properties, result_properties, result_stream):
                    try:
                        self.assertEqual(original_properties.height, result_properties.width)
                    except:
                        self.assertEqual(original_properties.height - 1, result_properties.width)

                    try:
                        self.assertEqual(original_properties.width, result_properties.height)
                    except:
                        self.assertEqual(original_properties.width - 1, result_properties.height)

                for input_file in self.input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name

                    for format in formats_to_export:
                        out_name = '{0}_crop.{1}'.format(name, format)

                        self.post_request_tester('PostImageRotateFlipTest', save_result_to_storage,
                                                 'Input image: {0}; Output format: {1}; Method: '
                                                 '{2}'.format(name, format, method),
                                                 name, out_name, request_invoker, properties_tester, folder, storage)