## Documentation for API endpoints

All URIs are relative to *https://api.aspose.cloud/v3.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ImagingApi* | [**add_search_image**](ImagingApi.md#add_search_image) | **POST** /imaging/ai/imageSearch/{searchContextId}/image | Add image and images features to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**add_search_image_async**](ImagingApi.md#add_search_image_async) | **POST** /imaging/ai/imageSearch/{searchContextId}/image | Add image and images features to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**append_tiff**](ImagingApi.md#append_tiff) | **POST** /imaging/tiff/{name}/appendTiff | Appends existing TIFF image to another existing TIFF image (i.e. merges TIFF images).
*ImagingApi* | [**append_tiff_async**](ImagingApi.md#append_tiff_async) | **POST** /imaging/tiff/{name}/appendTiff | Appends existing TIFF image to another existing TIFF image (i.e. merges TIFF images).
*ImagingApi* | [**compare_images**](ImagingApi.md#compare_images) | **POST** /imaging/ai/imageSearch/{searchContextId}/compare | Compare two images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**compare_images_async**](ImagingApi.md#compare_images_async) | **POST** /imaging/ai/imageSearch/{searchContextId}/compare | Compare two images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**convert_tiff_to_fax**](ImagingApi.md#convert_tiff_to_fax) | **GET** /imaging/tiff/{name}/toFax | Update parameters of existing TIFF image accordingly to fax parameters.
*ImagingApi* | [**convert_tiff_to_fax_async**](ImagingApi.md#convert_tiff_to_fax_async) | **GET** /imaging/tiff/{name}/toFax | Update parameters of existing TIFF image accordingly to fax parameters.
*ImagingApi* | [**copy_file**](ImagingApi.md#copy_file) | **PUT** /imaging/storage/file/copy/{srcPath} | Copy file
*ImagingApi* | [**copy_file_async**](ImagingApi.md#copy_file_async) | **PUT** /imaging/storage/file/copy/{srcPath} | Copy file
*ImagingApi* | [**copy_folder**](ImagingApi.md#copy_folder) | **PUT** /imaging/storage/folder/copy/{srcPath} | Copy folder
*ImagingApi* | [**copy_folder_async**](ImagingApi.md#copy_folder_async) | **PUT** /imaging/storage/folder/copy/{srcPath} | Copy folder
*ImagingApi* | [**create_cropped_image**](ImagingApi.md#create_cropped_image) | **POST** /imaging/crop | Crop an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_cropped_image_async**](ImagingApi.md#create_cropped_image_async) | **POST** /imaging/crop | Crop an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_deskewed_image**](ImagingApi.md#create_deskewed_image) | **POST** /imaging/deskew | Deskew an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_deskewed_image_async**](ImagingApi.md#create_deskewed_image_async) | **POST** /imaging/deskew | Deskew an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_fax_tiff**](ImagingApi.md#create_fax_tiff) | **POST** /imaging/tiff/toFax | Update parameters of TIFF image accordingly to fax parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_fax_tiff_async**](ImagingApi.md#create_fax_tiff_async) | **POST** /imaging/tiff/toFax | Update parameters of TIFF image accordingly to fax parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_folder**](ImagingApi.md#create_folder) | **PUT** /imaging/storage/folder/{path} | Create the folder
*ImagingApi* | [**create_folder_async**](ImagingApi.md#create_folder_async) | **PUT** /imaging/storage/folder/{path} | Create the folder
*ImagingApi* | [**create_grayscaled_image**](ImagingApi.md#create_grayscaled_image) | **POST** /imaging/grayscale | Grayscales an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_grayscaled_image_async**](ImagingApi.md#create_grayscaled_image_async) | **POST** /imaging/grayscale | Grayscales an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_image_features**](ImagingApi.md#create_image_features) | **POST** /imaging/ai/imageSearch/{searchContextId}/features | Extract images features and add them to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_image_features_async**](ImagingApi.md#create_image_features_async) | **POST** /imaging/ai/imageSearch/{searchContextId}/features | Extract images features and add them to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_image_frame**](ImagingApi.md#create_image_frame) | **POST** /imaging/frames/{frameId} | Get separate frame from existing image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_image_frame_async**](ImagingApi.md#create_image_frame_async) | **POST** /imaging/frames/{frameId} | Get separate frame from existing image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_image_frame_range**](ImagingApi.md#create_image_frame_range) | **POST** /imaging/frames/range | Get separate frame from existing image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_image_frame_range_async**](ImagingApi.md#create_image_frame_range_async) | **POST** /imaging/frames/range | Get separate frame from existing image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_image_search**](ImagingApi.md#create_image_search) | **POST** /imaging/ai/imageSearch/create | Create new search context.
*ImagingApi* | [**create_image_search_async**](ImagingApi.md#create_image_search_async) | **POST** /imaging/ai/imageSearch/create | Create new search context.
*ImagingApi* | [**create_image_tag**](ImagingApi.md#create_image_tag) | **POST** /imaging/ai/imageSearch/{searchContextId}/addTag | Add tag and reference image to search context. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_image_tag_async**](ImagingApi.md#create_image_tag_async) | **POST** /imaging/ai/imageSearch/{searchContextId}/addTag | Add tag and reference image to search context. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_modified_bmp**](ImagingApi.md#create_modified_bmp) | **POST** /imaging/bmp | Update parameters of BMP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_modified_bmp_async**](ImagingApi.md#create_modified_bmp_async) | **POST** /imaging/bmp | Update parameters of BMP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_modified_emf**](ImagingApi.md#create_modified_emf) | **POST** /imaging/emf | Process existing EMF imaging using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_modified_emf_async**](ImagingApi.md#create_modified_emf_async) | **POST** /imaging/emf | Process existing EMF imaging using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_modified_gif**](ImagingApi.md#create_modified_gif) | **POST** /imaging/gif | Update parameters of GIF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_modified_gif_async**](ImagingApi.md#create_modified_gif_async) | **POST** /imaging/gif | Update parameters of GIF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_modified_jpeg**](ImagingApi.md#create_modified_jpeg) | **POST** /imaging/jpg | Update parameters of JPEG image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_modified_jpeg_async**](ImagingApi.md#create_modified_jpeg_async) | **POST** /imaging/jpg | Update parameters of JPEG image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_modified_jpeg2000**](ImagingApi.md#create_modified_jpeg2000) | **POST** /imaging/jpg2000 | Update parameters of JPEG2000 image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_modified_jpeg2000_async**](ImagingApi.md#create_modified_jpeg2000_async) | **POST** /imaging/jpg2000 | Update parameters of JPEG2000 image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_modified_psd**](ImagingApi.md#create_modified_psd) | **POST** /imaging/psd | Update parameters of PSD image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_modified_psd_async**](ImagingApi.md#create_modified_psd_async) | **POST** /imaging/psd | Update parameters of PSD image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_modified_svg**](ImagingApi.md#create_modified_svg) | **POST** /imaging/svg | Update parameters of SVG image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_modified_svg_async**](ImagingApi.md#create_modified_svg_async) | **POST** /imaging/svg | Update parameters of SVG image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_modified_tiff**](ImagingApi.md#create_modified_tiff) | **POST** /imaging/tiff | Update parameters of TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_modified_tiff_async**](ImagingApi.md#create_modified_tiff_async) | **POST** /imaging/tiff | Update parameters of TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_modified_web_p**](ImagingApi.md#create_modified_web_p) | **POST** /imaging/webp | Update parameters of WEBP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_modified_web_p_async**](ImagingApi.md#create_modified_web_p_async) | **POST** /imaging/webp | Update parameters of WEBP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_modified_wmf**](ImagingApi.md#create_modified_wmf) | **POST** /imaging/wmf | Process existing WMF image using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_modified_wmf_async**](ImagingApi.md#create_modified_wmf_async) | **POST** /imaging/wmf | Process existing WMF image using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_object_bounds**](ImagingApi.md#create_object_bounds) | **POST** /imaging/ai/objectdetection/bounds | Detects objects bounds. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_object_bounds_async**](ImagingApi.md#create_object_bounds_async) | **POST** /imaging/ai/objectdetection/bounds | Detects objects bounds. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_resized_image**](ImagingApi.md#create_resized_image) | **POST** /imaging/resize | Resize an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_resized_image_async**](ImagingApi.md#create_resized_image_async) | **POST** /imaging/resize | Resize an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_rotate_flipped_image**](ImagingApi.md#create_rotate_flipped_image) | **POST** /imaging/rotateflip | Rotate and/or flip an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_rotate_flipped_image_async**](ImagingApi.md#create_rotate_flipped_image_async) | **POST** /imaging/rotateflip | Rotate and/or flip an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_saved_image_as**](ImagingApi.md#create_saved_image_as) | **POST** /imaging/saveAs | Export existing image to another format. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.             
*ImagingApi* | [**create_saved_image_as_async**](ImagingApi.md#create_saved_image_as_async) | **POST** /imaging/saveAs | Export existing image to another format. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.             
*ImagingApi* | [**create_updated_image**](ImagingApi.md#create_updated_image) | **POST** /imaging/updateImage | Perform scaling, cropping and flipping of an image in a single request. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_updated_image_async**](ImagingApi.md#create_updated_image_async) | **POST** /imaging/updateImage | Perform scaling, cropping and flipping of an image in a single request. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**create_visual_object_bounds**](ImagingApi.md#create_visual_object_bounds) | **POST** /imaging/ai/objectdetection/visualbounds | Detect objects bounds and draw them on the original image
*ImagingApi* | [**create_visual_object_bounds_async**](ImagingApi.md#create_visual_object_bounds_async) | **POST** /imaging/ai/objectdetection/visualbounds | Detect objects bounds and draw them on the original image
*ImagingApi* | [**create_web_site_image_features**](ImagingApi.md#create_web_site_image_features) | **POST** /imaging/ai/imageSearch/{searchContextId}/features/web | Extract images features from web page and add them to search context
*ImagingApi* | [**create_web_site_image_features_async**](ImagingApi.md#create_web_site_image_features_async) | **POST** /imaging/ai/imageSearch/{searchContextId}/features/web | Extract images features from web page and add them to search context
*ImagingApi* | [**crop_image**](ImagingApi.md#crop_image) | **GET** /imaging/{name}/crop | Crop an existing image.
*ImagingApi* | [**crop_image_async**](ImagingApi.md#crop_image_async) | **GET** /imaging/{name}/crop | Crop an existing image.
*ImagingApi* | [**delete_file**](ImagingApi.md#delete_file) | **DELETE** /imaging/storage/file/{path} | Delete file
*ImagingApi* | [**delete_file_async**](ImagingApi.md#delete_file_async) | **DELETE** /imaging/storage/file/{path} | Delete file
*ImagingApi* | [**delete_folder**](ImagingApi.md#delete_folder) | **DELETE** /imaging/storage/folder/{path} | Delete folder
*ImagingApi* | [**delete_folder_async**](ImagingApi.md#delete_folder_async) | **DELETE** /imaging/storage/folder/{path} | Delete folder
*ImagingApi* | [**delete_image_features**](ImagingApi.md#delete_image_features) | **DELETE** /imaging/ai/imageSearch/{searchContextId}/features | Deletes image features from search context.
*ImagingApi* | [**delete_image_features_async**](ImagingApi.md#delete_image_features_async) | **DELETE** /imaging/ai/imageSearch/{searchContextId}/features | Deletes image features from search context.
*ImagingApi* | [**delete_image_search**](ImagingApi.md#delete_image_search) | **DELETE** /imaging/ai/imageSearch/{searchContextId} | Deletes the search context.
*ImagingApi* | [**delete_image_search_async**](ImagingApi.md#delete_image_search_async) | **DELETE** /imaging/ai/imageSearch/{searchContextId} | Deletes the search context.
*ImagingApi* | [**delete_search_image**](ImagingApi.md#delete_search_image) | **DELETE** /imaging/ai/imageSearch/{searchContextId}/image | Delete image and images features from search context
*ImagingApi* | [**delete_search_image_async**](ImagingApi.md#delete_search_image_async) | **DELETE** /imaging/ai/imageSearch/{searchContextId}/image | Delete image and images features from search context
*ImagingApi* | [**deskew_image**](ImagingApi.md#deskew_image) | **GET** /imaging/{name}/deskew | Deskew an existing image.
*ImagingApi* | [**deskew_image_async**](ImagingApi.md#deskew_image_async) | **GET** /imaging/{name}/deskew | Deskew an existing image.
*ImagingApi* | [**download_file**](ImagingApi.md#download_file) | **GET** /imaging/storage/file/{path} | Download file
*ImagingApi* | [**download_file_async**](ImagingApi.md#download_file_async) | **GET** /imaging/storage/file/{path} | Download file
*ImagingApi* | [**extract_image_features**](ImagingApi.md#extract_image_features) | **GET** /imaging/ai/imageSearch/{searchContextId}/image2features | Extract features from image without adding to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**extract_image_features_async**](ImagingApi.md#extract_image_features_async) | **GET** /imaging/ai/imageSearch/{searchContextId}/image2features | Extract features from image without adding to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**extract_image_frame_properties**](ImagingApi.md#extract_image_frame_properties) | **POST** /imaging/frames/{frameId}/properties | Get separate frame properties of existing image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**extract_image_frame_properties_async**](ImagingApi.md#extract_image_frame_properties_async) | **POST** /imaging/frames/{frameId}/properties | Get separate frame properties of existing image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**extract_image_properties**](ImagingApi.md#extract_image_properties) | **POST** /imaging/properties | Get properties of an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**extract_image_properties_async**](ImagingApi.md#extract_image_properties_async) | **POST** /imaging/properties | Get properties of an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**filter_effect_image**](ImagingApi.md#filter_effect_image) | **PUT** /imaging/{name}/filterEffect | Apply filtering effects to an existing image.
*ImagingApi* | [**filter_effect_image_async**](ImagingApi.md#filter_effect_image_async) | **PUT** /imaging/{name}/filterEffect | Apply filtering effects to an existing image.
*ImagingApi* | [**find_image_duplicates**](ImagingApi.md#find_image_duplicates) | **GET** /imaging/ai/imageSearch/{searchContextId}/findDuplicates | Find images duplicates.
*ImagingApi* | [**find_image_duplicates_async**](ImagingApi.md#find_image_duplicates_async) | **GET** /imaging/ai/imageSearch/{searchContextId}/findDuplicates | Find images duplicates.
*ImagingApi* | [**find_images_by_tags**](ImagingApi.md#find_images_by_tags) | **POST** /imaging/ai/imageSearch/{searchContextId}/findByTags | Find images by tags. Tags JSON string is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**find_images_by_tags_async**](ImagingApi.md#find_images_by_tags_async) | **POST** /imaging/ai/imageSearch/{searchContextId}/findByTags | Find images by tags. Tags JSON string is passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**find_similar_images**](ImagingApi.md#find_similar_images) | **GET** /imaging/ai/imageSearch/{searchContextId}/findSimilar | Find similar images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**find_similar_images_async**](ImagingApi.md#find_similar_images_async) | **GET** /imaging/ai/imageSearch/{searchContextId}/findSimilar | Find similar images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**get_disc_usage**](ImagingApi.md#get_disc_usage) | **GET** /imaging/storage/disc | Get disc usage
*ImagingApi* | [**get_disc_usage_async**](ImagingApi.md#get_disc_usage_async) | **GET** /imaging/storage/disc | Get disc usage
*ImagingApi* | [**get_file_versions**](ImagingApi.md#get_file_versions) | **GET** /imaging/storage/version/{path} | Get file versions
*ImagingApi* | [**get_file_versions_async**](ImagingApi.md#get_file_versions_async) | **GET** /imaging/storage/version/{path} | Get file versions
*ImagingApi* | [**get_files_list**](ImagingApi.md#get_files_list) | **GET** /imaging/storage/folder/{path} | Get all files and folders within a folder
*ImagingApi* | [**get_files_list_async**](ImagingApi.md#get_files_list_async) | **GET** /imaging/storage/folder/{path} | Get all files and folders within a folder
*ImagingApi* | [**get_image_features**](ImagingApi.md#get_image_features) | **GET** /imaging/ai/imageSearch/{searchContextId}/features | Gets image features from search context.
*ImagingApi* | [**get_image_features_async**](ImagingApi.md#get_image_features_async) | **GET** /imaging/ai/imageSearch/{searchContextId}/features | Gets image features from search context.
*ImagingApi* | [**get_image_frame**](ImagingApi.md#get_image_frame) | **GET** /imaging/{name}/frames/{frameId} | Get separate frame from existing image.
*ImagingApi* | [**get_image_frame_async**](ImagingApi.md#get_image_frame_async) | **GET** /imaging/{name}/frames/{frameId} | Get separate frame from existing image.
*ImagingApi* | [**get_image_frame_properties**](ImagingApi.md#get_image_frame_properties) | **GET** /imaging/{name}/frames/{frameId}/properties | Get separate frame properties of existing image.
*ImagingApi* | [**get_image_frame_properties_async**](ImagingApi.md#get_image_frame_properties_async) | **GET** /imaging/{name}/frames/{frameId}/properties | Get separate frame properties of existing image.
*ImagingApi* | [**get_image_frame_range**](ImagingApi.md#get_image_frame_range) | **GET** /imaging/{name}/frames/range | Get frames range from existing image.
*ImagingApi* | [**get_image_frame_range_async**](ImagingApi.md#get_image_frame_range_async) | **GET** /imaging/{name}/frames/range | Get frames range from existing image.
*ImagingApi* | [**get_image_properties**](ImagingApi.md#get_image_properties) | **GET** /imaging/{name}/properties | Get properties of an image.
*ImagingApi* | [**get_image_properties_async**](ImagingApi.md#get_image_properties_async) | **GET** /imaging/{name}/properties | Get properties of an image.
*ImagingApi* | [**get_image_search_status**](ImagingApi.md#get_image_search_status) | **GET** /imaging/ai/imageSearch/{searchContextId}/status | Gets the search context status.
*ImagingApi* | [**get_image_search_status_async**](ImagingApi.md#get_image_search_status_async) | **GET** /imaging/ai/imageSearch/{searchContextId}/status | Gets the search context status.
*ImagingApi* | [**get_search_image**](ImagingApi.md#get_search_image) | **GET** /imaging/ai/imageSearch/{searchContextId}/image | Get image from search context
*ImagingApi* | [**get_search_image_async**](ImagingApi.md#get_search_image_async) | **GET** /imaging/ai/imageSearch/{searchContextId}/image | Get image from search context
*ImagingApi* | [**grayscale_image**](ImagingApi.md#grayscale_image) | **GET** /imaging/{name}/grayscale | Grayscale an existing image.
*ImagingApi* | [**grayscale_image_async**](ImagingApi.md#grayscale_image_async) | **GET** /imaging/{name}/grayscale | Grayscale an existing image.
*ImagingApi* | [**modify_bmp**](ImagingApi.md#modify_bmp) | **GET** /imaging/{name}/bmp | Update parameters of existing BMP image.
*ImagingApi* | [**modify_bmp_async**](ImagingApi.md#modify_bmp_async) | **GET** /imaging/{name}/bmp | Update parameters of existing BMP image.
*ImagingApi* | [**modify_emf**](ImagingApi.md#modify_emf) | **GET** /imaging/{name}/emf | Process existing EMF imaging using given parameters.
*ImagingApi* | [**modify_emf_async**](ImagingApi.md#modify_emf_async) | **GET** /imaging/{name}/emf | Process existing EMF imaging using given parameters.
*ImagingApi* | [**modify_gif**](ImagingApi.md#modify_gif) | **GET** /imaging/{name}/gif | Update parameters of existing GIF image.
*ImagingApi* | [**modify_gif_async**](ImagingApi.md#modify_gif_async) | **GET** /imaging/{name}/gif | Update parameters of existing GIF image.
*ImagingApi* | [**modify_jpeg**](ImagingApi.md#modify_jpeg) | **GET** /imaging/{name}/jpg | Update parameters of existing JPEG image.
*ImagingApi* | [**modify_jpeg_async**](ImagingApi.md#modify_jpeg_async) | **GET** /imaging/{name}/jpg | Update parameters of existing JPEG image.
*ImagingApi* | [**modify_jpeg2000**](ImagingApi.md#modify_jpeg2000) | **GET** /imaging/{name}/jpg2000 | Update parameters of existing JPEG2000 image.
*ImagingApi* | [**modify_jpeg2000_async**](ImagingApi.md#modify_jpeg2000_async) | **GET** /imaging/{name}/jpg2000 | Update parameters of existing JPEG2000 image.
*ImagingApi* | [**modify_psd**](ImagingApi.md#modify_psd) | **GET** /imaging/{name}/psd | Update parameters of existing PSD image.
*ImagingApi* | [**modify_psd_async**](ImagingApi.md#modify_psd_async) | **GET** /imaging/{name}/psd | Update parameters of existing PSD image.
*ImagingApi* | [**modify_svg**](ImagingApi.md#modify_svg) | **GET** /imaging/{name}/svg | Update parameters of existing SVG image.
*ImagingApi* | [**modify_svg_async**](ImagingApi.md#modify_svg_async) | **GET** /imaging/{name}/svg | Update parameters of existing SVG image.
*ImagingApi* | [**modify_tiff**](ImagingApi.md#modify_tiff) | **GET** /imaging/{name}/tiff | Update parameters of existing TIFF image.
*ImagingApi* | [**modify_tiff_async**](ImagingApi.md#modify_tiff_async) | **GET** /imaging/{name}/tiff | Update parameters of existing TIFF image.
*ImagingApi* | [**modify_web_p**](ImagingApi.md#modify_web_p) | **GET** /imaging/{name}/webp | Update parameters of existing WEBP image.
*ImagingApi* | [**modify_web_p_async**](ImagingApi.md#modify_web_p_async) | **GET** /imaging/{name}/webp | Update parameters of existing WEBP image.
*ImagingApi* | [**modify_wmf**](ImagingApi.md#modify_wmf) | **GET** /imaging/{name}/wmf | Process existing WMF image using given parameters.
*ImagingApi* | [**modify_wmf_async**](ImagingApi.md#modify_wmf_async) | **GET** /imaging/{name}/wmf | Process existing WMF image using given parameters.
*ImagingApi* | [**move_file**](ImagingApi.md#move_file) | **PUT** /imaging/storage/file/move/{srcPath} | Move file
*ImagingApi* | [**move_file_async**](ImagingApi.md#move_file_async) | **PUT** /imaging/storage/file/move/{srcPath} | Move file
*ImagingApi* | [**move_folder**](ImagingApi.md#move_folder) | **PUT** /imaging/storage/folder/move/{srcPath} | Move folder
*ImagingApi* | [**move_folder_async**](ImagingApi.md#move_folder_async) | **PUT** /imaging/storage/folder/move/{srcPath} | Move folder
*ImagingApi* | [**object_bounds**](ImagingApi.md#object_bounds) | **GET** /imaging/ai/objectdetection/bounds | Detect objects&#39; bounds
*ImagingApi* | [**object_bounds_async**](ImagingApi.md#object_bounds_async) | **GET** /imaging/ai/objectdetection/bounds | Detect objects&#39; bounds
*ImagingApi* | [**object_exists**](ImagingApi.md#object_exists) | **GET** /imaging/storage/exist/{path} | Check if file or folder exists
*ImagingApi* | [**object_exists_async**](ImagingApi.md#object_exists_async) | **GET** /imaging/storage/exist/{path} | Check if file or folder exists
*ImagingApi* | [**resize_image**](ImagingApi.md#resize_image) | **GET** /imaging/{name}/resize | Resize an existing image.
*ImagingApi* | [**resize_image_async**](ImagingApi.md#resize_image_async) | **GET** /imaging/{name}/resize | Resize an existing image.
*ImagingApi* | [**rotate_flip_image**](ImagingApi.md#rotate_flip_image) | **GET** /imaging/{name}/rotateflip | Rotate and/or flip an existing image.
*ImagingApi* | [**rotate_flip_image_async**](ImagingApi.md#rotate_flip_image_async) | **GET** /imaging/{name}/rotateflip | Rotate and/or flip an existing image.
*ImagingApi* | [**save_image_as**](ImagingApi.md#save_image_as) | **GET** /imaging/{name}/saveAs | Export existing image to another format.
*ImagingApi* | [**save_image_as_async**](ImagingApi.md#save_image_as_async) | **GET** /imaging/{name}/saveAs | Export existing image to another format.
*ImagingApi* | [**storage_exists**](ImagingApi.md#storage_exists) | **GET** /imaging/storage/{storageName}/exist | Check if storage exists
*ImagingApi* | [**storage_exists_async**](ImagingApi.md#storage_exists_async) | **GET** /imaging/storage/{storageName}/exist | Check if storage exists
*ImagingApi* | [**update_image**](ImagingApi.md#update_image) | **GET** /imaging/{name}/updateImage | Perform scaling, cropping and flipping of an existing image in a single request.
*ImagingApi* | [**update_image_async**](ImagingApi.md#update_image_async) | **GET** /imaging/{name}/updateImage | Perform scaling, cropping and flipping of an existing image in a single request.
*ImagingApi* | [**update_image_features**](ImagingApi.md#update_image_features) | **PUT** /imaging/ai/imageSearch/{searchContextId}/features | Update images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**update_image_features_async**](ImagingApi.md#update_image_features_async) | **PUT** /imaging/ai/imageSearch/{searchContextId}/features | Update images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**update_search_image**](ImagingApi.md#update_search_image) | **PUT** /imaging/ai/imageSearch/{searchContextId}/image | Update image and images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**update_search_image_async**](ImagingApi.md#update_search_image_async) | **PUT** /imaging/ai/imageSearch/{searchContextId}/image | Update image and images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.
*ImagingApi* | [**upload_file**](ImagingApi.md#upload_file) | **PUT** /imaging/storage/file/{path} | Upload file
*ImagingApi* | [**upload_file_async**](ImagingApi.md#upload_file_async) | **PUT** /imaging/storage/file/{path} | Upload file
*ImagingApi* | [**visual_object_bounds**](ImagingApi.md#visual_object_bounds) | **GET** /imaging/ai/objectdetection/visualbounds | Detect objects bounds and draw them on the original image
*ImagingApi* | [**visual_object_bounds_async**](ImagingApi.md#visual_object_bounds_async) | **GET** /imaging/ai/objectdetection/visualbounds | Detect objects bounds and draw them on the original image


## Documentation for Models

 - [asposeimagingcloud.models.BmpProperties](BmpProperties.md)
 - [asposeimagingcloud.models.DetectedObject](DetectedObject.md)
 - [asposeimagingcloud.models.DetectedObjectList](DetectedObjectList.md)
 - [asposeimagingcloud.models.DicomProperties](DicomProperties.md)
 - [asposeimagingcloud.models.DiscUsage](DiscUsage.md)
 - [asposeimagingcloud.models.DjvuProperties](DjvuProperties.md)
 - [asposeimagingcloud.models.DngProperties](DngProperties.md)
 - [asposeimagingcloud.models.Error](Error.md)
 - [asposeimagingcloud.models.ErrorDetails](ErrorDetails.md)
 - [asposeimagingcloud.models.ExifData](ExifData.md)
 - [asposeimagingcloud.models.FileVersions](FileVersions.md)
 - [asposeimagingcloud.models.FilesList](FilesList.md)
 - [asposeimagingcloud.models.FilesUploadResult](FilesUploadResult.md)
 - [asposeimagingcloud.models.FilterPropertiesBase](FilterPropertiesBase.md)
 - [asposeimagingcloud.models.GifProperties](GifProperties.md)
 - [asposeimagingcloud.models.ImageDuplicates](ImageDuplicates.md)
 - [asposeimagingcloud.models.ImageDuplicatesSet](ImageDuplicatesSet.md)
 - [asposeimagingcloud.models.ImageFeatures](ImageFeatures.md)
 - [asposeimagingcloud.models.ImagingResponse](ImagingResponse.md)
 - [asposeimagingcloud.models.JfifData](JfifData.md)
 - [asposeimagingcloud.models.Jpeg2000Properties](Jpeg2000Properties.md)
 - [asposeimagingcloud.models.JpegProperties](JpegProperties.md)
 - [asposeimagingcloud.models.ObjectExist](ObjectExist.md)
 - [asposeimagingcloud.models.OdgMetadata](OdgMetadata.md)
 - [asposeimagingcloud.models.OdgPage](OdgPage.md)
 - [asposeimagingcloud.models.OdgProperties](OdgProperties.md)
 - [asposeimagingcloud.models.PngProperties](PngProperties.md)
 - [asposeimagingcloud.models.PsdProperties](PsdProperties.md)
 - [asposeimagingcloud.models.Rectangle](Rectangle.md)
 - [asposeimagingcloud.models.SearchContextStatus](SearchContextStatus.md)
 - [asposeimagingcloud.models.SearchResult](SearchResult.md)
 - [asposeimagingcloud.models.SearchResultsSet](SearchResultsSet.md)
 - [asposeimagingcloud.models.StorageExist](StorageExist.md)
 - [asposeimagingcloud.models.StorageFile](StorageFile.md)
 - [asposeimagingcloud.models.SvgProperties](SvgProperties.md)
 - [asposeimagingcloud.models.TiffFrame](TiffFrame.md)
 - [asposeimagingcloud.models.TiffOptions](TiffOptions.md)
 - [asposeimagingcloud.models.TiffProperties](TiffProperties.md)
 - [asposeimagingcloud.models.WebPProperties](WebPProperties.md)
 - [asposeimagingcloud.models.BigRectangularFilterProperties](BigRectangularFilterProperties.md)
 - [asposeimagingcloud.models.BilateralSmoothingFilterProperties](BilateralSmoothingFilterProperties.md)
 - [asposeimagingcloud.models.ConvolutionFilterProperties](ConvolutionFilterProperties.md)
 - [asposeimagingcloud.models.DeconvolutionFilterProperties](DeconvolutionFilterProperties.md)
 - [asposeimagingcloud.models.FileVersion](FileVersion.md)
 - [asposeimagingcloud.models.JpegExifData](JpegExifData.md)
 - [asposeimagingcloud.models.MedianFilterProperties](MedianFilterProperties.md)
 - [asposeimagingcloud.models.SmallRectangularFilterProperties](SmallRectangularFilterProperties.md)
 - [asposeimagingcloud.models.GaussWienerFilterProperties](GaussWienerFilterProperties.md)
 - [asposeimagingcloud.models.GaussianBlurFilterProperties](GaussianBlurFilterProperties.md)
 - [asposeimagingcloud.models.MotionWienerFilterProperties](MotionWienerFilterProperties.md)
 - [asposeimagingcloud.models.SharpenFilterProperties](SharpenFilterProperties.md)

