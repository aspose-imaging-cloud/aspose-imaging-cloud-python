from test.api.imaging_api_tester import ImagingApiTester
from itertools import product


#
# Class for testing CropAPI
#
class TestCropApi(ImagingApiTester):

    #
    # Test get_image_crop
    #
    def test_get_image_crop(self):
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

                x = 10
                y = 10
                width = 100
                height = 150
                folder = self.temp_folder
                storage = self.test_storage

                formats_to_export = set(self.basic_export_formats).union(additional_export_formats)

                def request_invoker(file_name, out_path):
                    kwargs = {"out_path": out_path, "folder": folder, "storage": storage} if out_path else {
                        "folder": folder,
                        "storage": storage}

                    return self.imaging_api.get_image_crop(file_name, format, x, y, width, height, **kwargs)

                def properties_tester(original_properties, result_properties, result_stream):
                    self.assertEqual(width, result_properties.width)
                    self.assertEqual(height, result_properties.height)

                for input_file in self.input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name

                    for format in formats_to_export:
                        out_name = '{0}_crop.{1}'.format(name, format)

                        self.get_request_tester('GetImageCropTest', save_result_to_storage,
                                                'Input image: {0}; Output format: {1}; Width: {2}; Height: {3}; X: {4};'
                                                ' Y: {5}'.format(name, format, width, height, x, y),
                                                name, out_name, request_invoker, properties_tester, folder, storage)

    #
    # Test post_image_crop
    #
    def test_post_image_crop(self):
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

                x = 10
                y = 10
                width = 100
                height = 150
                folder = self.temp_folder
                storage = self.test_storage

                formats_to_export = set(self.basic_export_formats).union(additional_export_formats)

                def request_invoker(input_stream, out_path):
                    kwargs = {"out_path": out_path, "storage": storage} if out_path else {"storage": storage}

                    return self.imaging_api.post_image_crop(input_stream, format, x, y, width, height, **kwargs)

                def properties_tester(original_properties, result_properties, result_stream):
                    self.assertEqual(width, result_properties.width)
                    self.assertEqual(height, result_properties.height)

                for input_file in self.input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name

                    for format in formats_to_export:
                        out_name = '{0}_crop.{1}'.format(name, format)

                        self.post_request_tester('PostImageCropTest', save_result_to_storage,
                                                 'Input image: {0}; Output format: {1}; Width: {2}; Height: {3}; X: {4};'
                                                 ' Y: {5}'.format(name, format, width, height, x, y),
                                                 name, out_name, request_invoker, properties_tester, folder, storage)
