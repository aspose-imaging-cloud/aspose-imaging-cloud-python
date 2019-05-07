from test.api.imaging_api_tester import ImagingApiTester


class TestBmpApi(ImagingApiTester):

    def test_get_image_bmp(self):
        name = "test.bmp"
        bits_per_pixel = 32
        horizontal_resolution = 300
        vertical_resolution = 300
        from_scratch = None
        out_name = name + '_specific.bmp'
        folder = self.temp_folder
        storage = self.test_storage

        def properties_tester(original_properties, result_properties, result_stream):
            self.assertIsNotNone(result_properties.bpm_properties)

        self.test_get_request('GetImageBmpTest', False,
                              'Input image: {0}; Bits per pixel: {1}; Horizontal resolution: {2}; '
                              'Vertical resolution: {3}'.format(name, bits_per_pixel, horizontal_resolution,
                                                                vertical_resolution),
                              name, out_name,
                              lambda file_name, out_path: self.imaging_api.get_image_bmp(file_name, bits_per_pixel,
                                                                                         horizontal_resolution,
                                                                                         vertical_resolution,
                                                                                         from_scratch, out_path, folder,
                                                                                         storage),
                              properties_tester, folder, storage)
