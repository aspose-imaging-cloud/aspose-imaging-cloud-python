#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="__init__.py">
#    Copyright (c) 2018-2020 Aspose Pty Ltd. All rights reserved.
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
from asposeimagingcloud.models.filter_properties_base import FilterPropertiesBase
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
from asposeimagingcloud.models.svg_properties import SvgProperties
from asposeimagingcloud.models.tiff_frame import TiffFrame
from asposeimagingcloud.models.tiff_options import TiffOptions
from asposeimagingcloud.models.tiff_properties import TiffProperties
from asposeimagingcloud.models.web_p_properties import WebPProperties
from asposeimagingcloud.models.big_rectangular_filter_properties import BigRectangularFilterProperties
from asposeimagingcloud.models.bilateral_smoothing_filter_properties import BilateralSmoothingFilterProperties
from asposeimagingcloud.models.convolution_filter_properties import ConvolutionFilterProperties
from asposeimagingcloud.models.deconvolution_filter_properties import DeconvolutionFilterProperties
from asposeimagingcloud.models.file_version import FileVersion
from asposeimagingcloud.models.jpeg_exif_data import JpegExifData
from asposeimagingcloud.models.median_filter_properties import MedianFilterProperties
from asposeimagingcloud.models.small_rectangular_filter_properties import SmallRectangularFilterProperties
from asposeimagingcloud.models.gauss_wiener_filter_properties import GaussWienerFilterProperties
from asposeimagingcloud.models.gaussian_blur_filter_properties import GaussianBlurFilterProperties
from asposeimagingcloud.models.motion_wiener_filter_properties import MotionWienerFilterProperties
from asposeimagingcloud.models.sharpen_filter_properties import SharpenFilterProperties

