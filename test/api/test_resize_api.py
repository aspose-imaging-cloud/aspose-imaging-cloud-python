from test.api import ImagingApiTester
from itertools import product


#
# Class for testing ResizeAPI
#
class TestResizeApi(ImagingApiTester):

    #
    # Test get_image_resize
    #
    def test_get_image_resize(self):
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

                new_width = 100
                new_height = 150
                folder = self.temp_folder
                storage = self.test_storage

                formats_to_export = set(self.basic_export_formats).union(additional_export_formats)

                def request_invoker(file_name, out_path):
                    kwargs = {"folder": folder, "storage": storage}
                    if out_path:
                        kwargs["out_path"] = out_path

                    return self.imaging_api.get_image_resize(file_name, format, new_width, new_height, **kwargs)

                def properties_tester(original_properties, result_properties, result_stream):
                    self.assertEqual(new_width, result_properties.width)
                    self.assertEqual(new_height, result_properties.height)

                for input_file in self.input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name

                    for format in formats_to_export:
                        out_name = '{0}_crop.{1}'.format(name, format)

                        self.test_get_request('GetImageResizeTest', save_result_to_storage,
                                              'Input image: {0}; Output format: {1}; New width: {2}; New height: '
                                              '{3};'.format(name, format, new_width, new_height),
                                              name, out_name, request_invoker, properties_tester, folder, storage)

    #
    # Test post_image_resize
    #
    def test_post_image_resize(self):
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

                new_width = 100
                new_height = 150
                folder = self.temp_folder
                storage = self.test_storage

                formats_to_export = set(self.basic_export_formats).union(additional_export_formats)

                def request_invoker(input_stream, out_path):
                    kwargs = {"storage": storage}
                    if out_path:
                        kwargs["out_path"] = out_path

                    return self.imaging_api.post_image_resize(input_stream, format, new_width, new_height, **kwargs)

                def properties_tester(original_properties, result_properties, result_stream):
                    self.assertEqual(new_width, result_properties.width)
                    self.assertEqual(new_height, result_properties.height)

                for input_file in self.input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name

                    for format in formats_to_export:
                        out_name = '{0}_crop.{1}'.format(name, format)

                        self.test_post_request('PostImageResizeTest', save_result_to_storage,
                                               'Input image: {0}; Output format: {1}; New width: {2}; New height: '
                                               '{3};'.format(name, format, new_width, new_height),
                                               name, out_name, request_invoker, properties_tester, folder, storage)
