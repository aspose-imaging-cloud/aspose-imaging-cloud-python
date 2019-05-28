# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="get_search_context_extract_image_features_request.py">
#   Copyright (c) 2019 Aspose Pty Ltd. All rights reserved.
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------


class GetSearchContextExtractImageFeaturesRequest(object):
    """
    Request model for get_search_context_extract_image_features operation.
    Initializes a new instance.
    :param search_context_id The search context identifier.
    :param image_id The image identifier.
    :param image_data Input image
    :param folder The folder.
    :param storage The storage.
    """

    def __init__(self, search_context_id, image_id, image_data=None, folder=None, storage=None):
        self.search_context_id = search_context_id
        self.image_id = image_id
        self.image_data = image_data
        self.folder = folder
        self.storage = storage
