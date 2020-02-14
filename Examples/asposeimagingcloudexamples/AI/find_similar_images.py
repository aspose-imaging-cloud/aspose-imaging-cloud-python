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

        # Upload images to Cloud Storage
        for image_name in ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg']:
            # Upload local image to Cloud Storage
            self._upload_image_to_cloud(image_name)

        self._create_image_features(self.__images_path, True)

        print()

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
