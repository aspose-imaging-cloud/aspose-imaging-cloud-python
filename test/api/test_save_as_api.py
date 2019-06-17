from test.api_tester import ApiTester
from test.api import ImagingApiTester
from itertools import product
import asposeimagingcloud.models.requests as requests


class TestSaveAsApi(ImagingApiTester):
    """ Class for testing SaveAsAPI """

    def test_get_image_save_as(self):
        """
        Performs SaveAs (export to another format) operation test with GET
        method, taking input data from storage
        """

        additional_export_formats = set()
        if not self.EXTENDED_TEST:
            format_extension_test_cases = ['.jpg']
        else:
            format_extension_test_cases = [
                '.jpg',
                '.bmp',
                '.dicom',
                '.gif',
                '.j2k',
                '.png',
                '.psd',
                '.tiff',
                '.webp']
        save_result_to_storage_test_cases = [True, False]

        for (
                save_result_to_storage,
                format_extension) in list(
                product(
                save_result_to_storage_test_cases,
                format_extension_test_cases)):
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)) and \
                    self.subTest('format_extension: ' + str(format_extension)):

                folder = ApiTester.temp_folder
                storage = ApiTester.test_storage

                formats_to_export = set(
                    ApiTester.basic_export_formats).union(additional_export_formats)

                def request_invoker(file_name, out_path):
                    kwargs = {"folder": folder, "storage": storage}
                    if out_path:
                        kwargs["out_path"] = out_path

                    return ApiTester.imaging_api.get_image_save_as(
                        requests.GetImageSaveAsRequest(
                            file_name, format, out_path, folder, storage))

                for input_file in ApiTester.input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name

                    for format in formats_to_export:
                        out_name = '{0}_crop.{1}'.format(name, format)

                        self.get_request_tester(
                            'GetImageSaveAsTest',
                            save_result_to_storage,
                            'Input image: {0}; Output format: {1}'.format(
                                name,
                                format),
                            name,
                            out_name,
                            request_invoker,
                            lambda x,
                            y,
                            z: None,
                            folder,
                            storage)

    def test_post_image_save_as(self):
        """
        Performs SaveAs (export to another format) operation test with POST
        method, sending input data in request stream.
        """

        additional_export_formats = set()
        if not self.EXTENDED_TEST:
            format_extension_test_cases = ['.jpg']
        else:
            format_extension_test_cases = [
                '.jpg',
                '.bmp',
                '.dicom',
                '.gif',
                '.j2k',
                '.png',
                '.psd',
                '.tiff',
                '.webp']
        save_result_to_storage_test_cases = [True, False]

        for (
                save_result_to_storage,
                format_extension) in list(
                product(
                save_result_to_storage_test_cases,
                format_extension_test_cases)):
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)) and \
                    self.subTest('format_extension: ' + str(format_extension)):

                folder = ApiTester.temp_folder
                storage = ApiTester.test_storage

                formats_to_export = set(
                    ApiTester.basic_export_formats).union(additional_export_formats)

                def request_invoker(input_stream, out_path):
                    kwargs = {"storage": storage}
                    if out_path:
                        kwargs["out_path"] = out_path

                    return ApiTester.imaging_api.post_image_save_as(
                        requests.PostImageSaveAsRequest(
                            input_stream, format, out_path, storage))

                for input_file in ApiTester.input_test_files:
                    if not str(input_file.name).endswith(format_extension):
                        continue

                    name = input_file.name

                    for format in formats_to_export:
                        out_name = '{0}_crop.{1}'.format(name, format)

                        self.post_request_tester(
                            'PostImageSaveAsTest',
                            save_result_to_storage,
                            'Input image: {0}; Output format: {1}'.format(
                                name,
                                format),
                            name,
                            out_name,
                            request_invoker,
                            lambda x,
                            y,
                            z: None,
                            folder,
                            storage)
