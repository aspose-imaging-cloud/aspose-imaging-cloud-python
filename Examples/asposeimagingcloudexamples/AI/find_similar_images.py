#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="find_similar_images.py">
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

import json
import os
import tempfile

import six

if six.PY2:
    import urllib as urllib
else:
    import urllib.parse as urllib

import requests as req
import asposeimagingcloud.models.requests as requests

from asposeimagingcloudexamples.AI.imaging_ai_base import ImagingAiBase


class FindSimilarImages(ImagingAiBase):
    """Find similar images example"""

    def __init__(self, imaging_api):
        ImagingAiBase.__init__(self, imaging_api)
        self._print_header('Find similar images example:')

        self.__image_to_find = '4.jpg'
        self.__image_to_find_by_tag = 'ComparingImageSimilar75.jpg'
        self.__images_path = 'FindSimilar'

    def prepare_search_context(self):
        """Prepares the search context"""
        self._create_search_context()

        # # Upload images to Cloud Storage
        # for image_name in ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg']:
        #     # Upload local image to Cloud Storage
        #     self._upload_image_to_cloud(image_name)
        #
        # self._create_image_features(self.__images_path, True)
        #
        # print()

    def find_similar_images(self):
        """Finds the similar images"""
        print('Finds the similar images:')

        find_image_id = os.path.join(self.__images_path, self.__image_to_find)
        similarity_threshold = 3
        max_count = 3
        folder = ImagingAiBase.CLOUD_PATH  # Folder with image to process
        storage = None  # We are using default Cloud Storage

        request = requests.FindSimilarImagesRequest(self._search_context_id, similarity_threshold, max_count,
                                                    image_id=find_image_id, folder=folder, storage=storage)

        print("Call FindSimilarImages with params: similarity threshold: {0}, max count: {1}, image id: {2}".format(
            similarity_threshold, max_count, find_image_id))

        response = self._imaging_api.find_similar_images(request)

        print('Results count: ' + str(len(response.results)))
        print()

    def find_images_by_tag(self):
        """Finds the images by tag"""
        print('Finds the images by tag:')

        file_name = self.__image_to_find_by_tag
        tag_name = 'ImageTag'
        similarity_threshold = 60
        max_count = 5
        folder = ImagingAiBase.CLOUD_PATH  # Folder with image to process
        storage = None  # We are using default Cloud Storage

        input_stream = os.path.join(ImagingAiBase.EXAMPLE_IMAGES_FOLDER, file_name)
        create_tag_request = requests.CreateImageTagRequest(input_stream, self._search_context_id, tag_name, folder,
                                                            storage)

        print('Call CreateImageTag with params: tag name: ' + tag_name)

        self._imaging_api.create_image_tag(create_tag_request)

        tags = json.dumps([tag_name])
        find_request = requests.FindImagesByTagsRequest(tags, self._search_context_id, similarity_threshold,
                                                        max_count, folder, storage)

        print("Call FindImagesByTags with params: similarity threshold: {0}, max count: {1}, tags: {2}".format(
            similarity_threshold, max_count, tags))

        find_response = self._imaging_api.find_images_by_tags(find_request)

        for find_result in find_response.results:
            print('Image name: ' + find_result.image_id + ', similarity: ' + find_result.similarity)
        print()

    def search_image_from_web_source(self):
        """Finds the similar images from the URL source"""
        print('Finds similar images from URL:')

        similarity_threshold = 30.0
        max_count = 3
        folder = ImagingAiBase.CLOUD_PATH  # Folder with image to process
        storage = None  # We are using default Cloud Storage

        # Add images from the website to the search context
        image_source_url = urllib.quote_plus('https://www.f1news.ru/interview/hamilton/140909.shtml')
        self._imaging_api.create_web_site_image_features(
            requests.CreateWebSiteImageFeaturesRequest(self._search_context_id, image_source_url,
                                                       folder, storage))

        self._wait_idle(self._search_context_id)

        # Download the image from the website
        image_data = req.get('https://cdn.f1ne.ws/userfiles/hamilton/140909.jpg')
        f = tempfile.NamedTemporaryFile()
        f.write(image_data.content)

        # Resize downloaded image
        resized_image = self._imaging_api.create_resized_image(requests.CreateResizedImageRequest(
            f.name, 600, 400, "jpg", storage=storage))
        f.close()

        # Upload image to cloud
        self._imaging_api.upload_file(requests.UploadFileRequest(ImagingAiBase.CLOUD_PATH + "/" +
                                                                 "ReverseSearch.jpg", resized_image, storage))

        # Find similar images in the search context
        find_response = self._imaging_api.find_similar_images(requests.FindSimilarImagesRequest(
            self._search_context_id, similarity_threshold, max_count, image_id=ImagingAiBase.CLOUD_PATH + "/" +
                                                                               "ReverseSearch.jpg", folder=folder,
            storage=storage))

        print('Similar images found: ' + str(len(find_response.results)))
