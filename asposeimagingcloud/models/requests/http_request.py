#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="http_request.py">
#    Copyright (c) 2018-2019 Aspose Pty Ltd. All rights reserved.
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

class HttpRequest(object):

    def __init__(self, resource_path, path_params, query_params, header_params,
                 form_params, body_params, files, collection_formats,
                 auth_settings, return_http_data_only=None,
                 preload_content=None, request_timeout=None):
        """Makes the HTTP request (synchronous) and returns deserialized data.

        To make an async request, set the async parameter.

        :param resource_path: Path to method endpoint.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be placed in the request
            header.
        :param form_params: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param body_params: Request body.
        :param files: dict key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param auth_settings: Auth Settings names for the request.
        :param return_http_data_only: response data without head status code
                                       and headers

        :param preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Request thread.
        """
        self.resource_path = resource_path
        self.path_params = path_params
        self.query_params = query_params
        self.header_params = header_params
        self.form_params = form_params
        self.body_params = body_params
        self.files = files
        self.collection_formats = collection_formats
        self.auth_settings = auth_settings
        self.return_http_data_only = return_http_data_only or True
        self.preload_content = preload_content or True
        self.request_timeout = request_timeout or ''
