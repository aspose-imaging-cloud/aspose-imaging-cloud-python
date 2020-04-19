#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="find_duplicate_images.py">
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

import asposeimagingcloud.models.requests as requests

from asposeimagingcloudexamples.AI.imaging_ai_base import ImagingAiBase


class FindDuplicateImages(ImagingAiBase):
    """Find duplicate images example"""

    def __init__(self, imaging_api):
        ImagingAiBase.__init__(self, imaging_api)
        self._print_header('Find duplicate images example:')

        self.__comparable_image = 'ComparableImage.jpg'
        self.__comparable_image_similar_less_15 = 'ComparingImageSimilar15.jpg'
        self.__comparable_image_similar_more_75 = 'ComparingImageSimilar75.jpg'

    def prepare_search_context(self):
        """Prepares the search context"""
        self._create_search_context()

        # Upload images to Cloud Storage
        for image_name in [self.__comparable_image, self.__comparable_image_similar_less_15,
                           self.__comparable_image_similar_more_75]:
            self._upload_image_to_cloud(image_name)

        self._create_image_features(self.__comparable_image, False)
        self._create_image_features(self.__comparable_image_similar_less_15, False)
        self._create_image_features(self.__comparable_image_similar_more_75, False)

        print()

    def find_image_duplicates(self):
        """Finds the image duplicates"""
        print('Finds the image duplicates:')

        similarity_threshold = 60
        folder = None
        storage = None  # We are using default Cloud Storage

        request = requests.FindImageDuplicatesRequest(self._search_context_id, similarity_threshold, folder, storage)

        print('Call FindImageDuplicates with params: similarity threshold: ' + str(similarity_threshold))

        response = self._imaging_api.find_image_duplicates(request)
        print('Duplicates count: ' + str(len(response.duplicates)))
        print()
