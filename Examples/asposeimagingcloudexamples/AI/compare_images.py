#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="compare_images.py">
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

import os

import asposeimagingcloud.models.requests as requests

from asposeimagingcloudexamples.AI.imaging_ai_base import ImagingAiBase


class CompareImages(ImagingAiBase):
    """Compare images example"""
    def __init__(self, imaging_api):
        ImagingAiBase.__init__(self, imaging_api)
        self._print_header('Compare images example:')

        self.__comparable_image = 'ComparableImage.jpg'
        self.__comparable_image_similar_less_15 = 'ComparingImageSimilar15.jpg'
        self.__comparable_image_similar_more_75 = 'ComparingImageSimilar75.jpg'

    def prepare_search_context(self):
        """Prepares the search context"""
        self._create_search_context()

        # Upload images to Cloud Storage
        for image_name in [self.__comparable_image, self.__comparable_image_similar_more_75]:
            # Upload local image to Cloud Storage
            self._upload_image_to_cloud(image_name)

        self._create_image_features(self.__comparable_image, False)
        self._create_image_features(self.__comparable_image_similar_more_75, False)

        print()

    def compare_two_images_in_cloud(self):
        """Compares the two images in cloud"""
        print('Compares the two images in cloud storage:')

        # Compare two images
        folder = ImagingAiBase.CLOUD_PATH  # Folder with image to process
        storage = None  # We are using default Cloud Storage

        request = requests.CompareImagesRequest(self._search_context_id, self.__comparable_image,
                                                image_id2=self.__comparable_image_similar_more_75, folder=folder,
                                                storage=storage)

        print("Call CompareImages with params: image1: {0}, image2: {1}".format(self.__comparable_image,
                                                                                self.__comparable_image_similar_more_75))

        search_results = self._imaging_api.compare_images(request)

        similarity = search_results.results[0].similarity
        print('Images Similarity: ' + similarity)
        print()

    def compare_loaded_image_to_image_in_cloud(self):
        """Compares the loaded image to image in cloud"""
        print('Compares the loaded image to image in cloud storage:')

        input_stream = os.path.join(ImagingAiBase.EXAMPLE_IMAGES_FOLDER, self.__comparable_image_similar_less_15)
        request = requests.CompareImagesRequest(self._search_context_id, self.__comparable_image, input_stream)

        print('Call CompareImages with params: image: ' + self.__comparable_image)

        search_results = self._imaging_api.compare_images(request)

        similarity = search_results.results[0].similarity
        print('Images Similarity: ' + similarity)
        print()
