from test.api import ImagingApiTester


#
# Class for testing TiffApi
#
class TestTiffApi(ImagingApiTester):

    #
    # Test get_image_tiff
    #
    def test_get_image_tiff(self):
        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):

                name = 'test.tiff'
                compression = 'adobedeflate'
                resolution_unit = 'inch'
                bit_depth = 1
                horizontal_resolution = 150
                vertical_resolution = 150
                out_name = name + '_specific.tiff'
                folder = self.temp_folder
                storage = self.test_storage

                def request_invoker(file_name, out_path):
                    kwargs = {"horizontal_resolution": horizontal_resolution,
                              "vertical_resolution": vertical_resolution, "folder": folder, "storage": storage}
                    if out_path:
                        kwargs["out_path"] = out_path

                    return self.imaging_api.get_image_tiff(name, compression, resolution_unit, bit_depth, **kwargs)

                def properties_tester(original_properties, result_properties, result_stream):
                    self.assertIsNotNone(result_properties.tiff_properties)
                    self.assertEqual(bit_depth * 4 if bit_depth > 1 else bit_depth, result_properties.bits_per_pixel)
                    self.assertEqual(vertical_resolution, result_properties.vertical_resolution)
                    self.assertEqual(horizontal_resolution, result_properties.horizontal_resolution)

                    self.assertIsNotNone(original_properties.tiff_properties)
                    self.assertEqual(len(original_properties.tiff_properties.frames),
                                     len(result_properties.tiff_properties.frames))
                    self.assertEqual(original_properties.width, result_properties.width)
                    self.assertEqual(original_properties.height, result_properties.height)

                self.get_request_tester('GetImageTiffTest', save_result_to_storage,
                                        'Input image: {0}; Compression: {1}; Bit depth: {2}; Horizontal resolution: {3};'
                                        ' Vertical resolution: {4}'.format(name, compression, bit_depth,
                                                                           horizontal_resolution, vertical_resolution),
                                        name, out_name, request_invoker, properties_tester, folder, storage)

    #
    # Test post_image_tiff
    #
    def test_post_image_tiff(self):
        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):

                name = 'test.tiff'
                compression = 'adobedeflate'
                resolution_unit = 'inch'
                bit_depth = 1
                horizontal_resolution = 150
                vertical_resolution = 150
                out_name = name + '_specific.tiff'
                folder = self.temp_folder
                storage = self.test_storage

                def request_invoker(input_stream, out_path):
                    kwargs = {"horizontal_resolution": horizontal_resolution,
                              "vertical_resolution": vertical_resolution, "storage": storage}
                    if out_path:
                        kwargs["out_path"] = out_path

                    return self.imaging_api.post_image_tiff(input_stream, compression, resolution_unit, bit_depth,
                                                            **kwargs)

                def properties_tester(original_properties, result_properties, result_stream):
                    self.assertIsNotNone(result_properties.tiff_properties)
                    self.assertEqual(bit_depth * 4 if bit_depth > 1 else bit_depth, result_properties.bits_per_pixel)
                    self.assertEqual(vertical_resolution, result_properties.vertical_resolution)
                    self.assertEqual(horizontal_resolution, result_properties.horizontal_resolution)

                    self.assertIsNotNone(original_properties.tiff_properties)
                    self.assertEqual(len(original_properties.tiff_properties.frames),
                                     len(result_properties.tiff_properties.frames))
                    self.assertEqual(original_properties.width, result_properties.width)
                    self.assertEqual(original_properties.height, result_properties.height)

                self.post_request_tester('PostImageTiffTest', save_result_to_storage,
                                         'Input image: {0}; Compression: {1}; Bit depth: {2}; Horizontal resolution: {3};'
                                         ' Vertical resolution: {4}'.format(name, compression, bit_depth,
                                                                            horizontal_resolution, vertical_resolution),
                                         name, out_name, request_invoker, properties_tester, folder, storage)

    #
    # Test get_tiff_to_fax
    #
    def test_get_tiff_to_fax(self):
        name = 'test.tiff'
        out_name = name + '_specific.tiff'
        folder = self.temp_folder
        storage = self.test_storage

        def request_invoker(file_name, out_path):
            kwargs = {"folder": folder, "storage": storage}
            if out_path:
                kwargs["out_path"] = out_path

            return self.imaging_api.get_tiff_to_fax(name, **kwargs)

        def properties_tester(original_properties, result_properties, result_stream):
            self.assertIsNotNone(result_properties.tiff_properties)
            self.assertEqual(1, result_properties.bits_per_pixel)
            self.assertEqual(196, result_properties.vertical_resolution)
            self.assertEqual(204, result_properties.horizontal_resolution)
            self.assertEqual(1728, result_properties.width)
            self.assertEqual(2200, result_properties.height)

        self.get_request_tester('GetTiffToFaxTest', True, 'Input image: {0}'.format(name), name, out_name,
                                request_invoker, properties_tester, folder, storage)

    #
    # Test post_tiff_append
    #
    def test_post_tiff_append(self):
        passed = False
        print('PostTiffAppendTest')

        input_file_name = 'test.tiff'
        folder = self.temp_folder

        if not self._check_input_file_exists(input_file_name):
            raise ValueError(
                'Input file {0} doesn\'t exist in the specified storage folder: {1}. Please, upload it first.'.format(
                    input_file_name, folder))

        result_file_name = input_file_name + '_merged.tiff'
        out_path = None
        input_path = self.temp_folder + '/' + input_file_name
        storage = self.test_storage

        try:
            print('Input image: ' + input_file_name)

            out_path = self.temp_folder + '/' + result_file_name

            # remove output file from the storage (if exists)
            if self.imaging_api.object_exists(out_path, **{"storage_name": storage}).exists:
                self.imaging_api.delete_file(out_path, **{"storage_name": storage})

            if not self.imaging_api.object_exists(input_path, **{"storage_name": storage}).exists:
                self.imaging_api.copy_file(self.original_data_folder + '/' + input_file_name,
                                           folder + '/' + input_file_name,
                                           **{"src_storage_name": storage, "dest_storage_name": storage})

            self.imaging_api.copy_file(input_path, out_path,
                                       **{"src_storage_name": storage, "dest_storage_name": storage})
            self.assertTrue(self.imaging_api.object_exists(out_path, **{"storage_name": storage}))

            self.imaging_api.post_tiff_append(result_file_name, input_file_name,
                                              **{"storage": storage, "folder": folder})

            result_info = self._get_storage_file_info(folder, result_file_name, storage)
            if not result_info:
                raise ValueError('Result file {0} doesn\'t exist in the specified storage folder: {1}. Result isn\'t '
                                 'present in the storage by an unknown reason.'.format(result_file_name, folder))

            result_properties = self.imaging_api.get_image_properties(result_file_name,
                                                                      **{"folder": folder, "storage": storage})
            self.assertIsNotNone(result_properties)

            original_properties = self.imaging_api.get_image_properties(input_file_name,
                                                                        **{"folder": folder, "storage": storage})
            self.assertIsNotNone(original_properties)

            self.assertIsNotNone(result_properties.tiff_properties)
            self.assertIsNotNone(original_properties.tiff_properties)
            self.assertEqual(len(original_properties.tiff_properties.frames) * 2,
                             len(result_properties.tiff_properties.frames))
            self.assertEqual(original_properties.width, result_properties.width)
            self.assertEqual(original_properties.height, result_properties.height)

            passed = True

        except Exception as e:
            self.failed_any_test = True
            print(e)

        finally:
            if self.remove_result and self.imaging_api.object_exists(out_path, **{"storage_name": storage}).exists:
                self.imaging_api.delete_file(out_path, **{"storage_name": storage})

                print('Test passed: ' + str(passed))
