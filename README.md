# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 3.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ImagingApi(swagger_client.ApiClient(configuration))
src_path = 'src_path_example' # str | Source file path e.g. '/folder/file.ext'
dest_path = 'dest_path_example' # str | Destination file path
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)
version_id = 'version_id_example' # str | File version ID to copy (optional)

try:
    # Copy file
    api_instance.copy_file(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)
except ApiException as e:
    print("Exception when calling ImagingApi->copy_file: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api-qa.aspose.cloud/v3.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ImagingApi* | [**copy_file**](docs/ImagingApi.md#copy_file) | **PUT** /imaging/storage/file/copy/{srcPath} | Copy file
*ImagingApi* | [**copy_folder**](docs/ImagingApi.md#copy_folder) | **PUT** /imaging/storage/folder/copy/{srcPath} | Copy folder
*ImagingApi* | [**create_folder**](docs/ImagingApi.md#create_folder) | **POST** /imaging/storage/folder/{path} | Create the folder
*ImagingApi* | [**delete_file**](docs/ImagingApi.md#delete_file) | **DELETE** /imaging/storage/file/{path} | Delete file
*ImagingApi* | [**delete_folder**](docs/ImagingApi.md#delete_folder) | **DELETE** /imaging/storage/folder/{path} | Delete folder
*ImagingApi* | [**delete_search_context**](docs/ImagingApi.md#delete_search_context) | **DELETE** /imaging/ai/imageSearch/{searchContextId} | Deletes the search context.
*ImagingApi* | [**delete_search_context_image**](docs/ImagingApi.md#delete_search_context_image) | **DELETE** /imaging/ai/imageSearch/{searchContextId}/image | Delete image and images features from search context
*ImagingApi* | [**delete_search_context_image_features**](docs/ImagingApi.md#delete_search_context_image_features) | **DELETE** /imaging/ai/imageSearch/{searchContextId}/features | Deletes image features from search context.
*ImagingApi* | [**download_file**](docs/ImagingApi.md#download_file) | **GET** /imaging/storage/file/{path} | Download file
*ImagingApi* | [**get_disc_usage**](docs/ImagingApi.md#get_disc_usage) | **GET** /imaging/storage/disc | Get disc usage
*ImagingApi* | [**get_file_versions**](docs/ImagingApi.md#get_file_versions) | **GET** /imaging/storage/version/{path} | Get file versions
*ImagingApi* | [**get_files_list**](docs/ImagingApi.md#get_files_list) | **GET** /imaging/storage/folder/{path} | Get all files and folders within a folder
*ImagingApi* | [**get_image_bmp**](docs/ImagingApi.md#get_image_bmp) | **GET** /imaging/{name}/bmp | Update parameters of existing BMP image.
*ImagingApi* | [**get_image_crop**](docs/ImagingApi.md#get_image_crop) | **GET** /imaging/{name}/crop | Crop an existing image.
*ImagingApi* | [**get_image_emf**](docs/ImagingApi.md#get_image_emf) | **GET** /imaging/{name}/emf | Process existing EMF imaging using given parameters.
*ImagingApi* | [**get_image_frame**](docs/ImagingApi.md#get_image_frame) | **GET** /imaging/{name}/frames/{frameId} | Get separate frame from existing TIFF image.
*ImagingApi* | [**get_image_frame_properties**](docs/ImagingApi.md#get_image_frame_properties) | **GET** /imaging/{name}/frames/{frameId}/properties | Get separate frame properties of existing TIFF image.
*ImagingApi* | [**get_image_gif**](docs/ImagingApi.md#get_image_gif) | **GET** /imaging/{name}/gif | Update parameters of existing GIF image.
*ImagingApi* | [**get_image_jpeg2000**](docs/ImagingApi.md#get_image_jpeg2000) | **GET** /imaging/{name}/jpg2000 | Update parameters of existing JPEG2000 image.
*ImagingApi* | [**get_image_jpg**](docs/ImagingApi.md#get_image_jpg) | **GET** /imaging/{name}/jpg | Update parameters of existing JPEG image.
*ImagingApi* | [**get_image_properties**](docs/ImagingApi.md#get_image_properties) | **GET** /imaging/{name}/properties | Get properties of an image.
*ImagingApi* | [**get_image_psd**](docs/ImagingApi.md#get_image_psd) | **GET** /imaging/{name}/psd | Update parameters of existing PSD image.
*ImagingApi* | [**get_image_resize**](docs/ImagingApi.md#get_image_resize) | **GET** /imaging/{name}/resize | Resize an existing image.
*ImagingApi* | [**get_image_rotate_flip**](docs/ImagingApi.md#get_image_rotate_flip) | **GET** /imaging/{name}/rotateflip | Rotate and/or flip an existing image.
*ImagingApi* | [**get_image_save_as**](docs/ImagingApi.md#get_image_save_as) | **GET** /imaging/{name}/saveAs | Export existing image to another format.
*ImagingApi* | [**get_image_tiff**](docs/ImagingApi.md#get_image_tiff) | **GET** /imaging/{name}/tiff | Update parameters of existing TIFF image.
*ImagingApi* | [**get_image_update**](docs/ImagingApi.md#get_image_update) | **GET** /imaging/{name}/updateImage | Perform scaling, cropping and flipping of an existing image in a single request.
*ImagingApi* | [**get_image_web_p**](docs/ImagingApi.md#get_image_web_p) | **GET** /imaging/{name}/webp | Update parameters of existing WEBP image.
*ImagingApi* | [**get_image_wmf**](docs/ImagingApi.md#get_image_wmf) | **GET** /imaging/{name}/wmf | Process existing WMF image using given parameters.
*ImagingApi* | [**get_search_context_extract_image_features**](docs/ImagingApi.md#get_search_context_extract_image_features) | **GET** /imaging/ai/imageSearch/{searchContextId}/image2features | Extract features from image without adding to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**get_search_context_find_duplicates**](docs/ImagingApi.md#get_search_context_find_duplicates) | **GET** /imaging/ai/imageSearch/{searchContextId}/findDuplicates | Find images duplicates.
*ImagingApi* | [**get_search_context_find_similar**](docs/ImagingApi.md#get_search_context_find_similar) | **GET** /imaging/ai/imageSearch/{searchContextId}/findSimilar | Find similar images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**get_search_context_image**](docs/ImagingApi.md#get_search_context_image) | **GET** /imaging/ai/imageSearch/{searchContextId}/image | Get image from search context
*ImagingApi* | [**get_search_context_image_features**](docs/ImagingApi.md#get_search_context_image_features) | **GET** /imaging/ai/imageSearch/{searchContextId}/features | Gets image features from search context.
*ImagingApi* | [**get_search_context_status**](docs/ImagingApi.md#get_search_context_status) | **GET** /imaging/ai/imageSearch/{searchContextId}/status | Gets the search context status.
*ImagingApi* | [**get_tiff_to_fax**](docs/ImagingApi.md#get_tiff_to_fax) | **GET** /imaging/tiff/{name}/toFax | Update parameters of existing TIFF image accordingly to fax parameters.
*ImagingApi* | [**move_file**](docs/ImagingApi.md#move_file) | **PUT** /imaging/storage/file/move/{srcPath} | Move file
*ImagingApi* | [**move_folder**](docs/ImagingApi.md#move_folder) | **PUT** /imaging/storage/folder/move/{srcPath} | Move folder
*ImagingApi* | [**object_exists**](docs/ImagingApi.md#object_exists) | **GET** /imaging/storage/exist/{path} | Check if file or folder exists
*ImagingApi* | [**post_create_search_context**](docs/ImagingApi.md#post_create_search_context) | **POST** /imaging/ai/imageSearch/create | Create new search context.
*ImagingApi* | [**post_image_bmp**](docs/ImagingApi.md#post_image_bmp) | **POST** /imaging/bmp | Update parameters of BMP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**post_image_crop**](docs/ImagingApi.md#post_image_crop) | **POST** /imaging/crop | Crop an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**post_image_emf**](docs/ImagingApi.md#post_image_emf) | **POST** /imaging/emf | Process existing EMF imaging using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**post_image_frame**](docs/ImagingApi.md#post_image_frame) | **POST** /imaging/frames/{frameId} | Get separate frame from existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**post_image_frame_properties**](docs/ImagingApi.md#post_image_frame_properties) | **POST** /imaging/frames/{frameId}/properties | Get separate frame properties of existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**post_image_gif**](docs/ImagingApi.md#post_image_gif) | **POST** /imaging/gif | Update parameters of GIF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**post_image_jpeg2000**](docs/ImagingApi.md#post_image_jpeg2000) | **POST** /imaging/jpg2000 | Update parameters of JPEG2000 image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**post_image_jpg**](docs/ImagingApi.md#post_image_jpg) | **POST** /imaging/jpg | Update parameters of JPEG image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**post_image_properties**](docs/ImagingApi.md#post_image_properties) | **POST** /imaging/properties | Get properties of an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**post_image_psd**](docs/ImagingApi.md#post_image_psd) | **POST** /imaging/psd | Update parameters of PSD image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**post_image_resize**](docs/ImagingApi.md#post_image_resize) | **POST** /imaging/resize | Resize an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**post_image_rotate_flip**](docs/ImagingApi.md#post_image_rotate_flip) | **POST** /imaging/rotateflip | Rotate and/or flip an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**post_image_save_as**](docs/ImagingApi.md#post_image_save_as) | **POST** /imaging/saveAs | Export existing image to another format. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.             
*ImagingApi* | [**post_image_tiff**](docs/ImagingApi.md#post_image_tiff) | **POST** /imaging/tiff | Update parameters of TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**post_image_update**](docs/ImagingApi.md#post_image_update) | **POST** /imaging/updateImage | Perform scaling, cropping and flipping of an image in a single request. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.             
*ImagingApi* | [**post_image_web_p**](docs/ImagingApi.md#post_image_web_p) | **POST** /imaging/webp | Update parameters of WEBP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**post_image_wmf**](docs/ImagingApi.md#post_image_wmf) | **POST** /imaging/wmf | Process existing WMF image using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**post_search_context_add_image**](docs/ImagingApi.md#post_search_context_add_image) | **POST** /imaging/ai/imageSearch/{searchContextId}/image | Add image and images features to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**post_search_context_add_tag**](docs/ImagingApi.md#post_search_context_add_tag) | **POST** /imaging/ai/imageSearch/{searchContextId}/addTag | Add tag and reference image to search context. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**post_search_context_compare_images**](docs/ImagingApi.md#post_search_context_compare_images) | **POST** /imaging/ai/imageSearch/{searchContextId}/compare | Compare two images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**post_search_context_extract_image_features**](docs/ImagingApi.md#post_search_context_extract_image_features) | **POST** /imaging/ai/imageSearch/{searchContextId}/features | Extract images features and add them to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**post_search_context_find_by_tags**](docs/ImagingApi.md#post_search_context_find_by_tags) | **POST** /imaging/ai/imageSearch/{searchContextId}/findByTags | Find images by tags. Tags JSON string is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**post_tiff_append**](docs/ImagingApi.md#post_tiff_append) | **POST** /imaging/tiff/{name}/appendTiff | Appends existing TIFF image to another existing TIFF image (i.e. merges TIFF images).
*ImagingApi* | [**put_search_context_image**](docs/ImagingApi.md#put_search_context_image) | **PUT** /imaging/ai/imageSearch/{searchContextId}/image | Update image and images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**put_search_context_image_features**](docs/ImagingApi.md#put_search_context_image_features) | **PUT** /imaging/ai/imageSearch/{searchContextId}/features | Update images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**storage_exists**](docs/ImagingApi.md#storage_exists) | **GET** /imaging/storage/{storageName}/exist | Check if storage exists
*ImagingApi* | [**upload_file**](docs/ImagingApi.md#upload_file) | **POST** /imaging/storage/file/{path} | Upload file


## Documentation For Models

 - [BmpProperties](docs/BmpProperties.md)
 - [DicomProperties](docs/DicomProperties.md)
 - [DiscUsage](docs/DiscUsage.md)
 - [DjvuProperties](docs/DjvuProperties.md)
 - [DngProperties](docs/DngProperties.md)
 - [Error](docs/Error.md)
 - [ErrorDetails](docs/ErrorDetails.md)
 - [ExifData](docs/ExifData.md)
 - [FileVersions](docs/FileVersions.md)
 - [FilesList](docs/FilesList.md)
 - [FilesUploadResult](docs/FilesUploadResult.md)
 - [GifProperties](docs/GifProperties.md)
 - [ImageDuplicates](docs/ImageDuplicates.md)
 - [ImageDuplicatesSet](docs/ImageDuplicatesSet.md)
 - [ImageFeatures](docs/ImageFeatures.md)
 - [ImagingResponse](docs/ImagingResponse.md)
 - [JfifData](docs/JfifData.md)
 - [Jpeg2000Properties](docs/Jpeg2000Properties.md)
 - [JpegProperties](docs/JpegProperties.md)
 - [ObjectExist](docs/ObjectExist.md)
 - [OdgMetadata](docs/OdgMetadata.md)
 - [OdgPage](docs/OdgPage.md)
 - [OdgProperties](docs/OdgProperties.md)
 - [PngProperties](docs/PngProperties.md)
 - [PsdProperties](docs/PsdProperties.md)
 - [SearchContextStatus](docs/SearchContextStatus.md)
 - [SearchResult](docs/SearchResult.md)
 - [SearchResultsSet](docs/SearchResultsSet.md)
 - [StorageExist](docs/StorageExist.md)
 - [StorageFile](docs/StorageFile.md)
 - [TiffFrame](docs/TiffFrame.md)
 - [TiffOptions](docs/TiffOptions.md)
 - [TiffProperties](docs/TiffProperties.md)
 - [WebPProperties](docs/WebPProperties.md)
 - [FileVersion](docs/FileVersion.md)
 - [JpegExifData](docs/JpegExifData.md)


## Documentation For Authorization


## JWT

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: N/A


## Author



