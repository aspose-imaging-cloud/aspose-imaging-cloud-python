#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="imaging_api.py">
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

from __future__ import absolute_import

import six
from asposeimagingcloud.rest import ApiException
from asposeimagingcloud.api_client import ApiClient


class ImagingApi(object):
    """
    Aspose.Imaging Cloud API

    :param api_client: an api client to perform http requests
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

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

    def create_folder(self, request):
        """Create the folder


        :param request create_folder_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def create_folder_async(self, request):
        """Create the folder


        :param request create_folder_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

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

    def delete_search_context(self, request):
        """Deletes the search context.


        :param request delete_search_context_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_search_context_async(self, request):
        """Deletes the search context.


        :param request delete_search_context_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_search_context_image(self, request):
        """Delete image and images features from search context


        :param request delete_search_context_image_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_search_context_image_async(self, request):
        """Delete image and images features from search context


        :param request delete_search_context_image_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'DELETE', None)

    def delete_search_context_image_features(self, request):
        """Deletes image features from search context.


        :param request delete_search_context_image_features_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'DELETE', None)

    def delete_search_context_image_features_async(self, request):
        """Deletes image features from search context.


        :param request delete_search_context_image_features_request object with parameters
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

    def get_image_bmp(self, request):
        """Update parameters of existing BMP image.


        :param request get_image_bmp_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_image_bmp_async(self, request):
        """Update parameters of existing BMP image.


        :param request get_image_bmp_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_image_crop(self, request):
        """Crop an existing image.


        :param request get_image_crop_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_image_crop_async(self, request):
        """Crop an existing image.


        :param request get_image_crop_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_image_emf(self, request):
        """Process existing EMF imaging using given parameters.


        :param request get_image_emf_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_image_emf_async(self, request):
        """Process existing EMF imaging using given parameters.


        :param request get_image_emf_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

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
        return self.__make_request_async(
            http_request, 'GET', 'ImagingResponse')

    def get_image_gif(self, request):
        """Update parameters of existing GIF image.


        :param request get_image_gif_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_image_gif_async(self, request):
        """Update parameters of existing GIF image.


        :param request get_image_gif_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_image_jpeg2000(self, request):
        """Update parameters of existing JPEG2000 image.


        :param request get_image_jpeg2000_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_image_jpeg2000_async(self, request):
        """Update parameters of existing JPEG2000 image.


        :param request get_image_jpeg2000_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_image_jpg(self, request):
        """Update parameters of existing JPEG image.


        :param request get_image_jpg_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_image_jpg_async(self, request):
        """Update parameters of existing JPEG image.


        :param request get_image_jpg_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

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
        return self.__make_request_async(
            http_request, 'GET', 'ImagingResponse')

    def get_image_psd(self, request):
        """Update parameters of existing PSD image.


        :param request get_image_psd_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_image_psd_async(self, request):
        """Update parameters of existing PSD image.


        :param request get_image_psd_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_image_resize(self, request):
        """Resize an existing image.


        :param request get_image_resize_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_image_resize_async(self, request):
        """Resize an existing image.


        :param request get_image_resize_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_image_rotate_flip(self, request):
        """Rotate and/or flip an existing image.


        :param request get_image_rotate_flip_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_image_rotate_flip_async(self, request):
        """Rotate and/or flip an existing image.


        :param request get_image_rotate_flip_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_image_save_as(self, request):
        """Export existing image to another format.


        :param request get_image_save_as_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_image_save_as_async(self, request):
        """Export existing image to another format.


        :param request get_image_save_as_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_image_tiff(self, request):
        """Update parameters of existing TIFF image.


        :param request get_image_tiff_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_image_tiff_async(self, request):
        """Update parameters of existing TIFF image.


        :param request get_image_tiff_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_image_update(self, request):
        """Perform scaling, cropping and flipping of an existing image in a single request.


        :param request get_image_update_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_image_update_async(self, request):
        """Perform scaling, cropping and flipping of an existing image in a single request.


        :param request get_image_update_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_image_web_p(self, request):
        """Update parameters of existing WEBP image.


        :param request get_image_web_p_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_image_web_p_async(self, request):
        """Update parameters of existing WEBP image.


        :param request get_image_web_p_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_image_wmf(self, request):
        """Process existing WMF image using given parameters.


        :param request get_image_wmf_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_image_wmf_async(self, request):
        """Process existing WMF image using given parameters.


        :param request get_image_wmf_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_search_context_extract_image_features(self, request):
        """Extract features from image without adding to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request get_search_context_extract_image_features_request object with parameters
        :return: ImageFeatures
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ImageFeatures')

    def get_search_context_extract_image_features_async(self, request):
        """Extract features from image without adding to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request get_search_context_extract_image_features_request object with parameters
        :return: ImageFeatures
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ImageFeatures')

    def get_search_context_find_duplicates(self, request):
        """Find images duplicates.


        :param request get_search_context_find_duplicates_request object with parameters
        :return: ImageDuplicatesSet
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ImageDuplicatesSet')

    def get_search_context_find_duplicates_async(self, request):
        """Find images duplicates.


        :param request get_search_context_find_duplicates_request object with parameters
        :return: ImageDuplicatesSet
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(
            http_request, 'GET', 'ImageDuplicatesSet')

    def get_search_context_find_similar(self, request):
        """Find similar images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request get_search_context_find_similar_request object with parameters
        :return: SearchResultsSet
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'SearchResultsSet')

    def get_search_context_find_similar_async(self, request):
        """Find similar images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request get_search_context_find_similar_request object with parameters
        :return: SearchResultsSet
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(
            http_request, 'GET', 'SearchResultsSet')

    def get_search_context_image(self, request):
        """Get image from search context


        :param request get_search_context_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_search_context_image_async(self, request):
        """Get image from search context


        :param request get_search_context_image_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'file')

    def get_search_context_image_features(self, request):
        """Gets image features from search context.


        :param request get_search_context_image_features_request object with parameters
        :return: ImageFeatures
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'ImageFeatures')

    def get_search_context_image_features_async(self, request):
        """Gets image features from search context.


        :param request get_search_context_image_features_request object with parameters
        :return: ImageFeatures
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'GET', 'ImageFeatures')

    def get_search_context_status(self, request):
        """Gets the search context status.


        :param request get_search_context_status_request object with parameters
        :return: SearchContextStatus
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'SearchContextStatus')

    def get_search_context_status_async(self, request):
        """Gets the search context status.


        :param request get_search_context_status_request object with parameters
        :return: SearchContextStatus
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(
            http_request, 'GET', 'SearchContextStatus')

    def get_tiff_to_fax(self, request):
        """Update parameters of existing TIFF image accordingly to fax parameters.


        :param request get_tiff_to_fax_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'GET', 'file')

    def get_tiff_to_fax_async(self, request):
        """Update parameters of existing TIFF image accordingly to fax parameters.


        :param request get_tiff_to_fax_request object with parameters
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

    def post_create_search_context(self, request):
        """Create new search context.


        :param request post_create_search_context_request object with parameters
        :return: SearchContextStatus
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'SearchContextStatus')

    def post_create_search_context_async(self, request):
        """Create new search context.


        :param request post_create_search_context_request object with parameters
        :return: SearchContextStatus
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(
            http_request, 'POST', 'SearchContextStatus')

    def post_image_bmp(self, request):
        """Update parameters of BMP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_bmp_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def post_image_bmp_async(self, request):
        """Update parameters of BMP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_bmp_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def post_image_crop(self, request):
        """Crop an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_crop_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def post_image_crop_async(self, request):
        """Crop an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_crop_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def post_image_emf(self, request):
        """Process existing EMF imaging using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_emf_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def post_image_emf_async(self, request):
        """Process existing EMF imaging using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_emf_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def post_image_frame(self, request):
        """Get separate frame from existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_frame_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def post_image_frame_async(self, request):
        """Get separate frame from existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_frame_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def post_image_frame_properties(self, request):
        """Get separate frame properties of existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_frame_properties_request object with parameters
        :return: ImagingResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'ImagingResponse')

    def post_image_frame_properties_async(self, request):
        """Get separate frame properties of existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_frame_properties_request object with parameters
        :return: ImagingResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(
            http_request, 'POST', 'ImagingResponse')

    def post_image_gif(self, request):
        """Update parameters of GIF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_gif_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def post_image_gif_async(self, request):
        """Update parameters of GIF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_gif_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def post_image_jpeg2000(self, request):
        """Update parameters of JPEG2000 image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_jpeg2000_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def post_image_jpeg2000_async(self, request):
        """Update parameters of JPEG2000 image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_jpeg2000_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def post_image_jpg(self, request):
        """Update parameters of JPEG image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_jpg_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def post_image_jpg_async(self, request):
        """Update parameters of JPEG image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_jpg_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def post_image_properties(self, request):
        """Get properties of an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_properties_request object with parameters
        :return: ImagingResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'ImagingResponse')

    def post_image_properties_async(self, request):
        """Get properties of an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_properties_request object with parameters
        :return: ImagingResponse
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(
            http_request, 'POST', 'ImagingResponse')

    def post_image_psd(self, request):
        """Update parameters of PSD image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_psd_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def post_image_psd_async(self, request):
        """Update parameters of PSD image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_psd_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def post_image_resize(self, request):
        """Resize an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_resize_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def post_image_resize_async(self, request):
        """Resize an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_resize_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def post_image_rotate_flip(self, request):
        """Rotate and/or flip an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_rotate_flip_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def post_image_rotate_flip_async(self, request):
        """Rotate and/or flip an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_rotate_flip_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def post_image_save_as(self, request):
        """Export existing image to another format. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_save_as_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def post_image_save_as_async(self, request):
        """Export existing image to another format. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_save_as_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def post_image_tiff(self, request):
        """Update parameters of TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_tiff_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def post_image_tiff_async(self, request):
        """Update parameters of TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_tiff_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def post_image_update(self, request):
        """Perform scaling, cropping and flipping of an image in a single request. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_update_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def post_image_update_async(self, request):
        """Perform scaling, cropping and flipping of an image in a single request. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_update_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def post_image_web_p(self, request):
        """Update parameters of WEBP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_web_p_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def post_image_web_p_async(self, request):
        """Update parameters of WEBP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_web_p_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def post_image_wmf(self, request):
        """Process existing WMF image using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_wmf_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'file')

    def post_image_wmf_async(self, request):
        """Process existing WMF image using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_image_wmf_request object with parameters
        :return: file
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', 'file')

    def post_search_context_add_image(self, request):
        """Add image and images features to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_search_context_add_image_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def post_search_context_add_image_async(self, request):
        """Add image and images features to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_search_context_add_image_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def post_search_context_add_tag(self, request):
        """Add tag and reference image to search context. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_search_context_add_tag_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def post_search_context_add_tag_async(self, request):
        """Add tag and reference image to search context. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_search_context_add_tag_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def post_search_context_compare_images(self, request):
        """Compare two images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_search_context_compare_images_request object with parameters
        :return: SearchResultsSet
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'SearchResultsSet')

    def post_search_context_compare_images_async(self, request):
        """Compare two images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_search_context_compare_images_request object with parameters
        :return: SearchResultsSet
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(
            http_request, 'POST', 'SearchResultsSet')

    def post_search_context_extract_image_features(self, request):
        """Extract images features and add them to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_search_context_extract_image_features_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def post_search_context_extract_image_features_async(self, request):
        """Extract images features and add them to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_search_context_extract_image_features_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def post_search_context_find_by_tags(self, request):
        """Find images by tags. Tags JSON string is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_search_context_find_by_tags_request object with parameters
        :return: SearchResultsSet
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'SearchResultsSet')

    def post_search_context_find_by_tags_async(self, request):
        """Find images by tags. Tags JSON string is passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request post_search_context_find_by_tags_request object with parameters
        :return: SearchResultsSet
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(
            http_request, 'POST', 'SearchResultsSet')

    def post_tiff_append(self, request):
        """Appends existing TIFF image to another existing TIFF image (i.e. merges TIFF images).


        :param request post_tiff_append_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', None)

    def post_tiff_append_async(self, request):
        """Appends existing TIFF image to another existing TIFF image (i.e. merges TIFF images).


        :param request post_tiff_append_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'POST', None)

    def put_search_context_image(self, request):
        """Update image and images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request put_search_context_image_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def put_search_context_image_async(self, request):
        """Update image and images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request put_search_context_image_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

    def put_search_context_image_features(self, request):
        """Update images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request put_search_context_image_features_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'PUT', None)

    def put_search_context_image_features_async(self, request):
        """Update images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.


        :param request put_search_context_image_features_request object with parameters
        :return: None
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(http_request, 'PUT', None)

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

    def upload_file(self, request):
        """Upload file


        :param request upload_file_request object with parameters
        :return: FilesUploadResult
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request(http_request, 'POST', 'FilesUploadResult')

    def upload_file_async(self, request):
        """Upload file


        :param request upload_file_request object with parameters
        :return: FilesUploadResult
        """
        http_request = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(
            http_request, 'POST', 'FilesUploadResult')

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
            if ex.status == 401:
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
            if ex.status == 401:
                self.__request_token()
                return call_api_async()
            raise

    def __request_token(self):
        config = self.api_client.configuration
        request_url = "/connect/token"
        form_params = [
            ('grant_type',
             'client_credentials'),
            ('client_id',
             config.api_key['app_sid']),
            ('client_secret',
             config.api_key['api_key'])]

        header_params = {'Accept': 'application/json',
                         'Content-Type': 'application/x-www-form-urlencoded'}

        api_version = self.api_client.configuration.api_version
        self.api_client.configuration.api_version = ''

        data = self.api_client.call_api(request_url, 'POST',
                                        {},
                                        [],
                                        header_params,
                                        post_params=form_params,
                                        response_type='object',
                                        files={}, _return_http_data_only=True)
        access_token = data['access_token'] if six.PY3 else data['access_token'].encode(
            'utf8')
        self.api_client.configuration.access_token = access_token

        self.api_client.configuration.api_version = api_version
