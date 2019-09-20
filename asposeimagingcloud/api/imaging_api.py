#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="imaging_api.py">
#    Copyright (c) 2018-2019 Aspose Pty Ltd. All rights reserved.
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

from __future__ import absolute_import

import six

from asposeimagingcloud.api_client import ApiClient
from asposeimagingcloud.configuration import Configuration
from asposeimagingcloud.rest import ApiException


class ImagingApi(object):
    """
    Aspose.Imaging Cloud API

    """

    def __init__(self, app_key=None, app_sid=None, base_url=None,
                 api_version=None, debug=False):
        """
        Initializes a new instance of the ImagingApi class.

        :param app_key: The app key.
        :param app_sid: The app sid.
        :param base_url: The base URL.
        :param api_version: API version.
        :param debug: If debug mode is enabled. False by default.
        :param on_premise:
            True for on-premise solution with metered license usage.
            False for Aspose Cloud-hosted solution usage, default.
        """
        configuration = Configuration(app_key=app_key,
                                      app_sid=app_sid,
                                      base_url=base_url,
                                      api_version=api_version,
                                      debug=debug)
        self.api_client = ApiClient(configuration)

    def add_search_image(self, request):
        """Add image and images features to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request add_search_image_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def add_search_image_async(self, request):
        """Add image and images features to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request add_search_image_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def append_tiff(self, request):
        """Appends existing TIFF image to another existing TIFF image (i.e. merges TIFF images).


        :param request append_tiff_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def append_tiff_async(self, request):
        """Appends existing TIFF image to another existing TIFF image (i.e. merges TIFF images).


        :param request append_tiff_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def compare_images(self, request):
        """Compare two images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request compare_images_request object with parameters
        :return: SearchResultsSet
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'SearchResultsSet')

    def compare_images_async(self, request):
        """Compare two images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request compare_images_request object with parameters
        :return: SearchResultsSet
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'SearchResultsSet')

    def convert_tiff_to_fax(self, request):
        """Update parameters of existing TIFF image accordingly to fax parameters.


        :param request convert_tiff_to_fax_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def convert_tiff_to_fax_async(self, request):
        """Update parameters of existing TIFF image accordingly to fax parameters.


        :param request convert_tiff_to_fax_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def copy_file(self, request):
        """Copy file


        :param request copy_file_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def copy_file_async(self, request):
        """Copy file


        :param request copy_file_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def copy_folder(self, request):
        """Copy folder


        :param request copy_folder_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def copy_folder_async(self, request):
        """Copy folder


        :param request copy_folder_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def create_cropped_image(self, request):
        """Crop an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_cropped_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def create_cropped_image_async(self, request):
        """Crop an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_cropped_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def create_folder(self, request):
        """Create the folder


        :param request create_folder_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def create_folder_async(self, request):
        """Create the folder


        :param request create_folder_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def create_image_features(self, request):
        """Extract images features and add them to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_image_features_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def create_image_features_async(self, request):
        """Extract images features and add them to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_image_features_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def create_image_frame(self, request):
        """Get separate frame from existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_image_frame_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def create_image_frame_async(self, request):
        """Get separate frame from existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_image_frame_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def create_image_search(self, request):
        """Create new search context.


        :param request create_image_search_request object with parameters
        :return: SearchContextStatus
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'SearchContextStatus')

    def create_image_search_async(self, request):
        """Create new search context.


        :param request create_image_search_request object with parameters
        :return: SearchContextStatus
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'SearchContextStatus')

    def create_image_tag(self, request):
        """Add tag and reference image to search context. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_image_tag_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def create_image_tag_async(self, request):
        """Add tag and reference image to search context. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_image_tag_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def create_modified_bmp(self, request):
        """Update parameters of BMP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_modified_bmp_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def create_modified_bmp_async(self, request):
        """Update parameters of BMP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_modified_bmp_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def create_modified_emf(self, request):
        """Process existing EMF imaging using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_modified_emf_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def create_modified_emf_async(self, request):
        """Process existing EMF imaging using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_modified_emf_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def create_modified_gif(self, request):
        """Update parameters of GIF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_modified_gif_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def create_modified_gif_async(self, request):
        """Update parameters of GIF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_modified_gif_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def create_modified_jpeg(self, request):
        """Update parameters of JPEG image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_modified_jpeg_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def create_modified_jpeg_async(self, request):
        """Update parameters of JPEG image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_modified_jpeg_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def create_modified_jpeg2000(self, request):
        """Update parameters of JPEG2000 image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_modified_jpeg2000_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def create_modified_jpeg2000_async(self, request):
        """Update parameters of JPEG2000 image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_modified_jpeg2000_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def create_modified_psd(self, request):
        """Update parameters of PSD image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_modified_psd_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def create_modified_psd_async(self, request):
        """Update parameters of PSD image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_modified_psd_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def create_modified_svg(self, request):
        """Update parameters of SVG image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_modified_svg_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def create_modified_svg_async(self, request):
        """Update parameters of SVG image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_modified_svg_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def create_modified_tiff(self, request):
        """Update parameters of TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_modified_tiff_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def create_modified_tiff_async(self, request):
        """Update parameters of TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_modified_tiff_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def create_modified_web_p(self, request):
        """Update parameters of WEBP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_modified_web_p_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def create_modified_web_p_async(self, request):
        """Update parameters of WEBP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_modified_web_p_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def create_modified_wmf(self, request):
        """Process existing WMF image using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_modified_wmf_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def create_modified_wmf_async(self, request):
        """Process existing WMF image using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_modified_wmf_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def create_resized_image(self, request):
        """Resize an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_resized_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def create_resized_image_async(self, request):
        """Resize an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_resized_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def create_rotate_flipped_image(self, request):
        """Rotate and/or flip an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_rotate_flipped_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def create_rotate_flipped_image_async(self, request):
        """Rotate and/or flip an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_rotate_flipped_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def create_saved_image_as(self, request):
        """Export existing image to another format. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.             


        :param request create_saved_image_as_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def create_saved_image_as_async(self, request):
        """Export existing image to another format. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.             


        :param request create_saved_image_as_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def create_updated_image(self, request):
        """Perform scaling, cropping and flipping of an image in a single request. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_updated_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def create_updated_image_async(self, request):
        """Perform scaling, cropping and flipping of an image in a single request. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request create_updated_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def crop_image(self, request):
        """Crop an existing image.


        :param request crop_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def crop_image_async(self, request):
        """Crop an existing image.


        :param request crop_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def delete_file(self, request):
        """Delete file


        :param request delete_file_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_file_async(self, request):
        """Delete file


        :param request delete_file_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_folder(self, request):
        """Delete folder


        :param request delete_folder_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_folder_async(self, request):
        """Delete folder


        :param request delete_folder_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_image_features(self, request):
        """Deletes image features from search context.


        :param request delete_image_features_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_image_features_async(self, request):
        """Deletes image features from search context.


        :param request delete_image_features_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_image_search(self, request):
        """Deletes the search context.


        :param request delete_image_search_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_image_search_async(self, request):
        """Deletes the search context.


        :param request delete_image_search_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_search_image(self, request):
        """Delete image and images features from search context


        :param request delete_search_image_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_search_image_async(self, request):
        """Delete image and images features from search context


        :param request delete_search_image_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def download_file(self, request):
        """Download file


        :param request download_file_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def download_file_async(self, request):
        """Download file


        :param request download_file_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def extract_image_features(self, request):
        """Extract features from image without adding to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request extract_image_features_request object with parameters
        :return: ImageFeatures
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ImageFeatures')

    def extract_image_features_async(self, request):
        """Extract features from image without adding to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request extract_image_features_request object with parameters
        :return: ImageFeatures
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ImageFeatures')

    def extract_image_frame_properties(self, request):
        """Get separate frame properties of existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request extract_image_frame_properties_request object with parameters
        :return: ImagingResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'ImagingResponse')

    def extract_image_frame_properties_async(self, request):
        """Get separate frame properties of existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request extract_image_frame_properties_request object with parameters
        :return: ImagingResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'ImagingResponse')

    def extract_image_properties(self, request):
        """Get properties of an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request extract_image_properties_request object with parameters
        :return: ImagingResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'ImagingResponse')

    def extract_image_properties_async(self, request):
        """Get properties of an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request extract_image_properties_request object with parameters
        :return: ImagingResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'ImagingResponse')

    def filter_effect_image(self, request):
        """Performs filtering effects on an existing image.


        :param request filter_effect_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', 'file')

    def filter_effect_image_async(self, request):
        """Performs filtering effects on an existing image.


        :param request filter_effect_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', 'file')

    def find_image_duplicates(self, request):
        """Find images duplicates.


        :param request find_image_duplicates_request object with parameters
        :return: ImageDuplicatesSet
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ImageDuplicatesSet')

    def find_image_duplicates_async(self, request):
        """Find images duplicates.


        :param request find_image_duplicates_request object with parameters
        :return: ImageDuplicatesSet
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ImageDuplicatesSet')

    def find_images_by_tags(self, request):
        """Find images by tags. Tags JSON string is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request find_images_by_tags_request object with parameters
        :return: SearchResultsSet
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'SearchResultsSet')

    def find_images_by_tags_async(self, request):
        """Find images by tags. Tags JSON string is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request find_images_by_tags_request object with parameters
        :return: SearchResultsSet
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'SearchResultsSet')

    def find_similar_images(self, request):
        """Find similar images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request find_similar_images_request object with parameters
        :return: SearchResultsSet
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'SearchResultsSet')

    def find_similar_images_async(self, request):
        """Find similar images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request find_similar_images_request object with parameters
        :return: SearchResultsSet
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'SearchResultsSet')

    def get_disc_usage(self, request):
        """Get disc usage


        :param request get_disc_usage_request object with parameters
        :return: DiscUsage
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'DiscUsage')

    def get_disc_usage_async(self, request):
        """Get disc usage


        :param request get_disc_usage_request object with parameters
        :return: DiscUsage
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'DiscUsage')

    def get_file_versions(self, request):
        """Get file versions


        :param request get_file_versions_request object with parameters
        :return: FileVersions
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'FileVersions')

    def get_file_versions_async(self, request):
        """Get file versions


        :param request get_file_versions_request object with parameters
        :return: FileVersions
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'FileVersions')

    def get_files_list(self, request):
        """Get all files and folders within a folder


        :param request get_files_list_request object with parameters
        :return: FilesList
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'FilesList')

    def get_files_list_async(self, request):
        """Get all files and folders within a folder


        :param request get_files_list_request object with parameters
        :return: FilesList
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'FilesList')

    def get_image_features(self, request):
        """Gets image features from search context.


        :param request get_image_features_request object with parameters
        :return: ImageFeatures
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ImageFeatures')

    def get_image_features_async(self, request):
        """Gets image features from search context.


        :param request get_image_features_request object with parameters
        :return: ImageFeatures
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ImageFeatures')

    def get_image_frame(self, request):
        """Get separate frame from existing TIFF image.


        :param request get_image_frame_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_image_frame_async(self, request):
        """Get separate frame from existing TIFF image.


        :param request get_image_frame_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_image_frame_properties(self, request):
        """Get separate frame properties of existing TIFF image.


        :param request get_image_frame_properties_request object with parameters
        :return: ImagingResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ImagingResponse')

    def get_image_frame_properties_async(self, request):
        """Get separate frame properties of existing TIFF image.


        :param request get_image_frame_properties_request object with parameters
        :return: ImagingResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ImagingResponse')

    def get_image_properties(self, request):
        """Get properties of an image.


        :param request get_image_properties_request object with parameters
        :return: ImagingResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ImagingResponse')

    def get_image_properties_async(self, request):
        """Get properties of an image.


        :param request get_image_properties_request object with parameters
        :return: ImagingResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ImagingResponse')

    def get_image_search_status(self, request):
        """Gets the search context status.


        :param request get_image_search_status_request object with parameters
        :return: SearchContextStatus
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'SearchContextStatus')

    def get_image_search_status_async(self, request):
        """Gets the search context status.


        :param request get_image_search_status_request object with parameters
        :return: SearchContextStatus
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'SearchContextStatus')

    def get_search_image(self, request):
        """Get image from search context


        :param request get_search_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_search_image_async(self, request):
        """Get image from search context


        :param request get_search_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def modify_bmp(self, request):
        """Update parameters of existing BMP image.


        :param request modify_bmp_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def modify_bmp_async(self, request):
        """Update parameters of existing BMP image.


        :param request modify_bmp_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def modify_emf(self, request):
        """Process existing EMF imaging using given parameters.


        :param request modify_emf_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def modify_emf_async(self, request):
        """Process existing EMF imaging using given parameters.


        :param request modify_emf_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def modify_gif(self, request):
        """Update parameters of existing GIF image.


        :param request modify_gif_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def modify_gif_async(self, request):
        """Update parameters of existing GIF image.


        :param request modify_gif_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def modify_jpeg(self, request):
        """Update parameters of existing JPEG image.


        :param request modify_jpeg_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def modify_jpeg_async(self, request):
        """Update parameters of existing JPEG image.


        :param request modify_jpeg_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def modify_jpeg2000(self, request):
        """Update parameters of existing JPEG2000 image.


        :param request modify_jpeg2000_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def modify_jpeg2000_async(self, request):
        """Update parameters of existing JPEG2000 image.


        :param request modify_jpeg2000_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def modify_psd(self, request):
        """Update parameters of existing PSD image.


        :param request modify_psd_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def modify_psd_async(self, request):
        """Update parameters of existing PSD image.


        :param request modify_psd_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def modify_svg(self, request):
        """Update parameters of existing SVG image.


        :param request modify_svg_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def modify_svg_async(self, request):
        """Update parameters of existing SVG image.


        :param request modify_svg_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def modify_tiff(self, request):
        """Update parameters of existing TIFF image.


        :param request modify_tiff_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def modify_tiff_async(self, request):
        """Update parameters of existing TIFF image.


        :param request modify_tiff_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def modify_web_p(self, request):
        """Update parameters of existing WEBP image.


        :param request modify_web_p_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def modify_web_p_async(self, request):
        """Update parameters of existing WEBP image.


        :param request modify_web_p_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def modify_wmf(self, request):
        """Process existing WMF image using given parameters.


        :param request modify_wmf_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def modify_wmf_async(self, request):
        """Process existing WMF image using given parameters.


        :param request modify_wmf_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def move_file(self, request):
        """Move file


        :param request move_file_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def move_file_async(self, request):
        """Move file


        :param request move_file_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def move_folder(self, request):
        """Move folder


        :param request move_folder_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def move_folder_async(self, request):
        """Move folder


        :param request move_folder_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def object_exists(self, request):
        """Check if file or folder exists


        :param request object_exists_request object with parameters
        :return: ObjectExist
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ObjectExist')

    def object_exists_async(self, request):
        """Check if file or folder exists


        :param request object_exists_request object with parameters
        :return: ObjectExist
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ObjectExist')

    def resize_image(self, request):
        """Resize an existing image.


        :param request resize_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def resize_image_async(self, request):
        """Resize an existing image.


        :param request resize_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def rotate_flip_image(self, request):
        """Rotate and/or flip an existing image.


        :param request rotate_flip_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def rotate_flip_image_async(self, request):
        """Rotate and/or flip an existing image.


        :param request rotate_flip_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def save_image_as(self, request):
        """Export existing image to another format.


        :param request save_image_as_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def save_image_as_async(self, request):
        """Export existing image to another format.


        :param request save_image_as_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def storage_exists(self, request):
        """Check if storage exists


        :param request storage_exists_request object with parameters
        :return: StorageExist
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'StorageExist')

    def storage_exists_async(self, request):
        """Check if storage exists


        :param request storage_exists_request object with parameters
        :return: StorageExist
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'StorageExist')

    def update_image(self, request):
        """Perform scaling, cropping and flipping of an existing image in a single request.


        :param request update_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def update_image_async(self, request):
        """Perform scaling, cropping and flipping of an existing image in a single request.


        :param request update_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def update_image_features(self, request):
        """Update images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request update_image_features_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def update_image_features_async(self, request):
        """Update images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request update_image_features_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def update_search_image(self, request):
        """Update image and images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request update_search_image_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def update_search_image_async(self, request):
        """Update image and images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request update_search_image_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def upload_file(self, request):
        """Upload file


        :param request upload_file_request object with parameters
        :return: FilesUploadResult
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', 'FilesUploadResult')

    def upload_file_async(self, request):
        """Upload file


        :param request upload_file_request object with parameters
        :return: FilesUploadResult
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', 'FilesUploadResult')

    def __make_request(self, http_request, method, return_type):
        def call_api():
            return self.api_client.call_api(
                resource_path=http_request.resource_path,
                method=method,
                path_params=http_request.path_params,
                query_params=http_request.query_params,
                header_params=http_request.header_params,
                body=http_request.body_params,
                post_params=http_request.form_params,
                files=http_request.files,
                response_type=return_type,
                auth_settings=http_request.auth_settings,
                _return_http_data_only=http_request.return_http_data_only,
                _preload_content=http_request.preload_content,
                _request_timeout=http_request.request_timeout,
                collection_formats=http_request.collection_formats)

        try:
            return call_api()
        except ApiException as ex:
            if ex.code == 401:
                self.__request_token()
                return call_api()
            raise

    def __make_request_async(self, http_request, method, return_type):
        def call_api_async():
            self.api_client.call_api_async(
                resource_path=http_request.resource_path,
                method=method,
                path_params=http_request.path_params,
                query_params=http_request.query_params,
                header_params=http_request.header_params,
                body=http_request.body_params,
                post_params=http_request.form_params,
                files=http_request.files,
                response_type=return_type,
                auth_settings=http_request.auth_settings,
                _return_http_data_only=http_request.return_http_data_only,
                _preload_content=http_request.preload_content,
                _request_timeout=http_request.request_timeout,
                collection_formats=http_request.collection_formats)

        try:
            return call_api_async()
        except ApiException as ex:
            if ex.code == 401:
                self.__request_token()
                return call_api_async()
            raise

    def __request_token(self):
        config = self.api_client.configuration
        request_url = "/connect/token"
        form_params = [('grant_type', 'client_credentials'), ('client_id', config.api_key['app_sid']),
                       ('client_secret', config.api_key['api_key'])]

        header_params = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

        api_version = self.api_client.configuration.api_version
        self.api_client.configuration.api_version = ''

        data = self.api_client.call_api(request_url, 'POST',
                                        {},
                                        [],
                                        header_params,
                                        post_params=form_params,
                                        response_type='object',
                                        files={}, _return_http_data_only=True)
        access_token = data['access_token'] if six.PY3 else data['access_token'].encode('utf8')
        self.api_client.configuration.access_token = access_token

        self.api_client.configuration.api_version = api_version

