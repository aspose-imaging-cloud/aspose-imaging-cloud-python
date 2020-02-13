#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="search_images.py">
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
import six

if six.PY2:
    import urllib as urllib
else:
    import urllib.parse as urllib

import asposeimagingcloud.models.requests as requests

from asposeimagingcloudexamples.AI.imaging_ai_base import ImagingAiBase


class SearchImages(ImagingAiBase):
    """Search images"""

    def __init__(self, imaging_api):
        ImagingAiBase.__init__(self, imaging_api)
        self._print_header('Search images example:')

    def prepare_search_context(self):
        """Prepares search context"""
        self._create_search_context()

    def search_image_from_web_source(self):
        """Searches for images from a web source"""
        print('Searches for images from a web source')

        folder = ImagingAiBase.CLOUD_PATH  # Folder with image to process
        storage = None  # We are using default Cloud Storage

        image_source_url = urllib.quote_plus('https://www.f1news.ru/interview/hamilton/140909.shtml')
        self._imaging_api.create_web_site_image_features(
            requests.CreateWebSiteImageFeaturesRequest(self._search_context_id, image_source_url,
                                                       folder, storage))

        self._wait_idle(self._search_context_id)

        image_url = urllib.quote_plus('https://cdn.f1ne.ws/userfiles/hamilton/140909.jpg')
        response = self._imaging_api.get_image_features(
            requests.GetImageFeaturesRequest(self._search_context_id, image_url, folder, storage))

        print('Image features found: ' + str(response.features_count))
