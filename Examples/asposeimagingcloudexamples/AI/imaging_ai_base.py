#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="imaging_ai_base.py">
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
import time

import asposeimagingcloud.models.requests as requests


class ImagingAiBase:
    """Base class for AI examples"""
    # The example images folder path
    EXAMPLE_IMAGES_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(
        __file__)))), os.path.join('Images', 'AI'))

    # The output folder path
    OUTPUT_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))),
                                 os.path.join('Output', 'AI'))

    # The cloud path
    CLOUD_PATH = os.path.join('Examples', 'AI')

    def __init__(self, imaging_api):
        self._imaging_api = imaging_api
        self._search_context_id = None

    def delete_search_context(self):
        """Deletes the image search context"""
        folder = None  # File will be saved at the root of the storage
        storage = None  # We are using default Cloud Storage

        request = requests.DeleteImageSearchRequest(self._search_context_id, folder, storage)
        self._imaging_api.delete_image_search(request)

        print("Deleted new Search context with SearchContextId: {0}".format(self._search_context_id))
        print()

    def _create_search_context(self):
        """Creates the image search"""
        detector = 'akaze'
        matching_algorithm = 'randomBinaryTree'
        folder = None  # File will be saved at the root of the storage
        storage = None  # We are using default Cloud Storage

        request = requests.CreateImageSearchRequest(detector, matching_algorithm, folder, storage)
        status = self._imaging_api.create_image_search(request)

        self._search_context_id = status.id

        print("Created new Search context with SearchContextId: {0}".format(self._search_context_id))
        print()

    def _create_image_features(self, source_path, is_folder):
        """Extract images features and add them to search context"""
        folder = None  # File will be saved at the root of the storage
        storage = None  # We are using default Cloud Storage

        request = requests.CreateImageFeaturesRequest(self._search_context_id, images_folder=os.path.join(
            ImagingAiBase.CLOUD_PATH, source_path), folder=folder, storage=storage) if is_folder else \
            requests.CreateImageFeaturesRequest(self._search_context_id, image_id=os.path.join(
                ImagingAiBase.CLOUD_PATH, source_path), folder=folder, storage=storage)
        self._imaging_api.create_image_features(request)

        if is_folder:
            print('Creating Search context image features...')
            self._wait_idle(self._search_context_id)
        else:
            print("Created Search context image features for {0}".format(source_path))

    def _upload_image_to_cloud(self, image_name, sub_folder=None):
        """Uploads the image to cloud"""
        folder = os.path.join(ImagingAiBase.EXAMPLE_IMAGES_FOLDER, sub_folder) if sub_folder else \
            ImagingAiBase.EXAMPLE_IMAGES_FOLDER

        local_input_image = os.path.join(folder, image_name)
        request = requests.UploadFileRequest(os.path.join(ImagingAiBase.CLOUD_PATH, image_name), local_input_image)
        self._imaging_api.upload_file(request)

        print("Image {0} was uploaded to cloud storage".format(image_name))

    @staticmethod
    def _print_header(header):
        print(header)
        print()

    def _wait_idle(self, search_context_id):
        """Waits the idle"""
        print('Waiting Search context Idle...')

        folder = None  # File will be saved at the root of the storage
        storage = None  # We are using default Cloud Storage

        while self._imaging_api.get_image_search_status(requests.GetImageSearchStatusRequest(search_context_id,
                                                                                             folder,
                                                                                             storage)).search_status != 'Idle':
            time.sleep(1)
