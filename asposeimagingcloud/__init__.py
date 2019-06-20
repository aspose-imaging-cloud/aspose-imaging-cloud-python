#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="__init__.py">
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

# import apis into sdk package
from asposeimagingcloud.api.imaging_api import ImagingApi

# import ApiClient
from asposeimagingcloud.api_client import ApiClient
from asposeimagingcloud.configuration import Configuration
# import models into sdk package
from asposeimagingcloud.models.bmp_properties import BmpProperties
from asposeimagingcloud.models.dicom_properties import DicomProperties
from asposeimagingcloud.models.disc_usage import DiscUsage
from asposeimagingcloud.models.djvu_properties import DjvuProperties
from asposeimagingcloud.models.dng_properties import DngProperties
from asposeimagingcloud.models.error import Error
from asposeimagingcloud.models.error_details import ErrorDetails
from asposeimagingcloud.models.exif_data import ExifData
from asposeimagingcloud.models.file_versions import FileVersions
from asposeimagingcloud.models.files_list import FilesList
from asposeimagingcloud.models.files_upload_result import FilesUploadResult
from asposeimagingcloud.models.gif_properties import GifProperties
from asposeimagingcloud.models.image_duplicates import ImageDuplicates
from asposeimagingcloud.models.image_duplicates_set import ImageDuplicatesSet
from asposeimagingcloud.models.image_features import ImageFeatures
from asposeimagingcloud.models.imaging_response import ImagingResponse
from asposeimagingcloud.models.jfif_data import JfifData
from asposeimagingcloud.models.jpeg2000_properties import Jpeg2000Properties
from asposeimagingcloud.models.jpeg_properties import JpegProperties
from asposeimagingcloud.models.object_exist import ObjectExist
from asposeimagingcloud.models.odg_metadata import OdgMetadata
from asposeimagingcloud.models.odg_page import OdgPage
from asposeimagingcloud.models.odg_properties import OdgProperties
from asposeimagingcloud.models.png_properties import PngProperties
from asposeimagingcloud.models.psd_properties import PsdProperties
from asposeimagingcloud.models.search_context_status import SearchContextStatus
from asposeimagingcloud.models.search_result import SearchResult
from asposeimagingcloud.models.search_results_set import SearchResultsSet
from asposeimagingcloud.models.storage_exist import StorageExist
from asposeimagingcloud.models.storage_file import StorageFile
from asposeimagingcloud.models.tiff_frame import TiffFrame
from asposeimagingcloud.models.tiff_options import TiffOptions
from asposeimagingcloud.models.tiff_properties import TiffProperties
from asposeimagingcloud.models.web_p_properties import WebPProperties
from asposeimagingcloud.models.file_version import FileVersion
from asposeimagingcloud.models.jpeg_exif_data import JpegExifData
from asposeimagingcloud.models.requests.copy_file_request import CopyFileRequest
from asposeimagingcloud.models.requests.copy_folder_request import CopyFolderRequest
from asposeimagingcloud.models.requests.create_folder_request import CreateFolderRequest
from asposeimagingcloud.models.requests.delete_file_request import DeleteFileRequest
from asposeimagingcloud.models.requests.delete_folder_request import DeleteFolderRequest
from asposeimagingcloud.models.requests.delete_search_context_image_features_request import \
    DeleteSearchContextImageFeaturesRequest
from asposeimagingcloud.models.requests.delete_search_context_image_request import DeleteSearchContextImageRequest
from asposeimagingcloud.models.requests.delete_search_context_request import DeleteSearchContextRequest
from asposeimagingcloud.models.requests.download_file_request import DownloadFileRequest
from asposeimagingcloud.models.requests.get_disc_usage_request import GetDiscUsageRequest
from asposeimagingcloud.models.requests.get_file_versions_request import GetFileVersionsRequest
from asposeimagingcloud.models.requests.get_files_list_request import GetFilesListRequest
from asposeimagingcloud.models.requests.get_image_bmp_request import GetImageBmpRequest
from asposeimagingcloud.models.requests.get_image_crop_request import GetImageCropRequest
from asposeimagingcloud.models.requests.get_image_emf_request import GetImageEmfRequest
from asposeimagingcloud.models.requests.get_image_frame_properties_request import GetImageFramePropertiesRequest
from asposeimagingcloud.models.requests.get_image_frame_request import GetImageFrameRequest
from asposeimagingcloud.models.requests.get_image_gif_request import GetImageGifRequest
from asposeimagingcloud.models.requests.get_image_jpeg2000_request import GetImageJpeg2000Request
from asposeimagingcloud.models.requests.get_image_jpg_request import GetImageJpgRequest
from asposeimagingcloud.models.requests.get_image_properties_request import GetImagePropertiesRequest
from asposeimagingcloud.models.requests.get_image_psd_request import GetImagePsdRequest
from asposeimagingcloud.models.requests.get_image_resize_request import GetImageResizeRequest
from asposeimagingcloud.models.requests.get_image_rotate_flip_request import GetImageRotateFlipRequest
from asposeimagingcloud.models.requests.get_image_save_as_request import GetImageSaveAsRequest
from asposeimagingcloud.models.requests.get_image_tiff_request import GetImageTiffRequest
from asposeimagingcloud.models.requests.get_image_update_request import GetImageUpdateRequest
from asposeimagingcloud.models.requests.get_image_web_p_request import GetImageWebPRequest
from asposeimagingcloud.models.requests.get_image_wmf_request import GetImageWmfRequest
from asposeimagingcloud.models.requests.get_search_context_extract_image_features_request import \
    GetSearchContextExtractImageFeaturesRequest
