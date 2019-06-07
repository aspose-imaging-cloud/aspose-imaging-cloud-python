# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="post_image_web_p_request.py">
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

from asposeimagingcloud.models.requests.imaging_request import ImagingRequest
from asposeimagingcloud.models.requests.http_request import HttpRequest


class PostImageWebPRequest(ImagingRequest):
    """
    Request model for post_image_web_p operation.
    Initializes a new instance.

    :param image_data Input image
    :param loss_less If WEBP should be in lossless format.
    :param quality Quality (0-100).
    :param anim_loop_count The animation loop count.
    :param anim_background_color Color of the animation background.
    :param from_scratch Specifies where additional parameters we do not support should be taken from. If this is true – they will be taken from default values for standard image, if it is false – they will be saved from current image. Default is false.
    :param out_path Path to updated file (if this is empty, response contains streamed image).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, image_data, loss_less, quality, anim_loop_count, anim_background_color, from_scratch=None, out_path=None, storage=None):
        ImagingRequest.__init__(self)
        self.image_data = image_data
        self.loss_less = loss_less
        self.quality = quality
        self.anim_loop_count = anim_loop_count
        self.anim_background_color = anim_background_color
        self.from_scratch = from_scratch
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: Imaging API configuration
        :type: asposeimagingcloud.Configuration
        :return: http_request configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'image_data' is set
        if self.image_data is None:
            raise ValueError("Missing the required parameter `image_data` when calling `post_image_web_p`")  # noqa: E501
        # verify the required parameter 'loss_less' is set
        if self.loss_less is None:
            raise ValueError("Missing the required parameter `loss_less` when calling `post_image_web_p`")  # noqa: E501
        # verify the required parameter 'quality' is set
        if self.quality is None:
            raise ValueError("Missing the required parameter `quality` when calling `post_image_web_p`")  # noqa: E501
        # verify the required parameter 'anim_loop_count' is set
        if self.anim_loop_count is None:
            raise ValueError("Missing the required parameter `anim_loop_count` when calling `post_image_web_p`")  # noqa: E501
        # verify the required parameter 'anim_background_color' is set
        if self.anim_background_color is None:
            raise ValueError("Missing the required parameter `anim_background_color` when calling `post_image_web_p`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/webp'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('lossLess') in path:
            path = path.replace('{' + self._lowercase_first_letter('lossLess' + '}'), self.loss_less if self.loss_less is not None else '')
        else:
            if self.loss_less is not None:
                query_params.append((self._lowercase_first_letter('lossLess'), self.loss_less))  # noqa: E501
        if self._lowercase_first_letter('quality') in path:
            path = path.replace('{' + self._lowercase_first_letter('quality' + '}'), self.quality if self.quality is not None else '')
        else:
            if self.quality is not None:
                query_params.append((self._lowercase_first_letter('quality'), self.quality))  # noqa: E501
        if self._lowercase_first_letter('animLoopCount') in path:
            path = path.replace('{' + self._lowercase_first_letter('animLoopCount' + '}'), self.anim_loop_count if self.anim_loop_count is not None else '')
        else:
            if self.anim_loop_count is not None:
                query_params.append((self._lowercase_first_letter('animLoopCount'), self.anim_loop_count))  # noqa: E501
        if self._lowercase_first_letter('animBackgroundColor') in path:
            path = path.replace('{' + self._lowercase_first_letter('animBackgroundColor' + '}'), self.anim_background_color if self.anim_background_color is not None else '')
        else:
            if self.anim_background_color is not None:
                query_params.append((self._lowercase_first_letter('animBackgroundColor'), self.anim_background_color))  # noqa: E501
        if self._lowercase_first_letter('fromScratch') in path:
            path = path.replace('{' + self._lowercase_first_letter('fromScratch' + '}'), self.from_scratch if self.from_scratch is not None else '')
        else:
            if self.from_scratch is not None:
                query_params.append((self._lowercase_first_letter('fromScratch'), self.from_scratch))  # noqa: E501
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))  # noqa: E501
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if self.image_data is not None:
            local_var_files.append((self._lowercase_first_letter('imageData'), self.image_data))  # noqa: E501

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self._select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
