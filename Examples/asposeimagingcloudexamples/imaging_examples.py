#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="imaging_examples.py">
#    Copyright (c) 2019 Aspose Pty Ltd. All rights reserved.
#  </copyright>
#  <summary>
#    Permission is hereby granted, free of charge, to any person obtaining a
#   copy  of this software and associated documentation files (the "Software"),
#   to deal  in the Software without restriction, including without limitation
#   the rights  to use, copy, modify, merge, publish, distribute, sublicense,
#   and/or sell  copies of the Software, and to permit persons to whom the
#   Software is  furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all  copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM,  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#   DEALINGS IN THE SOFTWARE.
#  </summary>
#  ----------------------------------------------------------------------------

import os
import shutil
import sys

from asposeimagingcloud import ImagingApi

from asposeimagingcloudexamples.AI.compare_images import CompareImages
from asposeimagingcloudexamples.AI.find_duplicate_images import FindDuplicateImages
from asposeimagingcloudexamples.AI.find_similar_images import FindSimilarImages
from asposeimagingcloudexamples.crop_image import CropImage
from asposeimagingcloudexamples.deskew_image import DeskewImage
from asposeimagingcloudexamples.export_image import ExportImage
from asposeimagingcloudexamples.filter_image import FilterImage
from asposeimagingcloudexamples.grayscale_image import GrayscaleImage
from asposeimagingcloudexamples.image_properties import ImageProperties
from asposeimagingcloudexamples.imaging_base import ImagingBase
from asposeimagingcloudexamples.multiframe_image import MultiframeImage
from asposeimagingcloudexamples.object_detection_image import ObjectDetectionImage
from asposeimagingcloudexamples.resize_image import ResizeImage
from asposeimagingcloudexamples.rotate_flip_image import RotateFlipImage
from asposeimagingcloudexamples.update_bmp_image import UpdateBmpImage
from asposeimagingcloudexamples.update_emf_image import UpdateEmfImage
from asposeimagingcloudexamples.update_gif_image import UpdateGifImage
from asposeimagingcloudexamples.update_image import UpdateImage
from asposeimagingcloudexamples.update_jpeg2000_image import UpdateJpeg2000Image
from asposeimagingcloudexamples.update_jpeg_image import UpdateJpegImage
from asposeimagingcloudexamples.update_psd_image import UpdatePsdImage
from asposeimagingcloudexamples.update_tiff_image import UpdateTiffImage
from asposeimagingcloudexamples.update_web_p_image import UpdateWebPImage
from asposeimagingcloudexamples.update_wmf_image import UpdateWmfImage


def process_argument(argv, key, description, errors, default_value=None):
    """Retrieves argument value or writes error message"""
    argument_value = None
    for i, v in enumerate(argv):
        if v.startswith(key + '='):
            argument_value = v[v.index('=') + 1:]
        elif v == key and i < len(argv) - 1:
            argument_value = argv[i + 1]

        if argument_value:
            return argument_value

    if default_value:
        argument_value = default_value
    else:
        errors.append("Please, provide {0}: \'{1}\' <value>\' or \'{2}=<value>\'".format(description, key, key))

    return argument_value


def process_arguments(argv):
    """Process CLI arguments, exit on invalid input"""
    errors = []

    app_key = process_argument(argv, '--appKey', 'app key', errors)
    app_sid = process_argument(argv, '--appSid', 'app sid', errors)
    base_url = process_argument(argv, '--baseUrl', 'Base url', errors, 'https://api.aspose.cloud/')

    if not errors:
        return app_key, app_sid, base_url

    print('Failed to launch examples:' + os.linesep + os.linesep.join(errors))
    sys.exit(1)


