from asposeimagingcloud import ImagingApi, ApiClient
from test.api import ImagingApiTester
import os


#
# Tests that correspond with examples code
#
class TestExamples(ImagingApiTester):

    #
    # Saves as from storage example test
    #
    def test_save_as_from_storage(self):
        config = self.imaging_api.api_client.configuration
        imaging_api = ImagingApi(ApiClient(config))
        remote_folder = 'ExampleFolderPython'
        remote_input_image = 'inputImage.png'
        remote_result_image = 'resultImage.jpg'

        try:
            # upload local image to storage
            result = imaging_api.upload_file(remote_folder + '/' + remote_input_image,
                                             os.path.join(self._local_test_folder, 'test.png'))

            # self.assertIsNone(result.errors)
            # self.assertIsNotNone(result.uploaded)
            # self.assertTrue(remote_input_image in result.uploaded)

            # convert image from storage to JPEG and save it to storage
            # please, use outPath parameter for saving the result to storage
            imaging_api.get_image_save_as(remote_input_image, 'jpg', out_path=remote_folder + '/' + remote_result_image,
                                          folder=remote_folder)

            # download saved image from storage
            saved_file = imaging_api.download_file(remote_folder + '/' + remote_result_image)
            # TODO: process resulting image from storage

            # convert image from storage to JPEG and read it from resulting stream
            # please, don't set outPath parameter to return result in request stream instead of saving to storage

            image_stream = imaging_api.get_image_save_as(remote_input_image, 'jpg', folder=remote_folder)
            # TODO:  process resulting image from response stream

        finally:
            # remove files from storage
            imaging_api.delete_file(remote_folder + '/' + remote_input_image)
            imaging_api.delete_file(remote_folder + '/' + remote_result_image)

    #
    # Saves as from stream example
    #
    def test_save_as_from_stream_example(self):
        config = self.imaging_api.api_client.configuration
        imaging_api = ImagingApi(ApiClient(config))
        remote_result_image = 'ExampleFolderPython' + '/' + 'resultImage.jpg'

        try:
            # get local image stream
            local_input_image = os.path.join(self._local_test_folder, 'test.png')
            # convert image from request stream to JPEG and save it to storage
            # please, use outPath parameter for saving the result to storage
            imaging_api.post_image_save_as(local_input_image, 'jpg', out_path=remote_result_image)

            #  download saved image from storage
            saved_file = imaging_api.download_file(remote_result_image)
            # TODO: process resulting image from storage

            # convert image from request stream to JPEG and read it from resulting stream
            image_stream = imaging_api.post_image_save_as(local_input_image, "jpg")
            # TODO: process resulting image from response stream

        finally:
            imaging_api.delete_file(remote_result_image)
