from test.api import ImagingApiTester


#
# Class for testing FramesAPI
#
class TestFramesPostApi(ImagingApiTester):

    #
    # Test post_image_frame
    #
    def test_post_image_single_frame(self):
        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.tiff'
                frame_id = 2
                new_width = 300
                new_height = 450
                x = 10
                y = 10
                rect_width = 200
                rect_height = 300
                rotate_flip_method = 'Rotate90FlipX'
                save_other_frames = False
                folder = self.temp_folder
                storage = self.test_storage
                out_name = name + '_singleFrame.tiff'

                def request_invoker(input_stream, out_path):
                    kwargs = (
                        {"new_width": new_width, "new_height": new_height, "x": x, "y": y, "rect_width": rect_width,
                         "rect_height": rect_height, "rotate_flip_method": rotate_flip_method,
                         "save_other_frames": save_other_frames, "storage": storage})
                    if out_path:
                        kwargs["out_path"] = out_path

                    return self.imaging_api.post_image_frame(input_stream, frame_id, **kwargs)

                def properties_tester(original_properties, result_properties, result_stream):
                    self.assertIsNotNone(result_properties)
                    self.assertIsNotNone(result_properties.tiff_properties)
                    self.assertIsNotNone(result_properties.tiff_properties.frames)
                    self.assertEqual(1, len(result_properties.tiff_properties.frames))

                    # please note that rotation was performed, so switching of width and height comparison is valid

                    self.assertEqual(rect_height, result_properties.tiff_properties.frames[0].width)
                    self.assertEqual(rect_width, result_properties.tiff_properties.frames[0].height)
                    self.assertEqual(result_properties.tiff_properties.frames[0].frame_options.image_width, rect_height)
                    self.assertEqual(rect_width, result_properties.tiff_properties.frames[0].frame_options.image_length)
                    self.assertEqual(rect_height, result_properties.width)
                    self.assertEqual(rect_width, result_properties.height)

                    if save_result_to_storage:
                        frame_properties = self.imaging_api.get_image_frame_properties(out_name, 0,
                                                                                       **{"folder": folder,
                                                                                          "storage": storage})
                    else:
                        frame_properties = self.imaging_api.post_image_frame_properties(result_stream, 0)

                    self.assertIsNotNone(frame_properties)
                    self.assertIsNotNone(frame_properties.tiff_properties)
                    self.assertIsNotNone(frame_properties.tiff_properties.frames)
                    self.assertEqual(rect_height, frame_properties.width)
                    self.assertEqual(rect_width, frame_properties.height)
                    self.assertEqual(frame_properties.tiff_properties.frames[0].width, frame_properties.width)
                    self.assertEqual(frame_properties.tiff_properties.frames[0].height, frame_properties.height)
                    self.assertEqual(frame_properties.tiff_properties.frames[0].frame_options.image_width,
                                     frame_properties.width)
                    self.assertEqual(frame_properties.tiff_properties.frames[0].frame_options.image_length,
                                     frame_properties.height)

                self.post_request_tester('GetImageSingleFrameTest', save_result_to_storage,
                                         'Input image: {0}; Frame ID: {1}; New width: {2}; New height: {3}; '
                                         'Rotate/flip method: {4}; Save other frames: {5}; X: {6}; Y: {7}; Rect width: '
                                         '{8}; Rect height: {9}'.format(name, frame_id, new_width, new_height,
                                                                        rotate_flip_method, save_other_frames, x, y,
                                                                        rect_width, rect_height),
                                         name, out_name, request_invoker, properties_tester, folder, storage)

    #
    # Test post_image_frame
    #
    def test_post_image_all_frames(self):
        save_result_to_storage_test_cases = [True, False]

        for save_result_to_storage in save_result_to_storage_test_cases:
            with self.subTest('save_result_to_storage: ' + str(save_result_to_storage)):
                name = 'test.tiff'
                frame_id = 2
                new_width = 300
                new_height = 450
                x = 10
                y = 10
                rect_width = 200
                rect_height = 300
                rotate_flip_method = 'Rotate90FlipX'
                save_other_frames = True
                folder = self.temp_folder
                storage = self.test_storage
                out_name = name + '_allFrame.tiff'

                def request_invoker(input_stream, out_path):
                    kwargs = (
                        {"new_width": new_width, "new_height": new_height, "x": x, "y": y, "rect_width": rect_width,
                         "rect_height": rect_height, "rotate_flip_method": rotate_flip_method,
                         "save_other_frames": save_other_frames, "storage": storage})
                    if out_path:
                        kwargs["out_path"] = out_path

                    return self.imaging_api.post_image_frame(input_stream, frame_id, **kwargs)

                def properties_tester(original_properties, result_properties, result_stream):
                    self.assertIsNotNone(original_properties)
                    self.assertIsNotNone(original_properties.tiff_properties)
                    self.assertIsNotNone(original_properties.tiff_properties.frames)

                    self.assertIsNotNone(result_properties)
                    self.assertIsNotNone(result_properties.tiff_properties)
                    self.assertIsNotNone(result_properties.tiff_properties.frames)
                    self.assertEqual(len(original_properties.tiff_properties.frames),
                                     len(result_properties.tiff_properties.frames))
                    self.assertEqual(original_properties.width, result_properties.width)
                    self.assertEqual(original_properties.height, result_properties.height)

                    # please note that rotation was performed, so switching of width and height comparison is valid

                    self.assertEqual(rect_height, result_properties.tiff_properties.frames[frame_id].width)
                    self.assertEqual(rect_width, result_properties.tiff_properties.frames[frame_id].height)
                    self.assertEqual(rect_height,
                                     result_properties.tiff_properties.frames[frame_id].frame_options.image_width)
                    self.assertEqual(rect_width,
                                     result_properties.tiff_properties.frames[frame_id].frame_options.image_length)

                self.post_request_tester('GetImageAllFramesTest', save_result_to_storage,
                                         'Input image: {0}; Frame ID: {1}; New width: {2}; New height: {3}; '
                                         'Rotate/flip method: {4}; Save other frames: {5}; X: {6}; Y: {7}; Rect width: '
                                         '{8}; Rect height: {9}'.format(name, frame_id, new_width, new_height,
                                                                        rotate_flip_method, save_other_frames, x, y,
                                                                        rect_width, rect_height),
                                         name, out_name, request_invoker, properties_tester, folder, storage)