def main():
    app_key, app_sid, base_url = process_arguments(sys.argv)

    try:
        api = ImagingApi(app_key, app_sid, base_url)

        if os.path.isdir(ImagingBase.OUTPUT_FOLDER):
            shutil.rmtree(ImagingBase.OUTPUT_FOLDER)

        os.mkdir(ImagingBase.OUTPUT_FOLDER)

        print('Running Imaging Cloud examples:')
        print()

        # # Crop an existing image
        # crop_image = CropImage(api)
        # crop_image.crop_image_from_storage()
        # crop_image.crop_image_and_upload_to_storage()
        # crop_image.create_cropped_image_from_request_body()
        #
        # # Deskew an existing image
        # deskew_image = DeskewImage(api)
        # deskew_image.deskew_image_from_storage()
        # deskew_image.deskew_image_and_upload_to_storage()
        # deskew_image.create_deskewed_image_from_request_body()
        #
        # # Grayscales an existing image
        # grayscale_image = GrayscaleImage(api)
        # grayscale_image.grayscale_image_from_storage()
        # grayscale_image.grayscale_image_and_upload_to_storage()
        # grayscale_image.create_grayscaled_image_from_request_body()
        #
        # # Export existing image to another format
        # export_image = ExportImage(api)
        # export_image.save_image_as_from_storage()
        # export_image.save_image_as_and_upload_to_storage()
        # export_image.create_saved_image_as_from_request_body()
        #
        # # Apply a filtering effect to an image
        # filter_image = FilterImage(api)
        # filter_image.filter_image_from_storage()
        # filter_image.filter_image_and_upload_to_storage()
        #
        # # Get properties of an image
        # image_properties = ImageProperties(api)
        # image_properties.get_image_properties_from_storage()
        # image_properties.extract_image_properties_from_request_body()
        #
        # # Resize an existing image
        # resize_image = ResizeImage(api)
        # resize_image.resize_image_from_storage()
        # resize_image.resize_image_and_upload_to_storage()
        # resize_image.create_resized_image_from_request_body()
        #
        # # Rotate and/or flip an existing image
        # rotate_flip_image = RotateFlipImage(api)
        # rotate_flip_image.rotate_flip_image_from_storage()
        # rotate_flip_image.rotate_flip_image_and_upload_to_storage()
        # rotate_flip_image.create_rotate_flipped_image_from_request_body()
        #
        # # Multiframe image
        # multiframe_image = MultiframeImage(api)
        # multiframe_image.get_image_frame_from_storage()
        # multiframe_image.get_image_frame_and_upload_to_storage()
        # multiframe_image.create_image_frame_from_request_body()
        # multiframe_image.get_image_frame_range_from_storage()
        # multiframe_image.get_image_frame_range_and_upload_to_storage()
        # multiframe_image.create_image_frame_range_from_request_body()
        # multiframe_image.get_image_frame_properties_from_storage()
        # multiframe_image.extract_image_frame_properties_from_request_body()
        #
        # # Update parameters of existing TIFF image
        # tiff_image = UpdateTiffImage(api)
        # tiff_image.modify_tiff_from_storage()
        # tiff_image.modify_tiff_and_upload_to_storage()
        # tiff_image.create_modified_tiff_from_request_body()
        # tiff_image.update_tiff_to_fax_from_storage()
        # tiff_image.convert_tiff_to_fax_from_request_body()
        # tiff_image.append_tiff_from_storage()
        #
        # # Update parameters of existing BMP image
        # bmp_image = UpdateBmpImage(api)
        # bmp_image.modify_bmp_from_storage()
        # bmp_image.modify_bmp_and_upload_to_storage()
        # bmp_image.create_modified_bmp_from_request_body()
        #
        # # Process existing EMF imaging using given parameters
        # emf_image = UpdateEmfImage(api)
        # emf_image.modify_emf_from_storage()
        # emf_image.modify_emf_and_upload_to_storage()
        # emf_image.create_modified_emf_from_request_body()
        #
        # # Process existing GIF imaging using given parameters
        # gif_image = UpdateGifImage(api)
        # gif_image.modify_gif_from_storage()
        # gif_image.modify_gif_and_upload_to_storage()
        # gif_image.create_modified_gif_from_request_body()
        #
        # # Perform scaling, cropping and flipping of an existing image in a single request
        # update_image = UpdateImage(api)
        # update_image.update_image_from_storage()
        # update_image.update_image_and_upload_to_storage()
        # update_image.create_updated_image_from_request_body()
        #
        # # Process existing JPEG2000 imaging using given parameters
        # jpeg2000_image = UpdateJpeg2000Image(api)
        # jpeg2000_image.modify_jpeg2000_from_storage()
        # jpeg2000_image.modify_jpeg2000_and_upload_to_storage()
        # jpeg2000_image.create_modified_jpeg2000_from_request_body()
        #
        # # Process existing JPEG imaging using given parameters
        # jpeg_image = UpdateJpegImage(api)
        # jpeg_image.modify_jpeg_from_storage()
        # jpeg_image.modify_jpeg_and_upload_to_storage()
        # jpeg_image.create_modified_jpeg_from_request_body()
        #
        # # Process existing PSD imaging using given parameters
        # psd_image = UpdatePsdImage(api)
        # psd_image.modify_psd_from_storage()
        # psd_image.modify_psd_and_upload_to_storage()
        # psd_image.create_modified_psd_from_request_body()
        #
        # # Process existing WEBP imaging using given parameters
        # web_p_image = UpdateWebPImage(api)
        # web_p_image.modify_web_p_from_storage()
        # web_p_image.modify_web_p_and_upload_to_storage()
        # web_p_image.create_modified_web_p_from_request_body()
        #
        # # Process existing WMF imaging using given parameters
        # wmf_image = UpdateWmfImage(api)
        # wmf_image.modify_wmf_from_storage()
        # wmf_image.modify_wmf_and_upload_to_storage()
        # wmf_image.create_modified_wmf_from_request_body()
        #
        # # AI APIs
        # print('Running AI examples:')
        # print()
        #
        # # Compare two images
        # compare_images = CompareImages(api)
        # compare_images.prepare_search_context()
        # compare_images.compare_two_images_in_cloud()
        # compare_images.compare_loaded_image_to_image_in_cloud()
        # compare_images.delete_search_context()
        #
        # # Find Duplicate Images
        # find_duplicate_images = FindDuplicateImages(api)
        # find_duplicate_images.prepare_search_context()
        # find_duplicate_images.find_image_duplicates()
        # find_duplicate_images.delete_search_context()
        #
        # # Find Similar Images
        # find_similar_images = FindSimilarImages(api)
        # find_similar_images.prepare_search_context()
        # find_similar_images.find_similar_images()
        # find_similar_images.find_images_by_tag()
        # find_similar_images.search_image_from_web_source()
        # find_similar_images.delete_search_context()

        #Object Detection
        object_detection_image = ObjectDetectionImage(api)
        object_detection_image.detect_objects_image_from_request_body()
        object_detection_image.detect_objects_image_from_storage()
        object_detection_image.visualize_detected_objects_image_from_storage()
        object_detection_image.visualize_detect_objects_image_from_request_body()

    except Exception as e:
        print('Something goes wrong: ' + str(e))
        sys.exit(1)

    sys.exit()


main()
