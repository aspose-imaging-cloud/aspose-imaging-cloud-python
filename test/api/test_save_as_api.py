from test.api import ImagingApiTester
from itertools import product


#
# Class for testing SaveAsAPI
#
class TestSaveAsApi(ImagingApiTester):

    #
    # Performs SaveAs (export to another format) operation test with GET method, taking input data from storage
    #
    def test_get_image_save_as(self):
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

                folder = self.temp_folder
                storage = self.test_storage

                formats_to_export = set(self.basic_export_formats).union(additional_export_formats)

                def request_invoker(file_name, out_path):
                    kwargs = {"folder": folder, "storage": storage}
                    if out_path:
                        kwargs["out_path"] = out_path

                    return self.imaging_api.get_image_save_as(file_name, format, **kwargs)

                for input_file in self.input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name

                    for format in formats_to_export:
                        out_name = '{0}_crop.{1}'.format(name, format)

                        self.get_request_tester('GetImageSaveAsTest', save_result_to_storage,
                                                'Input image: {0}; Output format: {1}'.format(name, format),
                                                name, out_name, request_invoker, lambda x, y, z: None, folder, storage)

    #
    # Performs SaveAs (export to another format) operation test with POST method, sending input data in request stream.
    #
    def test_post_image_save_as(self):
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

                folder = self.temp_folder
                storage = self.test_storage

                formats_to_export = set(self.basic_export_formats).union(additional_export_formats)

                def request_invoker(input_stream, out_path):
                    kwargs = {"storage": storage}
                    if out_path:
                        kwargs["out_path"] = out_path

                    return self.imaging_api.post_image_save_as(input_stream, format, **kwargs)

                for input_file in self.input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name

                    for format in formats_to_export:
                        out_name = '{0}_crop.{1}'.format(name, format)

                        self.post_request_tester('PostImageSaveAsTest', save_result_to_storage,
                                                 'Input image: {0}; Output format: {1}'.format(name, format),
                                                 name, out_name, request_invoker, lambda x, y, z: None, folder, storage)