from asposeimagingcloud.models.requests.get_search_context_find_duplicates_request import \
    GetSearchContextFindDuplicatesRequest
from asposeimagingcloud.models.requests.get_search_context_find_similar_request import \
    GetSearchContextFindSimilarRequest
from asposeimagingcloud.models.requests.get_search_context_image_features_request import \
    GetSearchContextImageFeaturesRequest
from asposeimagingcloud.models.requests.get_search_context_image_request import GetSearchContextImageRequest
from asposeimagingcloud.models.requests.get_search_context_status_request import GetSearchContextStatusRequest
from asposeimagingcloud.models.requests.get_tiff_to_fax_request import GetTiffToFaxRequest
from asposeimagingcloud.models.requests.http_request import HttpRequest
from asposeimagingcloud.models.requests.imaging_request import ImagingRequest
from asposeimagingcloud.models.requests.move_file_request import MoveFileRequest
from asposeimagingcloud.models.requests.move_folder_request import MoveFolderRequest
from asposeimagingcloud.models.requests.object_exists_request import ObjectExistsRequest
from asposeimagingcloud.models.requests.post_create_search_context_request import PostCreateSearchContextRequest
from asposeimagingcloud.models.requests.post_image_bmp_request import PostImageBmpRequest
from asposeimagingcloud.models.requests.post_image_crop_request import PostImageCropRequest
from asposeimagingcloud.models.requests.post_image_emf_request import PostImageEmfRequest
from asposeimagingcloud.models.requests.post_image_frame_properties_request import PostImageFramePropertiesRequest
from asposeimagingcloud.models.requests.post_image_frame_request import PostImageFrameRequest
from asposeimagingcloud.models.requests.post_image_gif_request import PostImageGifRequest
from asposeimagingcloud.models.requests.post_image_jpeg2000_request import PostImageJpeg2000Request
from asposeimagingcloud.models.requests.post_image_jpg_request import PostImageJpgRequest
from asposeimagingcloud.models.requests.post_image_properties_request import PostImagePropertiesRequest
from asposeimagingcloud.models.requests.post_image_psd_request import PostImagePsdRequest
from asposeimagingcloud.models.requests.post_image_resize_request import PostImageResizeRequest
from asposeimagingcloud.models.requests.post_image_rotate_flip_request import PostImageRotateFlipRequest
from asposeimagingcloud.models.requests.post_image_save_as_request import PostImageSaveAsRequest
from asposeimagingcloud.models.requests.post_image_tiff_request import PostImageTiffRequest
from asposeimagingcloud.models.requests.post_image_update_request import PostImageUpdateRequest
from asposeimagingcloud.models.requests.post_image_web_p_request import PostImageWebPRequest
from asposeimagingcloud.models.requests.post_image_wmf_request import PostImageWmfRequest
from asposeimagingcloud.models.requests.post_search_context_add_image_request import PostSearchContextAddImageRequest
from asposeimagingcloud.models.requests.post_search_context_add_tag_request import PostSearchContextAddTagRequest
from asposeimagingcloud.models.requests.post_search_context_compare_images_request import \
    PostSearchContextCompareImagesRequest
from asposeimagingcloud.models.requests.post_search_context_extract_image_features_request import \
    PostSearchContextExtractImageFeaturesRequest
from asposeimagingcloud.models.requests.post_search_context_find_by_tags_request import \
    PostSearchContextFindByTagsRequest
from asposeimagingcloud.models.requests.post_tiff_append_request import PostTiffAppendRequest
from asposeimagingcloud.models.requests.put_search_context_image_features_request import \
    PutSearchContextImageFeaturesRequest
from asposeimagingcloud.models.requests.put_search_context_image_request import PutSearchContextImageRequest
from asposeimagingcloud.models.requests.storage_exists_request import StorageExistsRequest
from asposeimagingcloud.models.requests.upload_file_request import UploadFileRequest
