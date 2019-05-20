# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="get_search_context_find_similar_request.py">
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


class GetSearchContextFindSimilarRequest(object):
    """
    Request model for get_search_context_find_similar operation.
    Initializes a new instance.
    :param search_context_id The search context identifier.
    :param similarity_threshold The similarity threshold.
    :param max_count The maximum count.
    :param image_data Input image
    :param image_id The search image identifier.
    :param folder The folder.
    :param storage The storage.
    """

    def __init__(self, search_context_id, similarity_threshold, max_count, image_data=None, image_id=None, folder=None, storage=None):
        self.search_context_id = search_context_id
        self.similarity_threshold = similarity_threshold
        self.max_count = max_count
        self.image_data = image_data
        self.image_id = image_id
        self.folder = folder
        self.storage = storage
