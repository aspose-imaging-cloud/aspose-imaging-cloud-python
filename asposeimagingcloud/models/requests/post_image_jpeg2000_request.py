# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="post_image_jpeg2000_request.py">
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


class PostImageJpeg2000Request(object):
    """
    Request model for post_image_jpeg2000 operation.
    Initializes a new instance.
    :param image_data Input image
    :param comment The comment (can be either single or comma-separated).
    :param codec The codec (j2k or jp2).
    :param from_scratch Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false.
    :param out_path Path to updated file (if this is empty, response contains streamed image).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, image_data, comment, codec=None, from_scratch=None, out_path=None, storage=None):
        self.image_data = image_data
        self.comment = comment
        self.codec = codec
        self.from_scratch = from_scratch
        self.out_path = out_path
        self.storage = storage
