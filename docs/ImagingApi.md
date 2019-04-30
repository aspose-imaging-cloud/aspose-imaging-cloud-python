# swagger_client.ImagingApi

All URIs are relative to *https://api-qa.aspose.cloud/v3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_file**](ImagingApi.md#copy_file) | **PUT** /imaging/storage/file/copy/{srcPath} | Copy file
[**copy_folder**](ImagingApi.md#copy_folder) | **PUT** /imaging/storage/folder/copy/{srcPath} | Copy folder
[**create_folder**](ImagingApi.md#create_folder) | **POST** /imaging/storage/folder/{path} | Create the folder
[**delete_file**](ImagingApi.md#delete_file) | **DELETE** /imaging/storage/file/{path} | Delete file
[**delete_folder**](ImagingApi.md#delete_folder) | **DELETE** /imaging/storage/folder/{path} | Delete folder
[**delete_search_context**](ImagingApi.md#delete_search_context) | **DELETE** /imaging/ai/imageSearch/{searchContextId} | Deletes the search context.
[**delete_search_context_image**](ImagingApi.md#delete_search_context_image) | **DELETE** /imaging/ai/imageSearch/{searchContextId}/image | Delete image and images features from search context
[**delete_search_context_image_features**](ImagingApi.md#delete_search_context_image_features) | **DELETE** /imaging/ai/imageSearch/{searchContextId}/features | Deletes image features from search context.
[**download_file**](ImagingApi.md#download_file) | **GET** /imaging/storage/file/{path} | Download file
[**get_disc_usage**](ImagingApi.md#get_disc_usage) | **GET** /imaging/storage/disc | Get disc usage
[**get_file_versions**](ImagingApi.md#get_file_versions) | **GET** /imaging/storage/version/{path} | Get file versions
[**get_files_list**](ImagingApi.md#get_files_list) | **GET** /imaging/storage/folder/{path} | Get all files and folders within a folder
[**get_image_bmp**](ImagingApi.md#get_image_bmp) | **GET** /imaging/{name}/bmp | Update parameters of existing BMP image.
[**get_image_crop**](ImagingApi.md#get_image_crop) | **GET** /imaging/{name}/crop | Crop an existing image.
[**get_image_emf**](ImagingApi.md#get_image_emf) | **GET** /imaging/{name}/emf | Process existing EMF imaging using given parameters.
[**get_image_frame**](ImagingApi.md#get_image_frame) | **GET** /imaging/{name}/frames/{frameId} | Get separate frame from existing TIFF image.
[**get_image_frame_properties**](ImagingApi.md#get_image_frame_properties) | **GET** /imaging/{name}/frames/{frameId}/properties | Get separate frame properties of existing TIFF image.
[**get_image_gif**](ImagingApi.md#get_image_gif) | **GET** /imaging/{name}/gif | Update parameters of existing GIF image.
[**get_image_jpeg2000**](ImagingApi.md#get_image_jpeg2000) | **GET** /imaging/{name}/jpg2000 | Update parameters of existing JPEG2000 image.
[**get_image_jpg**](ImagingApi.md#get_image_jpg) | **GET** /imaging/{name}/jpg | Update parameters of existing JPEG image.
[**get_image_properties**](ImagingApi.md#get_image_properties) | **GET** /imaging/{name}/properties | Get properties of an image.
[**get_image_psd**](ImagingApi.md#get_image_psd) | **GET** /imaging/{name}/psd | Update parameters of existing PSD image.
[**get_image_resize**](ImagingApi.md#get_image_resize) | **GET** /imaging/{name}/resize | Resize an existing image.
[**get_image_rotate_flip**](ImagingApi.md#get_image_rotate_flip) | **GET** /imaging/{name}/rotateflip | Rotate and/or flip an existing image.
[**get_image_save_as**](ImagingApi.md#get_image_save_as) | **GET** /imaging/{name}/saveAs | Export existing image to another format.
[**get_image_tiff**](ImagingApi.md#get_image_tiff) | **GET** /imaging/{name}/tiff | Update parameters of existing TIFF image.
[**get_image_update**](ImagingApi.md#get_image_update) | **GET** /imaging/{name}/updateImage | Perform scaling, cropping and flipping of an existing image in a single request.
[**get_image_web_p**](ImagingApi.md#get_image_web_p) | **GET** /imaging/{name}/webp | Update parameters of existing WEBP image.
[**get_image_wmf**](ImagingApi.md#get_image_wmf) | **GET** /imaging/{name}/wmf | Process existing WMF image using given parameters.
[**get_search_context_extract_image_features**](ImagingApi.md#get_search_context_extract_image_features) | **GET** /imaging/ai/imageSearch/{searchContextId}/image2features | Extract features from image without adding to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
[**get_search_context_find_duplicates**](ImagingApi.md#get_search_context_find_duplicates) | **GET** /imaging/ai/imageSearch/{searchContextId}/findDuplicates | Find images duplicates.
[**get_search_context_find_similar**](ImagingApi.md#get_search_context_find_similar) | **GET** /imaging/ai/imageSearch/{searchContextId}/findSimilar | Find similar images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
[**get_search_context_image**](ImagingApi.md#get_search_context_image) | **GET** /imaging/ai/imageSearch/{searchContextId}/image | Get image from search context
[**get_search_context_image_features**](ImagingApi.md#get_search_context_image_features) | **GET** /imaging/ai/imageSearch/{searchContextId}/features | Gets image features from search context.
[**get_search_context_status**](ImagingApi.md#get_search_context_status) | **GET** /imaging/ai/imageSearch/{searchContextId}/status | Gets the search context status.
[**get_tiff_to_fax**](ImagingApi.md#get_tiff_to_fax) | **GET** /imaging/tiff/{name}/toFax | Update parameters of existing TIFF image accordingly to fax parameters.
[**move_file**](ImagingApi.md#move_file) | **PUT** /imaging/storage/file/move/{srcPath} | Move file
[**move_folder**](ImagingApi.md#move_folder) | **PUT** /imaging/storage/folder/move/{srcPath} | Move folder
[**object_exists**](ImagingApi.md#object_exists) | **GET** /imaging/storage/exist/{path} | Check if file or folder exists
[**post_create_search_context**](ImagingApi.md#post_create_search_context) | **POST** /imaging/ai/imageSearch/create | Create new search context.
[**post_image_bmp**](ImagingApi.md#post_image_bmp) | **POST** /imaging/bmp | Update parameters of BMP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
[**post_image_crop**](ImagingApi.md#post_image_crop) | **POST** /imaging/crop | Crop an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
[**post_image_emf**](ImagingApi.md#post_image_emf) | **POST** /imaging/emf | Process existing EMF imaging using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
[**post_image_frame**](ImagingApi.md#post_image_frame) | **POST** /imaging/frames/{frameId} | Get separate frame from existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
[**post_image_frame_properties**](ImagingApi.md#post_image_frame_properties) | **POST** /imaging/frames/{frameId}/properties | Get separate frame properties of existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
[**post_image_gif**](ImagingApi.md#post_image_gif) | **POST** /imaging/gif | Update parameters of GIF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
[**post_image_jpeg2000**](ImagingApi.md#post_image_jpeg2000) | **POST** /imaging/jpg2000 | Update parameters of JPEG2000 image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
[**post_image_jpg**](ImagingApi.md#post_image_jpg) | **POST** /imaging/jpg | Update parameters of JPEG image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
[**post_image_properties**](ImagingApi.md#post_image_properties) | **POST** /imaging/properties | Get properties of an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
[**post_image_psd**](ImagingApi.md#post_image_psd) | **POST** /imaging/psd | Update parameters of PSD image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
[**post_image_resize**](ImagingApi.md#post_image_resize) | **POST** /imaging/resize | Resize an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
[**post_image_rotate_flip**](ImagingApi.md#post_image_rotate_flip) | **POST** /imaging/rotateflip | Rotate and/or flip an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
[**post_image_save_as**](ImagingApi.md#post_image_save_as) | **POST** /imaging/saveAs | Export existing image to another format. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.             
[**post_image_tiff**](ImagingApi.md#post_image_tiff) | **POST** /imaging/tiff | Update parameters of TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
[**post_image_update**](ImagingApi.md#post_image_update) | **POST** /imaging/updateImage | Perform scaling, cropping and flipping of an image in a single request. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.             
[**post_image_web_p**](ImagingApi.md#post_image_web_p) | **POST** /imaging/webp | Update parameters of WEBP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
[**post_image_wmf**](ImagingApi.md#post_image_wmf) | **POST** /imaging/wmf | Process existing WMF image using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
[**post_search_context_add_image**](ImagingApi.md#post_search_context_add_image) | **POST** /imaging/ai/imageSearch/{searchContextId}/image | Add image and images features to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
[**post_search_context_add_tag**](ImagingApi.md#post_search_context_add_tag) | **POST** /imaging/ai/imageSearch/{searchContextId}/addTag | Add tag and reference image to search context. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
[**post_search_context_compare_images**](ImagingApi.md#post_search_context_compare_images) | **POST** /imaging/ai/imageSearch/{searchContextId}/compare | Compare two images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
[**post_search_context_extract_image_features**](ImagingApi.md#post_search_context_extract_image_features) | **POST** /imaging/ai/imageSearch/{searchContextId}/features | Extract images features and add them to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
[**post_search_context_find_by_tags**](ImagingApi.md#post_search_context_find_by_tags) | **POST** /imaging/ai/imageSearch/{searchContextId}/findByTags | Find images by tags. Tags JSON string is passed as zero-indexed multipart/form-data content or as raw body stream.
[**post_tiff_append**](ImagingApi.md#post_tiff_append) | **POST** /imaging/tiff/{name}/appendTiff | Appends existing TIFF image to another existing TIFF image (i.e. merges TIFF images).
[**put_search_context_image**](ImagingApi.md#put_search_context_image) | **PUT** /imaging/ai/imageSearch/{searchContextId}/image | Update image and images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
[**put_search_context_image_features**](ImagingApi.md#put_search_context_image_features) | **PUT** /imaging/ai/imageSearch/{searchContextId}/features | Update images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
[**storage_exists**](ImagingApi.md#storage_exists) | **GET** /imaging/storage/{storageName}/exist | Check if storage exists
[**upload_file**](ImagingApi.md#upload_file) | **POST** /imaging/storage/file/{path} | Upload file


# **copy_file**
> copy_file(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)

Copy file

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/folder/file.ext&#39; | 
 **dest_path** | **str**| Destination file path | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to copy | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_folder**
> copy_folder(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)

Copy folder

### Example
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
src_path = 'src_path_example' # str | Source folder path e.g. '/src'
dest_path = 'dest_path_example' # str | Destination folder path e.g. '/dst'
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)

try:
    # Copy folder
    api_instance.copy_folder(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)
except ApiException as e:
    print("Exception when calling ImagingApi->copy_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source folder path e.g. &#39;/src&#39; | 
 **dest_path** | **str**| Destination folder path e.g. &#39;/dst&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder**
> create_folder(path, storage_name=storage_name)

Create the folder

### Example
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
path = 'path_example' # str | Folder path to create e.g. 'folder_1/folder_2/'
storage_name = 'storage_name_example' # str | Storage name (optional)

try:
    # Create the folder
    api_instance.create_folder(path, storage_name=storage_name)
except ApiException as e:
    print("Exception when calling ImagingApi->create_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path to create e.g. &#39;folder_1/folder_2/&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file(path, storage_name=storage_name, version_id=version_id)

Delete file

### Example
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
path = 'path_example' # str | File path e.g. '/folder/file.ext'
storage_name = 'storage_name_example' # str | Storage name (optional)
version_id = 'version_id_example' # str | File version ID to delete (optional)

try:
    # Delete file
    api_instance.delete_file(path, storage_name=storage_name, version_id=version_id)
except ApiException as e:
    print("Exception when calling ImagingApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to delete | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> delete_folder(path, storage_name=storage_name, recursive=recursive)

Delete folder

### Example
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
path = 'path_example' # str | Folder path e.g. '/folder'
storage_name = 'storage_name_example' # str | Storage name (optional)
recursive = false # bool | Enable to delete folders, subfolders and files (optional) (default to false)

try:
    # Delete folder
    api_instance.delete_folder(path, storage_name=storage_name, recursive=recursive)
except ApiException as e:
    print("Exception when calling ImagingApi->delete_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path e.g. &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **recursive** | **bool**| Enable to delete folders, subfolders and files | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_search_context**
> delete_search_context(search_context_id, folder=folder, storage=storage)

Deletes the search context.

### Example
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
search_context_id = 'search_context_id_example' # str | The search context identifier.
folder = 'folder_example' # str | The folder. (optional)
storage = 'storage_example' # str | The storage. (optional)

try:
    # Deletes the search context.
    api_instance.delete_search_context(search_context_id, folder=folder, storage=storage)
except ApiException as e:
    print("Exception when calling ImagingApi->delete_search_context: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| The search context identifier. | 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_search_context_image**
> delete_search_context_image(search_context_id, image_id, folder=folder, storage=storage)

Delete image and images features from search context

### Example
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
search_context_id = 'search_context_id_example' # str | Search context identifier.
image_id = 'image_id_example' # str | Image identifier.
folder = 'folder_example' # str | Folder. (optional)
storage = 'storage_example' # str | Storage (optional)

try:
    # Delete image and images features from search context
    api_instance.delete_search_context_image(search_context_id, image_id, folder=folder, storage=storage)
except ApiException as e:
    print("Exception when calling ImagingApi->delete_search_context_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| Search context identifier. | 
 **image_id** | **str**| Image identifier. | 
 **folder** | **str**| Folder. | [optional] 
 **storage** | **str**| Storage | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_search_context_image_features**
> delete_search_context_image_features(search_context_id, image_id, folder=folder, storage=storage)

Deletes image features from search context.

### Example
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
search_context_id = 'search_context_id_example' # str | The search context identifier.
image_id = 'image_id_example' # str | The image identifier.
folder = 'folder_example' # str | The folder. (optional)
storage = 'storage_example' # str | The storage. (optional)

try:
    # Deletes image features from search context.
    api_instance.delete_search_context_image_features(search_context_id, image_id, folder=folder, storage=storage)
except ApiException as e:
    print("Exception when calling ImagingApi->delete_search_context_image_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| The search context identifier. | 
 **image_id** | **str**| The image identifier. | 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> file download_file(path, storage_name=storage_name, version_id=version_id)

Download file

### Example
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
path = 'path_example' # str | File path e.g. '/folder/file.ext'
storage_name = 'storage_name_example' # str | Storage name (optional)
version_id = 'version_id_example' # str | File version ID to download (optional)

try:
    # Download file
    api_response = api_instance.download_file(path, storage_name=storage_name, version_id=version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to download | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disc_usage**
> DiscUsage get_disc_usage(storage_name=storage_name)

Get disc usage

### Example
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
storage_name = 'storage_name_example' # str | Storage name (optional)

try:
    # Get disc usage
    api_response = api_instance.get_disc_usage(storage_name=storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_disc_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**DiscUsage**](DiscUsage.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_versions**
> FileVersions get_file_versions(path, storage_name=storage_name)

Get file versions

### Example
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
path = 'path_example' # str | File path e.g. '/file.ext'
storage_name = 'storage_name_example' # str | Storage name (optional)

try:
    # Get file versions
    api_response = api_instance.get_file_versions(path, storage_name=storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_file_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**FileVersions**](FileVersions.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files_list**
> FilesList get_files_list(path, storage_name=storage_name)

Get all files and folders within a folder

### Example
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
path = 'path_example' # str | Folder path e.g. '/folder'
storage_name = 'storage_name_example' # str | Storage name (optional)

try:
    # Get all files and folders within a folder
    api_response = api_instance.get_files_list(path, storage_name=storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_files_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path e.g. &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**FilesList**](FilesList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_bmp**
> file get_image_bmp(name, bits_per_pixel, horizontal_resolution, vertical_resolution, from_scratch=from_scratch, out_path=out_path, folder=folder, storage=storage)

Update parameters of existing BMP image.

### Example
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
name = 'name_example' # str | Filename of image.
bits_per_pixel = 56 # int | Color depth.
horizontal_resolution = 56 # int | New horizontal resolution.
vertical_resolution = 56 # int | New vertical resolution.
from_scratch = false # bool | Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. (optional) (default to false)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
folder = 'folder_example' # str | Folder with image to process. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Update parameters of existing BMP image.
    api_response = api_instance.get_image_bmp(name, bits_per_pixel, horizontal_resolution, vertical_resolution, from_scratch=from_scratch, out_path=out_path, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_image_bmp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **bits_per_pixel** | **int**| Color depth. | 
 **horizontal_resolution** | **int**| New horizontal resolution. | 
 **vertical_resolution** | **int**| New vertical resolution. | 
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_crop**
> file get_image_crop(name, format, x, y, width, height, out_path=out_path, folder=folder, storage=storage)

Crop an existing image.

### Example
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
name = 'name_example' # str | Filename of an image.
format = 'format_example' # str | Resulting image format.
x = 56 # int | X position of start point for cropping rectangle.
y = 56 # int | Y position of start point for cropping rectangle.
width = 56 # int | Width of cropping rectangle
height = 56 # int | Height of cropping rectangle.
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
folder = 'folder_example' # str | Folder with image to process. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Crop an existing image.
    api_response = api_instance.get_image_crop(name, format, x, y, width, height, out_path=out_path, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_image_crop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an image. | 
 **format** | **str**| Resulting image format. | 
 **x** | **int**| X position of start point for cropping rectangle. | 
 **y** | **int**| Y position of start point for cropping rectangle. | 
 **width** | **int**| Width of cropping rectangle | 
 **height** | **int**| Height of cropping rectangle. | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_emf**
> file get_image_emf(name, bk_color, page_width, page_height, border_x, border_y, from_scratch=from_scratch, out_path=out_path, folder=folder, storage=storage, format=format)

Process existing EMF imaging using given parameters.

### Example
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
name = 'name_example' # str | Filename of image.
bk_color = 'bk_color_example' # str | Color of the background.
page_width = 56 # int | Width of the page.
page_height = 56 # int | Height of the page.
border_x = 56 # int | Border width.
border_y = 56 # int | Border height.
from_scratch = false # bool | Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. (optional) (default to false)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
folder = 'folder_example' # str | Folder with image to process. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)
format = 'png' # str | Export format (PNG is the default one). (optional) (default to png)

try:
    # Process existing EMF imaging using given parameters.
    api_response = api_instance.get_image_emf(name, bk_color, page_width, page_height, border_x, border_y, from_scratch=from_scratch, out_path=out_path, folder=folder, storage=storage, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_image_emf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **bk_color** | **str**| Color of the background. | 
 **page_width** | **int**| Width of the page. | 
 **page_height** | **int**| Height of the page. | 
 **border_x** | **int**| Border width. | 
 **border_y** | **int**| Border height. | 
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 
 **format** | **str**| Export format (PNG is the default one). | [optional] [default to png]

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_frame**
> file get_image_frame(name, frame_id, new_width=new_width, new_height=new_height, x=x, y=y, rect_width=rect_width, rect_height=rect_height, rotate_flip_method=rotate_flip_method, save_other_frames=save_other_frames, out_path=out_path, folder=folder, storage=storage)

Get separate frame from existing TIFF image.

### Example
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
name = 'name_example' # str | Filename of image.
frame_id = 56 # int | Number of a frame.
new_width = 56 # int | New width. (optional)
new_height = 56 # int | New height. (optional)
x = 56 # int | X position of start point for cropping rectangle. (optional)
y = 56 # int | Y position of start point for cropping rectangle. (optional)
rect_width = 56 # int | Width of cropping rectangle. (optional)
rect_height = 56 # int | Height of cropping rectangle. (optional)
rotate_flip_method = 'rotate_flip_method_example' # str | RotateFlip method (Rotate180FlipNone, Rotate180FlipX, Rotate180FlipXY, Rotate180FlipY, Rotate270FlipNone, Rotate270FlipX, Rotate270FlipXY, Rotate270FlipY, Rotate90FlipNone, Rotate90FlipX, Rotate90FlipXY, Rotate90FlipY, RotateNoneFlipNone, RotateNoneFlipX, RotateNoneFlipXY, RotateNoneFlipY). Default is RotateNoneFlipNone. (optional)
save_other_frames = false # bool | If result will include all other frames or just a specified frame. (optional) (default to false)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
folder = 'folder_example' # str | Folder with image to process. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Get separate frame from existing TIFF image.
    api_response = api_instance.get_image_frame(name, frame_id, new_width=new_width, new_height=new_height, x=x, y=y, rect_width=rect_width, rect_height=rect_height, rotate_flip_method=rotate_flip_method, save_other_frames=save_other_frames, out_path=out_path, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_image_frame: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **frame_id** | **int**| Number of a frame. | 
 **new_width** | **int**| New width. | [optional] 
 **new_height** | **int**| New height. | [optional] 
 **x** | **int**| X position of start point for cropping rectangle. | [optional] 
 **y** | **int**| Y position of start point for cropping rectangle. | [optional] 
 **rect_width** | **int**| Width of cropping rectangle. | [optional] 
 **rect_height** | **int**| Height of cropping rectangle. | [optional] 
 **rotate_flip_method** | **str**| RotateFlip method (Rotate180FlipNone, Rotate180FlipX, Rotate180FlipXY, Rotate180FlipY, Rotate270FlipNone, Rotate270FlipX, Rotate270FlipXY, Rotate270FlipY, Rotate90FlipNone, Rotate90FlipX, Rotate90FlipXY, Rotate90FlipY, RotateNoneFlipNone, RotateNoneFlipX, RotateNoneFlipXY, RotateNoneFlipY). Default is RotateNoneFlipNone. | [optional] 
 **save_other_frames** | **bool**| If result will include all other frames or just a specified frame. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_frame_properties**
> ImagingResponse get_image_frame_properties(name, frame_id, folder=folder, storage=storage)

Get separate frame properties of existing TIFF image.

### Example
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
name = 'name_example' # str | Filename with image.
frame_id = 56 # int | Number of a frame.
folder = 'folder_example' # str | Folder with image to process. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Get separate frame properties of existing TIFF image.
    api_response = api_instance.get_image_frame_properties(name, frame_id, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_image_frame_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename with image. | 
 **frame_id** | **int**| Number of a frame. | 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**ImagingResponse**](ImagingResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_gif**
> file get_image_gif(name, background_color_index=background_color_index, color_resolution=color_resolution, has_trailer=has_trailer, interlaced=interlaced, is_palette_sorted=is_palette_sorted, pixel_aspect_ratio=pixel_aspect_ratio, from_scratch=from_scratch, out_path=out_path, folder=folder, storage=storage)

Update parameters of existing GIF image.

### Example
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
name = 'name_example' # str | Filename of image.
background_color_index = 32 # int | Index of the background color. (optional) (default to 32)
color_resolution = 3 # int | Color resolution. (optional) (default to 3)
has_trailer = true # bool | Specifies if image has trailer. (optional) (default to true)
interlaced = true # bool | Specifies if image is interlaced. (optional) (default to true)
is_palette_sorted = false # bool | Specifies if palette is sorted. (optional) (default to false)
pixel_aspect_ratio = 3 # int | Pixel aspect ratio. (optional) (default to 3)
from_scratch = true # bool | Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. (optional) (default to true)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
folder = 'folder_example' # str | Folder with image to process. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Update parameters of existing GIF image.
    api_response = api_instance.get_image_gif(name, background_color_index=background_color_index, color_resolution=color_resolution, has_trailer=has_trailer, interlaced=interlaced, is_palette_sorted=is_palette_sorted, pixel_aspect_ratio=pixel_aspect_ratio, from_scratch=from_scratch, out_path=out_path, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_image_gif: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **background_color_index** | **int**| Index of the background color. | [optional] [default to 32]
 **color_resolution** | **int**| Color resolution. | [optional] [default to 3]
 **has_trailer** | **bool**| Specifies if image has trailer. | [optional] [default to true]
 **interlaced** | **bool**| Specifies if image is interlaced. | [optional] [default to true]
 **is_palette_sorted** | **bool**| Specifies if palette is sorted. | [optional] [default to false]
 **pixel_aspect_ratio** | **int**| Pixel aspect ratio. | [optional] [default to 3]
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to true]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_jpeg2000**
> file get_image_jpeg2000(name, comment, codec=codec, from_scratch=from_scratch, out_path=out_path, folder=folder, storage=storage)

Update parameters of existing JPEG2000 image.

### Example
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
name = 'name_example' # str | Filename of image.
comment = 'comment_example' # str | The comment.
codec = 'j2k' # str | The codec. (optional) (default to j2k)
from_scratch = false # bool | Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. (optional) (default to false)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
folder = 'folder_example' # str | Folder with image to process. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Update parameters of existing JPEG2000 image.
    api_response = api_instance.get_image_jpeg2000(name, comment, codec=codec, from_scratch=from_scratch, out_path=out_path, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_image_jpeg2000: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **comment** | **str**| The comment. | 
 **codec** | **str**| The codec. | [optional] [default to j2k]
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_jpg**
> file get_image_jpg(name, quality=quality, compression_type=compression_type, from_scratch=from_scratch, out_path=out_path, folder=folder, storage=storage)

Update parameters of existing JPEG image.

### Example
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
name = 'name_example' # str | Filename of image.
quality = 75 # int | Quality of an image from 0 to 100. Default is 75. (optional) (default to 75)
compression_type = 'baseline' # str | Compression type. (optional) (default to baseline)
from_scratch = false # bool | Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. (optional) (default to false)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
folder = 'folder_example' # str | Folder with image to process. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Update parameters of existing JPEG image.
    api_response = api_instance.get_image_jpg(name, quality=quality, compression_type=compression_type, from_scratch=from_scratch, out_path=out_path, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_image_jpg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **quality** | **int**| Quality of an image from 0 to 100. Default is 75. | [optional] [default to 75]
 **compression_type** | **str**| Compression type. | [optional] [default to baseline]
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_properties**
> ImagingResponse get_image_properties(name, folder=folder, storage=storage)

Get properties of an image.

### Example
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
name = 'name_example' # str | Filename of an image.
folder = 'folder_example' # str | Folder with image to process. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Get properties of an image.
    api_response = api_instance.get_image_properties(name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_image_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an image. | 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**ImagingResponse**](ImagingResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_psd**
> file get_image_psd(name, channels_count=channels_count, compression_method=compression_method, from_scratch=from_scratch, out_path=out_path, folder=folder, storage=storage)

Update parameters of existing PSD image.

### Example
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
name = 'name_example' # str | Filename of image.
channels_count = 4 # int | Count of color channels. (optional) (default to 4)
compression_method = 'rle' # str | Compression method. (optional) (default to rle)
from_scratch = false # bool | Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. (optional) (default to false)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
folder = 'folder_example' # str | Folder with image to process. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Update parameters of existing PSD image.
    api_response = api_instance.get_image_psd(name, channels_count=channels_count, compression_method=compression_method, from_scratch=from_scratch, out_path=out_path, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_image_psd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **channels_count** | **int**| Count of color channels. | [optional] [default to 4]
 **compression_method** | **str**| Compression method. | [optional] [default to rle]
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_resize**
> file get_image_resize(name, format, new_width, new_height, out_path=out_path, folder=folder, storage=storage)

Resize an existing image.

### Example
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
name = 'name_example' # str | Filename of an image.
format = 'format_example' # str | Resulting image format.
new_width = 56 # int | New width.
new_height = 56 # int | New height.
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
folder = 'folder_example' # str | Folder with image to process. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Resize an existing image.
    api_response = api_instance.get_image_resize(name, format, new_width, new_height, out_path=out_path, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_image_resize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an image. | 
 **format** | **str**| Resulting image format. | 
 **new_width** | **int**| New width. | 
 **new_height** | **int**| New height. | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_rotate_flip**
> file get_image_rotate_flip(name, format, method, out_path=out_path, folder=folder, storage=storage)

Rotate and/or flip an existing image.

### Example
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
name = 'name_example' # str | Filename of an image.
format = 'format_example' # str | Resulting image format.
method = 'method_example' # str | RotateFlip method (Rotate180FlipNone, Rotate180FlipX, Rotate180FlipXY, Rotate180FlipY, Rotate270FlipNone, Rotate270FlipX, Rotate270FlipXY, Rotate270FlipY, Rotate90FlipNone, Rotate90FlipX, Rotate90FlipXY, Rotate90FlipY, RotateNoneFlipNone, RotateNoneFlipX, RotateNoneFlipXY, RotateNoneFlipY).
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
folder = 'folder_example' # str | Folder with image to process. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Rotate and/or flip an existing image.
    api_response = api_instance.get_image_rotate_flip(name, format, method, out_path=out_path, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_image_rotate_flip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an image. | 
 **format** | **str**| Resulting image format. | 
 **method** | **str**| RotateFlip method (Rotate180FlipNone, Rotate180FlipX, Rotate180FlipXY, Rotate180FlipY, Rotate270FlipNone, Rotate270FlipX, Rotate270FlipXY, Rotate270FlipY, Rotate90FlipNone, Rotate90FlipX, Rotate90FlipXY, Rotate90FlipY, RotateNoneFlipNone, RotateNoneFlipX, RotateNoneFlipXY, RotateNoneFlipY). | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_save_as**
> file get_image_save_as(name, format, out_path=out_path, folder=folder, storage=storage)

Export existing image to another format.

### Example
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
name = 'name_example' # str | Filename of image.
format = 'format_example' # str | Resulting image format.
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
folder = 'folder_example' # str | Folder with image to process. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export existing image to another format.
    api_response = api_instance.get_image_save_as(name, format, out_path=out_path, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_image_save_as: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **format** | **str**| Resulting image format. | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_tiff**
> file get_image_tiff(name, compression, resolution_unit, bit_depth, from_scratch=from_scratch, horizontal_resolution=horizontal_resolution, vertical_resolution=vertical_resolution, out_path=out_path, folder=folder, storage=storage)

Update parameters of existing TIFF image.

### Example
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
name = 'name_example' # str | Filename of image.
compression = 'compression_example' # str | Compression.
resolution_unit = 'resolution_unit_example' # str | New resolution unit.
bit_depth = 56 # int | Bit depth.
from_scratch = false # bool | Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. (optional) (default to false)
horizontal_resolution = 0.0 # float | New horizontal resolution. (optional) (default to 0.0)
vertical_resolution = 0.0 # float | New verstical resolution. (optional) (default to 0.0)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
folder = 'folder_example' # str | Folder with image to process. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Update parameters of existing TIFF image.
    api_response = api_instance.get_image_tiff(name, compression, resolution_unit, bit_depth, from_scratch=from_scratch, horizontal_resolution=horizontal_resolution, vertical_resolution=vertical_resolution, out_path=out_path, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_image_tiff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **compression** | **str**| Compression. | 
 **resolution_unit** | **str**| New resolution unit. | 
 **bit_depth** | **int**| Bit depth. | 
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **horizontal_resolution** | **float**| New horizontal resolution. | [optional] [default to 0.0]
 **vertical_resolution** | **float**| New verstical resolution. | [optional] [default to 0.0]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_update**
> file get_image_update(name, format, new_width, new_height, x, y, rect_width, rect_height, rotate_flip_method, out_path=out_path, folder=folder, storage=storage)

Perform scaling, cropping and flipping of an existing image in a single request.

### Example
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
name = 'name_example' # str | Filename of an image.
format = 'format_example' # str | Resulting image format.
new_width = 56 # int | New width of the scaled image.
new_height = 56 # int | New height of the scaled image.
x = 56 # int | X position of start point for cropping rectangle.
y = 56 # int | Y position of start point for cropping rectangle.
rect_width = 56 # int | Width of cropping rectangle.
rect_height = 56 # int | Height of cropping rectangle.
rotate_flip_method = 'rotate_flip_method_example' # str | RotateFlip method (Rotate180FlipNone, Rotate180FlipX, Rotate180FlipXY, Rotate180FlipY, Rotate270FlipNone, Rotate270FlipX, Rotate270FlipXY, Rotate270FlipY, Rotate90FlipNone, Rotate90FlipX, Rotate90FlipXY, Rotate90FlipY, RotateNoneFlipNone, RotateNoneFlipX, RotateNoneFlipXY, RotateNoneFlipY). Default is RotateNoneFlipNone.
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
folder = 'folder_example' # str | Folder with image to process. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Perform scaling, cropping and flipping of an existing image in a single request.
    api_response = api_instance.get_image_update(name, format, new_width, new_height, x, y, rect_width, rect_height, rotate_flip_method, out_path=out_path, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_image_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an image. | 
 **format** | **str**| Resulting image format. | 
 **new_width** | **int**| New width of the scaled image. | 
 **new_height** | **int**| New height of the scaled image. | 
 **x** | **int**| X position of start point for cropping rectangle. | 
 **y** | **int**| Y position of start point for cropping rectangle. | 
 **rect_width** | **int**| Width of cropping rectangle. | 
 **rect_height** | **int**| Height of cropping rectangle. | 
 **rotate_flip_method** | **str**| RotateFlip method (Rotate180FlipNone, Rotate180FlipX, Rotate180FlipXY, Rotate180FlipY, Rotate270FlipNone, Rotate270FlipX, Rotate270FlipXY, Rotate270FlipY, Rotate90FlipNone, Rotate90FlipX, Rotate90FlipXY, Rotate90FlipY, RotateNoneFlipNone, RotateNoneFlipX, RotateNoneFlipXY, RotateNoneFlipY). Default is RotateNoneFlipNone. | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_web_p**
> file get_image_web_p(name, loss_less, quality, anim_loop_count, anim_background_color, from_scratch=from_scratch, out_path=out_path, folder=folder, storage=storage)

Update parameters of existing WEBP image.

### Example
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
name = 'name_example' # str | Filename of image.
loss_less = true # bool | If WEBP is lossless.
quality = 56 # int | Quality.
anim_loop_count = 56 # int | The animation loop count.
anim_background_color = 'anim_background_color_example' # str | Color of the animation background.
from_scratch = false # bool | Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. (optional) (default to false)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
folder = 'folder_example' # str | Folder with image to process. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Update parameters of existing WEBP image.
    api_response = api_instance.get_image_web_p(name, loss_less, quality, anim_loop_count, anim_background_color, from_scratch=from_scratch, out_path=out_path, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_image_web_p: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **loss_less** | **bool**| If WEBP is lossless. | 
 **quality** | **int**| Quality. | 
 **anim_loop_count** | **int**| The animation loop count. | 
 **anim_background_color** | **str**| Color of the animation background. | 
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_wmf**
> file get_image_wmf(name, bk_color, page_width, page_height, border_x, border_y, from_scratch=from_scratch, out_path=out_path, folder=folder, storage=storage, format=format)

Process existing WMF image using given parameters.

### Example
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
name = 'name_example' # str | Filename of image.
bk_color = 'bk_color_example' # str | Color of the background.
page_width = 56 # int | Width of the page.
page_height = 56 # int | Height of the page.
border_x = 56 # int | Border width.
border_y = 56 # int | Border height.
from_scratch = false # bool | Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. (optional) (default to false)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
folder = 'folder_example' # str | Folder with image to process. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)
format = 'png' # str | Export format (PNG is the default one). (optional) (default to png)

try:
    # Process existing WMF image using given parameters.
    api_response = api_instance.get_image_wmf(name, bk_color, page_width, page_height, border_x, border_y, from_scratch=from_scratch, out_path=out_path, folder=folder, storage=storage, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_image_wmf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **bk_color** | **str**| Color of the background. | 
 **page_width** | **int**| Width of the page. | 
 **page_height** | **int**| Height of the page. | 
 **border_x** | **int**| Border width. | 
 **border_y** | **int**| Border height. | 
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 
 **format** | **str**| Export format (PNG is the default one). | [optional] [default to png]

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_context_extract_image_features**
> ImageFeatures get_search_context_extract_image_features(search_context_id, image_id, image_data=image_data, folder=folder, storage=storage)

Extract features from image without adding to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
search_context_id = 'search_context_id_example' # str | The search context identifier.
image_id = 'image_id_example' # str | The image identifier.
image_data = '/path/to/file.txt' # file | Input image (optional)
folder = 'folder_example' # str | The folder. (optional)
storage = 'storage_example' # str | The storage. (optional)

try:
    # Extract features from image without adding to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.get_search_context_extract_image_features(search_context_id, image_id, image_data=image_data, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_search_context_extract_image_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| The search context identifier. | 
 **image_id** | **str**| The image identifier. | 
 **image_data** | **file**| Input image | [optional] 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

### Return type

[**ImageFeatures**](ImageFeatures.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_context_find_duplicates**
> ImageDuplicatesSet get_search_context_find_duplicates(search_context_id, similarity_threshold, folder=folder, storage=storage)

Find images duplicates.

### Example
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
search_context_id = 'search_context_id_example' # str | The search context identifier.
similarity_threshold = 1.2 # float | The similarity threshold.
folder = 'folder_example' # str | The folder. (optional)
storage = 'storage_example' # str | The storage. (optional)

try:
    # Find images duplicates.
    api_response = api_instance.get_search_context_find_duplicates(search_context_id, similarity_threshold, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_search_context_find_duplicates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| The search context identifier. | 
 **similarity_threshold** | **float**| The similarity threshold. | 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

### Return type

[**ImageDuplicatesSet**](ImageDuplicatesSet.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_context_find_similar**
> SearchResultsSet get_search_context_find_similar(search_context_id, similarity_threshold, max_count, image_data=image_data, image_id=image_id, folder=folder, storage=storage)

Find similar images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
search_context_id = 'search_context_id_example' # str | The search context identifier.
similarity_threshold = 1.2 # float | The similarity threshold.
max_count = 56 # int | The maximum count.
image_data = '/path/to/file.txt' # file | Input image (optional)
image_id = 'image_id_example' # str | The search image identifier. (optional)
folder = 'folder_example' # str | The folder. (optional)
storage = 'storage_example' # str | The storage. (optional)

try:
    # Find similar images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.get_search_context_find_similar(search_context_id, similarity_threshold, max_count, image_data=image_data, image_id=image_id, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_search_context_find_similar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| The search context identifier. | 
 **similarity_threshold** | **float**| The similarity threshold. | 
 **max_count** | **int**| The maximum count. | 
 **image_data** | **file**| Input image | [optional] 
 **image_id** | **str**| The search image identifier. | [optional] 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

### Return type

[**SearchResultsSet**](SearchResultsSet.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_context_image**
> file get_search_context_image(search_context_id, image_id, folder=folder, storage=storage)

Get image from search context

### Example
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
search_context_id = 'search_context_id_example' # str | Search context identifier.
image_id = 'image_id_example' # str | Image identifier.
folder = 'folder_example' # str | Folder. (optional)
storage = 'storage_example' # str | Storage (optional)

try:
    # Get image from search context
    api_response = api_instance.get_search_context_image(search_context_id, image_id, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_search_context_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| Search context identifier. | 
 **image_id** | **str**| Image identifier. | 
 **folder** | **str**| Folder. | [optional] 
 **storage** | **str**| Storage | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_context_image_features**
> ImageFeatures get_search_context_image_features(search_context_id, image_id, folder=folder, storage=storage)

Gets image features from search context.

### Example
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
search_context_id = 'search_context_id_example' # str | The search context identifier.
image_id = 'image_id_example' # str | The image identifier.
folder = 'folder_example' # str | The folder. (optional)
storage = 'storage_example' # str | The storage. (optional)

try:
    # Gets image features from search context.
    api_response = api_instance.get_search_context_image_features(search_context_id, image_id, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_search_context_image_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| The search context identifier. | 
 **image_id** | **str**| The image identifier. | 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

### Return type

[**ImageFeatures**](ImageFeatures.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_context_status**
> SearchContextStatus get_search_context_status(search_context_id, folder=folder, storage=storage)

Gets the search context status.

### Example
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
search_context_id = 'search_context_id_example' # str | The search context identifier.
folder = 'folder_example' # str | The folder. (optional)
storage = 'storage_example' # str | The storage. (optional)

try:
    # Gets the search context status.
    api_response = api_instance.get_search_context_status(search_context_id, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_search_context_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| The search context identifier. | 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

### Return type

[**SearchContextStatus**](SearchContextStatus.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tiff_to_fax**
> file get_tiff_to_fax(name, storage=storage, folder=folder, out_path=out_path)

Update parameters of existing TIFF image accordingly to fax parameters.

### Example
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
name = 'name_example' # str | Filename of image.
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)
folder = 'folder_example' # str | Folder with image to process. (optional)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)

try:
    # Update parameters of existing TIFF image accordingly to fax parameters.
    api_response = api_instance.get_tiff_to_fax(name, storage=storage, folder=folder, out_path=out_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->get_tiff_to_fax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_file**
> move_file(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)

Move file

### Example
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
src_path = 'src_path_example' # str | Source file path e.g. '/src.ext'
dest_path = 'dest_path_example' # str | Destination file path e.g. '/dest.ext'
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)
version_id = 'version_id_example' # str | File version ID to move (optional)

try:
    # Move file
    api_instance.move_file(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)
except ApiException as e:
    print("Exception when calling ImagingApi->move_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/src.ext&#39; | 
 **dest_path** | **str**| Destination file path e.g. &#39;/dest.ext&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to move | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_folder**
> move_folder(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)

Move folder

### Example
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
src_path = 'src_path_example' # str | Folder path to move e.g. '/folder'
dest_path = 'dest_path_example' # str | Destination folder path to move to e.g '/dst'
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)

try:
    # Move folder
    api_instance.move_folder(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)
except ApiException as e:
    print("Exception when calling ImagingApi->move_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Folder path to move e.g. &#39;/folder&#39; | 
 **dest_path** | **str**| Destination folder path to move to e.g &#39;/dst&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_exists**
> ObjectExist object_exists(path, storage_name=storage_name, version_id=version_id)

Check if file or folder exists

### Example
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
path = 'path_example' # str | File or folder path e.g. '/file.ext' or '/folder'
storage_name = 'storage_name_example' # str | Storage name (optional)
version_id = 'version_id_example' # str | File version ID (optional)

try:
    # Check if file or folder exists
    api_response = api_instance.object_exists(path, storage_name=storage_name, version_id=version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->object_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File or folder path e.g. &#39;/file.ext&#39; or &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID | [optional] 

### Return type

[**ObjectExist**](ObjectExist.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_search_context**
> SearchContextStatus post_create_search_context(detector=detector, matching_algorithm=matching_algorithm, folder=folder, storage=storage)

Create new search context.

### Example
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
detector = 'akaze' # str | The image features detector. (optional) (default to akaze)
matching_algorithm = 'randomBinaryTree' # str | The matching algorithm. (optional) (default to randomBinaryTree)
folder = 'folder_example' # str | The folder. (optional)
storage = 'storage_example' # str | The storage. (optional)

try:
    # Create new search context.
    api_response = api_instance.post_create_search_context(detector=detector, matching_algorithm=matching_algorithm, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->post_create_search_context: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detector** | **str**| The image features detector. | [optional] [default to akaze]
 **matching_algorithm** | **str**| The matching algorithm. | [optional] [default to randomBinaryTree]
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

### Return type

[**SearchContextStatus**](SearchContextStatus.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_bmp**
> file post_image_bmp(image_data, bits_per_pixel, horizontal_resolution, vertical_resolution, from_scratch=from_scratch, out_path=out_path, storage=storage)

Update parameters of BMP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
image_data = '/path/to/file.txt' # file | Input image
bits_per_pixel = 56 # int | Color depth.
horizontal_resolution = 56 # int | New horizontal resolution.
vertical_resolution = 56 # int | New vertical resolution.
from_scratch = false # bool | Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. (optional) (default to false)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Update parameters of BMP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.post_image_bmp(image_data, bits_per_pixel, horizontal_resolution, vertical_resolution, from_scratch=from_scratch, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->post_image_bmp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **bits_per_pixel** | **int**| Color depth. | 
 **horizontal_resolution** | **int**| New horizontal resolution. | 
 **vertical_resolution** | **int**| New vertical resolution. | 
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_crop**
> file post_image_crop(image_data, format, x, y, width, height, out_path=out_path, storage=storage)

Crop an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
image_data = '/path/to/file.txt' # file | Input image
format = 'format_example' # str | Resulting image format.
x = 56 # int | X position of start point for cropping rectangle.
y = 56 # int | Y position of start point for cropping rectangle.
width = 56 # int | Width of cropping rectangle.
height = 56 # int | Height of cropping rectangle.
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Crop an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.post_image_crop(image_data, format, x, y, width, height, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->post_image_crop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **format** | **str**| Resulting image format. | 
 **x** | **int**| X position of start point for cropping rectangle. | 
 **y** | **int**| Y position of start point for cropping rectangle. | 
 **width** | **int**| Width of cropping rectangle. | 
 **height** | **int**| Height of cropping rectangle. | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_emf**
> file post_image_emf(image_data, bk_color, page_width, page_height, border_x, border_y, from_scratch=from_scratch, out_path=out_path, storage=storage, format=format)

Process existing EMF imaging using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
image_data = '/path/to/file.txt' # file | Input image
bk_color = 'bk_color_example' # str | Color of the background.
page_width = 56 # int | Width of the page.
page_height = 56 # int | Height of the page.
border_x = 56 # int | Border width.
border_y = 56 # int | Border height.
from_scratch = false # bool | Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. (optional) (default to false)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)
format = 'png' # str | Export format (PNG is the default one). (optional) (default to png)

try:
    # Process existing EMF imaging using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.post_image_emf(image_data, bk_color, page_width, page_height, border_x, border_y, from_scratch=from_scratch, out_path=out_path, storage=storage, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->post_image_emf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **bk_color** | **str**| Color of the background. | 
 **page_width** | **int**| Width of the page. | 
 **page_height** | **int**| Height of the page. | 
 **border_x** | **int**| Border width. | 
 **border_y** | **int**| Border height. | 
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 
 **format** | **str**| Export format (PNG is the default one). | [optional] [default to png]

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_frame**
> file post_image_frame(image_data, frame_id, new_width=new_width, new_height=new_height, x=x, y=y, rect_width=rect_width, rect_height=rect_height, rotate_flip_method=rotate_flip_method, save_other_frames=save_other_frames, out_path=out_path, storage=storage)

Get separate frame from existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
image_data = '/path/to/file.txt' # file | Input image
frame_id = 56 # int | Number of a frame.
new_width = 56 # int | New width. (optional)
new_height = 56 # int | New height. (optional)
x = 56 # int | X position of start point for cropping rectangle. (optional)
y = 56 # int | Y position of start point for cropping rectangle. (optional)
rect_width = 56 # int | Width of cropping rectangle. (optional)
rect_height = 56 # int | Height of cropping rectangle. (optional)
rotate_flip_method = 'rotate_flip_method_example' # str | RotateFlip method (Rotate180FlipNone, Rotate180FlipX, Rotate180FlipXY, Rotate180FlipY, Rotate270FlipNone, Rotate270FlipX, Rotate270FlipXY, Rotate270FlipY, Rotate90FlipNone, Rotate90FlipX, Rotate90FlipXY, Rotate90FlipY, RotateNoneFlipNone, RotateNoneFlipX, RotateNoneFlipXY, RotateNoneFlipY). Default is RotateNoneFlipNone. (optional)
save_other_frames = false # bool | If result will include all other frames or just a specified frame. (optional) (default to false)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Get separate frame from existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.post_image_frame(image_data, frame_id, new_width=new_width, new_height=new_height, x=x, y=y, rect_width=rect_width, rect_height=rect_height, rotate_flip_method=rotate_flip_method, save_other_frames=save_other_frames, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->post_image_frame: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **frame_id** | **int**| Number of a frame. | 
 **new_width** | **int**| New width. | [optional] 
 **new_height** | **int**| New height. | [optional] 
 **x** | **int**| X position of start point for cropping rectangle. | [optional] 
 **y** | **int**| Y position of start point for cropping rectangle. | [optional] 
 **rect_width** | **int**| Width of cropping rectangle. | [optional] 
 **rect_height** | **int**| Height of cropping rectangle. | [optional] 
 **rotate_flip_method** | **str**| RotateFlip method (Rotate180FlipNone, Rotate180FlipX, Rotate180FlipXY, Rotate180FlipY, Rotate270FlipNone, Rotate270FlipX, Rotate270FlipXY, Rotate270FlipY, Rotate90FlipNone, Rotate90FlipX, Rotate90FlipXY, Rotate90FlipY, RotateNoneFlipNone, RotateNoneFlipX, RotateNoneFlipXY, RotateNoneFlipY). Default is RotateNoneFlipNone. | [optional] 
 **save_other_frames** | **bool**| If result will include all other frames or just a specified frame. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_frame_properties**
> ImagingResponse post_image_frame_properties(image_data, frame_id)

Get separate frame properties of existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
image_data = '/path/to/file.txt' # file | Input image
frame_id = 56 # int | Number of a frame.

try:
    # Get separate frame properties of existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.post_image_frame_properties(image_data, frame_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->post_image_frame_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **frame_id** | **int**| Number of a frame. | 

### Return type

[**ImagingResponse**](ImagingResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_gif**
> file post_image_gif(image_data, background_color_index=background_color_index, color_resolution=color_resolution, has_trailer=has_trailer, interlaced=interlaced, is_palette_sorted=is_palette_sorted, pixel_aspect_ratio=pixel_aspect_ratio, from_scratch=from_scratch, out_path=out_path, storage=storage)

Update parameters of GIF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
image_data = '/path/to/file.txt' # file | Input image
background_color_index = 32 # int | Index of the background color. (optional) (default to 32)
color_resolution = 3 # int | Color resolution. (optional) (default to 3)
has_trailer = true # bool | Specifies if image has trailer. (optional) (default to true)
interlaced = true # bool | Specifies if image is interlaced. (optional) (default to true)
is_palette_sorted = false # bool | Specifies if palette is sorted. (optional) (default to false)
pixel_aspect_ratio = 3 # int | Pixel aspect ratio. (optional) (default to 3)
from_scratch = true # bool | Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. (optional) (default to true)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Update parameters of GIF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.post_image_gif(image_data, background_color_index=background_color_index, color_resolution=color_resolution, has_trailer=has_trailer, interlaced=interlaced, is_palette_sorted=is_palette_sorted, pixel_aspect_ratio=pixel_aspect_ratio, from_scratch=from_scratch, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->post_image_gif: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **background_color_index** | **int**| Index of the background color. | [optional] [default to 32]
 **color_resolution** | **int**| Color resolution. | [optional] [default to 3]
 **has_trailer** | **bool**| Specifies if image has trailer. | [optional] [default to true]
 **interlaced** | **bool**| Specifies if image is interlaced. | [optional] [default to true]
 **is_palette_sorted** | **bool**| Specifies if palette is sorted. | [optional] [default to false]
 **pixel_aspect_ratio** | **int**| Pixel aspect ratio. | [optional] [default to 3]
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to true]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_jpeg2000**
> file post_image_jpeg2000(image_data, comment, codec=codec, from_scratch=from_scratch, out_path=out_path, storage=storage)

Update parameters of JPEG2000 image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
image_data = '/path/to/file.txt' # file | Input image
comment = 'comment_example' # str | The comment.
codec = 'j2k' # str | The codec. (optional) (default to j2k)
from_scratch = false # bool | Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. (optional) (default to false)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Update parameters of JPEG2000 image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.post_image_jpeg2000(image_data, comment, codec=codec, from_scratch=from_scratch, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->post_image_jpeg2000: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **comment** | **str**| The comment. | 
 **codec** | **str**| The codec. | [optional] [default to j2k]
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_jpg**
> file post_image_jpg(image_data, quality=quality, compression_type=compression_type, from_scratch=from_scratch, out_path=out_path, storage=storage)

Update parameters of JPEG image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
image_data = '/path/to/file.txt' # file | Input image
quality = 75 # int | Quality of an image from 0 to 100. Default is 75. (optional) (default to 75)
compression_type = 'baseline' # str | Compression type. (optional) (default to baseline)
from_scratch = false # bool | Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. (optional) (default to false)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Update parameters of JPEG image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.post_image_jpg(image_data, quality=quality, compression_type=compression_type, from_scratch=from_scratch, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->post_image_jpg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **quality** | **int**| Quality of an image from 0 to 100. Default is 75. | [optional] [default to 75]
 **compression_type** | **str**| Compression type. | [optional] [default to baseline]
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_properties**
> ImagingResponse post_image_properties(image_data)

Get properties of an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
image_data = '/path/to/file.txt' # file | Input image

try:
    # Get properties of an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.post_image_properties(image_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->post_image_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 

### Return type

[**ImagingResponse**](ImagingResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_psd**
> file post_image_psd(image_data, channels_count=channels_count, compression_method=compression_method, from_scratch=from_scratch, out_path=out_path, storage=storage)

Update parameters of PSD image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
image_data = '/path/to/file.txt' # file | Input image
channels_count = 4 # int | Count of color channels. (optional) (default to 4)
compression_method = 'rle' # str | Compression method. (optional) (default to rle)
from_scratch = false # bool | Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. (optional) (default to false)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Update parameters of PSD image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.post_image_psd(image_data, channels_count=channels_count, compression_method=compression_method, from_scratch=from_scratch, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->post_image_psd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **channels_count** | **int**| Count of color channels. | [optional] [default to 4]
 **compression_method** | **str**| Compression method. | [optional] [default to rle]
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_resize**
> file post_image_resize(image_data, format, new_width, new_height, out_path=out_path, storage=storage)

Resize an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
image_data = '/path/to/file.txt' # file | Input image
format = 'format_example' # str | Resulting image format.
new_width = 56 # int | New width.
new_height = 56 # int | New height.
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Resize an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.post_image_resize(image_data, format, new_width, new_height, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->post_image_resize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **format** | **str**| Resulting image format. | 
 **new_width** | **int**| New width. | 
 **new_height** | **int**| New height. | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_rotate_flip**
> file post_image_rotate_flip(image_data, format, method, out_path=out_path, storage=storage)

Rotate and/or flip an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
image_data = '/path/to/file.txt' # file | Input image
format = 'format_example' # str | Resulting image format.
method = 'method_example' # str | RotateFlip method (Rotate180FlipNone, Rotate180FlipX, Rotate180FlipXY, Rotate180FlipY, Rotate270FlipNone, Rotate270FlipX, Rotate270FlipXY, Rotate270FlipY, Rotate90FlipNone, Rotate90FlipX, Rotate90FlipXY, Rotate90FlipY, RotateNoneFlipNone, RotateNoneFlipX, RotateNoneFlipXY, RotateNoneFlipY).
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Rotate and/or flip an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.post_image_rotate_flip(image_data, format, method, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->post_image_rotate_flip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **format** | **str**| Resulting image format. | 
 **method** | **str**| RotateFlip method (Rotate180FlipNone, Rotate180FlipX, Rotate180FlipXY, Rotate180FlipY, Rotate270FlipNone, Rotate270FlipX, Rotate270FlipXY, Rotate270FlipY, Rotate90FlipNone, Rotate90FlipX, Rotate90FlipXY, Rotate90FlipY, RotateNoneFlipNone, RotateNoneFlipX, RotateNoneFlipXY, RotateNoneFlipY). | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_save_as**
> file post_image_save_as(image_data, format, out_path=out_path, storage=storage)

Export existing image to another format. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.             

### Example
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
image_data = '/path/to/file.txt' # file | Input image
format = 'format_example' # str | Resulting image format.
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export existing image to another format. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.             
    api_response = api_instance.post_image_save_as(image_data, format, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->post_image_save_as: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **format** | **str**| Resulting image format. | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_tiff**
> file post_image_tiff(image_data, compression, resolution_unit, bit_depth, from_scratch=from_scratch, horizontal_resolution=horizontal_resolution, vertical_resolution=vertical_resolution, out_path=out_path, storage=storage)

Update parameters of TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
image_data = '/path/to/file.txt' # file | Input image
compression = 'compression_example' # str | Compression.
resolution_unit = 'resolution_unit_example' # str | New resolution unit.
bit_depth = 56 # int | Bit depth.
from_scratch = false # bool | Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. (optional) (default to false)
horizontal_resolution = 0.0 # float | New horizontal resolution. (optional) (default to 0.0)
vertical_resolution = 0.0 # float | New verstical resolution. (optional) (default to 0.0)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Update parameters of TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.post_image_tiff(image_data, compression, resolution_unit, bit_depth, from_scratch=from_scratch, horizontal_resolution=horizontal_resolution, vertical_resolution=vertical_resolution, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->post_image_tiff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **compression** | **str**| Compression. | 
 **resolution_unit** | **str**| New resolution unit. | 
 **bit_depth** | **int**| Bit depth. | 
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **horizontal_resolution** | **float**| New horizontal resolution. | [optional] [default to 0.0]
 **vertical_resolution** | **float**| New verstical resolution. | [optional] [default to 0.0]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_update**
> file post_image_update(image_data, format, new_width, new_height, x, y, rect_width, rect_height, rotate_flip_method, out_path=out_path, storage=storage)

Perform scaling, cropping and flipping of an image in a single request. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.             

### Example
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
image_data = '/path/to/file.txt' # file | Input image
format = 'format_example' # str | Resulting image format.
new_width = 56 # int | New width of the scaled image.
new_height = 56 # int | New height of the scaled image.
x = 56 # int | X position of start point for cropping rectangle.
y = 56 # int | Y position of start point for cropping rectangle.
rect_width = 56 # int | Width of cropping rectangle.
rect_height = 56 # int | Height of cropping rectangle.
rotate_flip_method = 'rotate_flip_method_example' # str | RotateFlip method (Rotate180FlipNone, Rotate180FlipX, Rotate180FlipXY, Rotate180FlipY, Rotate270FlipNone, Rotate270FlipX, Rotate270FlipXY, Rotate270FlipY, Rotate90FlipNone, Rotate90FlipX, Rotate90FlipXY, Rotate90FlipY, RotateNoneFlipNone, RotateNoneFlipX, RotateNoneFlipXY, RotateNoneFlipY). Default is RotateNoneFlipNone.
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Perform scaling, cropping and flipping of an image in a single request. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.             
    api_response = api_instance.post_image_update(image_data, format, new_width, new_height, x, y, rect_width, rect_height, rotate_flip_method, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->post_image_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **format** | **str**| Resulting image format. | 
 **new_width** | **int**| New width of the scaled image. | 
 **new_height** | **int**| New height of the scaled image. | 
 **x** | **int**| X position of start point for cropping rectangle. | 
 **y** | **int**| Y position of start point for cropping rectangle. | 
 **rect_width** | **int**| Width of cropping rectangle. | 
 **rect_height** | **int**| Height of cropping rectangle. | 
 **rotate_flip_method** | **str**| RotateFlip method (Rotate180FlipNone, Rotate180FlipX, Rotate180FlipXY, Rotate180FlipY, Rotate270FlipNone, Rotate270FlipX, Rotate270FlipXY, Rotate270FlipY, Rotate90FlipNone, Rotate90FlipX, Rotate90FlipXY, Rotate90FlipY, RotateNoneFlipNone, RotateNoneFlipX, RotateNoneFlipXY, RotateNoneFlipY). Default is RotateNoneFlipNone. | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_web_p**
> file post_image_web_p(image_data, loss_less, quality, anim_loop_count, anim_background_color, from_scratch=from_scratch, out_path=out_path, storage=storage)

Update parameters of WEBP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
image_data = '/path/to/file.txt' # file | Input image
loss_less = true # bool | If WEBP is lossless.
quality = 56 # int | Quality.
anim_loop_count = 56 # int | The animation loop count.
anim_background_color = 'anim_background_color_example' # str | Color of the animation background.
from_scratch = false # bool | Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. (optional) (default to false)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Update parameters of WEBP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.post_image_web_p(image_data, loss_less, quality, anim_loop_count, anim_background_color, from_scratch=from_scratch, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->post_image_web_p: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **loss_less** | **bool**| If WEBP is lossless. | 
 **quality** | **int**| Quality. | 
 **anim_loop_count** | **int**| The animation loop count. | 
 **anim_background_color** | **str**| Color of the animation background. | 
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_wmf**
> file post_image_wmf(image_data, bk_color, page_width, page_height, border_x, border_y, from_scratch=from_scratch, out_path=out_path, storage=storage, format=format)

Process existing WMF image using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
image_data = '/path/to/file.txt' # file | Input image
bk_color = 'bk_color_example' # str | Color of the background.
page_width = 56 # int | Width of the page.
page_height = 56 # int | Height of the page.
border_x = 56 # int | Border width.
border_y = 56 # int | Border height.
from_scratch = false # bool | Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. (optional) (default to false)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed image). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)
format = 'png' # str | Export format (PNG is the default one). (optional) (default to png)

try:
    # Process existing WMF image using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.post_image_wmf(image_data, bk_color, page_width, page_height, border_x, border_y, from_scratch=from_scratch, out_path=out_path, storage=storage, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->post_image_wmf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **bk_color** | **str**| Color of the background. | 
 **page_width** | **int**| Width of the page. | 
 **page_height** | **int**| Height of the page. | 
 **border_x** | **int**| Border width. | 
 **border_y** | **int**| Border height. | 
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 
 **format** | **str**| Export format (PNG is the default one). | [optional] [default to png]

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_search_context_add_image**
> post_search_context_add_image(search_context_id, image_id, image_data=image_data, folder=folder, storage=storage)

Add image and images features to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
search_context_id = 'search_context_id_example' # str | Search context identifier.
image_id = 'image_id_example' # str | Image identifier.
image_data = '/path/to/file.txt' # file | Input image (optional)
folder = 'folder_example' # str | Folder. (optional)
storage = 'storage_example' # str | Storage (optional)

try:
    # Add image and images features to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
    api_instance.post_search_context_add_image(search_context_id, image_id, image_data=image_data, folder=folder, storage=storage)
except ApiException as e:
    print("Exception when calling ImagingApi->post_search_context_add_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| Search context identifier. | 
 **image_id** | **str**| Image identifier. | 
 **image_data** | **file**| Input image | [optional] 
 **folder** | **str**| Folder. | [optional] 
 **storage** | **str**| Storage | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_search_context_add_tag**
> post_search_context_add_tag(image_data, search_context_id, tag_name, folder=folder, storage=storage)

Add tag and reference image to search context. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
image_data = '/path/to/file.txt' # file | Input image
search_context_id = 'search_context_id_example' # str | The search context identifier.
tag_name = 'tag_name_example' # str | The tag.
folder = 'folder_example' # str | The folder. (optional)
storage = 'storage_example' # str | The storage. (optional)

try:
    # Add tag and reference image to search context. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
    api_instance.post_search_context_add_tag(image_data, search_context_id, tag_name, folder=folder, storage=storage)
except ApiException as e:
    print("Exception when calling ImagingApi->post_search_context_add_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **search_context_id** | **str**| The search context identifier. | 
 **tag_name** | **str**| The tag. | 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_search_context_compare_images**
> SearchResultsSet post_search_context_compare_images(search_context_id, image_id1, image_data=image_data, image_id2=image_id2, folder=folder, storage=storage)

Compare two images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
search_context_id = 'search_context_id_example' # str | The search context identifier.
image_id1 = 'image_id1_example' # str | The first image Id in storage.
image_data = '/path/to/file.txt' # file | Input image (optional)
image_id2 = 'image_id2_example' # str | The second image Idin storage or null(if image loading in request). (optional)
folder = 'folder_example' # str | The folder. (optional)
storage = 'storage_example' # str | The storage. (optional)

try:
    # Compare two images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.post_search_context_compare_images(search_context_id, image_id1, image_data=image_data, image_id2=image_id2, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->post_search_context_compare_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| The search context identifier. | 
 **image_id1** | **str**| The first image Id in storage. | 
 **image_data** | **file**| Input image | [optional] 
 **image_id2** | **str**| The second image Idin storage or null(if image loading in request). | [optional] 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

### Return type

[**SearchResultsSet**](SearchResultsSet.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_search_context_extract_image_features**
> post_search_context_extract_image_features(search_context_id, image_data=image_data, image_id=image_id, images_folder=images_folder, folder=folder, storage=storage)

Extract images features and add them to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
search_context_id = 'search_context_id_example' # str | The search context identifier.
image_data = '/path/to/file.txt' # file | Input image (optional)
image_id = 'image_id_example' # str | The image identifier. (optional)
images_folder = 'images_folder_example' # str | Images folder. (optional)
folder = 'folder_example' # str | The folder. (optional)
storage = 'storage_example' # str | The storage. (optional)

try:
    # Extract images features and add them to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
    api_instance.post_search_context_extract_image_features(search_context_id, image_data=image_data, image_id=image_id, images_folder=images_folder, folder=folder, storage=storage)
except ApiException as e:
    print("Exception when calling ImagingApi->post_search_context_extract_image_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| The search context identifier. | 
 **image_data** | **file**| Input image | [optional] 
 **image_id** | **str**| The image identifier. | [optional] 
 **images_folder** | **str**| Images folder. | [optional] 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_search_context_find_by_tags**
> SearchResultsSet post_search_context_find_by_tags(tags, search_context_id, similarity_threshold, max_count, folder=folder, storage=storage)

Find images by tags. Tags JSON string is passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
tags = 'tags_example' # str | Tags array for searching
search_context_id = 'search_context_id_example' # str | The search context identifier.
similarity_threshold = 1.2 # float | The similarity threshold.
max_count = 56 # int | The maximum count.
folder = 'folder_example' # str | The folder. (optional)
storage = 'storage_example' # str | The storage. (optional)

try:
    # Find images by tags. Tags JSON string is passed as zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.post_search_context_find_by_tags(tags, search_context_id, similarity_threshold, max_count, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->post_search_context_find_by_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | **str**| Tags array for searching | 
 **search_context_id** | **str**| The search context identifier. | 
 **similarity_threshold** | **float**| The similarity threshold. | 
 **max_count** | **int**| The maximum count. | 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

### Return type

[**SearchResultsSet**](SearchResultsSet.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tiff_append**
> post_tiff_append(name, append_file, storage=storage, folder=folder)

Appends existing TIFF image to another existing TIFF image (i.e. merges TIFF images).

### Example
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
name = 'name_example' # str | Original image file name.
append_file = 'append_file_example' # str | Image file name to be appended to original one.
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)
folder = 'folder_example' # str | Folder with images to process. (optional)

try:
    # Appends existing TIFF image to another existing TIFF image (i.e. merges TIFF images).
    api_instance.post_tiff_append(name, append_file, storage=storage, folder=folder)
except ApiException as e:
    print("Exception when calling ImagingApi->post_tiff_append: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Original image file name. | 
 **append_file** | **str**| Image file name to be appended to original one. | 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 
 **folder** | **str**| Folder with images to process. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_search_context_image**
> put_search_context_image(search_context_id, image_id, image_data=image_data, folder=folder, storage=storage)

Update image and images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
search_context_id = 'search_context_id_example' # str | Search context identifier.
image_id = 'image_id_example' # str | Image identifier.
image_data = '/path/to/file.txt' # file | Input image (optional)
folder = 'folder_example' # str | Folder. (optional)
storage = 'storage_example' # str | Storage (optional)

try:
    # Update image and images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
    api_instance.put_search_context_image(search_context_id, image_id, image_data=image_data, folder=folder, storage=storage)
except ApiException as e:
    print("Exception when calling ImagingApi->put_search_context_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| Search context identifier. | 
 **image_id** | **str**| Image identifier. | 
 **image_data** | **file**| Input image | [optional] 
 **folder** | **str**| Folder. | [optional] 
 **storage** | **str**| Storage | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_search_context_image_features**
> put_search_context_image_features(search_context_id, image_id, image_data=image_data, folder=folder, storage=storage)

Update images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.

### Example
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
search_context_id = 'search_context_id_example' # str | The search context identifier.
image_id = 'image_id_example' # str | The image identifier.
image_data = '/path/to/file.txt' # file | Input image (optional)
folder = 'folder_example' # str | The folder. (optional)
storage = 'storage_example' # str | The storage. (optional)

try:
    # Update images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
    api_instance.put_search_context_image_features(search_context_id, image_id, image_data=image_data, folder=folder, storage=storage)
except ApiException as e:
    print("Exception when calling ImagingApi->put_search_context_image_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| The search context identifier. | 
 **image_id** | **str**| The image identifier. | 
 **image_data** | **file**| Input image | [optional] 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_exists**
> StorageExist storage_exists(storage_name)

Check if storage exists

### Example
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
storage_name = 'storage_name_example' # str | Storage name

try:
    # Check if storage exists
    api_response = api_instance.storage_exists(storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->storage_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str**| Storage name | 

### Return type

[**StorageExist**](StorageExist.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> FilesUploadResult upload_file(path, file, storage_name=storage_name)

Upload file

### Example
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
path = 'path_example' # str | Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext             If the content is multipart and path does not contains the file name it tries to get them from filename parameter             from Content-Disposition header.             
file = '/path/to/file.txt' # file | File to upload
storage_name = 'storage_name_example' # str | Storage name (optional)

try:
    # Upload file
    api_response = api_instance.upload_file(path, file, storage_name=storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagingApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext             If the content is multipart and path does not contains the file name it tries to get them from filename parameter             from Content-Disposition header.              | 
 **file** | **file**| File to upload | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**FilesUploadResult**](FilesUploadResult.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