from asposeimagingcloud.models.requests.add_search_image_request import AddSearchImageRequest
from asposeimagingcloud.models.requests.append_tiff_request import AppendTiffRequest
from asposeimagingcloud.models.requests.compare_images_request import CompareImagesRequest
from asposeimagingcloud.models.requests.convert_tiff_to_fax_request import ConvertTiffToFaxRequest
from asposeimagingcloud.models.requests.copy_file_request import CopyFileRequest
from asposeimagingcloud.models.requests.copy_folder_request import CopyFolderRequest
from asposeimagingcloud.models.requests.create_cropped_image_request import CreateCroppedImageRequest
from asposeimagingcloud.models.requests.create_deskewed_image_request import CreateDeskewedImageRequest
from asposeimagingcloud.models.requests.create_folder_request import CreateFolderRequest
from asposeimagingcloud.models.requests.create_grayscaled_image_request import CreateGrayscaledImageRequest
from asposeimagingcloud.models.requests.create_image_features_request import CreateImageFeaturesRequest
from asposeimagingcloud.models.requests.create_image_frame_range_request import CreateImageFrameRangeRequest
from asposeimagingcloud.models.requests.create_image_frame_request import CreateImageFrameRequest
from asposeimagingcloud.models.requests.create_image_search_request import CreateImageSearchRequest
from asposeimagingcloud.models.requests.create_image_tag_request import CreateImageTagRequest
from asposeimagingcloud.models.requests.create_modified_bmp_request import CreateModifiedBmpRequest
from asposeimagingcloud.models.requests.create_modified_emf_request import CreateModifiedEmfRequest
from asposeimagingcloud.models.requests.create_modified_gif_request import CreateModifiedGifRequest
from asposeimagingcloud.models.requests.create_modified_jpeg2000_request import CreateModifiedJpeg2000Request
from asposeimagingcloud.models.requests.create_modified_jpeg_request import CreateModifiedJpegRequest
from asposeimagingcloud.models.requests.create_modified_psd_request import CreateModifiedPsdRequest
from asposeimagingcloud.models.requests.create_modified_svg_request import CreateModifiedSvgRequest
from asposeimagingcloud.models.requests.create_modified_tiff_request import CreateModifiedTiffRequest
from asposeimagingcloud.models.requests.create_modified_web_p_request import CreateModifiedWebPRequest
from asposeimagingcloud.models.requests.create_modified_wmf_request import CreateModifiedWmfRequest
from asposeimagingcloud.models.requests.create_resized_image_request import CreateResizedImageRequest
from asposeimagingcloud.models.requests.create_rotate_flipped_image_request import CreateRotateFlippedImageRequest
from asposeimagingcloud.models.requests.create_saved_image_as_request import CreateSavedImageAsRequest
from asposeimagingcloud.models.requests.create_updated_image_request import CreateUpdatedImageRequest
from asposeimagingcloud.models.requests.create_web_site_image_features_request import CreateWebSiteImageFeaturesRequest
from asposeimagingcloud.models.requests.crop_image_request import CropImageRequest
from asposeimagingcloud.models.requests.delete_file_request import DeleteFileRequest
from asposeimagingcloud.models.requests.delete_folder_request import DeleteFolderRequest
from asposeimagingcloud.models.requests.delete_image_features_request import DeleteImageFeaturesRequest
from asposeimagingcloud.models.requests.delete_image_search_request import DeleteImageSearchRequest
from asposeimagingcloud.models.requests.delete_search_image_request import DeleteSearchImageRequest
from asposeimagingcloud.models.requests.deskew_image_request import DeskewImageRequest
from asposeimagingcloud.models.requests.download_file_request import DownloadFileRequest
from asposeimagingcloud.models.requests.extract_image_features_request import ExtractImageFeaturesRequest
from asposeimagingcloud.models.requests.extract_image_frame_properties_request import ExtractImageFramePropertiesRequest
from asposeimagingcloud.models.requests.extract_image_properties_request import ExtractImagePropertiesRequest
from asposeimagingcloud.models.requests.filter_effect_image_request import FilterEffectImageRequest
from asposeimagingcloud.models.requests.find_images_by_tags_request import FindImagesByTagsRequest
from asposeimagingcloud.models.requests.find_image_duplicates_request import FindImageDuplicatesRequest
from asposeimagingcloud.models.requests.find_similar_images_request import FindSimilarImagesRequest
from asposeimagingcloud.models.requests.get_disc_usage_request import GetDiscUsageRequest
from asposeimagingcloud.models.requests.get_files_list_request import GetFilesListRequest
from asposeimagingcloud.models.requests.get_file_versions_request import GetFileVersionsRequest
from asposeimagingcloud.models.requests.get_image_features_request import GetImageFeaturesRequest
from asposeimagingcloud.models.requests.get_image_frame_properties_request import GetImageFramePropertiesRequest
from asposeimagingcloud.models.requests.get_image_frame_range_request import GetImageFrameRangeRequest
from asposeimagingcloud.models.requests.get_image_frame_request import GetImageFrameRequest
from asposeimagingcloud.models.requests.get_image_properties_request import GetImagePropertiesRequest
from asposeimagingcloud.models.requests.get_image_search_status_request import GetImageSearchStatusRequest
from asposeimagingcloud.models.requests.get_search_image_request import GetSearchImageRequest
from asposeimagingcloud.models.requests.grayscale_image_request import GrayscaleImageRequest
from asposeimagingcloud.models.requests.http_request import HttpRequest
from asposeimagingcloud.models.requests.imaging_request import ImagingRequest
from asposeimagingcloud.models.requests.modify_bmp_request import ModifyBmpRequest
from asposeimagingcloud.models.requests.modify_emf_request import ModifyEmfRequest
from asposeimagingcloud.models.requests.modify_gif_request import ModifyGifRequest
from asposeimagingcloud.models.requests.modify_jpeg2000_request import ModifyJpeg2000Request
from asposeimagingcloud.models.requests.modify_jpeg_request import ModifyJpegRequest
from asposeimagingcloud.models.requests.modify_psd_request import ModifyPsdRequest
from asposeimagingcloud.models.requests.modify_svg_request import ModifySvgRequest
from asposeimagingcloud.models.requests.modify_tiff_request import ModifyTiffRequest
from asposeimagingcloud.models.requests.modify_web_p_request import ModifyWebPRequest
from asposeimagingcloud.models.requests.modify_wmf_request import ModifyWmfRequest
from asposeimagingcloud.models.requests.move_file_request import MoveFileRequest
from asposeimagingcloud.models.requests.move_folder_request import MoveFolderRequest
from asposeimagingcloud.models.requests.object_exists_request import ObjectExistsRequest
from asposeimagingcloud.models.requests.resize_image_request import ResizeImageRequest
from asposeimagingcloud.models.requests.rotate_flip_image_request import RotateFlipImageRequest
from asposeimagingcloud.models.requests.save_image_as_request import SaveImageAsRequest
from asposeimagingcloud.models.requests.storage_exists_request import StorageExistsRequest
from asposeimagingcloud.models.requests.update_image_features_request import UpdateImageFeaturesRequest
from asposeimagingcloud.models.requests.update_image_request import UpdateImageRequest
from asposeimagingcloud.models.requests.update_search_image_request import UpdateSearchImageRequest
from asposeimagingcloud.models.requests.upload_file_request import UploadFileRequest

