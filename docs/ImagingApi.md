# asposeimagingcloud.ImagingApi

<a name="add_search_image"></a>
# **add_search_image**
> add_search_image(self, add_search_image_request)

Add image and images features to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

void (empty response body)

<a name="add_search_image_async"></a>
# **add_search_image_async**
> add_search_image_async(self, add_search_image_request)

Add image and images features to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

void (empty response body)

### AddSearchImageRequest Parameters
```python
__init__(self, 
    search_context_id, 
    image_id, 
    image_data=image_data, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| Search context identifier. | 
 **image_id** | **str**| Image identifier. | 
 **image_data** | **file**| Input image | [optional] 
 **folder** | **str**| Folder. | [optional] 
 **storage** | **str**| Storage | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="append_tiff"></a>
# **append_tiff**
> append_tiff(self, append_tiff_request)

Appends existing TIFF image to another existing TIFF image (i.e. merges TIFF images).

### Return type

void (empty response body)

<a name="append_tiff_async"></a>
# **append_tiff_async**
> append_tiff_async(self, append_tiff_request)

Appends existing TIFF image to another existing TIFF image (i.e. merges TIFF images).

Performs operation asynchronously.

### Return type

void (empty response body)

### AppendTiffRequest Parameters
```python
__init__(self, 
    name, 
    append_file, 
    storage=storage, 
    folder=folder)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Original image file name. | 
 **append_file** | **str**| Image file name to be appended to original one. | 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 
 **folder** | **str**| Folder with images to process. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="compare_images"></a>
# **compare_images**
> compare_images(self, compare_images_request)

Compare two images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

[**SearchResultsSet**](SearchResultsSet.md)

<a name="compare_images_async"></a>
# **compare_images_async**
> compare_images_async(self, compare_images_request)

Compare two images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

[**SearchResultsSet**](SearchResultsSet.md)

### CompareImagesRequest Parameters
```python
__init__(self, 
    search_context_id, 
    image_id1, 
    image_data=image_data, 
    image_id2=image_id2, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| The search context identifier. | 
 **image_id1** | **str**| The first image Id in storage. | 
 **image_data** | **file**| Input image | [optional] 
 **image_id2** | **str**| The second image Id in storage or null (if image loading in request). | [optional] 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="convert_tiff_to_fax"></a>
# **convert_tiff_to_fax**
> convert_tiff_to_fax(self, convert_tiff_to_fax_request)

Update parameters of existing TIFF image accordingly to fax parameters.

### Return type

**file**

<a name="convert_tiff_to_fax_async"></a>
# **convert_tiff_to_fax_async**
> convert_tiff_to_fax_async(self, convert_tiff_to_fax_request)

Update parameters of existing TIFF image accordingly to fax parameters.

Performs operation asynchronously.

### Return type

**file**

### ConvertTiffToFaxRequest Parameters
```python
__init__(self, 
    name, 
    storage=storage, 
    folder=folder)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="copy_file"></a>
# **copy_file**
> copy_file(self, copy_file_request)

Copy file

### Return type

void (empty response body)

<a name="copy_file_async"></a>
# **copy_file_async**
> copy_file_async(self, copy_file_request)

Copy file

Performs operation asynchronously.

### Return type

void (empty response body)

