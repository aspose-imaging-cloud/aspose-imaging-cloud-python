### Imaging - Save as: convert image from storage to another format
```python
# optional parameters are base URL, API version and debug mode
imaging_api = ImagingApi('yourAppKey', 'yourAppSid')

try:
    # upload local image to storage
    upload_file_request = UploadFileRequest(
        'ExampleFolderPython/inputImage.png', 'test.png')
    result = imaging_api.upload_file(upload_file_request)
    # inspect result.errors list if there were any
    # inspect result.uploaded list for uploaded file names

    # convert image from storage to JPEG
    save_as_request = SaveImageAsRequest(
        'inputImage.png', 'jpg', 'ExampleFolderPython')
    converted_image = imaging_api.save_image_as(save_as_request)

    # process resulted image
    # for example, save it to storage
    upload_file_request = UploadFileRequest(
        "ExampleFolderPython/resultImage.jpg", converted_image)
    result = imaging_api.upload_file(upload_file_request)
    # inspect result.errors list if there were any
    # inspect result.uploaded list for uploaded file names

finally:
    # remove files from storage
    imaging_api.delete_file(
        DeleteFileRequest('ExampleFolderPython/inputImage.png'))
    imaging_api.delete_file(
        DeleteFileRequest('ExampleFolderPython/resultImage.png'))
```

### Imaging - Save as: convert image from request stream to another format
```python
# optional parameters are base URL, API version and debug mode
imaging_api = ImagingApi('yourAppKey', 'yourAppSid')

try:
    # convert image from request to JPEG and save it to storage
    # please, use outPath parameter for saving the result to storage
    save_as_to_storage_request = CreateSavedImageAsRequest(
        'test.png', 'jpg', 'ExampleFolderPython/resultImage.png')
    imaging_api.create_saved_image_as(save_as_to_storage_request)

    # download saved image from storage
    saved_file = imaging_api.download_file(
        DownloadFileRequest('ExampleFolderPython/resultImage.png'))
    # process resulting image from storage

    # convert image from request to JPEG and download it
    save_as_to_stream_request = CreateSavedImageAsRequest('test.png', 'jpg')
    converted_image = imaging_api.create_saved_image_as(
        save_as_to_stream_request)

finally:
    # remove files from storage
    imaging_api.delete_file(
        DeleteFileRequest('ExampleFolderPython/resultImage.png'))

# other Imaging requests typically follow the same principles
```

### Imaging.AI - Compare two images
```python
# optional parameters are base URL, API version and debug mode
imaging_api = ImagingApi('yourAppKey', 'yourAppSid')

# create search context or use existing search context ID if search context was
# created earlier
api_response = imaging_api.create_image_search(CreateImageSearchRequest())
search_context_id = api_response.id

# specify images for comparing (image ID is a path to image in storage)
image_in_storage1 = 'WorkFolder\\Image1.jpg'
image_in_storage2 = 'WorkFolder\\Image2.jpg'

# compare images
response = imaging_api.compare_images(CompareImagesRequest(
    search_context_id, image_in_storage1, image_id2=image_in_storage2))
similarity = response.results[0].similarity
```

### Imaging.AI - Find similar images
```python
# optional parameters are base URL, API version and debug mode
imaging_api = ImagingApi('yourAppKey', 'yourAppSid')

# create search context or use existing search context ID if search context was
# created earlier
api_response = imaging_api.create_image_search(CreateImageSearchRequest())
search_context_id = api_response.id

# extract images features if it was not done before
imaging_api.create_image_features(CreateImageFeaturesRequest(
    search_context_id, image_id=None, images_folder='WorkFolder'))

# wait 'till image features extraction is completed
while imaging_api.get_image_search_status(
        GetImageSearchStatusRequest(
            search_context_id)).search_status != 'Idle':
    time.sleep(10)

image_from_storage = True

if image_from_storage:
    # use search image from storage
    storage_image_id = 'searchImage.jpg'
    results = imaging_api.find_similar_images(
        FindSimilarImagesRequest(api_response.id, 90, 5, None,
                                 storage_image_id))
else:
    # load search image
    results = imaging_api.find_similar_images(
        FindSimilarImagesRequest(api_response.id, 90, 5,
                                 'localInputImage.jpg'))

for search_result in results.results:
    print('ImageName: {0}, Similarity: {1}'.format(search_result.image_id,
                                                   search_result.similarity))
```

### Imaging.AI - Find duplicate images
```python
# optional parameters are base URL, API version and debug mode
imaging_api = ImagingApi('yourAppKey', 'yourAppSid')

# create search context or use existing search context ID if search context was
# created earlier
api_response = imaging_api.create_image_search(CreateImageSearchRequest())
search_context_id = api_response.id

# extract images features if it was not done before
imaging_api.create_image_features(CreateImageFeaturesRequest(
    search_context_id, image_id=None, images_folder='WorkFolder'))

# wait 'till image features extraction is completed
while imaging_api.get_image_search_status(
        GetImageSearchStatusRequest(
            search_context_id)).search_status != 'Idle':
    time.sleep(10)

# request finding duplicates
response = imaging_api.find_image_duplicates(
    FindImageDuplicatesRequest(search_context_id, 90))

# process duplicates search result
for duplicates in response.duplicates:
    print('Duplicates:')
    for duplicate in duplicates.duplicate_images:
        print('ImageName: {0}, Similarity: {1}'.format(duplicate.image_id,
                                                       duplicate.similarity))
```

### Imaging.AI - Search images by tags
```python
# optional parameters are base URL, API version and debug mode
imaging_api = ImagingApi('yourAppKey', 'yourAppSid')

# create search context or use existing search context ID if search context was
# created earlier
api_response = imaging_api.create_image_search(CreateImageSearchRequest())
search_context_id = api_response.id

# extract images features if it was not done before
imaging_api.create_image_features(CreateImageFeaturesRequest(
    search_context_id, image_id=None, images_folder='WorkFolder'))

# wait 'till image features extraction is completed
while imaging_api.get_image_search_status(
        GetImageSearchStatusRequest(
            search_context_id)).search_status != 'Idle':
    time.sleep(10)

tag = 'MyTag'
# load tag image
imaging_api.create_image_tag(
    CreateImageTagRequest('testImage.jpg', search_context_id, tag))

# search images by tags 
search_tags = [tag]
response = imaging_api.find_images_by_tags(
    FindImagesByTagsRequest(search_tags, search_context_id, 90, 10))

# process search results
for search_result in response.results:
    print('ImageName: {0}, Similarity: {1}'.format(search_result.image_id,
                                                   search_result.similarity))
```

### Imaging.AI - Delete search context
```python
# search context is stored in the storage, and in case if search context is not
# needed anymore it should be removed
imaging_api.delete_image_search(DeleteImageSearchRequest(search_context_id))
```

### Exception handling and error codes
```python
try:
    imaging_api.delete_image_search(DeleteImageSearchRequest(search_context_id))
except ApiException as ex:
    print(ex.code)
    print(ex.message)
    # inspect ex.error
```