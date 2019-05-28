# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="post_search_context_compare_images_request.py">
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


class PostSearchContextCompareImagesRequest(object):
    """
    Request model for post_search_context_compare_images operation.
    Initializes a new instance.
    :param search_context_id The search context identifier.
    :param image_id1 The first image Id in storage.
    :param image_data Input image
    :param image_id2 The second image Idin storage or null(if image loading in request).
    :param folder The folder.
    :param storage The storage.
    """

    def __init__(self, search_context_id, image_id1, image_data=None, image_id2=None, folder=None, storage=None):
        self.search_context_id = search_context_id
        self.image_id1 = image_id1
        self.image_data = image_data
        self.image_id2 = image_id2
        self.folder = folder
        self.storage = storage