### CopyFileRequest Parameters
```python
__init__(self, 
    src_path, 
    dest_path, 
    src_storage_name=src_storage_name, 
    dest_storage_name=dest_storage_name, 
    version_id=version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/folder/file.ext&#39; | 
 **dest_path** | **str**| Destination file path | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to copy | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="copy_folder"></a>
# **copy_folder**
> copy_folder(self, copy_folder_request)

Copy folder

### Return type

void (empty response body)

<a name="copy_folder_async"></a>
# **copy_folder_async**
> copy_folder_async(self, copy_folder_request)

Copy folder

Performs operation asynchronously.

### Return type

void (empty response body)

### CopyFolderRequest Parameters
```python
__init__(self, 
    src_path, 
    dest_path, 
    src_storage_name=src_storage_name, 
    dest_storage_name=dest_storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source folder path e.g. &#39;/src&#39; | 
 **dest_path** | **str**| Destination folder path e.g. &#39;/dst&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_cropped_image"></a>
# **create_cropped_image**
> create_cropped_image(self, create_cropped_image_request)

Crop an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

**file**

<a name="create_cropped_image_async"></a>
# **create_cropped_image_async**
> create_cropped_image_async(self, create_cropped_image_request)

Crop an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

**file**

### CreateCroppedImageRequest Parameters
```python
__init__(self, 
    image_data, 
    x, 
    y, 
    width, 
    height, 
    format=format, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **x** | **int**| X position of start point for cropping rectangle. | 
 **y** | **int**| Y position of start point for cropping rectangle. | 
 **width** | **int**| Width of cropping rectangle. | 
 **height** | **int**| Height of cropping rectangle. | 
 **format** | **str**| Resulting image format. Please, refer to https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_deskewed_image"></a>
# **create_deskewed_image**
> create_deskewed_image(self, create_deskewed_image_request)

Deskew an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

**file**

<a name="create_deskewed_image_async"></a>
# **create_deskewed_image_async**
> create_deskewed_image_async(self, create_deskewed_image_request)

Deskew an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

**file**

### CreateDeskewedImageRequest Parameters
```python
__init__(self, 
    image_data, 
    resize_proportionally, 
    bk_color=bk_color, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **resize_proportionally** | **bool**| Resize proportionally | 
 **bk_color** | **str**| Background color | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image) | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_folder"></a>
# **create_folder**
> create_folder(self, create_folder_request)

Create the folder

### Return type

void (empty response body)

<a name="create_folder_async"></a>
# **create_folder_async**
> create_folder_async(self, create_folder_request)

Create the folder

Performs operation asynchronously.

### Return type

void (empty response body)

### CreateFolderRequest Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path to create e.g. &#39;folder_1/folder_2/&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_grayscaled_image"></a>
# **create_grayscaled_image**
> create_grayscaled_image(self, create_grayscaled_image_request)

Grayscales an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

**file**

<a name="create_grayscaled_image_async"></a>
# **create_grayscaled_image_async**
> create_grayscaled_image_async(self, create_grayscaled_image_request)

Grayscales an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

**file**

### CreateGrayscaledImageRequest Parameters
```python
__init__(self, 
    image_data, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image) | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_image_features"></a>
# **create_image_features**
> create_image_features(self, create_image_features_request)

Extract images features and add them to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

void (empty response body)

<a name="create_image_features_async"></a>
# **create_image_features_async**
> create_image_features_async(self, create_image_features_request)

Extract images features and add them to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

void (empty response body)

### CreateImageFeaturesRequest Parameters
```python
__init__(self, 
    search_context_id, 
    image_data=image_data, 
    image_id=image_id, 
    images_folder=images_folder, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| The search context identifier. | 
 **image_data** | **file**| Input image | [optional] 
 **image_id** | **str**| The image identifier. | [optional] 
 **images_folder** | **str**| Images source - a folder | [optional] 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_image_frame"></a>
# **create_image_frame**
> create_image_frame(self, create_image_frame_request)

Get separate frame from existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

**file**

<a name="create_image_frame_async"></a>
# **create_image_frame_async**
> create_image_frame_async(self, create_image_frame_request)

Get separate frame from existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

**file**

### CreateImageFrameRequest Parameters
```python
__init__(self, 
    image_data, 
    frame_id, 
    new_width=new_width, 
    new_height=new_height, 
    x=x, 
    y=y, 
    rect_width=rect_width, 
    rect_height=rect_height, 
    rotate_flip_method=rotate_flip_method, 
    save_other_frames=save_other_frames, 
    out_path=out_path, 
    storage=storage)
```

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

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_image_search"></a>
# **create_image_search**
> create_image_search(self, create_image_search_request)

Create new search context.

### Return type

[**SearchContextStatus**](SearchContextStatus.md)

<a name="create_image_search_async"></a>
# **create_image_search_async**
> create_image_search_async(self, create_image_search_request)

Create new search context.

Performs operation asynchronously.

### Return type

[**SearchContextStatus**](SearchContextStatus.md)

### CreateImageSearchRequest Parameters
```python
__init__(self, 
    detector=detector, 
    matching_algorithm=matching_algorithm, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detector** | **str**| The image features detector. | [optional] [default to akaze]
 **matching_algorithm** | **str**| The matching algorithm. | [optional] [default to randomBinaryTree]
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_image_tag"></a>
# **create_image_tag**
> create_image_tag(self, create_image_tag_request)

Add tag and reference image to search context. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

void (empty response body)

<a name="create_image_tag_async"></a>
# **create_image_tag_async**
> create_image_tag_async(self, create_image_tag_request)

Add tag and reference image to search context. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

void (empty response body)

### CreateImageTagRequest Parameters
```python
__init__(self, 
    image_data, 
    search_context_id, 
    tag_name, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **search_context_id** | **str**| The search context identifier. | 
 **tag_name** | **str**| The tag. | 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_modified_bmp"></a>
# **create_modified_bmp**
> create_modified_bmp(self, create_modified_bmp_request)

Update parameters of BMP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

**file**

<a name="create_modified_bmp_async"></a>
# **create_modified_bmp_async**
> create_modified_bmp_async(self, create_modified_bmp_request)

Update parameters of BMP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

**file**

### CreateModifiedBmpRequest Parameters
```python
__init__(self, 
    image_data, 
    bits_per_pixel, 
    horizontal_resolution, 
    vertical_resolution, 
    from_scratch=from_scratch, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **bits_per_pixel** | **int**| Color depth. | 
 **horizontal_resolution** | **int**| New horizontal resolution. | 
 **vertical_resolution** | **int**| New vertical resolution. | 
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_modified_emf"></a>
# **create_modified_emf**
> create_modified_emf(self, create_modified_emf_request)

Process existing EMF imaging using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

**file**

<a name="create_modified_emf_async"></a>
# **create_modified_emf_async**
> create_modified_emf_async(self, create_modified_emf_request)

Process existing EMF imaging using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

**file**

### CreateModifiedEmfRequest Parameters
```python
__init__(self, 
    image_data, 
    bk_color, 
    page_width, 
    page_height, 
    border_x, 
    border_y, 
    from_scratch=from_scratch, 
    out_path=out_path, 
    storage=storage, 
    format=format)
```

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
 **format** | **str**| Export format (PNG is the default one). Please, refer to the export table from https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases. | [optional] [default to png]

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_modified_gif"></a>
# **create_modified_gif**
> create_modified_gif(self, create_modified_gif_request)

Update parameters of GIF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

**file**

<a name="create_modified_gif_async"></a>
# **create_modified_gif_async**
> create_modified_gif_async(self, create_modified_gif_request)

Update parameters of GIF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

**file**

### CreateModifiedGifRequest Parameters
```python
__init__(self, 
    image_data, 
    background_color_index=background_color_index, 
    color_resolution=color_resolution, 
    has_trailer=has_trailer, 
    interlaced=interlaced, 
    is_palette_sorted=is_palette_sorted, 
    pixel_aspect_ratio=pixel_aspect_ratio, 
    from_scratch=from_scratch, 
    out_path=out_path, 
    storage=storage)
```

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

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_modified_jpeg"></a>
# **create_modified_jpeg**
> create_modified_jpeg(self, create_modified_jpeg_request)

Update parameters of JPEG image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

**file**

<a name="create_modified_jpeg_async"></a>
# **create_modified_jpeg_async**
> create_modified_jpeg_async(self, create_modified_jpeg_request)

Update parameters of JPEG image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

**file**

### CreateModifiedJpegRequest Parameters
```python
__init__(self, 
    image_data, 
    quality=quality, 
    compression_type=compression_type, 
    from_scratch=from_scratch, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **quality** | **int**| Quality of an image from 0 to 100. Default is 75. | [optional] [default to 75]
 **compression_type** | **str**| Compression type: baseline (default), progressive, lossless or jpegls. | [optional] [default to baseline]
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_modified_jpeg2000"></a>
# **create_modified_jpeg2000**
> create_modified_jpeg2000(self, create_modified_jpeg2000_request)

Update parameters of JPEG2000 image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

**file**

<a name="create_modified_jpeg2000_async"></a>
# **create_modified_jpeg2000_async**
> create_modified_jpeg2000_async(self, create_modified_jpeg2000_request)

Update parameters of JPEG2000 image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

**file**

### CreateModifiedJpeg2000Request Parameters
```python
__init__(self, 
    image_data, 
    comment, 
    codec=codec, 
    from_scratch=from_scratch, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **comment** | **str**| The comment (can be either single or comma-separated). | 
 **codec** | **str**| The codec (j2k or jp2). | [optional] [default to j2k]
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_modified_psd"></a>
# **create_modified_psd**
> create_modified_psd(self, create_modified_psd_request)

Update parameters of PSD image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

**file**

<a name="create_modified_psd_async"></a>
# **create_modified_psd_async**
> create_modified_psd_async(self, create_modified_psd_request)

Update parameters of PSD image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

**file**

### CreateModifiedPsdRequest Parameters
```python
__init__(self, 
    image_data, 
    channels_count=channels_count, 
    compression_method=compression_method, 
    from_scratch=from_scratch, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **channels_count** | **int**| Count of color channels. | [optional] [default to 4]
 **compression_method** | **str**| Compression method (for now, raw and RLE are supported). | [optional] [default to rle]
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_modified_svg"></a>
# **create_modified_svg**
> create_modified_svg(self, create_modified_svg_request)

Update parameters of SVG image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

**file**

<a name="create_modified_svg_async"></a>
# **create_modified_svg_async**
> create_modified_svg_async(self, create_modified_svg_request)

Update parameters of SVG image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

**file**

### CreateModifiedSvgRequest Parameters
```python
__init__(self, 
    image_data, 
    color_type=color_type, 
    text_as_shapes=text_as_shapes, 
    scale_x=scale_x, 
    scale_y=scale_y, 
    page_width=page_width, 
    page_height=page_height, 
    border_x=border_x, 
    border_y=border_y, 
    bk_color=bk_color, 
    from_scratch=from_scratch, 
    out_path=out_path, 
    storage=storage, 
    format=format)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **color_type** | **str**| Color type for SVG image. Only RGB is supported for now. | [optional] [default to Rgb]
 **text_as_shapes** | **bool**| Whether text must be converted as shapes. true if all text is turned into SVG shapes in the convertion; otherwise, false | [optional] [default to false]
 **scale_x** | **float**| Scale X. | [optional] [default to 0.0]
 **scale_y** | **float**| Scale Y. | [optional] [default to 0.0]
 **page_width** | **int**| Width of the page. | [optional] 
 **page_height** | **int**| Height of the page. | [optional] 
 **border_x** | **int**| Border width. Only 0 is supported for now. | [optional] 
 **border_y** | **int**| Border height. Only 0 is supported for now. | [optional] 
 **bk_color** | **str**| Background color (Default is white). | [optional] [default to white]
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 
 **format** | **str**| Export format (PNG is the default one). Please, refer to the export table from https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases. | [optional] [default to png]

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_modified_tiff"></a>
# **create_modified_tiff**
> create_modified_tiff(self, create_modified_tiff_request)

Update parameters of TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

**file**

<a name="create_modified_tiff_async"></a>
# **create_modified_tiff_async**
> create_modified_tiff_async(self, create_modified_tiff_request)

Update parameters of TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

**file**

### CreateModifiedTiffRequest Parameters
```python
__init__(self, 
    image_data, 
    bit_depth, 
    compression=compression, 
    resolution_unit=resolution_unit, 
    horizontal_resolution=horizontal_resolution, 
    vertical_resolution=vertical_resolution, 
    from_scratch=from_scratch, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **bit_depth** | **int**| Bit depth. | 
 **compression** | **str**| Compression (none is default). Please, refer to https://apireference.aspose.com/net/imaging/aspose.imaging.fileformats.tiff.enums/tiffcompressions for all possible values. | [optional] 
 **resolution_unit** | **str**| New resolution unit (none - the default one, inch or centimeter). | [optional] 
 **horizontal_resolution** | **float**| New horizontal resolution. | [optional] [default to 0.0]
 **vertical_resolution** | **float**| New vertical resolution. | [optional] [default to 0.0]
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_modified_web_p"></a>
# **create_modified_web_p**
> create_modified_web_p(self, create_modified_web_p_request)

Update parameters of WEBP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

**file**

<a name="create_modified_web_p_async"></a>
# **create_modified_web_p_async**
> create_modified_web_p_async(self, create_modified_web_p_request)

Update parameters of WEBP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

**file**

### CreateModifiedWebPRequest Parameters
```python
__init__(self, 
    image_data, 
    loss_less, 
    quality, 
    anim_loop_count, 
    anim_background_color, 
    from_scratch=from_scratch, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **loss_less** | **bool**| If WEBP should be in lossless format. | 
 **quality** | **int**| Quality (0-100). | 
 **anim_loop_count** | **int**| The animation loop count. | 
 **anim_background_color** | **str**| Color of the animation background. | 
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_modified_wmf"></a>
# **create_modified_wmf**
> create_modified_wmf(self, create_modified_wmf_request)

Process existing WMF image using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

**file**

<a name="create_modified_wmf_async"></a>
# **create_modified_wmf_async**
> create_modified_wmf_async(self, create_modified_wmf_request)

Process existing WMF image using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

**file**

### CreateModifiedWmfRequest Parameters
```python
__init__(self, 
    image_data, 
    bk_color, 
    page_width, 
    page_height, 
    border_x, 
    border_y, 
    from_scratch=from_scratch, 
    out_path=out_path, 
    storage=storage, 
    format=format)
```

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
 **format** | **str**| Export format (PNG is the default one). Please, refer to the export table from https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases. | [optional] [default to png]

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_resized_image"></a>
# **create_resized_image**
> create_resized_image(self, create_resized_image_request)

Resize an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

**file**

<a name="create_resized_image_async"></a>
# **create_resized_image_async**
> create_resized_image_async(self, create_resized_image_request)

Resize an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

**file**

### CreateResizedImageRequest Parameters
```python
__init__(self, 
    image_data, 
    new_width, 
    new_height, 
    format=format, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **new_width** | **int**| New width. | 
 **new_height** | **int**| New height. | 
 **format** | **str**| Resulting image format. Please, refer to https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_rotate_flipped_image"></a>
# **create_rotate_flipped_image**
> create_rotate_flipped_image(self, create_rotate_flipped_image_request)

Rotate and/or flip an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

**file**

<a name="create_rotate_flipped_image_async"></a>
# **create_rotate_flipped_image_async**
> create_rotate_flipped_image_async(self, create_rotate_flipped_image_request)

Rotate and/or flip an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

**file**

### CreateRotateFlippedImageRequest Parameters
```python
__init__(self, 
    image_data, 
    method, 
    format=format, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **method** | **str**| RotateFlip method (Rotate180FlipNone, Rotate180FlipX, Rotate180FlipXY, Rotate180FlipY, Rotate270FlipNone, Rotate270FlipX, Rotate270FlipXY, Rotate270FlipY, Rotate90FlipNone, Rotate90FlipX, Rotate90FlipXY, Rotate90FlipY, RotateNoneFlipNone, RotateNoneFlipX, RotateNoneFlipXY, RotateNoneFlipY). | 
 **format** | **str**| Resulting image format. Please, refer to https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_saved_image_as"></a>
# **create_saved_image_as**
> create_saved_image_as(self, create_saved_image_as_request)

Export existing image to another format. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.             

### Return type

**file**

<a name="create_saved_image_as_async"></a>
# **create_saved_image_as_async**
> create_saved_image_as_async(self, create_saved_image_as_request)

Export existing image to another format. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.             

Performs operation asynchronously.

### Return type

**file**

### CreateSavedImageAsRequest Parameters
```python
__init__(self, 
    image_data, 
    format, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **format** | **str**| Resulting image format. Please, refer to https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases. | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_updated_image"></a>
# **create_updated_image**
> create_updated_image(self, create_updated_image_request)

Perform scaling, cropping and flipping of an image in a single request. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

**file**

<a name="create_updated_image_async"></a>
# **create_updated_image_async**
> create_updated_image_async(self, create_updated_image_request)

Perform scaling, cropping and flipping of an image in a single request. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

**file**

### CreateUpdatedImageRequest Parameters
```python
__init__(self, 
    image_data, 
    new_width, 
    new_height, 
    x, 
    y, 
    rect_width, 
    rect_height, 
    rotate_flip_method, 
    format=format, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **new_width** | **int**| New width of the scaled image. | 
 **new_height** | **int**| New height of the scaled image. | 
 **x** | **int**| X position of start point for cropping rectangle. | 
 **y** | **int**| Y position of start point for cropping rectangle. | 
 **rect_width** | **int**| Width of cropping rectangle. | 
 **rect_height** | **int**| Height of cropping rectangle. | 
 **rotate_flip_method** | **str**| RotateFlip method (Rotate180FlipNone, Rotate180FlipX, Rotate180FlipXY, Rotate180FlipY, Rotate270FlipNone, Rotate270FlipX, Rotate270FlipXY, Rotate270FlipY, Rotate90FlipNone, Rotate90FlipX, Rotate90FlipXY, Rotate90FlipY, RotateNoneFlipNone, RotateNoneFlipX, RotateNoneFlipXY, RotateNoneFlipY). Default is RotateNoneFlipNone. | 
 **format** | **str**| Resulting image format. Please, refer to https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed image). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_web_site_image_features"></a>
# **create_web_site_image_features**
> create_web_site_image_features(self, create_web_site_image_features_request)

Extract images features from web page and add them to search context

### Return type

void (empty response body)

<a name="create_web_site_image_features_async"></a>
# **create_web_site_image_features_async**
> create_web_site_image_features_async(self, create_web_site_image_features_request)

Extract images features from web page and add them to search context

Performs operation asynchronously.

### Return type

void (empty response body)

### CreateWebSiteImageFeaturesRequest Parameters
```python
__init__(self, 
    search_context_id, 
    images_source, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| The search context identifier. | 
 **images_source** | **str**| Images source - a web page | 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="crop_image"></a>
# **crop_image**
> crop_image(self, crop_image_request)

Crop an existing image.

### Return type

**file**

<a name="crop_image_async"></a>
# **crop_image_async**
> crop_image_async(self, crop_image_request)

Crop an existing image.

Performs operation asynchronously.

### Return type

**file**

### CropImageRequest Parameters
```python
__init__(self, 
    name, 
    x, 
    y, 
    width, 
    height, 
    format=format, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an image. | 
 **x** | **int**| X position of start point for cropping rectangle. | 
 **y** | **int**| Y position of start point for cropping rectangle. | 
 **width** | **int**| Width of cropping rectangle | 
 **height** | **int**| Height of cropping rectangle. | 
 **format** | **str**| Resulting image format. Please, refer to https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases. | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="delete_file"></a>
# **delete_file**
> delete_file(self, delete_file_request)

Delete file

### Return type

void (empty response body)

<a name="delete_file_async"></a>
# **delete_file_async**
> delete_file_async(self, delete_file_request)

Delete file

Performs operation asynchronously.

### Return type

void (empty response body)

### DeleteFileRequest Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    version_id=version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to delete | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="delete_folder"></a>
# **delete_folder**
> delete_folder(self, delete_folder_request)

Delete folder

### Return type

void (empty response body)

<a name="delete_folder_async"></a>
# **delete_folder_async**
> delete_folder_async(self, delete_folder_request)

Delete folder

Performs operation asynchronously.

### Return type

void (empty response body)

### DeleteFolderRequest Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    recursive=recursive)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path e.g. &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **recursive** | **bool**| Enable to delete folders, subfolders and files | [optional] [default to false]

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="delete_image_features"></a>
# **delete_image_features**
> delete_image_features(self, delete_image_features_request)

Deletes image features from search context.

### Return type

void (empty response body)

<a name="delete_image_features_async"></a>
# **delete_image_features_async**
> delete_image_features_async(self, delete_image_features_request)

Deletes image features from search context.

Performs operation asynchronously.

### Return type

void (empty response body)

### DeleteImageFeaturesRequest Parameters
```python
__init__(self, 
    search_context_id, 
    image_id, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| The search context identifier. | 
 **image_id** | **str**| The image identifier. | 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="delete_image_search"></a>
# **delete_image_search**
> delete_image_search(self, delete_image_search_request)

Deletes the search context.

### Return type

void (empty response body)

<a name="delete_image_search_async"></a>
# **delete_image_search_async**
> delete_image_search_async(self, delete_image_search_request)

Deletes the search context.

Performs operation asynchronously.

### Return type

void (empty response body)

### DeleteImageSearchRequest Parameters
```python
__init__(self, 
    search_context_id, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| The search context identifier. | 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="delete_search_image"></a>
# **delete_search_image**
> delete_search_image(self, delete_search_image_request)

Delete image and images features from search context

### Return type

void (empty response body)

<a name="delete_search_image_async"></a>
# **delete_search_image_async**
> delete_search_image_async(self, delete_search_image_request)

Delete image and images features from search context

Performs operation asynchronously.

### Return type

void (empty response body)

### DeleteSearchImageRequest Parameters
```python
__init__(self, 
    search_context_id, 
    image_id, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| Search context identifier. | 
 **image_id** | **str**| Image identifier. | 
 **folder** | **str**| Folder. | [optional] 
 **storage** | **str**| Storage | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="deskew_image"></a>
# **deskew_image**
> deskew_image(self, deskew_image_request)

Deskew an existing image.

### Return type

**file**

<a name="deskew_image_async"></a>
# **deskew_image_async**
> deskew_image_async(self, deskew_image_request)

Deskew an existing image.

Performs operation asynchronously.

### Return type

**file**

### DeskewImageRequest Parameters
```python
__init__(self, 
    name, 
    resize_proportionally, 
    bk_color=bk_color, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Image file name. | 
 **resize_proportionally** | **bool**| Resize proportionally | 
 **bk_color** | **str**| Background color | [optional] 
 **folder** | **str**| Folder | [optional] 
 **storage** | **str**| Storage | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="download_file"></a>
# **download_file**
> download_file(self, download_file_request)

Download file

### Return type

[**file**](file.md)

<a name="download_file_async"></a>
# **download_file_async**
> download_file_async(self, download_file_request)

Download file

Performs operation asynchronously.

### Return type

[**file**](file.md)

### DownloadFileRequest Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    version_id=version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to download | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="extract_image_features"></a>
# **extract_image_features**
> extract_image_features(self, extract_image_features_request)

Extract features from image without adding to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

[**ImageFeatures**](ImageFeatures.md)

<a name="extract_image_features_async"></a>
# **extract_image_features_async**
> extract_image_features_async(self, extract_image_features_request)

Extract features from image without adding to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

[**ImageFeatures**](ImageFeatures.md)

### ExtractImageFeaturesRequest Parameters
```python
__init__(self, 
    search_context_id, 
    image_id, 
    image_data=image_data, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| The search context identifier. | 
 **image_id** | **str**| The image identifier. | 
 **image_data** | **file**| Input image | [optional] 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="extract_image_frame_properties"></a>
# **extract_image_frame_properties**
> extract_image_frame_properties(self, extract_image_frame_properties_request)

Get separate frame properties of existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

[**ImagingResponse**](ImagingResponse.md)

<a name="extract_image_frame_properties_async"></a>
# **extract_image_frame_properties_async**
> extract_image_frame_properties_async(self, extract_image_frame_properties_request)

Get separate frame properties of existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

[**ImagingResponse**](ImagingResponse.md)

### ExtractImageFramePropertiesRequest Parameters
```python
__init__(self, 
    image_data, 
    frame_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 
 **frame_id** | **int**| Number of a frame. | 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="extract_image_properties"></a>
# **extract_image_properties**
> extract_image_properties(self, extract_image_properties_request)

Get properties of an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

[**ImagingResponse**](ImagingResponse.md)

<a name="extract_image_properties_async"></a>
# **extract_image_properties_async**
> extract_image_properties_async(self, extract_image_properties_request)

Get properties of an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

[**ImagingResponse**](ImagingResponse.md)

### ExtractImagePropertiesRequest Parameters
```python
__init__(self, 
    image_data)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_data** | **file**| Input image | 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="filter_effect_image"></a>
# **filter_effect_image**
> filter_effect_image(self, filter_effect_image_request)

Apply filtering effects to an existing image.

### Return type

**file**

<a name="filter_effect_image_async"></a>
# **filter_effect_image_async**
> filter_effect_image_async(self, filter_effect_image_request)

Apply filtering effects to an existing image.

Performs operation asynchronously.

### Return type

**file**

### FilterEffectImageRequest Parameters
```python
__init__(self, 
    name, 
    filter_type, 
    filter_properties, 
    format=format, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an image. | 
 **filter_type** | **str**| Filter type (BigRectangular, SmallRectangular, Median, GaussWiener, MotionWiener, GaussianBlur, Sharpen, BilateralSmoothing). | 
 **filter_properties** | [**FilterPropertiesBase**](FilterPropertiesBase.md)| Filter properties. | 
 **format** | **str**| Resulting image format. Please, refer to https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases. | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="find_image_duplicates"></a>
# **find_image_duplicates**
> find_image_duplicates(self, find_image_duplicates_request)

Find images duplicates.

### Return type

[**ImageDuplicatesSet**](ImageDuplicatesSet.md)

<a name="find_image_duplicates_async"></a>
# **find_image_duplicates_async**
> find_image_duplicates_async(self, find_image_duplicates_request)

Find images duplicates.

Performs operation asynchronously.

### Return type

[**ImageDuplicatesSet**](ImageDuplicatesSet.md)

### FindImageDuplicatesRequest Parameters
```python
__init__(self, 
    search_context_id, 
    similarity_threshold, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| The search context identifier. | 
 **similarity_threshold** | **float**| The similarity threshold. | 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="find_images_by_tags"></a>
# **find_images_by_tags**
> find_images_by_tags(self, find_images_by_tags_request)

Find images by tags. Tags JSON string is passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

[**SearchResultsSet**](SearchResultsSet.md)

<a name="find_images_by_tags_async"></a>
# **find_images_by_tags_async**
> find_images_by_tags_async(self, find_images_by_tags_request)

Find images by tags. Tags JSON string is passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

[**SearchResultsSet**](SearchResultsSet.md)

### FindImagesByTagsRequest Parameters
```python
__init__(self, 
    tags, 
    search_context_id, 
    similarity_threshold, 
    max_count, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | **str**| Tags array for searching | 
 **search_context_id** | **str**| The search context identifier. | 
 **similarity_threshold** | **float**| The similarity threshold. | 
 **max_count** | **int**| The maximum count. | 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="find_similar_images"></a>
# **find_similar_images**
> find_similar_images(self, find_similar_images_request)

Find similar images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

[**SearchResultsSet**](SearchResultsSet.md)

<a name="find_similar_images_async"></a>
# **find_similar_images_async**
> find_similar_images_async(self, find_similar_images_request)

Find similar images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

[**SearchResultsSet**](SearchResultsSet.md)

### FindSimilarImagesRequest Parameters
```python
__init__(self, 
    search_context_id, 
    similarity_threshold, 
    max_count, 
    image_data=image_data, 
    image_id=image_id, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| The search context identifier. | 
 **similarity_threshold** | **float**| The similarity threshold. | 
 **max_count** | **int**| The maximum count. | 
 **image_data** | **file**| Input image | [optional] 
 **image_id** | **str**| The search image identifier. | [optional] 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="get_disc_usage"></a>
# **get_disc_usage**
> get_disc_usage(self, get_disc_usage_request)

Get disc usage

### Return type

[**DiscUsage**](DiscUsage.md)

<a name="get_disc_usage_async"></a>
# **get_disc_usage_async**
> get_disc_usage_async(self, get_disc_usage_request)

Get disc usage

Performs operation asynchronously.

### Return type

[**DiscUsage**](DiscUsage.md)

### GetDiscUsageRequest Parameters
```python
__init__(self, 
    storage_name=storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="get_file_versions"></a>
# **get_file_versions**
> get_file_versions(self, get_file_versions_request)

Get file versions

### Return type

[**FileVersions**](FileVersions.md)

<a name="get_file_versions_async"></a>
# **get_file_versions_async**
> get_file_versions_async(self, get_file_versions_request)

Get file versions

Performs operation asynchronously.

### Return type

[**FileVersions**](FileVersions.md)

### GetFileVersionsRequest Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="get_files_list"></a>
# **get_files_list**
> get_files_list(self, get_files_list_request)

Get all files and folders within a folder

### Return type

[**FilesList**](FilesList.md)

<a name="get_files_list_async"></a>
# **get_files_list_async**
> get_files_list_async(self, get_files_list_request)

Get all files and folders within a folder

Performs operation asynchronously.

### Return type

[**FilesList**](FilesList.md)

### GetFilesListRequest Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path e.g. &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="get_image_features"></a>
# **get_image_features**
> get_image_features(self, get_image_features_request)

Gets image features from search context.

### Return type

[**ImageFeatures**](ImageFeatures.md)

<a name="get_image_features_async"></a>
# **get_image_features_async**
> get_image_features_async(self, get_image_features_request)

Gets image features from search context.

Performs operation asynchronously.

### Return type

[**ImageFeatures**](ImageFeatures.md)

### GetImageFeaturesRequest Parameters
```python
__init__(self, 
    search_context_id, 
    image_id, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| The search context identifier. | 
 **image_id** | **str**| The image identifier. | 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="get_image_frame"></a>
# **get_image_frame**
> get_image_frame(self, get_image_frame_request)

Get separate frame from existing TIFF image.

### Return type

**file**

<a name="get_image_frame_async"></a>
# **get_image_frame_async**
> get_image_frame_async(self, get_image_frame_request)

Get separate frame from existing TIFF image.

Performs operation asynchronously.

### Return type

**file**

### GetImageFrameRequest Parameters
```python
__init__(self, 
    name, 
    frame_id, 
    new_width=new_width, 
    new_height=new_height, 
    x=x, 
    y=y, 
    rect_width=rect_width, 
    rect_height=rect_height, 
    rotate_flip_method=rotate_flip_method, 
    save_other_frames=save_other_frames, 
    folder=folder, 
    storage=storage)
```

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
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="get_image_frame_properties"></a>
# **get_image_frame_properties**
> get_image_frame_properties(self, get_image_frame_properties_request)

Get separate frame properties of existing TIFF image.

### Return type

[**ImagingResponse**](ImagingResponse.md)

<a name="get_image_frame_properties_async"></a>
# **get_image_frame_properties_async**
> get_image_frame_properties_async(self, get_image_frame_properties_request)

Get separate frame properties of existing TIFF image.

Performs operation asynchronously.

### Return type

[**ImagingResponse**](ImagingResponse.md)

### GetImageFramePropertiesRequest Parameters
```python
__init__(self, 
    name, 
    frame_id, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename with image. | 
 **frame_id** | **int**| Number of a frame. | 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="get_image_properties"></a>
# **get_image_properties**
> get_image_properties(self, get_image_properties_request)

Get properties of an image.

### Return type

[**ImagingResponse**](ImagingResponse.md)

<a name="get_image_properties_async"></a>
# **get_image_properties_async**
> get_image_properties_async(self, get_image_properties_request)

Get properties of an image.

Performs operation asynchronously.

### Return type

[**ImagingResponse**](ImagingResponse.md)

### GetImagePropertiesRequest Parameters
```python
__init__(self, 
    name, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an image. | 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="get_image_search_status"></a>
# **get_image_search_status**
> get_image_search_status(self, get_image_search_status_request)

Gets the search context status.

### Return type

[**SearchContextStatus**](SearchContextStatus.md)

<a name="get_image_search_status_async"></a>
# **get_image_search_status_async**
> get_image_search_status_async(self, get_image_search_status_request)

Gets the search context status.

Performs operation asynchronously.

### Return type

[**SearchContextStatus**](SearchContextStatus.md)

### GetImageSearchStatusRequest Parameters
```python
__init__(self, 
    search_context_id, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| The search context identifier. | 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="get_search_image"></a>
# **get_search_image**
> get_search_image(self, get_search_image_request)

Get image from search context

### Return type

**file**

<a name="get_search_image_async"></a>
# **get_search_image_async**
> get_search_image_async(self, get_search_image_request)

Get image from search context

Performs operation asynchronously.

### Return type

**file**

### GetSearchImageRequest Parameters
```python
__init__(self, 
    search_context_id, 
    image_id, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| Search context identifier. | 
 **image_id** | **str**| Image identifier. | 
 **folder** | **str**| Folder. | [optional] 
 **storage** | **str**| Storage | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="grayscale_image"></a>
# **grayscale_image**
> grayscale_image(self, grayscale_image_request)

Grayscale an existing image.

### Return type

**file**

<a name="grayscale_image_async"></a>
# **grayscale_image_async**
> grayscale_image_async(self, grayscale_image_request)

Grayscale an existing image.

Performs operation asynchronously.

### Return type

**file**

### GrayscaleImageRequest Parameters
```python
__init__(self, 
    name, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Image file name. | 
 **folder** | **str**| Folder | [optional] 
 **storage** | **str**| Storage | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="modify_bmp"></a>
# **modify_bmp**
> modify_bmp(self, modify_bmp_request)

Update parameters of existing BMP image.

### Return type

**file**

<a name="modify_bmp_async"></a>
# **modify_bmp_async**
> modify_bmp_async(self, modify_bmp_request)

Update parameters of existing BMP image.

Performs operation asynchronously.

### Return type

**file**

### ModifyBmpRequest Parameters
```python
__init__(self, 
    name, 
    bits_per_pixel, 
    horizontal_resolution, 
    vertical_resolution, 
    from_scratch=from_scratch, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **bits_per_pixel** | **int**| Color depth. | 
 **horizontal_resolution** | **int**| New horizontal resolution. | 
 **vertical_resolution** | **int**| New vertical resolution. | 
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="modify_emf"></a>
# **modify_emf**
> modify_emf(self, modify_emf_request)

Process existing EMF imaging using given parameters.

### Return type

**file**

<a name="modify_emf_async"></a>
# **modify_emf_async**
> modify_emf_async(self, modify_emf_request)

Process existing EMF imaging using given parameters.

Performs operation asynchronously.

### Return type

**file**

### ModifyEmfRequest Parameters
```python
__init__(self, 
    name, 
    bk_color, 
    page_width, 
    page_height, 
    border_x, 
    border_y, 
    from_scratch=from_scratch, 
    folder=folder, 
    storage=storage, 
    format=format)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **bk_color** | **str**| Color of the background. | 
 **page_width** | **int**| Width of the page. | 
 **page_height** | **int**| Height of the page. | 
 **border_x** | **int**| Border width. | 
 **border_y** | **int**| Border height. | 
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 
 **format** | **str**| Export format (PNG is the default one). Please, refer to the export table from https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases. | [optional] [default to png]

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="modify_gif"></a>
# **modify_gif**
> modify_gif(self, modify_gif_request)

Update parameters of existing GIF image.

### Return type

**file**

<a name="modify_gif_async"></a>
# **modify_gif_async**
> modify_gif_async(self, modify_gif_request)

Update parameters of existing GIF image.

Performs operation asynchronously.

### Return type

**file**

### ModifyGifRequest Parameters
```python
__init__(self, 
    name, 
    background_color_index=background_color_index, 
    color_resolution=color_resolution, 
    has_trailer=has_trailer, 
    interlaced=interlaced, 
    is_palette_sorted=is_palette_sorted, 
    pixel_aspect_ratio=pixel_aspect_ratio, 
    from_scratch=from_scratch, 
    folder=folder, 
    storage=storage)
```

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
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="modify_jpeg"></a>
# **modify_jpeg**
> modify_jpeg(self, modify_jpeg_request)

Update parameters of existing JPEG image.

### Return type

**file**

<a name="modify_jpeg_async"></a>
# **modify_jpeg_async**
> modify_jpeg_async(self, modify_jpeg_request)

Update parameters of existing JPEG image.

Performs operation asynchronously.

### Return type

**file**

### ModifyJpegRequest Parameters
```python
__init__(self, 
    name, 
    quality=quality, 
    compression_type=compression_type, 
    from_scratch=from_scratch, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **quality** | **int**| Quality of an image from 0 to 100. Default is 75. | [optional] [default to 75]
 **compression_type** | **str**| Compression type: baseline (default), progressive, lossless or jpegls. | [optional] [default to baseline]
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="modify_jpeg2000"></a>
# **modify_jpeg2000**
> modify_jpeg2000(self, modify_jpeg2000_request)

Update parameters of existing JPEG2000 image.

### Return type

**file**

<a name="modify_jpeg2000_async"></a>
# **modify_jpeg2000_async**
> modify_jpeg2000_async(self, modify_jpeg2000_request)

Update parameters of existing JPEG2000 image.

Performs operation asynchronously.

### Return type

**file**

### ModifyJpeg2000Request Parameters
```python
__init__(self, 
    name, 
    comment, 
    codec=codec, 
    from_scratch=from_scratch, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **comment** | **str**| The comment (can be either single or comma-separated). | 
 **codec** | **str**| The codec (j2k or jp2). | [optional] [default to j2k]
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="modify_psd"></a>
# **modify_psd**
> modify_psd(self, modify_psd_request)

Update parameters of existing PSD image.

### Return type

**file**

<a name="modify_psd_async"></a>
# **modify_psd_async**
> modify_psd_async(self, modify_psd_request)

Update parameters of existing PSD image.

Performs operation asynchronously.

### Return type

**file**

### ModifyPsdRequest Parameters
```python
__init__(self, 
    name, 
    channels_count=channels_count, 
    compression_method=compression_method, 
    from_scratch=from_scratch, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **channels_count** | **int**| Count of color channels. | [optional] [default to 4]
 **compression_method** | **str**| Compression method (for now, raw and RLE are supported). | [optional] [default to rle]
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="modify_svg"></a>
# **modify_svg**
> modify_svg(self, modify_svg_request)

Update parameters of existing SVG image.

### Return type

**file**

<a name="modify_svg_async"></a>
# **modify_svg_async**
> modify_svg_async(self, modify_svg_request)

Update parameters of existing SVG image.

Performs operation asynchronously.

### Return type

**file**

### ModifySvgRequest Parameters
```python
__init__(self, 
    name, 
    color_type=color_type, 
    text_as_shapes=text_as_shapes, 
    scale_x=scale_x, 
    scale_y=scale_y, 
    page_width=page_width, 
    page_height=page_height, 
    border_x=border_x, 
    border_y=border_y, 
    bk_color=bk_color, 
    from_scratch=from_scratch, 
    folder=folder, 
    storage=storage, 
    format=format)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **color_type** | **str**| Color type for SVG image. Only RGB is supported for now. | [optional] [default to Rgb]
 **text_as_shapes** | **bool**| Whether text must be converted as shapes. true if all text is turned into SVG shapes in the convertion; otherwise, false | [optional] [default to false]
 **scale_x** | **float**| Scale X. | [optional] [default to 0.0]
 **scale_y** | **float**| Scale Y. | [optional] [default to 0.0]
 **page_width** | **int**| Width of the page. | [optional] 
 **page_height** | **int**| Height of the page. | [optional] 
 **border_x** | **int**| Border width. Only 0 is supported for now. | [optional] 
 **border_y** | **int**| Border height. Only 0 is supported for now. | [optional] 
 **bk_color** | **str**| Background color (Default is white). | [optional] [default to white]
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 
 **format** | **str**| Export format (PNG is the default one). Please, refer to the export table from https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases. | [optional] [default to svg]

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="modify_tiff"></a>
# **modify_tiff**
> modify_tiff(self, modify_tiff_request)

Update parameters of existing TIFF image.

### Return type

**file**

<a name="modify_tiff_async"></a>
# **modify_tiff_async**
> modify_tiff_async(self, modify_tiff_request)

Update parameters of existing TIFF image.

Performs operation asynchronously.

### Return type

**file**

### ModifyTiffRequest Parameters
```python
__init__(self, 
    name, 
    bit_depth, 
    compression=compression, 
    resolution_unit=resolution_unit, 
    horizontal_resolution=horizontal_resolution, 
    vertical_resolution=vertical_resolution, 
    from_scratch=from_scratch, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **bit_depth** | **int**| Bit depth. | 
 **compression** | **str**| Compression (none is default). Please, refer to https://apireference.aspose.com/net/imaging/aspose.imaging.fileformats.tiff.enums/tiffcompressions for all possible values. | [optional] 
 **resolution_unit** | **str**| New resolution unit (none - the default one, inch or centimeter). | [optional] 
 **horizontal_resolution** | **float**| New horizontal resolution. | [optional] [default to 0.0]
 **vertical_resolution** | **float**| New vertical resolution. | [optional] [default to 0.0]
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="modify_web_p"></a>
# **modify_web_p**
> modify_web_p(self, modify_web_p_request)

Update parameters of existing WEBP image.

### Return type

**file**

<a name="modify_web_p_async"></a>
# **modify_web_p_async**
> modify_web_p_async(self, modify_web_p_request)

Update parameters of existing WEBP image.

Performs operation asynchronously.

### Return type

**file**

### ModifyWebPRequest Parameters
```python
__init__(self, 
    name, 
    loss_less, 
    quality, 
    anim_loop_count, 
    anim_background_color, 
    from_scratch=from_scratch, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **loss_less** | **bool**| If WEBP should be in lossless format. | 
 **quality** | **int**| Quality (0-100). | 
 **anim_loop_count** | **int**| The animation loop count. | 
 **anim_background_color** | **str**| Color of the animation background. | 
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="modify_wmf"></a>
# **modify_wmf**
> modify_wmf(self, modify_wmf_request)

Process existing WMF image using given parameters.

### Return type

**file**

<a name="modify_wmf_async"></a>
# **modify_wmf_async**
> modify_wmf_async(self, modify_wmf_request)

Process existing WMF image using given parameters.

Performs operation asynchronously.

### Return type

**file**

### ModifyWmfRequest Parameters
```python
__init__(self, 
    name, 
    bk_color, 
    page_width, 
    page_height, 
    border_x, 
    border_y, 
    from_scratch=from_scratch, 
    folder=folder, 
    storage=storage, 
    format=format)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **bk_color** | **str**| Color of the background. | 
 **page_width** | **int**| Width of the page. | 
 **page_height** | **int**| Height of the page. | 
 **border_x** | **int**| Border width. | 
 **border_y** | **int**| Border height. | 
 **from_scratch** | **bool**| Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false. | [optional] [default to false]
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 
 **format** | **str**| Export format (PNG is the default one). Please, refer to the export table from https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases. | [optional] [default to png]

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="move_file"></a>
# **move_file**
> move_file(self, move_file_request)

Move file

### Return type

void (empty response body)

<a name="move_file_async"></a>
# **move_file_async**
> move_file_async(self, move_file_request)

Move file

Performs operation asynchronously.

### Return type

void (empty response body)

### MoveFileRequest Parameters
```python
__init__(self, 
    src_path, 
    dest_path, 
    src_storage_name=src_storage_name, 
    dest_storage_name=dest_storage_name, 
    version_id=version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/src.ext&#39; | 
 **dest_path** | **str**| Destination file path e.g. &#39;/dest.ext&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to move | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="move_folder"></a>
# **move_folder**
> move_folder(self, move_folder_request)

Move folder

### Return type

void (empty response body)

<a name="move_folder_async"></a>
# **move_folder_async**
> move_folder_async(self, move_folder_request)

Move folder

Performs operation asynchronously.

### Return type

void (empty response body)

### MoveFolderRequest Parameters
```python
__init__(self, 
    src_path, 
    dest_path, 
    src_storage_name=src_storage_name, 
    dest_storage_name=dest_storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Folder path to move e.g. &#39;/folder&#39; | 
 **dest_path** | **str**| Destination folder path to move to e.g &#39;/dst&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="object_exists"></a>
# **object_exists**
> object_exists(self, object_exists_request)

Check if file or folder exists

### Return type

[**ObjectExist**](ObjectExist.md)

<a name="object_exists_async"></a>
# **object_exists_async**
> object_exists_async(self, object_exists_request)

Check if file or folder exists

Performs operation asynchronously.

### Return type

[**ObjectExist**](ObjectExist.md)

### ObjectExistsRequest Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    version_id=version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File or folder path e.g. &#39;/file.ext&#39; or &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="resize_image"></a>
# **resize_image**
> resize_image(self, resize_image_request)

Resize an existing image.

### Return type

**file**

<a name="resize_image_async"></a>
# **resize_image_async**
> resize_image_async(self, resize_image_request)

Resize an existing image.

Performs operation asynchronously.

### Return type

**file**

### ResizeImageRequest Parameters
```python
__init__(self, 
    name, 
    new_width, 
    new_height, 
    format=format, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an image. | 
 **new_width** | **int**| New width. | 
 **new_height** | **int**| New height. | 
 **format** | **str**| Resulting image format. Please, refer to https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases. | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="rotate_flip_image"></a>
# **rotate_flip_image**
> rotate_flip_image(self, rotate_flip_image_request)

Rotate and/or flip an existing image.

### Return type

**file**

<a name="rotate_flip_image_async"></a>
# **rotate_flip_image_async**
> rotate_flip_image_async(self, rotate_flip_image_request)

Rotate and/or flip an existing image.

Performs operation asynchronously.

### Return type

**file**

### RotateFlipImageRequest Parameters
```python
__init__(self, 
    name, 
    method, 
    format=format, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an image. | 
 **method** | **str**| RotateFlip method (Rotate180FlipNone, Rotate180FlipX, Rotate180FlipXY, Rotate180FlipY, Rotate270FlipNone, Rotate270FlipX, Rotate270FlipXY, Rotate270FlipY, Rotate90FlipNone, Rotate90FlipX, Rotate90FlipXY, Rotate90FlipY, RotateNoneFlipNone, RotateNoneFlipX, RotateNoneFlipXY, RotateNoneFlipY). | 
 **format** | **str**| Resulting image format. Please, refer to https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases. | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="save_image_as"></a>
# **save_image_as**
> save_image_as(self, save_image_as_request)

Export existing image to another format.

### Return type

**file**

<a name="save_image_as_async"></a>
# **save_image_as_async**
> save_image_as_async(self, save_image_as_request)

Export existing image to another format.

Performs operation asynchronously.

### Return type

**file**

### SaveImageAsRequest Parameters
```python
__init__(self, 
    name, 
    format, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of image. | 
 **format** | **str**| Resulting image format. Please, refer to https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases. | 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="storage_exists"></a>
# **storage_exists**
> storage_exists(self, storage_exists_request)

Check if storage exists

### Return type

[**StorageExist**](StorageExist.md)

<a name="storage_exists_async"></a>
# **storage_exists_async**
> storage_exists_async(self, storage_exists_request)

Check if storage exists

Performs operation asynchronously.

### Return type

[**StorageExist**](StorageExist.md)

### StorageExistsRequest Parameters
```python
__init__(self, 
    storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str**| Storage name | 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="update_image"></a>
# **update_image**
> update_image(self, update_image_request)

Perform scaling, cropping and flipping of an existing image in a single request.

### Return type

**file**

<a name="update_image_async"></a>
# **update_image_async**
> update_image_async(self, update_image_request)

Perform scaling, cropping and flipping of an existing image in a single request.

Performs operation asynchronously.

### Return type

**file**

### UpdateImageRequest Parameters
```python
__init__(self, 
    name, 
    new_width, 
    new_height, 
    x, 
    y, 
    rect_width, 
    rect_height, 
    rotate_flip_method, 
    format=format, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an image. | 
 **new_width** | **int**| New width of the scaled image. | 
 **new_height** | **int**| New height of the scaled image. | 
 **x** | **int**| X position of start point for cropping rectangle. | 
 **y** | **int**| Y position of start point for cropping rectangle. | 
 **rect_width** | **int**| Width of cropping rectangle. | 
 **rect_height** | **int**| Height of cropping rectangle. | 
 **rotate_flip_method** | **str**| RotateFlip method (Rotate180FlipNone, Rotate180FlipX, Rotate180FlipXY, Rotate180FlipY, Rotate270FlipNone, Rotate270FlipX, Rotate270FlipXY, Rotate270FlipY, Rotate90FlipNone, Rotate90FlipX, Rotate90FlipXY, Rotate90FlipY, RotateNoneFlipNone, RotateNoneFlipX, RotateNoneFlipXY, RotateNoneFlipY). Default is RotateNoneFlipNone. | 
 **format** | **str**| Resulting image format. Please, refer to https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases. | [optional] 
 **folder** | **str**| Folder with image to process. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="update_image_features"></a>
# **update_image_features**
> update_image_features(self, update_image_features_request)

Update images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

void (empty response body)

<a name="update_image_features_async"></a>
# **update_image_features_async**
> update_image_features_async(self, update_image_features_request)

Update images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

void (empty response body)

### UpdateImageFeaturesRequest Parameters
```python
__init__(self, 
    search_context_id, 
    image_id, 
    image_data=image_data, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| The search context identifier. | 
 **image_id** | **str**| The image identifier. | 
 **image_data** | **file**| Input image | [optional] 
 **folder** | **str**| The folder. | [optional] 
 **storage** | **str**| The storage. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="update_search_image"></a>
# **update_search_image**
> update_search_image(self, update_search_image_request)

Update image and images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.

### Return type

void (empty response body)

<a name="update_search_image_async"></a>
# **update_search_image_async**
> update_search_image_async(self, update_search_image_request)

Update image and images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

void (empty response body)

### UpdateSearchImageRequest Parameters
```python
__init__(self, 
    search_context_id, 
    image_id, 
    image_data=image_data, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_context_id** | **str**| Search context identifier. | 
 **image_id** | **str**| Image identifier. | 
 **image_data** | **file**| Input image | [optional] 
 **folder** | **str**| Folder. | [optional] 
 **storage** | **str**| Storage | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="upload_file"></a>
# **upload_file**
> upload_file(self, upload_file_request)

Upload file

### Return type

[**FilesUploadResult**](FilesUploadResult.md)

<a name="upload_file_async"></a>
# **upload_file_async**
> upload_file_async(self, upload_file_request)

Upload file

Performs operation asynchronously.

### Return type

[**FilesUploadResult**](FilesUploadResult.md)

### UploadFileRequest Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext             If the content is multipart and path does not contains the file name it tries to get them from filename parameter             from Content-Disposition header.              | 
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

