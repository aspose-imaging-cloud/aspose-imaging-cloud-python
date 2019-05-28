# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="ImagingApi.py">
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
from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six
from asposeimagingcloud.rest import ApiException
from asposeimagingcloud.api_client import ApiClient


class ImagingApi(object):
    """
    Aspose.Words for Cloud API

    :param api_client: an api client to perfom http requests
    """
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def copy_file(self, request, **kwargs):  # noqa: E501
        """Copy file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request copy_file_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.copy_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.copy_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.copy_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.copy_file_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def copy_file_with_http_info(self, request, **kwargs):  # noqa: E501
        """Copy file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request copy_file_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method copy_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'src_path' is set
        if request.src_path is None:
            raise ValueError("Missing the required parameter `src_path` when calling `copy_file`")  # noqa: E501
        # verify the required parameter 'dest_path' is set
        if request.dest_path is None:
            raise ValueError("Missing the required parameter `dest_path` when calling `copy_file`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/storage/file/copy/{srcPath}'
        path_params = {}
        if request.src_path is not None:
            path_params[self.__downcase_first_letter('srcPath')] = request.src_path  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('destPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('destPath' + '}'), request.dest_path if request.dest_path is not None else '')
        else:
            if request.dest_path is not None:
                query_params.append((self.__downcase_first_letter('destPath'), request.dest_path))  # noqa: E501
        if self.__downcase_first_letter('srcStorageName') in path:
            path = path.replace('{' + self.__downcase_first_letter('srcStorageName' + '}'), request.src_storage_name if request.src_storage_name is not None else '')
        else:
            if request.src_storage_name is not None:
                query_params.append((self.__downcase_first_letter('srcStorageName'), request.src_storage_name))  # noqa: E501
        if self.__downcase_first_letter('destStorageName') in path:
            path = path.replace('{' + self.__downcase_first_letter('destStorageName' + '}'), request.dest_storage_name if request.dest_storage_name is not None else '')
        else:
            if request.dest_storage_name is not None:
                query_params.append((self.__downcase_first_letter('destStorageName'), request.dest_storage_name))  # noqa: E501
        if self.__downcase_first_letter('versionId') in path:
            path = path.replace('{' + self.__downcase_first_letter('versionId' + '}'), request.version_id if request.version_id is not None else '')
        else:
            if request.version_id is not None:
                query_params.append((self.__downcase_first_letter('versionId'), request.version_id))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def copy_folder(self, request, **kwargs):  # noqa: E501
        """Copy folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request copy_folder_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.copy_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.copy_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.copy_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.copy_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def copy_folder_with_http_info(self, request, **kwargs):  # noqa: E501
        """Copy folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request copy_folder_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method copy_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'src_path' is set
        if request.src_path is None:
            raise ValueError("Missing the required parameter `src_path` when calling `copy_folder`")  # noqa: E501
        # verify the required parameter 'dest_path' is set
        if request.dest_path is None:
            raise ValueError("Missing the required parameter `dest_path` when calling `copy_folder`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/storage/folder/copy/{srcPath}'
        path_params = {}
        if request.src_path is not None:
            path_params[self.__downcase_first_letter('srcPath')] = request.src_path  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('destPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('destPath' + '}'), request.dest_path if request.dest_path is not None else '')
        else:
            if request.dest_path is not None:
                query_params.append((self.__downcase_first_letter('destPath'), request.dest_path))  # noqa: E501
        if self.__downcase_first_letter('srcStorageName') in path:
            path = path.replace('{' + self.__downcase_first_letter('srcStorageName' + '}'), request.src_storage_name if request.src_storage_name is not None else '')
        else:
            if request.src_storage_name is not None:
                query_params.append((self.__downcase_first_letter('srcStorageName'), request.src_storage_name))  # noqa: E501
        if self.__downcase_first_letter('destStorageName') in path:
            path = path.replace('{' + self.__downcase_first_letter('destStorageName' + '}'), request.dest_storage_name if request.dest_storage_name is not None else '')
        else:
            if request.dest_storage_name is not None:
                query_params.append((self.__downcase_first_letter('destStorageName'), request.dest_storage_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_folder(self, request, **kwargs):  # noqa: E501
        """Create the folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request create_folder_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.create_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.create_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.create_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.create_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def create_folder_with_http_info(self, request, **kwargs):  # noqa: E501
        """Create the folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request create_folder_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if request.path is None:
            raise ValueError("Missing the required parameter `path` when calling `create_folder`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/storage/folder/{path}'
        path_params = {}
        if request.path is not None:
            path_params[self.__downcase_first_letter('path')] = request.path  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('storageName') in path:
            path = path.replace('{' + self.__downcase_first_letter('storageName' + '}'), request.storage_name if request.storage_name is not None else '')
        else:
            if request.storage_name is not None:
                query_params.append((self.__downcase_first_letter('storageName'), request.storage_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_file(self, request, **kwargs):  # noqa: E501
        """Delete file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request delete_file_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_file_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def delete_file_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request delete_file_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if request.path is None:
            raise ValueError("Missing the required parameter `path` when calling `delete_file`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/storage/file/{path}'
        path_params = {}
        if request.path is not None:
            path_params[self.__downcase_first_letter('path')] = request.path  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('storageName') in path:
            path = path.replace('{' + self.__downcase_first_letter('storageName' + '}'), request.storage_name if request.storage_name is not None else '')
        else:
            if request.storage_name is not None:
                query_params.append((self.__downcase_first_letter('storageName'), request.storage_name))  # noqa: E501
        if self.__downcase_first_letter('versionId') in path:
            path = path.replace('{' + self.__downcase_first_letter('versionId' + '}'), request.version_id if request.version_id is not None else '')
        else:
            if request.version_id is not None:
                query_params.append((self.__downcase_first_letter('versionId'), request.version_id))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_folder(self, request, **kwargs):  # noqa: E501
        """Delete folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request delete_folder_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def delete_folder_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request delete_folder_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if request.path is None:
            raise ValueError("Missing the required parameter `path` when calling `delete_folder`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/storage/folder/{path}'
        path_params = {}
        if request.path is not None:
            path_params[self.__downcase_first_letter('path')] = request.path  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('storageName') in path:
            path = path.replace('{' + self.__downcase_first_letter('storageName' + '}'), request.storage_name if request.storage_name is not None else '')
        else:
            if request.storage_name is not None:
                query_params.append((self.__downcase_first_letter('storageName'), request.storage_name))  # noqa: E501
        if self.__downcase_first_letter('recursive') in path:
            path = path.replace('{' + self.__downcase_first_letter('recursive' + '}'), request.recursive if request.recursive is not None else '')
        else:
            if request.recursive is not None:
                query_params.append((self.__downcase_first_letter('recursive'), request.recursive))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_search_context(self, request, **kwargs):  # noqa: E501
        """Deletes the search context.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request delete_search_context_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_search_context_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_search_context_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_search_context_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_search_context_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def delete_search_context_with_http_info(self, request, **kwargs):  # noqa: E501
        """Deletes the search context.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request delete_search_context_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_search_context" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_context_id' is set
        if request.search_context_id is None:
            raise ValueError("Missing the required parameter `search_context_id` when calling `delete_search_context`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/ai/imageSearch/{searchContextId}'
        path_params = {}
        if request.search_context_id is not None:
            path_params[self.__downcase_first_letter('searchContextId')] = request.search_context_id  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_search_context_image(self, request, **kwargs):  # noqa: E501
        """Delete image and images features from search context  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request delete_search_context_image_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_search_context_image_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_search_context_image_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_search_context_image_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_search_context_image_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def delete_search_context_image_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete image and images features from search context  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request delete_search_context_image_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_search_context_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_context_id' is set
        if request.search_context_id is None:
            raise ValueError("Missing the required parameter `search_context_id` when calling `delete_search_context_image`")  # noqa: E501
        # verify the required parameter 'image_id' is set
        if request.image_id is None:
            raise ValueError("Missing the required parameter `image_id` when calling `delete_search_context_image`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/ai/imageSearch/{searchContextId}/image'
        path_params = {}
        if request.search_context_id is not None:
            path_params[self.__downcase_first_letter('searchContextId')] = request.search_context_id  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('imageId') in path:
            path = path.replace('{' + self.__downcase_first_letter('imageId' + '}'), request.image_id if request.image_id is not None else '')
        else:
            if request.image_id is not None:
                query_params.append((self.__downcase_first_letter('imageId'), request.image_id))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_search_context_image_features(self, request, **kwargs):  # noqa: E501
        """Deletes image features from search context.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request delete_search_context_image_features_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_search_context_image_features_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_search_context_image_features_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_search_context_image_features_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_search_context_image_features_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def delete_search_context_image_features_with_http_info(self, request, **kwargs):  # noqa: E501
        """Deletes image features from search context.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request delete_search_context_image_features_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_search_context_image_features" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_context_id' is set
        if request.search_context_id is None:
            raise ValueError("Missing the required parameter `search_context_id` when calling `delete_search_context_image_features`")  # noqa: E501
        # verify the required parameter 'image_id' is set
        if request.image_id is None:
            raise ValueError("Missing the required parameter `image_id` when calling `delete_search_context_image_features`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/ai/imageSearch/{searchContextId}/features'
        path_params = {}
        if request.search_context_id is not None:
            path_params[self.__downcase_first_letter('searchContextId')] = request.search_context_id  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('imageId') in path:
            path = path.replace('{' + self.__downcase_first_letter('imageId' + '}'), request.image_id if request.image_id is not None else '')
        else:
            if request.image_id is not None:
                query_params.append((self.__downcase_first_letter('imageId'), request.image_id))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def download_file(self, request, **kwargs):  # noqa: E501
        """Download file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request download_file_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.download_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.download_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.download_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.download_file_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def download_file_with_http_info(self, request, **kwargs):  # noqa: E501
        """Download file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request download_file_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if request.path is None:
            raise ValueError("Missing the required parameter `path` when calling `download_file`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/storage/file/{path}'
        path_params = {}
        if request.path is not None:
            path_params[self.__downcase_first_letter('path')] = request.path  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('storageName') in path:
            path = path.replace('{' + self.__downcase_first_letter('storageName' + '}'), request.storage_name if request.storage_name is not None else '')
        else:
            if request.storage_name is not None:
                query_params.append((self.__downcase_first_letter('storageName'), request.storage_name))  # noqa: E501
        if self.__downcase_first_letter('versionId') in path:
            path = path.replace('{' + self.__downcase_first_letter('versionId' + '}'), request.version_id if request.version_id is not None else '')
        else:
            if request.version_id is not None:
                query_params.append((self.__downcase_first_letter('versionId'), request.version_id))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_disc_usage(self, request, **kwargs):  # noqa: E501
        """Get disc usage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_disc_usage_request object with parameters
        :return: DiscUsage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_disc_usage_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_disc_usage_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_disc_usage_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_disc_usage_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_disc_usage_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get disc usage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_disc_usage_request object with parameters
        :return: DiscUsage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_disc_usage" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}
        path = '/imaging/storage/disc'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('storageName') in path:
            path = path.replace('{' + self.__downcase_first_letter('storageName' + '}'), request.storage_name if request.storage_name is not None else '')
        else:
            if request.storage_name is not None:
                query_params.append((self.__downcase_first_letter('storageName'), request.storage_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DiscUsage',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_file_versions(self, request, **kwargs):  # noqa: E501
        """Get file versions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_file_versions_request object with parameters
        :return: FileVersions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_file_versions_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_file_versions_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_file_versions_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_file_versions_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_file_versions_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get file versions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_file_versions_request object with parameters
        :return: FileVersions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_file_versions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if request.path is None:
            raise ValueError("Missing the required parameter `path` when calling `get_file_versions`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/storage/version/{path}'
        path_params = {}
        if request.path is not None:
            path_params[self.__downcase_first_letter('path')] = request.path  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('storageName') in path:
            path = path.replace('{' + self.__downcase_first_letter('storageName' + '}'), request.storage_name if request.storage_name is not None else '')
        else:
            if request.storage_name is not None:
                query_params.append((self.__downcase_first_letter('storageName'), request.storage_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FileVersions',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_files_list(self, request, **kwargs):  # noqa: E501
        """Get all files and folders within a folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_files_list_request object with parameters
        :return: FilesList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_files_list_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_files_list_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_files_list_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_files_list_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_files_list_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get all files and folders within a folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_files_list_request object with parameters
        :return: FilesList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_files_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if request.path is None:
            raise ValueError("Missing the required parameter `path` when calling `get_files_list`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/storage/folder/{path}'
        path_params = {}
        if request.path is not None:
            path_params[self.__downcase_first_letter('path')] = request.path  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('storageName') in path:
            path = path.replace('{' + self.__downcase_first_letter('storageName' + '}'), request.storage_name if request.storage_name is not None else '')
        else:
            if request.storage_name is not None:
                query_params.append((self.__downcase_first_letter('storageName'), request.storage_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilesList',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_image_bmp(self, request, **kwargs):  # noqa: E501
        """Update parameters of existing BMP image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_bmp_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_image_bmp_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_bmp_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_image_bmp_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_bmp_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_image_bmp_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update parameters of existing BMP image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_bmp_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_image_bmp" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_image_bmp`")  # noqa: E501
        # verify the required parameter 'bits_per_pixel' is set
        if request.bits_per_pixel is None:
            raise ValueError("Missing the required parameter `bits_per_pixel` when calling `get_image_bmp`")  # noqa: E501
        # verify the required parameter 'horizontal_resolution' is set
        if request.horizontal_resolution is None:
            raise ValueError("Missing the required parameter `horizontal_resolution` when calling `get_image_bmp`")  # noqa: E501
        # verify the required parameter 'vertical_resolution' is set
        if request.vertical_resolution is None:
            raise ValueError("Missing the required parameter `vertical_resolution` when calling `get_image_bmp`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/{name}/bmp'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('bitsPerPixel') in path:
            path = path.replace('{' + self.__downcase_first_letter('bitsPerPixel' + '}'), request.bits_per_pixel if request.bits_per_pixel is not None else '')
        else:
            if request.bits_per_pixel is not None:
                query_params.append((self.__downcase_first_letter('bitsPerPixel'), request.bits_per_pixel))  # noqa: E501
        if self.__downcase_first_letter('horizontalResolution') in path:
            path = path.replace('{' + self.__downcase_first_letter('horizontalResolution' + '}'), request.horizontal_resolution if request.horizontal_resolution is not None else '')
        else:
            if request.horizontal_resolution is not None:
                query_params.append((self.__downcase_first_letter('horizontalResolution'), request.horizontal_resolution))  # noqa: E501
        if self.__downcase_first_letter('verticalResolution') in path:
            path = path.replace('{' + self.__downcase_first_letter('verticalResolution' + '}'), request.vertical_resolution if request.vertical_resolution is not None else '')
        else:
            if request.vertical_resolution is not None:
                query_params.append((self.__downcase_first_letter('verticalResolution'), request.vertical_resolution))  # noqa: E501
        if self.__downcase_first_letter('fromScratch') in path:
            path = path.replace('{' + self.__downcase_first_letter('fromScratch' + '}'), request.from_scratch if request.from_scratch is not None else '')
        else:
            if request.from_scratch is not None:
                query_params.append((self.__downcase_first_letter('fromScratch'), request.from_scratch))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_image_crop(self, request, **kwargs):  # noqa: E501
        """Crop an existing image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_crop_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_image_crop_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_crop_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_image_crop_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_crop_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_image_crop_with_http_info(self, request, **kwargs):  # noqa: E501
        """Crop an existing image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_crop_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_image_crop" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_image_crop`")  # noqa: E501
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `get_image_crop`")  # noqa: E501
        # verify the required parameter 'x' is set
        if request.x is None:
            raise ValueError("Missing the required parameter `x` when calling `get_image_crop`")  # noqa: E501
        # verify the required parameter 'y' is set
        if request.y is None:
            raise ValueError("Missing the required parameter `y` when calling `get_image_crop`")  # noqa: E501
        # verify the required parameter 'width' is set
        if request.width is None:
            raise ValueError("Missing the required parameter `width` when calling `get_image_crop`")  # noqa: E501
        # verify the required parameter 'height' is set
        if request.height is None:
            raise ValueError("Missing the required parameter `height` when calling `get_image_crop`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/{name}/crop'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('format') in path:
            path = path.replace('{' + self.__downcase_first_letter('format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('x') in path:
            path = path.replace('{' + self.__downcase_first_letter('x' + '}'), request.x if request.x is not None else '')
        else:
            if request.x is not None:
                query_params.append((self.__downcase_first_letter('x'), request.x))  # noqa: E501
        if self.__downcase_first_letter('y') in path:
            path = path.replace('{' + self.__downcase_first_letter('y' + '}'), request.y if request.y is not None else '')
        else:
            if request.y is not None:
                query_params.append((self.__downcase_first_letter('y'), request.y))  # noqa: E501
        if self.__downcase_first_letter('width') in path:
            path = path.replace('{' + self.__downcase_first_letter('width' + '}'), request.width if request.width is not None else '')
        else:
            if request.width is not None:
                query_params.append((self.__downcase_first_letter('width'), request.width))  # noqa: E501
        if self.__downcase_first_letter('height') in path:
            path = path.replace('{' + self.__downcase_first_letter('height' + '}'), request.height if request.height is not None else '')
        else:
            if request.height is not None:
                query_params.append((self.__downcase_first_letter('height'), request.height))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_image_emf(self, request, **kwargs):  # noqa: E501
        """Process existing EMF imaging using given parameters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_emf_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_image_emf_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_emf_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_image_emf_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_emf_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_image_emf_with_http_info(self, request, **kwargs):  # noqa: E501
        """Process existing EMF imaging using given parameters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_emf_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_image_emf" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_image_emf`")  # noqa: E501
        # verify the required parameter 'bk_color' is set
        if request.bk_color is None:
            raise ValueError("Missing the required parameter `bk_color` when calling `get_image_emf`")  # noqa: E501
        # verify the required parameter 'page_width' is set
        if request.page_width is None:
            raise ValueError("Missing the required parameter `page_width` when calling `get_image_emf`")  # noqa: E501
        # verify the required parameter 'page_height' is set
        if request.page_height is None:
            raise ValueError("Missing the required parameter `page_height` when calling `get_image_emf`")  # noqa: E501
        # verify the required parameter 'border_x' is set
        if request.border_x is None:
            raise ValueError("Missing the required parameter `border_x` when calling `get_image_emf`")  # noqa: E501
        # verify the required parameter 'border_y' is set
        if request.border_y is None:
            raise ValueError("Missing the required parameter `border_y` when calling `get_image_emf`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/{name}/emf'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('bkColor') in path:
            path = path.replace('{' + self.__downcase_first_letter('bkColor' + '}'), request.bk_color if request.bk_color is not None else '')
        else:
            if request.bk_color is not None:
                query_params.append((self.__downcase_first_letter('bkColor'), request.bk_color))  # noqa: E501
        if self.__downcase_first_letter('pageWidth') in path:
            path = path.replace('{' + self.__downcase_first_letter('pageWidth' + '}'), request.page_width if request.page_width is not None else '')
        else:
            if request.page_width is not None:
                query_params.append((self.__downcase_first_letter('pageWidth'), request.page_width))  # noqa: E501
        if self.__downcase_first_letter('pageHeight') in path:
            path = path.replace('{' + self.__downcase_first_letter('pageHeight' + '}'), request.page_height if request.page_height is not None else '')
        else:
            if request.page_height is not None:
                query_params.append((self.__downcase_first_letter('pageHeight'), request.page_height))  # noqa: E501
        if self.__downcase_first_letter('borderX') in path:
            path = path.replace('{' + self.__downcase_first_letter('borderX' + '}'), request.border_x if request.border_x is not None else '')
        else:
            if request.border_x is not None:
                query_params.append((self.__downcase_first_letter('borderX'), request.border_x))  # noqa: E501
        if self.__downcase_first_letter('borderY') in path:
            path = path.replace('{' + self.__downcase_first_letter('borderY' + '}'), request.border_y if request.border_y is not None else '')
        else:
            if request.border_y is not None:
                query_params.append((self.__downcase_first_letter('borderY'), request.border_y))  # noqa: E501
        if self.__downcase_first_letter('fromScratch') in path:
            path = path.replace('{' + self.__downcase_first_letter('fromScratch' + '}'), request.from_scratch if request.from_scratch is not None else '')
        else:
            if request.from_scratch is not None:
                query_params.append((self.__downcase_first_letter('fromScratch'), request.from_scratch))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('format') in path:
            path = path.replace('{' + self.__downcase_first_letter('format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('format'), request.format))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_image_frame(self, request, **kwargs):  # noqa: E501
        """Get separate frame from existing TIFF image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_frame_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_image_frame_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_frame_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_image_frame_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_frame_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_image_frame_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get separate frame from existing TIFF image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_frame_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_image_frame" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_image_frame`")  # noqa: E501
        # verify the required parameter 'frame_id' is set
        if request.frame_id is None:
            raise ValueError("Missing the required parameter `frame_id` when calling `get_image_frame`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/{name}/frames/{frameId}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.frame_id is not None:
            path_params[self.__downcase_first_letter('frameId')] = request.frame_id  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('newWidth') in path:
            path = path.replace('{' + self.__downcase_first_letter('newWidth' + '}'), request.new_width if request.new_width is not None else '')
        else:
            if request.new_width is not None:
                query_params.append((self.__downcase_first_letter('newWidth'), request.new_width))  # noqa: E501
        if self.__downcase_first_letter('newHeight') in path:
            path = path.replace('{' + self.__downcase_first_letter('newHeight' + '}'), request.new_height if request.new_height is not None else '')
        else:
            if request.new_height is not None:
                query_params.append((self.__downcase_first_letter('newHeight'), request.new_height))  # noqa: E501
        if self.__downcase_first_letter('x') in path:
            path = path.replace('{' + self.__downcase_first_letter('x' + '}'), request.x if request.x is not None else '')
        else:
            if request.x is not None:
                query_params.append((self.__downcase_first_letter('x'), request.x))  # noqa: E501
        if self.__downcase_first_letter('y') in path:
            path = path.replace('{' + self.__downcase_first_letter('y' + '}'), request.y if request.y is not None else '')
        else:
            if request.y is not None:
                query_params.append((self.__downcase_first_letter('y'), request.y))  # noqa: E501
        if self.__downcase_first_letter('rectWidth') in path:
            path = path.replace('{' + self.__downcase_first_letter('rectWidth' + '}'), request.rect_width if request.rect_width is not None else '')
        else:
            if request.rect_width is not None:
                query_params.append((self.__downcase_first_letter('rectWidth'), request.rect_width))  # noqa: E501
        if self.__downcase_first_letter('rectHeight') in path:
            path = path.replace('{' + self.__downcase_first_letter('rectHeight' + '}'), request.rect_height if request.rect_height is not None else '')
        else:
            if request.rect_height is not None:
                query_params.append((self.__downcase_first_letter('rectHeight'), request.rect_height))  # noqa: E501
        if self.__downcase_first_letter('rotateFlipMethod') in path:
            path = path.replace('{' + self.__downcase_first_letter('rotateFlipMethod' + '}'), request.rotate_flip_method if request.rotate_flip_method is not None else '')
        else:
            if request.rotate_flip_method is not None:
                query_params.append((self.__downcase_first_letter('rotateFlipMethod'), request.rotate_flip_method))  # noqa: E501
        if self.__downcase_first_letter('saveOtherFrames') in path:
            path = path.replace('{' + self.__downcase_first_letter('saveOtherFrames' + '}'), request.save_other_frames if request.save_other_frames is not None else '')
        else:
            if request.save_other_frames is not None:
                query_params.append((self.__downcase_first_letter('saveOtherFrames'), request.save_other_frames))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_image_frame_properties(self, request, **kwargs):  # noqa: E501
        """Get separate frame properties of existing TIFF image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_frame_properties_request object with parameters
        :return: ImagingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_image_frame_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_frame_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_image_frame_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_frame_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_image_frame_properties_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get separate frame properties of existing TIFF image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_frame_properties_request object with parameters
        :return: ImagingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_image_frame_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_image_frame_properties`")  # noqa: E501
        # verify the required parameter 'frame_id' is set
        if request.frame_id is None:
            raise ValueError("Missing the required parameter `frame_id` when calling `get_image_frame_properties`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/{name}/frames/{frameId}/properties'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.frame_id is not None:
            path_params[self.__downcase_first_letter('frameId')] = request.frame_id  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ImagingResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_image_gif(self, request, **kwargs):  # noqa: E501
        """Update parameters of existing GIF image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_gif_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_image_gif_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_gif_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_image_gif_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_gif_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_image_gif_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update parameters of existing GIF image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_gif_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_image_gif" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_image_gif`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/{name}/gif'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('backgroundColorIndex') in path:
            path = path.replace('{' + self.__downcase_first_letter('backgroundColorIndex' + '}'), request.background_color_index if request.background_color_index is not None else '')
        else:
            if request.background_color_index is not None:
                query_params.append((self.__downcase_first_letter('backgroundColorIndex'), request.background_color_index))  # noqa: E501
        if self.__downcase_first_letter('colorResolution') in path:
            path = path.replace('{' + self.__downcase_first_letter('colorResolution' + '}'), request.color_resolution if request.color_resolution is not None else '')
        else:
            if request.color_resolution is not None:
                query_params.append((self.__downcase_first_letter('colorResolution'), request.color_resolution))  # noqa: E501
        if self.__downcase_first_letter('hasTrailer') in path:
            path = path.replace('{' + self.__downcase_first_letter('hasTrailer' + '}'), request.has_trailer if request.has_trailer is not None else '')
        else:
            if request.has_trailer is not None:
                query_params.append((self.__downcase_first_letter('hasTrailer'), request.has_trailer))  # noqa: E501
        if self.__downcase_first_letter('interlaced') in path:
            path = path.replace('{' + self.__downcase_first_letter('interlaced' + '}'), request.interlaced if request.interlaced is not None else '')
        else:
            if request.interlaced is not None:
                query_params.append((self.__downcase_first_letter('interlaced'), request.interlaced))  # noqa: E501
        if self.__downcase_first_letter('isPaletteSorted') in path:
            path = path.replace('{' + self.__downcase_first_letter('isPaletteSorted' + '}'), request.is_palette_sorted if request.is_palette_sorted is not None else '')
        else:
            if request.is_palette_sorted is not None:
                query_params.append((self.__downcase_first_letter('isPaletteSorted'), request.is_palette_sorted))  # noqa: E501
        if self.__downcase_first_letter('pixelAspectRatio') in path:
            path = path.replace('{' + self.__downcase_first_letter('pixelAspectRatio' + '}'), request.pixel_aspect_ratio if request.pixel_aspect_ratio is not None else '')
        else:
            if request.pixel_aspect_ratio is not None:
                query_params.append((self.__downcase_first_letter('pixelAspectRatio'), request.pixel_aspect_ratio))  # noqa: E501
        if self.__downcase_first_letter('fromScratch') in path:
            path = path.replace('{' + self.__downcase_first_letter('fromScratch' + '}'), request.from_scratch if request.from_scratch is not None else '')
        else:
            if request.from_scratch is not None:
                query_params.append((self.__downcase_first_letter('fromScratch'), request.from_scratch))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_image_jpeg2000(self, request, **kwargs):  # noqa: E501
        """Update parameters of existing JPEG2000 image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_jpeg2000_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_image_jpeg2000_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_jpeg2000_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_image_jpeg2000_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_jpeg2000_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_image_jpeg2000_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update parameters of existing JPEG2000 image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_jpeg2000_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_image_jpeg2000" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_image_jpeg2000`")  # noqa: E501
        # verify the required parameter 'comment' is set
        if request.comment is None:
            raise ValueError("Missing the required parameter `comment` when calling `get_image_jpeg2000`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/{name}/jpg2000'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('comment') in path:
            path = path.replace('{' + self.__downcase_first_letter('comment' + '}'), request.comment if request.comment is not None else '')
        else:
            if request.comment is not None:
                query_params.append((self.__downcase_first_letter('comment'), request.comment))  # noqa: E501
        if self.__downcase_first_letter('codec') in path:
            path = path.replace('{' + self.__downcase_first_letter('codec' + '}'), request.codec if request.codec is not None else '')
        else:
            if request.codec is not None:
                query_params.append((self.__downcase_first_letter('codec'), request.codec))  # noqa: E501
        if self.__downcase_first_letter('fromScratch') in path:
            path = path.replace('{' + self.__downcase_first_letter('fromScratch' + '}'), request.from_scratch if request.from_scratch is not None else '')
        else:
            if request.from_scratch is not None:
                query_params.append((self.__downcase_first_letter('fromScratch'), request.from_scratch))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_image_jpg(self, request, **kwargs):  # noqa: E501
        """Update parameters of existing JPEG image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_jpg_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_image_jpg_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_jpg_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_image_jpg_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_jpg_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_image_jpg_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update parameters of existing JPEG image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_jpg_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_image_jpg" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_image_jpg`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/{name}/jpg'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('quality') in path:
            path = path.replace('{' + self.__downcase_first_letter('quality' + '}'), request.quality if request.quality is not None else '')
        else:
            if request.quality is not None:
                query_params.append((self.__downcase_first_letter('quality'), request.quality))  # noqa: E501
        if self.__downcase_first_letter('compressionType') in path:
            path = path.replace('{' + self.__downcase_first_letter('compressionType' + '}'), request.compression_type if request.compression_type is not None else '')
        else:
            if request.compression_type is not None:
                query_params.append((self.__downcase_first_letter('compressionType'), request.compression_type))  # noqa: E501
        if self.__downcase_first_letter('fromScratch') in path:
            path = path.replace('{' + self.__downcase_first_letter('fromScratch' + '}'), request.from_scratch if request.from_scratch is not None else '')
        else:
            if request.from_scratch is not None:
                query_params.append((self.__downcase_first_letter('fromScratch'), request.from_scratch))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_image_properties(self, request, **kwargs):  # noqa: E501
        """Get properties of an image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_properties_request object with parameters
        :return: ImagingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_image_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_image_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_image_properties_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get properties of an image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_properties_request object with parameters
        :return: ImagingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_image_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_image_properties`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/{name}/properties'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ImagingResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_image_psd(self, request, **kwargs):  # noqa: E501
        """Update parameters of existing PSD image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_psd_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_image_psd_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_psd_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_image_psd_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_psd_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_image_psd_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update parameters of existing PSD image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_psd_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_image_psd" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_image_psd`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/{name}/psd'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('channelsCount') in path:
            path = path.replace('{' + self.__downcase_first_letter('channelsCount' + '}'), request.channels_count if request.channels_count is not None else '')
        else:
            if request.channels_count is not None:
                query_params.append((self.__downcase_first_letter('channelsCount'), request.channels_count))  # noqa: E501
        if self.__downcase_first_letter('compressionMethod') in path:
            path = path.replace('{' + self.__downcase_first_letter('compressionMethod' + '}'), request.compression_method if request.compression_method is not None else '')
        else:
            if request.compression_method is not None:
                query_params.append((self.__downcase_first_letter('compressionMethod'), request.compression_method))  # noqa: E501
        if self.__downcase_first_letter('fromScratch') in path:
            path = path.replace('{' + self.__downcase_first_letter('fromScratch' + '}'), request.from_scratch if request.from_scratch is not None else '')
        else:
            if request.from_scratch is not None:
                query_params.append((self.__downcase_first_letter('fromScratch'), request.from_scratch))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_image_resize(self, request, **kwargs):  # noqa: E501
        """Resize an existing image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_resize_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_image_resize_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_resize_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_image_resize_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_resize_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_image_resize_with_http_info(self, request, **kwargs):  # noqa: E501
        """Resize an existing image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_resize_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_image_resize" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_image_resize`")  # noqa: E501
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `get_image_resize`")  # noqa: E501
        # verify the required parameter 'new_width' is set
        if request.new_width is None:
            raise ValueError("Missing the required parameter `new_width` when calling `get_image_resize`")  # noqa: E501
        # verify the required parameter 'new_height' is set
        if request.new_height is None:
            raise ValueError("Missing the required parameter `new_height` when calling `get_image_resize`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/{name}/resize'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('format') in path:
            path = path.replace('{' + self.__downcase_first_letter('format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('newWidth') in path:
            path = path.replace('{' + self.__downcase_first_letter('newWidth' + '}'), request.new_width if request.new_width is not None else '')
        else:
            if request.new_width is not None:
                query_params.append((self.__downcase_first_letter('newWidth'), request.new_width))  # noqa: E501
        if self.__downcase_first_letter('newHeight') in path:
            path = path.replace('{' + self.__downcase_first_letter('newHeight' + '}'), request.new_height if request.new_height is not None else '')
        else:
            if request.new_height is not None:
                query_params.append((self.__downcase_first_letter('newHeight'), request.new_height))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_image_rotate_flip(self, request, **kwargs):  # noqa: E501
        """Rotate and/or flip an existing image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_rotate_flip_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_image_rotate_flip_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_rotate_flip_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_image_rotate_flip_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_rotate_flip_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_image_rotate_flip_with_http_info(self, request, **kwargs):  # noqa: E501
        """Rotate and/or flip an existing image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_rotate_flip_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_image_rotate_flip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_image_rotate_flip`")  # noqa: E501
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `get_image_rotate_flip`")  # noqa: E501
        # verify the required parameter 'method' is set
        if request.method is None:
            raise ValueError("Missing the required parameter `method` when calling `get_image_rotate_flip`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/{name}/rotateflip'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('format') in path:
            path = path.replace('{' + self.__downcase_first_letter('format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('method') in path:
            path = path.replace('{' + self.__downcase_first_letter('method' + '}'), request.method if request.method is not None else '')
        else:
            if request.method is not None:
                query_params.append((self.__downcase_first_letter('method'), request.method))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_image_save_as(self, request, **kwargs):  # noqa: E501
        """Export existing image to another format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_save_as_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_image_save_as_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_save_as_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_image_save_as_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_save_as_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_image_save_as_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export existing image to another format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_save_as_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_image_save_as" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_image_save_as`")  # noqa: E501
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `get_image_save_as`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/{name}/saveAs'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('format') in path:
            path = path.replace('{' + self.__downcase_first_letter('format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_image_tiff(self, request, **kwargs):  # noqa: E501
        """Update parameters of existing TIFF image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_tiff_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_image_tiff_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_tiff_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_image_tiff_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_tiff_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_image_tiff_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update parameters of existing TIFF image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_tiff_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_image_tiff" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_image_tiff`")  # noqa: E501
        # verify the required parameter 'bit_depth' is set
        if request.bit_depth is None:
            raise ValueError("Missing the required parameter `bit_depth` when calling `get_image_tiff`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/{name}/tiff'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('bitDepth') in path:
            path = path.replace('{' + self.__downcase_first_letter('bitDepth' + '}'), request.bit_depth if request.bit_depth is not None else '')
        else:
            if request.bit_depth is not None:
                query_params.append((self.__downcase_first_letter('bitDepth'), request.bit_depth))  # noqa: E501
        if self.__downcase_first_letter('fromScratch') in path:
            path = path.replace('{' + self.__downcase_first_letter('fromScratch' + '}'), request.from_scratch if request.from_scratch is not None else '')
        else:
            if request.from_scratch is not None:
                query_params.append((self.__downcase_first_letter('fromScratch'), request.from_scratch))  # noqa: E501
        if self.__downcase_first_letter('compression') in path:
            path = path.replace('{' + self.__downcase_first_letter('compression' + '}'), request.compression if request.compression is not None else '')
        else:
            if request.compression is not None:
                query_params.append((self.__downcase_first_letter('compression'), request.compression))  # noqa: E501
        if self.__downcase_first_letter('resolutionUnit') in path:
            path = path.replace('{' + self.__downcase_first_letter('resolutionUnit' + '}'), request.resolution_unit if request.resolution_unit is not None else '')
        else:
            if request.resolution_unit is not None:
                query_params.append((self.__downcase_first_letter('resolutionUnit'), request.resolution_unit))  # noqa: E501
        if self.__downcase_first_letter('horizontalResolution') in path:
            path = path.replace('{' + self.__downcase_first_letter('horizontalResolution' + '}'), request.horizontal_resolution if request.horizontal_resolution is not None else '')
        else:
            if request.horizontal_resolution is not None:
                query_params.append((self.__downcase_first_letter('horizontalResolution'), request.horizontal_resolution))  # noqa: E501
        if self.__downcase_first_letter('verticalResolution') in path:
            path = path.replace('{' + self.__downcase_first_letter('verticalResolution' + '}'), request.vertical_resolution if request.vertical_resolution is not None else '')
        else:
            if request.vertical_resolution is not None:
                query_params.append((self.__downcase_first_letter('verticalResolution'), request.vertical_resolution))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_image_update(self, request, **kwargs):  # noqa: E501
        """Perform scaling, cropping and flipping of an existing image in a single request.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_update_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_image_update_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_update_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_image_update_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_update_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_image_update_with_http_info(self, request, **kwargs):  # noqa: E501
        """Perform scaling, cropping and flipping of an existing image in a single request.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_update_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_image_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_image_update`")  # noqa: E501
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `get_image_update`")  # noqa: E501
        # verify the required parameter 'new_width' is set
        if request.new_width is None:
            raise ValueError("Missing the required parameter `new_width` when calling `get_image_update`")  # noqa: E501
        # verify the required parameter 'new_height' is set
        if request.new_height is None:
            raise ValueError("Missing the required parameter `new_height` when calling `get_image_update`")  # noqa: E501
        # verify the required parameter 'x' is set
        if request.x is None:
            raise ValueError("Missing the required parameter `x` when calling `get_image_update`")  # noqa: E501
        # verify the required parameter 'y' is set
        if request.y is None:
            raise ValueError("Missing the required parameter `y` when calling `get_image_update`")  # noqa: E501
        # verify the required parameter 'rect_width' is set
        if request.rect_width is None:
            raise ValueError("Missing the required parameter `rect_width` when calling `get_image_update`")  # noqa: E501
        # verify the required parameter 'rect_height' is set
        if request.rect_height is None:
            raise ValueError("Missing the required parameter `rect_height` when calling `get_image_update`")  # noqa: E501
        # verify the required parameter 'rotate_flip_method' is set
        if request.rotate_flip_method is None:
            raise ValueError("Missing the required parameter `rotate_flip_method` when calling `get_image_update`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/{name}/updateImage'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('format') in path:
            path = path.replace('{' + self.__downcase_first_letter('format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('newWidth') in path:
            path = path.replace('{' + self.__downcase_first_letter('newWidth' + '}'), request.new_width if request.new_width is not None else '')
        else:
            if request.new_width is not None:
                query_params.append((self.__downcase_first_letter('newWidth'), request.new_width))  # noqa: E501
        if self.__downcase_first_letter('newHeight') in path:
            path = path.replace('{' + self.__downcase_first_letter('newHeight' + '}'), request.new_height if request.new_height is not None else '')
        else:
            if request.new_height is not None:
                query_params.append((self.__downcase_first_letter('newHeight'), request.new_height))  # noqa: E501
        if self.__downcase_first_letter('x') in path:
            path = path.replace('{' + self.__downcase_first_letter('x' + '}'), request.x if request.x is not None else '')
        else:
            if request.x is not None:
                query_params.append((self.__downcase_first_letter('x'), request.x))  # noqa: E501
        if self.__downcase_first_letter('y') in path:
            path = path.replace('{' + self.__downcase_first_letter('y' + '}'), request.y if request.y is not None else '')
        else:
            if request.y is not None:
                query_params.append((self.__downcase_first_letter('y'), request.y))  # noqa: E501
        if self.__downcase_first_letter('rectWidth') in path:
            path = path.replace('{' + self.__downcase_first_letter('rectWidth' + '}'), request.rect_width if request.rect_width is not None else '')
        else:
            if request.rect_width is not None:
                query_params.append((self.__downcase_first_letter('rectWidth'), request.rect_width))  # noqa: E501
        if self.__downcase_first_letter('rectHeight') in path:
            path = path.replace('{' + self.__downcase_first_letter('rectHeight' + '}'), request.rect_height if request.rect_height is not None else '')
        else:
            if request.rect_height is not None:
                query_params.append((self.__downcase_first_letter('rectHeight'), request.rect_height))  # noqa: E501
        if self.__downcase_first_letter('rotateFlipMethod') in path:
            path = path.replace('{' + self.__downcase_first_letter('rotateFlipMethod' + '}'), request.rotate_flip_method if request.rotate_flip_method is not None else '')
        else:
            if request.rotate_flip_method is not None:
                query_params.append((self.__downcase_first_letter('rotateFlipMethod'), request.rotate_flip_method))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_image_web_p(self, request, **kwargs):  # noqa: E501
        """Update parameters of existing WEBP image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_web_p_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_image_web_p_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_web_p_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_image_web_p_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_web_p_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_image_web_p_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update parameters of existing WEBP image.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_web_p_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_image_web_p" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_image_web_p`")  # noqa: E501
        # verify the required parameter 'loss_less' is set
        if request.loss_less is None:
            raise ValueError("Missing the required parameter `loss_less` when calling `get_image_web_p`")  # noqa: E501
        # verify the required parameter 'quality' is set
        if request.quality is None:
            raise ValueError("Missing the required parameter `quality` when calling `get_image_web_p`")  # noqa: E501
        # verify the required parameter 'anim_loop_count' is set
        if request.anim_loop_count is None:
            raise ValueError("Missing the required parameter `anim_loop_count` when calling `get_image_web_p`")  # noqa: E501
        # verify the required parameter 'anim_background_color' is set
        if request.anim_background_color is None:
            raise ValueError("Missing the required parameter `anim_background_color` when calling `get_image_web_p`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/{name}/webp'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('lossLess') in path:
            path = path.replace('{' + self.__downcase_first_letter('lossLess' + '}'), request.loss_less if request.loss_less is not None else '')
        else:
            if request.loss_less is not None:
                query_params.append((self.__downcase_first_letter('lossLess'), request.loss_less))  # noqa: E501
        if self.__downcase_first_letter('quality') in path:
            path = path.replace('{' + self.__downcase_first_letter('quality' + '}'), request.quality if request.quality is not None else '')
        else:
            if request.quality is not None:
                query_params.append((self.__downcase_first_letter('quality'), request.quality))  # noqa: E501
        if self.__downcase_first_letter('animLoopCount') in path:
            path = path.replace('{' + self.__downcase_first_letter('animLoopCount' + '}'), request.anim_loop_count if request.anim_loop_count is not None else '')
        else:
            if request.anim_loop_count is not None:
                query_params.append((self.__downcase_first_letter('animLoopCount'), request.anim_loop_count))  # noqa: E501
        if self.__downcase_first_letter('animBackgroundColor') in path:
            path = path.replace('{' + self.__downcase_first_letter('animBackgroundColor' + '}'), request.anim_background_color if request.anim_background_color is not None else '')
        else:
            if request.anim_background_color is not None:
                query_params.append((self.__downcase_first_letter('animBackgroundColor'), request.anim_background_color))  # noqa: E501
        if self.__downcase_first_letter('fromScratch') in path:
            path = path.replace('{' + self.__downcase_first_letter('fromScratch' + '}'), request.from_scratch if request.from_scratch is not None else '')
        else:
            if request.from_scratch is not None:
                query_params.append((self.__downcase_first_letter('fromScratch'), request.from_scratch))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_image_wmf(self, request, **kwargs):  # noqa: E501
        """Process existing WMF image using given parameters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_wmf_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_image_wmf_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_wmf_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_image_wmf_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_image_wmf_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_image_wmf_with_http_info(self, request, **kwargs):  # noqa: E501
        """Process existing WMF image using given parameters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_image_wmf_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_image_wmf" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_image_wmf`")  # noqa: E501
        # verify the required parameter 'bk_color' is set
        if request.bk_color is None:
            raise ValueError("Missing the required parameter `bk_color` when calling `get_image_wmf`")  # noqa: E501
        # verify the required parameter 'page_width' is set
        if request.page_width is None:
            raise ValueError("Missing the required parameter `page_width` when calling `get_image_wmf`")  # noqa: E501
        # verify the required parameter 'page_height' is set
        if request.page_height is None:
            raise ValueError("Missing the required parameter `page_height` when calling `get_image_wmf`")  # noqa: E501
        # verify the required parameter 'border_x' is set
        if request.border_x is None:
            raise ValueError("Missing the required parameter `border_x` when calling `get_image_wmf`")  # noqa: E501
        # verify the required parameter 'border_y' is set
        if request.border_y is None:
            raise ValueError("Missing the required parameter `border_y` when calling `get_image_wmf`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/{name}/wmf'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('bkColor') in path:
            path = path.replace('{' + self.__downcase_first_letter('bkColor' + '}'), request.bk_color if request.bk_color is not None else '')
        else:
            if request.bk_color is not None:
                query_params.append((self.__downcase_first_letter('bkColor'), request.bk_color))  # noqa: E501
        if self.__downcase_first_letter('pageWidth') in path:
            path = path.replace('{' + self.__downcase_first_letter('pageWidth' + '}'), request.page_width if request.page_width is not None else '')
        else:
            if request.page_width is not None:
                query_params.append((self.__downcase_first_letter('pageWidth'), request.page_width))  # noqa: E501
        if self.__downcase_first_letter('pageHeight') in path:
            path = path.replace('{' + self.__downcase_first_letter('pageHeight' + '}'), request.page_height if request.page_height is not None else '')
        else:
            if request.page_height is not None:
                query_params.append((self.__downcase_first_letter('pageHeight'), request.page_height))  # noqa: E501
        if self.__downcase_first_letter('borderX') in path:
            path = path.replace('{' + self.__downcase_first_letter('borderX' + '}'), request.border_x if request.border_x is not None else '')
        else:
            if request.border_x is not None:
                query_params.append((self.__downcase_first_letter('borderX'), request.border_x))  # noqa: E501
        if self.__downcase_first_letter('borderY') in path:
            path = path.replace('{' + self.__downcase_first_letter('borderY' + '}'), request.border_y if request.border_y is not None else '')
        else:
            if request.border_y is not None:
                query_params.append((self.__downcase_first_letter('borderY'), request.border_y))  # noqa: E501
        if self.__downcase_first_letter('fromScratch') in path:
            path = path.replace('{' + self.__downcase_first_letter('fromScratch' + '}'), request.from_scratch if request.from_scratch is not None else '')
        else:
            if request.from_scratch is not None:
                query_params.append((self.__downcase_first_letter('fromScratch'), request.from_scratch))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('format') in path:
            path = path.replace('{' + self.__downcase_first_letter('format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('format'), request.format))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_search_context_extract_image_features(self, request, **kwargs):  # noqa: E501
        """Extract features from image without adding to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_search_context_extract_image_features_request object with parameters
        :return: ImageFeatures
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_search_context_extract_image_features_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_search_context_extract_image_features_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_search_context_extract_image_features_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_search_context_extract_image_features_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_search_context_extract_image_features_with_http_info(self, request, **kwargs):  # noqa: E501
        """Extract features from image without adding to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_search_context_extract_image_features_request object with parameters
        :return: ImageFeatures
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_search_context_extract_image_features" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_context_id' is set
        if request.search_context_id is None:
            raise ValueError("Missing the required parameter `search_context_id` when calling `get_search_context_extract_image_features`")  # noqa: E501
        # verify the required parameter 'image_id' is set
        if request.image_id is None:
            raise ValueError("Missing the required parameter `image_id` when calling `get_search_context_extract_image_features`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/ai/imageSearch/{searchContextId}/image2features'
        path_params = {}
        if request.search_context_id is not None:
            path_params[self.__downcase_first_letter('searchContextId')] = request.search_context_id  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('imageId') in path:
            path = path.replace('{' + self.__downcase_first_letter('imageId' + '}'), request.image_id if request.image_id is not None else '')
        else:
            if request.image_id is not None:
                query_params.append((self.__downcase_first_letter('imageId'), request.image_id))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ImageFeatures',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_search_context_find_duplicates(self, request, **kwargs):  # noqa: E501
        """Find images duplicates.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_search_context_find_duplicates_request object with parameters
        :return: ImageDuplicatesSet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_search_context_find_duplicates_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_search_context_find_duplicates_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_search_context_find_duplicates_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_search_context_find_duplicates_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_search_context_find_duplicates_with_http_info(self, request, **kwargs):  # noqa: E501
        """Find images duplicates.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_search_context_find_duplicates_request object with parameters
        :return: ImageDuplicatesSet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_search_context_find_duplicates" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_context_id' is set
        if request.search_context_id is None:
            raise ValueError("Missing the required parameter `search_context_id` when calling `get_search_context_find_duplicates`")  # noqa: E501
        # verify the required parameter 'similarity_threshold' is set
        if request.similarity_threshold is None:
            raise ValueError("Missing the required parameter `similarity_threshold` when calling `get_search_context_find_duplicates`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/ai/imageSearch/{searchContextId}/findDuplicates'
        path_params = {}
        if request.search_context_id is not None:
            path_params[self.__downcase_first_letter('searchContextId')] = request.search_context_id  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('similarityThreshold') in path:
            path = path.replace('{' + self.__downcase_first_letter('similarityThreshold' + '}'), request.similarity_threshold if request.similarity_threshold is not None else '')
        else:
            if request.similarity_threshold is not None:
                query_params.append((self.__downcase_first_letter('similarityThreshold'), request.similarity_threshold))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ImageDuplicatesSet',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_search_context_find_similar(self, request, **kwargs):  # noqa: E501
        """Find similar images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_search_context_find_similar_request object with parameters
        :return: SearchResultsSet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_search_context_find_similar_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_search_context_find_similar_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_search_context_find_similar_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_search_context_find_similar_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_search_context_find_similar_with_http_info(self, request, **kwargs):  # noqa: E501
        """Find similar images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_search_context_find_similar_request object with parameters
        :return: SearchResultsSet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_search_context_find_similar" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_context_id' is set
        if request.search_context_id is None:
            raise ValueError("Missing the required parameter `search_context_id` when calling `get_search_context_find_similar`")  # noqa: E501
        # verify the required parameter 'similarity_threshold' is set
        if request.similarity_threshold is None:
            raise ValueError("Missing the required parameter `similarity_threshold` when calling `get_search_context_find_similar`")  # noqa: E501
        # verify the required parameter 'max_count' is set
        if request.max_count is None:
            raise ValueError("Missing the required parameter `max_count` when calling `get_search_context_find_similar`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/ai/imageSearch/{searchContextId}/findSimilar'
        path_params = {}
        if request.search_context_id is not None:
            path_params[self.__downcase_first_letter('searchContextId')] = request.search_context_id  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('similarityThreshold') in path:
            path = path.replace('{' + self.__downcase_first_letter('similarityThreshold' + '}'), request.similarity_threshold if request.similarity_threshold is not None else '')
        else:
            if request.similarity_threshold is not None:
                query_params.append((self.__downcase_first_letter('similarityThreshold'), request.similarity_threshold))  # noqa: E501
        if self.__downcase_first_letter('maxCount') in path:
            path = path.replace('{' + self.__downcase_first_letter('maxCount' + '}'), request.max_count if request.max_count is not None else '')
        else:
            if request.max_count is not None:
                query_params.append((self.__downcase_first_letter('maxCount'), request.max_count))  # noqa: E501
        if self.__downcase_first_letter('imageId') in path:
            path = path.replace('{' + self.__downcase_first_letter('imageId' + '}'), request.image_id if request.image_id is not None else '')
        else:
            if request.image_id is not None:
                query_params.append((self.__downcase_first_letter('imageId'), request.image_id))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchResultsSet',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_search_context_image(self, request, **kwargs):  # noqa: E501
        """Get image from search context  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_search_context_image_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_search_context_image_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_search_context_image_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_search_context_image_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_search_context_image_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_search_context_image_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get image from search context  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_search_context_image_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_search_context_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_context_id' is set
        if request.search_context_id is None:
            raise ValueError("Missing the required parameter `search_context_id` when calling `get_search_context_image`")  # noqa: E501
        # verify the required parameter 'image_id' is set
        if request.image_id is None:
            raise ValueError("Missing the required parameter `image_id` when calling `get_search_context_image`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/ai/imageSearch/{searchContextId}/image'
        path_params = {}
        if request.search_context_id is not None:
            path_params[self.__downcase_first_letter('searchContextId')] = request.search_context_id  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('imageId') in path:
            path = path.replace('{' + self.__downcase_first_letter('imageId' + '}'), request.image_id if request.image_id is not None else '')
        else:
            if request.image_id is not None:
                query_params.append((self.__downcase_first_letter('imageId'), request.image_id))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_search_context_image_features(self, request, **kwargs):  # noqa: E501
        """Gets image features from search context.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_search_context_image_features_request object with parameters
        :return: ImageFeatures
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_search_context_image_features_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_search_context_image_features_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_search_context_image_features_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_search_context_image_features_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_search_context_image_features_with_http_info(self, request, **kwargs):  # noqa: E501
        """Gets image features from search context.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_search_context_image_features_request object with parameters
        :return: ImageFeatures
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_search_context_image_features" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_context_id' is set
        if request.search_context_id is None:
            raise ValueError("Missing the required parameter `search_context_id` when calling `get_search_context_image_features`")  # noqa: E501
        # verify the required parameter 'image_id' is set
        if request.image_id is None:
            raise ValueError("Missing the required parameter `image_id` when calling `get_search_context_image_features`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/ai/imageSearch/{searchContextId}/features'
        path_params = {}
        if request.search_context_id is not None:
            path_params[self.__downcase_first_letter('searchContextId')] = request.search_context_id  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('imageId') in path:
            path = path.replace('{' + self.__downcase_first_letter('imageId' + '}'), request.image_id if request.image_id is not None else '')
        else:
            if request.image_id is not None:
                query_params.append((self.__downcase_first_letter('imageId'), request.image_id))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ImageFeatures',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_search_context_status(self, request, **kwargs):  # noqa: E501
        """Gets the search context status.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_search_context_status_request object with parameters
        :return: SearchContextStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_search_context_status_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_search_context_status_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_search_context_status_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_search_context_status_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_search_context_status_with_http_info(self, request, **kwargs):  # noqa: E501
        """Gets the search context status.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_search_context_status_request object with parameters
        :return: SearchContextStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_search_context_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_context_id' is set
        if request.search_context_id is None:
            raise ValueError("Missing the required parameter `search_context_id` when calling `get_search_context_status`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/ai/imageSearch/{searchContextId}/status'
        path_params = {}
        if request.search_context_id is not None:
            path_params[self.__downcase_first_letter('searchContextId')] = request.search_context_id  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchContextStatus',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tiff_to_fax(self, request, **kwargs):  # noqa: E501
        """Update parameters of existing TIFF image accordingly to fax parameters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_tiff_to_fax_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_tiff_to_fax_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_tiff_to_fax_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_tiff_to_fax_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_tiff_to_fax_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def get_tiff_to_fax_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update parameters of existing TIFF image accordingly to fax parameters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_tiff_to_fax_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tiff_to_fax" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_tiff_to_fax`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/tiff/{name}/toFax'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def move_file(self, request, **kwargs):  # noqa: E501
        """Move file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request move_file_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.move_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.move_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.move_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.move_file_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def move_file_with_http_info(self, request, **kwargs):  # noqa: E501
        """Move file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request move_file_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method move_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'src_path' is set
        if request.src_path is None:
            raise ValueError("Missing the required parameter `src_path` when calling `move_file`")  # noqa: E501
        # verify the required parameter 'dest_path' is set
        if request.dest_path is None:
            raise ValueError("Missing the required parameter `dest_path` when calling `move_file`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/storage/file/move/{srcPath}'
        path_params = {}
        if request.src_path is not None:
            path_params[self.__downcase_first_letter('srcPath')] = request.src_path  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('destPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('destPath' + '}'), request.dest_path if request.dest_path is not None else '')
        else:
            if request.dest_path is not None:
                query_params.append((self.__downcase_first_letter('destPath'), request.dest_path))  # noqa: E501
        if self.__downcase_first_letter('srcStorageName') in path:
            path = path.replace('{' + self.__downcase_first_letter('srcStorageName' + '}'), request.src_storage_name if request.src_storage_name is not None else '')
        else:
            if request.src_storage_name is not None:
                query_params.append((self.__downcase_first_letter('srcStorageName'), request.src_storage_name))  # noqa: E501
        if self.__downcase_first_letter('destStorageName') in path:
            path = path.replace('{' + self.__downcase_first_letter('destStorageName' + '}'), request.dest_storage_name if request.dest_storage_name is not None else '')
        else:
            if request.dest_storage_name is not None:
                query_params.append((self.__downcase_first_letter('destStorageName'), request.dest_storage_name))  # noqa: E501
        if self.__downcase_first_letter('versionId') in path:
            path = path.replace('{' + self.__downcase_first_letter('versionId' + '}'), request.version_id if request.version_id is not None else '')
        else:
            if request.version_id is not None:
                query_params.append((self.__downcase_first_letter('versionId'), request.version_id))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def move_folder(self, request, **kwargs):  # noqa: E501
        """Move folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request move_folder_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.move_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.move_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.move_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.move_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def move_folder_with_http_info(self, request, **kwargs):  # noqa: E501
        """Move folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request move_folder_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method move_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'src_path' is set
        if request.src_path is None:
            raise ValueError("Missing the required parameter `src_path` when calling `move_folder`")  # noqa: E501
        # verify the required parameter 'dest_path' is set
        if request.dest_path is None:
            raise ValueError("Missing the required parameter `dest_path` when calling `move_folder`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/storage/folder/move/{srcPath}'
        path_params = {}
        if request.src_path is not None:
            path_params[self.__downcase_first_letter('srcPath')] = request.src_path  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('destPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('destPath' + '}'), request.dest_path if request.dest_path is not None else '')
        else:
            if request.dest_path is not None:
                query_params.append((self.__downcase_first_letter('destPath'), request.dest_path))  # noqa: E501
        if self.__downcase_first_letter('srcStorageName') in path:
            path = path.replace('{' + self.__downcase_first_letter('srcStorageName' + '}'), request.src_storage_name if request.src_storage_name is not None else '')
        else:
            if request.src_storage_name is not None:
                query_params.append((self.__downcase_first_letter('srcStorageName'), request.src_storage_name))  # noqa: E501
        if self.__downcase_first_letter('destStorageName') in path:
            path = path.replace('{' + self.__downcase_first_letter('destStorageName' + '}'), request.dest_storage_name if request.dest_storage_name is not None else '')
        else:
            if request.dest_storage_name is not None:
                query_params.append((self.__downcase_first_letter('destStorageName'), request.dest_storage_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def object_exists(self, request, **kwargs):  # noqa: E501
        """Check if file or folder exists  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request object_exists_request object with parameters
        :return: ObjectExist
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.object_exists_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.object_exists_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.object_exists_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.object_exists_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def object_exists_with_http_info(self, request, **kwargs):  # noqa: E501
        """Check if file or folder exists  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request object_exists_request object with parameters
        :return: ObjectExist
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method object_exists" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if request.path is None:
            raise ValueError("Missing the required parameter `path` when calling `object_exists`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/storage/exist/{path}'
        path_params = {}
        if request.path is not None:
            path_params[self.__downcase_first_letter('path')] = request.path  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('storageName') in path:
            path = path.replace('{' + self.__downcase_first_letter('storageName' + '}'), request.storage_name if request.storage_name is not None else '')
        else:
            if request.storage_name is not None:
                query_params.append((self.__downcase_first_letter('storageName'), request.storage_name))  # noqa: E501
        if self.__downcase_first_letter('versionId') in path:
            path = path.replace('{' + self.__downcase_first_letter('versionId' + '}'), request.version_id if request.version_id is not None else '')
        else:
            if request.version_id is not None:
                query_params.append((self.__downcase_first_letter('versionId'), request.version_id))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ObjectExist',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_create_search_context(self, request, **kwargs):  # noqa: E501
        """Create new search context.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_create_search_context_request object with parameters
        :return: SearchContextStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_create_search_context_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_create_search_context_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_create_search_context_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_create_search_context_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_create_search_context_with_http_info(self, request, **kwargs):  # noqa: E501
        """Create new search context.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_create_search_context_request object with parameters
        :return: SearchContextStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_create_search_context" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}
        path = '/imaging/ai/imageSearch/create'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('detector') in path:
            path = path.replace('{' + self.__downcase_first_letter('detector' + '}'), request.detector if request.detector is not None else '')
        else:
            if request.detector is not None:
                query_params.append((self.__downcase_first_letter('detector'), request.detector))  # noqa: E501
        if self.__downcase_first_letter('matchingAlgorithm') in path:
            path = path.replace('{' + self.__downcase_first_letter('matchingAlgorithm' + '}'), request.matching_algorithm if request.matching_algorithm is not None else '')
        else:
            if request.matching_algorithm is not None:
                query_params.append((self.__downcase_first_letter('matchingAlgorithm'), request.matching_algorithm))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchContextStatus',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_image_bmp(self, request, **kwargs):  # noqa: E501
        """Update parameters of BMP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_bmp_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_image_bmp_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_bmp_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_image_bmp_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_bmp_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_image_bmp_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update parameters of BMP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_bmp_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_image_bmp" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'image_data' is set
        if request.image_data is None:
            raise ValueError("Missing the required parameter `image_data` when calling `post_image_bmp`")  # noqa: E501
        # verify the required parameter 'bits_per_pixel' is set
        if request.bits_per_pixel is None:
            raise ValueError("Missing the required parameter `bits_per_pixel` when calling `post_image_bmp`")  # noqa: E501
        # verify the required parameter 'horizontal_resolution' is set
        if request.horizontal_resolution is None:
            raise ValueError("Missing the required parameter `horizontal_resolution` when calling `post_image_bmp`")  # noqa: E501
        # verify the required parameter 'vertical_resolution' is set
        if request.vertical_resolution is None:
            raise ValueError("Missing the required parameter `vertical_resolution` when calling `post_image_bmp`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/bmp'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('bitsPerPixel') in path:
            path = path.replace('{' + self.__downcase_first_letter('bitsPerPixel' + '}'), request.bits_per_pixel if request.bits_per_pixel is not None else '')
        else:
            if request.bits_per_pixel is not None:
                query_params.append((self.__downcase_first_letter('bitsPerPixel'), request.bits_per_pixel))  # noqa: E501
        if self.__downcase_first_letter('horizontalResolution') in path:
            path = path.replace('{' + self.__downcase_first_letter('horizontalResolution' + '}'), request.horizontal_resolution if request.horizontal_resolution is not None else '')
        else:
            if request.horizontal_resolution is not None:
                query_params.append((self.__downcase_first_letter('horizontalResolution'), request.horizontal_resolution))  # noqa: E501
        if self.__downcase_first_letter('verticalResolution') in path:
            path = path.replace('{' + self.__downcase_first_letter('verticalResolution' + '}'), request.vertical_resolution if request.vertical_resolution is not None else '')
        else:
            if request.vertical_resolution is not None:
                query_params.append((self.__downcase_first_letter('verticalResolution'), request.vertical_resolution))  # noqa: E501
        if self.__downcase_first_letter('fromScratch') in path:
            path = path.replace('{' + self.__downcase_first_letter('fromScratch' + '}'), request.from_scratch if request.from_scratch is not None else '')
        else:
            if request.from_scratch is not None:
                query_params.append((self.__downcase_first_letter('fromScratch'), request.from_scratch))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_image_crop(self, request, **kwargs):  # noqa: E501
        """Crop an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_crop_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_image_crop_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_crop_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_image_crop_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_crop_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_image_crop_with_http_info(self, request, **kwargs):  # noqa: E501
        """Crop an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_crop_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_image_crop" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'image_data' is set
        if request.image_data is None:
            raise ValueError("Missing the required parameter `image_data` when calling `post_image_crop`")  # noqa: E501
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `post_image_crop`")  # noqa: E501
        # verify the required parameter 'x' is set
        if request.x is None:
            raise ValueError("Missing the required parameter `x` when calling `post_image_crop`")  # noqa: E501
        # verify the required parameter 'y' is set
        if request.y is None:
            raise ValueError("Missing the required parameter `y` when calling `post_image_crop`")  # noqa: E501
        # verify the required parameter 'width' is set
        if request.width is None:
            raise ValueError("Missing the required parameter `width` when calling `post_image_crop`")  # noqa: E501
        # verify the required parameter 'height' is set
        if request.height is None:
            raise ValueError("Missing the required parameter `height` when calling `post_image_crop`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/crop'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('format') in path:
            path = path.replace('{' + self.__downcase_first_letter('format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('x') in path:
            path = path.replace('{' + self.__downcase_first_letter('x' + '}'), request.x if request.x is not None else '')
        else:
            if request.x is not None:
                query_params.append((self.__downcase_first_letter('x'), request.x))  # noqa: E501
        if self.__downcase_first_letter('y') in path:
            path = path.replace('{' + self.__downcase_first_letter('y' + '}'), request.y if request.y is not None else '')
        else:
            if request.y is not None:
                query_params.append((self.__downcase_first_letter('y'), request.y))  # noqa: E501
        if self.__downcase_first_letter('width') in path:
            path = path.replace('{' + self.__downcase_first_letter('width' + '}'), request.width if request.width is not None else '')
        else:
            if request.width is not None:
                query_params.append((self.__downcase_first_letter('width'), request.width))  # noqa: E501
        if self.__downcase_first_letter('height') in path:
            path = path.replace('{' + self.__downcase_first_letter('height' + '}'), request.height if request.height is not None else '')
        else:
            if request.height is not None:
                query_params.append((self.__downcase_first_letter('height'), request.height))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_image_emf(self, request, **kwargs):  # noqa: E501
        """Process existing EMF imaging using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_emf_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_image_emf_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_emf_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_image_emf_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_emf_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_image_emf_with_http_info(self, request, **kwargs):  # noqa: E501
        """Process existing EMF imaging using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_emf_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_image_emf" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'image_data' is set
        if request.image_data is None:
            raise ValueError("Missing the required parameter `image_data` when calling `post_image_emf`")  # noqa: E501
        # verify the required parameter 'bk_color' is set
        if request.bk_color is None:
            raise ValueError("Missing the required parameter `bk_color` when calling `post_image_emf`")  # noqa: E501
        # verify the required parameter 'page_width' is set
        if request.page_width is None:
            raise ValueError("Missing the required parameter `page_width` when calling `post_image_emf`")  # noqa: E501
        # verify the required parameter 'page_height' is set
        if request.page_height is None:
            raise ValueError("Missing the required parameter `page_height` when calling `post_image_emf`")  # noqa: E501
        # verify the required parameter 'border_x' is set
        if request.border_x is None:
            raise ValueError("Missing the required parameter `border_x` when calling `post_image_emf`")  # noqa: E501
        # verify the required parameter 'border_y' is set
        if request.border_y is None:
            raise ValueError("Missing the required parameter `border_y` when calling `post_image_emf`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/emf'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('bkColor') in path:
            path = path.replace('{' + self.__downcase_first_letter('bkColor' + '}'), request.bk_color if request.bk_color is not None else '')
        else:
            if request.bk_color is not None:
                query_params.append((self.__downcase_first_letter('bkColor'), request.bk_color))  # noqa: E501
        if self.__downcase_first_letter('pageWidth') in path:
            path = path.replace('{' + self.__downcase_first_letter('pageWidth' + '}'), request.page_width if request.page_width is not None else '')
        else:
            if request.page_width is not None:
                query_params.append((self.__downcase_first_letter('pageWidth'), request.page_width))  # noqa: E501
        if self.__downcase_first_letter('pageHeight') in path:
            path = path.replace('{' + self.__downcase_first_letter('pageHeight' + '}'), request.page_height if request.page_height is not None else '')
        else:
            if request.page_height is not None:
                query_params.append((self.__downcase_first_letter('pageHeight'), request.page_height))  # noqa: E501
        if self.__downcase_first_letter('borderX') in path:
            path = path.replace('{' + self.__downcase_first_letter('borderX' + '}'), request.border_x if request.border_x is not None else '')
        else:
            if request.border_x is not None:
                query_params.append((self.__downcase_first_letter('borderX'), request.border_x))  # noqa: E501
        if self.__downcase_first_letter('borderY') in path:
            path = path.replace('{' + self.__downcase_first_letter('borderY' + '}'), request.border_y if request.border_y is not None else '')
        else:
            if request.border_y is not None:
                query_params.append((self.__downcase_first_letter('borderY'), request.border_y))  # noqa: E501
        if self.__downcase_first_letter('fromScratch') in path:
            path = path.replace('{' + self.__downcase_first_letter('fromScratch' + '}'), request.from_scratch if request.from_scratch is not None else '')
        else:
            if request.from_scratch is not None:
                query_params.append((self.__downcase_first_letter('fromScratch'), request.from_scratch))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('format') in path:
            path = path.replace('{' + self.__downcase_first_letter('format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('format'), request.format))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_image_frame(self, request, **kwargs):  # noqa: E501
        """Get separate frame from existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_frame_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_image_frame_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_frame_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_image_frame_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_frame_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_image_frame_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get separate frame from existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_frame_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_image_frame" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'image_data' is set
        if request.image_data is None:
            raise ValueError("Missing the required parameter `image_data` when calling `post_image_frame`")  # noqa: E501
        # verify the required parameter 'frame_id' is set
        if request.frame_id is None:
            raise ValueError("Missing the required parameter `frame_id` when calling `post_image_frame`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/frames/{frameId}'
        path_params = {}
        if request.frame_id is not None:
            path_params[self.__downcase_first_letter('frameId')] = request.frame_id  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('newWidth') in path:
            path = path.replace('{' + self.__downcase_first_letter('newWidth' + '}'), request.new_width if request.new_width is not None else '')
        else:
            if request.new_width is not None:
                query_params.append((self.__downcase_first_letter('newWidth'), request.new_width))  # noqa: E501
        if self.__downcase_first_letter('newHeight') in path:
            path = path.replace('{' + self.__downcase_first_letter('newHeight' + '}'), request.new_height if request.new_height is not None else '')
        else:
            if request.new_height is not None:
                query_params.append((self.__downcase_first_letter('newHeight'), request.new_height))  # noqa: E501
        if self.__downcase_first_letter('x') in path:
            path = path.replace('{' + self.__downcase_first_letter('x' + '}'), request.x if request.x is not None else '')
        else:
            if request.x is not None:
                query_params.append((self.__downcase_first_letter('x'), request.x))  # noqa: E501
        if self.__downcase_first_letter('y') in path:
            path = path.replace('{' + self.__downcase_first_letter('y' + '}'), request.y if request.y is not None else '')
        else:
            if request.y is not None:
                query_params.append((self.__downcase_first_letter('y'), request.y))  # noqa: E501
        if self.__downcase_first_letter('rectWidth') in path:
            path = path.replace('{' + self.__downcase_first_letter('rectWidth' + '}'), request.rect_width if request.rect_width is not None else '')
        else:
            if request.rect_width is not None:
                query_params.append((self.__downcase_first_letter('rectWidth'), request.rect_width))  # noqa: E501
        if self.__downcase_first_letter('rectHeight') in path:
            path = path.replace('{' + self.__downcase_first_letter('rectHeight' + '}'), request.rect_height if request.rect_height is not None else '')
        else:
            if request.rect_height is not None:
                query_params.append((self.__downcase_first_letter('rectHeight'), request.rect_height))  # noqa: E501
        if self.__downcase_first_letter('rotateFlipMethod') in path:
            path = path.replace('{' + self.__downcase_first_letter('rotateFlipMethod' + '}'), request.rotate_flip_method if request.rotate_flip_method is not None else '')
        else:
            if request.rotate_flip_method is not None:
                query_params.append((self.__downcase_first_letter('rotateFlipMethod'), request.rotate_flip_method))  # noqa: E501
        if self.__downcase_first_letter('saveOtherFrames') in path:
            path = path.replace('{' + self.__downcase_first_letter('saveOtherFrames' + '}'), request.save_other_frames if request.save_other_frames is not None else '')
        else:
            if request.save_other_frames is not None:
                query_params.append((self.__downcase_first_letter('saveOtherFrames'), request.save_other_frames))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_image_frame_properties(self, request, **kwargs):  # noqa: E501
        """Get separate frame properties of existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_frame_properties_request object with parameters
        :return: ImagingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_image_frame_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_frame_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_image_frame_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_frame_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_image_frame_properties_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get separate frame properties of existing TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_frame_properties_request object with parameters
        :return: ImagingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_image_frame_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'image_data' is set
        if request.image_data is None:
            raise ValueError("Missing the required parameter `image_data` when calling `post_image_frame_properties`")  # noqa: E501
        # verify the required parameter 'frame_id' is set
        if request.frame_id is None:
            raise ValueError("Missing the required parameter `frame_id` when calling `post_image_frame_properties`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/frames/{frameId}/properties'
        path_params = {}
        if request.frame_id is not None:
            path_params[self.__downcase_first_letter('frameId')] = request.frame_id  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ImagingResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_image_gif(self, request, **kwargs):  # noqa: E501
        """Update parameters of GIF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_gif_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_image_gif_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_gif_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_image_gif_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_gif_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_image_gif_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update parameters of GIF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_gif_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_image_gif" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'image_data' is set
        if request.image_data is None:
            raise ValueError("Missing the required parameter `image_data` when calling `post_image_gif`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/gif'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('backgroundColorIndex') in path:
            path = path.replace('{' + self.__downcase_first_letter('backgroundColorIndex' + '}'), request.background_color_index if request.background_color_index is not None else '')
        else:
            if request.background_color_index is not None:
                query_params.append((self.__downcase_first_letter('backgroundColorIndex'), request.background_color_index))  # noqa: E501
        if self.__downcase_first_letter('colorResolution') in path:
            path = path.replace('{' + self.__downcase_first_letter('colorResolution' + '}'), request.color_resolution if request.color_resolution is not None else '')
        else:
            if request.color_resolution is not None:
                query_params.append((self.__downcase_first_letter('colorResolution'), request.color_resolution))  # noqa: E501
        if self.__downcase_first_letter('hasTrailer') in path:
            path = path.replace('{' + self.__downcase_first_letter('hasTrailer' + '}'), request.has_trailer if request.has_trailer is not None else '')
        else:
            if request.has_trailer is not None:
                query_params.append((self.__downcase_first_letter('hasTrailer'), request.has_trailer))  # noqa: E501
        if self.__downcase_first_letter('interlaced') in path:
            path = path.replace('{' + self.__downcase_first_letter('interlaced' + '}'), request.interlaced if request.interlaced is not None else '')
        else:
            if request.interlaced is not None:
                query_params.append((self.__downcase_first_letter('interlaced'), request.interlaced))  # noqa: E501
        if self.__downcase_first_letter('isPaletteSorted') in path:
            path = path.replace('{' + self.__downcase_first_letter('isPaletteSorted' + '}'), request.is_palette_sorted if request.is_palette_sorted is not None else '')
        else:
            if request.is_palette_sorted is not None:
                query_params.append((self.__downcase_first_letter('isPaletteSorted'), request.is_palette_sorted))  # noqa: E501
        if self.__downcase_first_letter('pixelAspectRatio') in path:
            path = path.replace('{' + self.__downcase_first_letter('pixelAspectRatio' + '}'), request.pixel_aspect_ratio if request.pixel_aspect_ratio is not None else '')
        else:
            if request.pixel_aspect_ratio is not None:
                query_params.append((self.__downcase_first_letter('pixelAspectRatio'), request.pixel_aspect_ratio))  # noqa: E501
        if self.__downcase_first_letter('fromScratch') in path:
            path = path.replace('{' + self.__downcase_first_letter('fromScratch' + '}'), request.from_scratch if request.from_scratch is not None else '')
        else:
            if request.from_scratch is not None:
                query_params.append((self.__downcase_first_letter('fromScratch'), request.from_scratch))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_image_jpeg2000(self, request, **kwargs):  # noqa: E501
        """Update parameters of JPEG2000 image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_jpeg2000_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_image_jpeg2000_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_jpeg2000_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_image_jpeg2000_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_jpeg2000_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_image_jpeg2000_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update parameters of JPEG2000 image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_jpeg2000_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_image_jpeg2000" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'image_data' is set
        if request.image_data is None:
            raise ValueError("Missing the required parameter `image_data` when calling `post_image_jpeg2000`")  # noqa: E501
        # verify the required parameter 'comment' is set
        if request.comment is None:
            raise ValueError("Missing the required parameter `comment` when calling `post_image_jpeg2000`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/jpg2000'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('comment') in path:
            path = path.replace('{' + self.__downcase_first_letter('comment' + '}'), request.comment if request.comment is not None else '')
        else:
            if request.comment is not None:
                query_params.append((self.__downcase_first_letter('comment'), request.comment))  # noqa: E501
        if self.__downcase_first_letter('codec') in path:
            path = path.replace('{' + self.__downcase_first_letter('codec' + '}'), request.codec if request.codec is not None else '')
        else:
            if request.codec is not None:
                query_params.append((self.__downcase_first_letter('codec'), request.codec))  # noqa: E501
        if self.__downcase_first_letter('fromScratch') in path:
            path = path.replace('{' + self.__downcase_first_letter('fromScratch' + '}'), request.from_scratch if request.from_scratch is not None else '')
        else:
            if request.from_scratch is not None:
                query_params.append((self.__downcase_first_letter('fromScratch'), request.from_scratch))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_image_jpg(self, request, **kwargs):  # noqa: E501
        """Update parameters of JPEG image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_jpg_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_image_jpg_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_jpg_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_image_jpg_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_jpg_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_image_jpg_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update parameters of JPEG image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_jpg_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_image_jpg" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'image_data' is set
        if request.image_data is None:
            raise ValueError("Missing the required parameter `image_data` when calling `post_image_jpg`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/jpg'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('quality') in path:
            path = path.replace('{' + self.__downcase_first_letter('quality' + '}'), request.quality if request.quality is not None else '')
        else:
            if request.quality is not None:
                query_params.append((self.__downcase_first_letter('quality'), request.quality))  # noqa: E501
        if self.__downcase_first_letter('compressionType') in path:
            path = path.replace('{' + self.__downcase_first_letter('compressionType' + '}'), request.compression_type if request.compression_type is not None else '')
        else:
            if request.compression_type is not None:
                query_params.append((self.__downcase_first_letter('compressionType'), request.compression_type))  # noqa: E501
        if self.__downcase_first_letter('fromScratch') in path:
            path = path.replace('{' + self.__downcase_first_letter('fromScratch' + '}'), request.from_scratch if request.from_scratch is not None else '')
        else:
            if request.from_scratch is not None:
                query_params.append((self.__downcase_first_letter('fromScratch'), request.from_scratch))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_image_properties(self, request, **kwargs):  # noqa: E501
        """Get properties of an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_properties_request object with parameters
        :return: ImagingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_image_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_image_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_image_properties_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get properties of an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_properties_request object with parameters
        :return: ImagingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_image_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'image_data' is set
        if request.image_data is None:
            raise ValueError("Missing the required parameter `image_data` when calling `post_image_properties`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/properties'
        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ImagingResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_image_psd(self, request, **kwargs):  # noqa: E501
        """Update parameters of PSD image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_psd_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_image_psd_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_psd_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_image_psd_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_psd_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_image_psd_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update parameters of PSD image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_psd_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_image_psd" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'image_data' is set
        if request.image_data is None:
            raise ValueError("Missing the required parameter `image_data` when calling `post_image_psd`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/psd'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('channelsCount') in path:
            path = path.replace('{' + self.__downcase_first_letter('channelsCount' + '}'), request.channels_count if request.channels_count is not None else '')
        else:
            if request.channels_count is not None:
                query_params.append((self.__downcase_first_letter('channelsCount'), request.channels_count))  # noqa: E501
        if self.__downcase_first_letter('compressionMethod') in path:
            path = path.replace('{' + self.__downcase_first_letter('compressionMethod' + '}'), request.compression_method if request.compression_method is not None else '')
        else:
            if request.compression_method is not None:
                query_params.append((self.__downcase_first_letter('compressionMethod'), request.compression_method))  # noqa: E501
        if self.__downcase_first_letter('fromScratch') in path:
            path = path.replace('{' + self.__downcase_first_letter('fromScratch' + '}'), request.from_scratch if request.from_scratch is not None else '')
        else:
            if request.from_scratch is not None:
                query_params.append((self.__downcase_first_letter('fromScratch'), request.from_scratch))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_image_resize(self, request, **kwargs):  # noqa: E501
        """Resize an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_resize_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_image_resize_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_resize_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_image_resize_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_resize_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_image_resize_with_http_info(self, request, **kwargs):  # noqa: E501
        """Resize an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_resize_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_image_resize" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'image_data' is set
        if request.image_data is None:
            raise ValueError("Missing the required parameter `image_data` when calling `post_image_resize`")  # noqa: E501
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `post_image_resize`")  # noqa: E501
        # verify the required parameter 'new_width' is set
        if request.new_width is None:
            raise ValueError("Missing the required parameter `new_width` when calling `post_image_resize`")  # noqa: E501
        # verify the required parameter 'new_height' is set
        if request.new_height is None:
            raise ValueError("Missing the required parameter `new_height` when calling `post_image_resize`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/resize'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('format') in path:
            path = path.replace('{' + self.__downcase_first_letter('format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('newWidth') in path:
            path = path.replace('{' + self.__downcase_first_letter('newWidth' + '}'), request.new_width if request.new_width is not None else '')
        else:
            if request.new_width is not None:
                query_params.append((self.__downcase_first_letter('newWidth'), request.new_width))  # noqa: E501
        if self.__downcase_first_letter('newHeight') in path:
            path = path.replace('{' + self.__downcase_first_letter('newHeight' + '}'), request.new_height if request.new_height is not None else '')
        else:
            if request.new_height is not None:
                query_params.append((self.__downcase_first_letter('newHeight'), request.new_height))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_image_rotate_flip(self, request, **kwargs):  # noqa: E501
        """Rotate and/or flip an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_rotate_flip_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_image_rotate_flip_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_rotate_flip_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_image_rotate_flip_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_rotate_flip_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_image_rotate_flip_with_http_info(self, request, **kwargs):  # noqa: E501
        """Rotate and/or flip an image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_rotate_flip_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_image_rotate_flip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'image_data' is set
        if request.image_data is None:
            raise ValueError("Missing the required parameter `image_data` when calling `post_image_rotate_flip`")  # noqa: E501
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `post_image_rotate_flip`")  # noqa: E501
        # verify the required parameter 'method' is set
        if request.method is None:
            raise ValueError("Missing the required parameter `method` when calling `post_image_rotate_flip`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/rotateflip'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('format') in path:
            path = path.replace('{' + self.__downcase_first_letter('format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('method') in path:
            path = path.replace('{' + self.__downcase_first_letter('method' + '}'), request.method if request.method is not None else '')
        else:
            if request.method is not None:
                query_params.append((self.__downcase_first_letter('method'), request.method))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_image_save_as(self, request, **kwargs):  # noqa: E501
        """Export existing image to another format. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.               # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_save_as_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_image_save_as_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_save_as_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_image_save_as_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_save_as_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_image_save_as_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export existing image to another format. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.               # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_save_as_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_image_save_as" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'image_data' is set
        if request.image_data is None:
            raise ValueError("Missing the required parameter `image_data` when calling `post_image_save_as`")  # noqa: E501
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `post_image_save_as`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/saveAs'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('format') in path:
            path = path.replace('{' + self.__downcase_first_letter('format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_image_tiff(self, request, **kwargs):  # noqa: E501
        """Update parameters of TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_tiff_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_image_tiff_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_tiff_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_image_tiff_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_tiff_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_image_tiff_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update parameters of TIFF image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_tiff_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_image_tiff" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'image_data' is set
        if request.image_data is None:
            raise ValueError("Missing the required parameter `image_data` when calling `post_image_tiff`")  # noqa: E501
        # verify the required parameter 'bit_depth' is set
        if request.bit_depth is None:
            raise ValueError("Missing the required parameter `bit_depth` when calling `post_image_tiff`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/tiff'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('bitDepth') in path:
            path = path.replace('{' + self.__downcase_first_letter('bitDepth' + '}'), request.bit_depth if request.bit_depth is not None else '')
        else:
            if request.bit_depth is not None:
                query_params.append((self.__downcase_first_letter('bitDepth'), request.bit_depth))  # noqa: E501
        if self.__downcase_first_letter('fromScratch') in path:
            path = path.replace('{' + self.__downcase_first_letter('fromScratch' + '}'), request.from_scratch if request.from_scratch is not None else '')
        else:
            if request.from_scratch is not None:
                query_params.append((self.__downcase_first_letter('fromScratch'), request.from_scratch))  # noqa: E501
        if self.__downcase_first_letter('compression') in path:
            path = path.replace('{' + self.__downcase_first_letter('compression' + '}'), request.compression if request.compression is not None else '')
        else:
            if request.compression is not None:
                query_params.append((self.__downcase_first_letter('compression'), request.compression))  # noqa: E501
        if self.__downcase_first_letter('resolutionUnit') in path:
            path = path.replace('{' + self.__downcase_first_letter('resolutionUnit' + '}'), request.resolution_unit if request.resolution_unit is not None else '')
        else:
            if request.resolution_unit is not None:
                query_params.append((self.__downcase_first_letter('resolutionUnit'), request.resolution_unit))  # noqa: E501
        if self.__downcase_first_letter('horizontalResolution') in path:
            path = path.replace('{' + self.__downcase_first_letter('horizontalResolution' + '}'), request.horizontal_resolution if request.horizontal_resolution is not None else '')
        else:
            if request.horizontal_resolution is not None:
                query_params.append((self.__downcase_first_letter('horizontalResolution'), request.horizontal_resolution))  # noqa: E501
        if self.__downcase_first_letter('verticalResolution') in path:
            path = path.replace('{' + self.__downcase_first_letter('verticalResolution' + '}'), request.vertical_resolution if request.vertical_resolution is not None else '')
        else:
            if request.vertical_resolution is not None:
                query_params.append((self.__downcase_first_letter('verticalResolution'), request.vertical_resolution))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_image_update(self, request, **kwargs):  # noqa: E501
        """Perform scaling, cropping and flipping of an image in a single request. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_update_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_image_update_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_update_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_image_update_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_update_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_image_update_with_http_info(self, request, **kwargs):  # noqa: E501
        """Perform scaling, cropping and flipping of an image in a single request. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_update_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_image_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'image_data' is set
        if request.image_data is None:
            raise ValueError("Missing the required parameter `image_data` when calling `post_image_update`")  # noqa: E501
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `post_image_update`")  # noqa: E501
        # verify the required parameter 'new_width' is set
        if request.new_width is None:
            raise ValueError("Missing the required parameter `new_width` when calling `post_image_update`")  # noqa: E501
        # verify the required parameter 'new_height' is set
        if request.new_height is None:
            raise ValueError("Missing the required parameter `new_height` when calling `post_image_update`")  # noqa: E501
        # verify the required parameter 'x' is set
        if request.x is None:
            raise ValueError("Missing the required parameter `x` when calling `post_image_update`")  # noqa: E501
        # verify the required parameter 'y' is set
        if request.y is None:
            raise ValueError("Missing the required parameter `y` when calling `post_image_update`")  # noqa: E501
        # verify the required parameter 'rect_width' is set
        if request.rect_width is None:
            raise ValueError("Missing the required parameter `rect_width` when calling `post_image_update`")  # noqa: E501
        # verify the required parameter 'rect_height' is set
        if request.rect_height is None:
            raise ValueError("Missing the required parameter `rect_height` when calling `post_image_update`")  # noqa: E501
        # verify the required parameter 'rotate_flip_method' is set
        if request.rotate_flip_method is None:
            raise ValueError("Missing the required parameter `rotate_flip_method` when calling `post_image_update`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/updateImage'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('format') in path:
            path = path.replace('{' + self.__downcase_first_letter('format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('format'), request.format))  # noqa: E501
        if self.__downcase_first_letter('newWidth') in path:
            path = path.replace('{' + self.__downcase_first_letter('newWidth' + '}'), request.new_width if request.new_width is not None else '')
        else:
            if request.new_width is not None:
                query_params.append((self.__downcase_first_letter('newWidth'), request.new_width))  # noqa: E501
        if self.__downcase_first_letter('newHeight') in path:
            path = path.replace('{' + self.__downcase_first_letter('newHeight' + '}'), request.new_height if request.new_height is not None else '')
        else:
            if request.new_height is not None:
                query_params.append((self.__downcase_first_letter('newHeight'), request.new_height))  # noqa: E501
        if self.__downcase_first_letter('x') in path:
            path = path.replace('{' + self.__downcase_first_letter('x' + '}'), request.x if request.x is not None else '')
        else:
            if request.x is not None:
                query_params.append((self.__downcase_first_letter('x'), request.x))  # noqa: E501
        if self.__downcase_first_letter('y') in path:
            path = path.replace('{' + self.__downcase_first_letter('y' + '}'), request.y if request.y is not None else '')
        else:
            if request.y is not None:
                query_params.append((self.__downcase_first_letter('y'), request.y))  # noqa: E501
        if self.__downcase_first_letter('rectWidth') in path:
            path = path.replace('{' + self.__downcase_first_letter('rectWidth' + '}'), request.rect_width if request.rect_width is not None else '')
        else:
            if request.rect_width is not None:
                query_params.append((self.__downcase_first_letter('rectWidth'), request.rect_width))  # noqa: E501
        if self.__downcase_first_letter('rectHeight') in path:
            path = path.replace('{' + self.__downcase_first_letter('rectHeight' + '}'), request.rect_height if request.rect_height is not None else '')
        else:
            if request.rect_height is not None:
                query_params.append((self.__downcase_first_letter('rectHeight'), request.rect_height))  # noqa: E501
        if self.__downcase_first_letter('rotateFlipMethod') in path:
            path = path.replace('{' + self.__downcase_first_letter('rotateFlipMethod' + '}'), request.rotate_flip_method if request.rotate_flip_method is not None else '')
        else:
            if request.rotate_flip_method is not None:
                query_params.append((self.__downcase_first_letter('rotateFlipMethod'), request.rotate_flip_method))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_image_web_p(self, request, **kwargs):  # noqa: E501
        """Update parameters of WEBP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_web_p_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_image_web_p_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_web_p_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_image_web_p_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_web_p_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_image_web_p_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update parameters of WEBP image. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_web_p_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_image_web_p" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'image_data' is set
        if request.image_data is None:
            raise ValueError("Missing the required parameter `image_data` when calling `post_image_web_p`")  # noqa: E501
        # verify the required parameter 'loss_less' is set
        if request.loss_less is None:
            raise ValueError("Missing the required parameter `loss_less` when calling `post_image_web_p`")  # noqa: E501
        # verify the required parameter 'quality' is set
        if request.quality is None:
            raise ValueError("Missing the required parameter `quality` when calling `post_image_web_p`")  # noqa: E501
        # verify the required parameter 'anim_loop_count' is set
        if request.anim_loop_count is None:
            raise ValueError("Missing the required parameter `anim_loop_count` when calling `post_image_web_p`")  # noqa: E501
        # verify the required parameter 'anim_background_color' is set
        if request.anim_background_color is None:
            raise ValueError("Missing the required parameter `anim_background_color` when calling `post_image_web_p`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/webp'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('lossLess') in path:
            path = path.replace('{' + self.__downcase_first_letter('lossLess' + '}'), request.loss_less if request.loss_less is not None else '')
        else:
            if request.loss_less is not None:
                query_params.append((self.__downcase_first_letter('lossLess'), request.loss_less))  # noqa: E501
        if self.__downcase_first_letter('quality') in path:
            path = path.replace('{' + self.__downcase_first_letter('quality' + '}'), request.quality if request.quality is not None else '')
        else:
            if request.quality is not None:
                query_params.append((self.__downcase_first_letter('quality'), request.quality))  # noqa: E501
        if self.__downcase_first_letter('animLoopCount') in path:
            path = path.replace('{' + self.__downcase_first_letter('animLoopCount' + '}'), request.anim_loop_count if request.anim_loop_count is not None else '')
        else:
            if request.anim_loop_count is not None:
                query_params.append((self.__downcase_first_letter('animLoopCount'), request.anim_loop_count))  # noqa: E501
        if self.__downcase_first_letter('animBackgroundColor') in path:
            path = path.replace('{' + self.__downcase_first_letter('animBackgroundColor' + '}'), request.anim_background_color if request.anim_background_color is not None else '')
        else:
            if request.anim_background_color is not None:
                query_params.append((self.__downcase_first_letter('animBackgroundColor'), request.anim_background_color))  # noqa: E501
        if self.__downcase_first_letter('fromScratch') in path:
            path = path.replace('{' + self.__downcase_first_letter('fromScratch' + '}'), request.from_scratch if request.from_scratch is not None else '')
        else:
            if request.from_scratch is not None:
                query_params.append((self.__downcase_first_letter('fromScratch'), request.from_scratch))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_image_wmf(self, request, **kwargs):  # noqa: E501
        """Process existing WMF image using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_wmf_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_image_wmf_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_wmf_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_image_wmf_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_image_wmf_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_image_wmf_with_http_info(self, request, **kwargs):  # noqa: E501
        """Process existing WMF image using given parameters. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_image_wmf_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_image_wmf" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'image_data' is set
        if request.image_data is None:
            raise ValueError("Missing the required parameter `image_data` when calling `post_image_wmf`")  # noqa: E501
        # verify the required parameter 'bk_color' is set
        if request.bk_color is None:
            raise ValueError("Missing the required parameter `bk_color` when calling `post_image_wmf`")  # noqa: E501
        # verify the required parameter 'page_width' is set
        if request.page_width is None:
            raise ValueError("Missing the required parameter `page_width` when calling `post_image_wmf`")  # noqa: E501
        # verify the required parameter 'page_height' is set
        if request.page_height is None:
            raise ValueError("Missing the required parameter `page_height` when calling `post_image_wmf`")  # noqa: E501
        # verify the required parameter 'border_x' is set
        if request.border_x is None:
            raise ValueError("Missing the required parameter `border_x` when calling `post_image_wmf`")  # noqa: E501
        # verify the required parameter 'border_y' is set
        if request.border_y is None:
            raise ValueError("Missing the required parameter `border_y` when calling `post_image_wmf`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/wmf'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('bkColor') in path:
            path = path.replace('{' + self.__downcase_first_letter('bkColor' + '}'), request.bk_color if request.bk_color is not None else '')
        else:
            if request.bk_color is not None:
                query_params.append((self.__downcase_first_letter('bkColor'), request.bk_color))  # noqa: E501
        if self.__downcase_first_letter('pageWidth') in path:
            path = path.replace('{' + self.__downcase_first_letter('pageWidth' + '}'), request.page_width if request.page_width is not None else '')
        else:
            if request.page_width is not None:
                query_params.append((self.__downcase_first_letter('pageWidth'), request.page_width))  # noqa: E501
        if self.__downcase_first_letter('pageHeight') in path:
            path = path.replace('{' + self.__downcase_first_letter('pageHeight' + '}'), request.page_height if request.page_height is not None else '')
        else:
            if request.page_height is not None:
                query_params.append((self.__downcase_first_letter('pageHeight'), request.page_height))  # noqa: E501
        if self.__downcase_first_letter('borderX') in path:
            path = path.replace('{' + self.__downcase_first_letter('borderX' + '}'), request.border_x if request.border_x is not None else '')
        else:
            if request.border_x is not None:
                query_params.append((self.__downcase_first_letter('borderX'), request.border_x))  # noqa: E501
        if self.__downcase_first_letter('borderY') in path:
            path = path.replace('{' + self.__downcase_first_letter('borderY' + '}'), request.border_y if request.border_y is not None else '')
        else:
            if request.border_y is not None:
                query_params.append((self.__downcase_first_letter('borderY'), request.border_y))  # noqa: E501
        if self.__downcase_first_letter('fromScratch') in path:
            path = path.replace('{' + self.__downcase_first_letter('fromScratch' + '}'), request.from_scratch if request.from_scratch is not None else '')
        else:
            if request.from_scratch is not None:
                query_params.append((self.__downcase_first_letter('fromScratch'), request.from_scratch))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('format') in path:
            path = path.replace('{' + self.__downcase_first_letter('format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('format'), request.format))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_search_context_add_image(self, request, **kwargs):  # noqa: E501
        """Add image and images features to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_search_context_add_image_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_search_context_add_image_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_search_context_add_image_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_search_context_add_image_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_search_context_add_image_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_search_context_add_image_with_http_info(self, request, **kwargs):  # noqa: E501
        """Add image and images features to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_search_context_add_image_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_search_context_add_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_context_id' is set
        if request.search_context_id is None:
            raise ValueError("Missing the required parameter `search_context_id` when calling `post_search_context_add_image`")  # noqa: E501
        # verify the required parameter 'image_id' is set
        if request.image_id is None:
            raise ValueError("Missing the required parameter `image_id` when calling `post_search_context_add_image`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/ai/imageSearch/{searchContextId}/image'
        path_params = {}
        if request.search_context_id is not None:
            path_params[self.__downcase_first_letter('searchContextId')] = request.search_context_id  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('imageId') in path:
            path = path.replace('{' + self.__downcase_first_letter('imageId' + '}'), request.image_id if request.image_id is not None else '')
        else:
            if request.image_id is not None:
                query_params.append((self.__downcase_first_letter('imageId'), request.image_id))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_search_context_add_tag(self, request, **kwargs):  # noqa: E501
        """Add tag and reference image to search context. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_search_context_add_tag_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_search_context_add_tag_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_search_context_add_tag_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_search_context_add_tag_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_search_context_add_tag_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_search_context_add_tag_with_http_info(self, request, **kwargs):  # noqa: E501
        """Add tag and reference image to search context. Image data is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_search_context_add_tag_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_search_context_add_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'image_data' is set
        if request.image_data is None:
            raise ValueError("Missing the required parameter `image_data` when calling `post_search_context_add_tag`")  # noqa: E501
        # verify the required parameter 'search_context_id' is set
        if request.search_context_id is None:
            raise ValueError("Missing the required parameter `search_context_id` when calling `post_search_context_add_tag`")  # noqa: E501
        # verify the required parameter 'tag_name' is set
        if request.tag_name is None:
            raise ValueError("Missing the required parameter `tag_name` when calling `post_search_context_add_tag`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/ai/imageSearch/{searchContextId}/addTag'
        path_params = {}
        if request.search_context_id is not None:
            path_params[self.__downcase_first_letter('searchContextId')] = request.search_context_id  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('tagName') in path:
            path = path.replace('{' + self.__downcase_first_letter('tagName' + '}'), request.tag_name if request.tag_name is not None else '')
        else:
            if request.tag_name is not None:
                query_params.append((self.__downcase_first_letter('tagName'), request.tag_name))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_search_context_compare_images(self, request, **kwargs):  # noqa: E501
        """Compare two images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_search_context_compare_images_request object with parameters
        :return: SearchResultsSet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_search_context_compare_images_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_search_context_compare_images_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_search_context_compare_images_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_search_context_compare_images_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_search_context_compare_images_with_http_info(self, request, **kwargs):  # noqa: E501
        """Compare two images. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_search_context_compare_images_request object with parameters
        :return: SearchResultsSet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_search_context_compare_images" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_context_id' is set
        if request.search_context_id is None:
            raise ValueError("Missing the required parameter `search_context_id` when calling `post_search_context_compare_images`")  # noqa: E501
        # verify the required parameter 'image_id1' is set
        if request.image_id1 is None:
            raise ValueError("Missing the required parameter `image_id1` when calling `post_search_context_compare_images`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/ai/imageSearch/{searchContextId}/compare'
        path_params = {}
        if request.search_context_id is not None:
            path_params[self.__downcase_first_letter('searchContextId')] = request.search_context_id  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('imageId1') in path:
            path = path.replace('{' + self.__downcase_first_letter('imageId1' + '}'), request.image_id1 if request.image_id1 is not None else '')
        else:
            if request.image_id1 is not None:
                query_params.append((self.__downcase_first_letter('imageId1'), request.image_id1))  # noqa: E501
        if self.__downcase_first_letter('imageId2') in path:
            path = path.replace('{' + self.__downcase_first_letter('imageId2' + '}'), request.image_id2 if request.image_id2 is not None else '')
        else:
            if request.image_id2 is not None:
                query_params.append((self.__downcase_first_letter('imageId2'), request.image_id2))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchResultsSet',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_search_context_extract_image_features(self, request, **kwargs):  # noqa: E501
        """Extract images features and add them to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_search_context_extract_image_features_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_search_context_extract_image_features_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_search_context_extract_image_features_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_search_context_extract_image_features_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_search_context_extract_image_features_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_search_context_extract_image_features_with_http_info(self, request, **kwargs):  # noqa: E501
        """Extract images features and add them to search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_search_context_extract_image_features_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_search_context_extract_image_features" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_context_id' is set
        if request.search_context_id is None:
            raise ValueError("Missing the required parameter `search_context_id` when calling `post_search_context_extract_image_features`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/ai/imageSearch/{searchContextId}/features'
        path_params = {}
        if request.search_context_id is not None:
            path_params[self.__downcase_first_letter('searchContextId')] = request.search_context_id  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('imageId') in path:
            path = path.replace('{' + self.__downcase_first_letter('imageId' + '}'), request.image_id if request.image_id is not None else '')
        else:
            if request.image_id is not None:
                query_params.append((self.__downcase_first_letter('imageId'), request.image_id))  # noqa: E501
        if self.__downcase_first_letter('imagesFolder') in path:
            path = path.replace('{' + self.__downcase_first_letter('imagesFolder' + '}'), request.images_folder if request.images_folder is not None else '')
        else:
            if request.images_folder is not None:
                query_params.append((self.__downcase_first_letter('imagesFolder'), request.images_folder))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_search_context_find_by_tags(self, request, **kwargs):  # noqa: E501
        """Find images by tags. Tags JSON string is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_search_context_find_by_tags_request object with parameters
        :return: SearchResultsSet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_search_context_find_by_tags_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_search_context_find_by_tags_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_search_context_find_by_tags_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_search_context_find_by_tags_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_search_context_find_by_tags_with_http_info(self, request, **kwargs):  # noqa: E501
        """Find images by tags. Tags JSON string is passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_search_context_find_by_tags_request object with parameters
        :return: SearchResultsSet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_search_context_find_by_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tags' is set
        if request.tags is None:
            raise ValueError("Missing the required parameter `tags` when calling `post_search_context_find_by_tags`")  # noqa: E501
        # verify the required parameter 'search_context_id' is set
        if request.search_context_id is None:
            raise ValueError("Missing the required parameter `search_context_id` when calling `post_search_context_find_by_tags`")  # noqa: E501
        # verify the required parameter 'similarity_threshold' is set
        if request.similarity_threshold is None:
            raise ValueError("Missing the required parameter `similarity_threshold` when calling `post_search_context_find_by_tags`")  # noqa: E501
        # verify the required parameter 'max_count' is set
        if request.max_count is None:
            raise ValueError("Missing the required parameter `max_count` when calling `post_search_context_find_by_tags`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/ai/imageSearch/{searchContextId}/findByTags'
        path_params = {}
        if request.search_context_id is not None:
            path_params[self.__downcase_first_letter('searchContextId')] = request.search_context_id  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('similarityThreshold') in path:
            path = path.replace('{' + self.__downcase_first_letter('similarityThreshold' + '}'), request.similarity_threshold if request.similarity_threshold is not None else '')
        else:
            if request.similarity_threshold is not None:
                query_params.append((self.__downcase_first_letter('similarityThreshold'), request.similarity_threshold))  # noqa: E501
        if self.__downcase_first_letter('maxCount') in path:
            path = path.replace('{' + self.__downcase_first_letter('maxCount' + '}'), request.max_count if request.max_count is not None else '')
        else:
            if request.max_count is not None:
                query_params.append((self.__downcase_first_letter('maxCount'), request.max_count))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.tags is not None:
            form_params.append((self.__downcase_first_letter('tags'), request.tags))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchResultsSet',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_tiff_append(self, request, **kwargs):  # noqa: E501
        """Appends existing TIFF image to another existing TIFF image (i.e. merges TIFF images).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_tiff_append_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_tiff_append_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_tiff_append_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_tiff_append_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_tiff_append_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_tiff_append_with_http_info(self, request, **kwargs):  # noqa: E501
        """Appends existing TIFF image to another existing TIFF image (i.e. merges TIFF images).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_tiff_append_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_tiff_append" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_tiff_append`")  # noqa: E501
        # verify the required parameter 'append_file' is set
        if request.append_file is None:
            raise ValueError("Missing the required parameter `append_file` when calling `post_tiff_append`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/tiff/{name}/appendTiff'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('appendFile') in path:
            path = path.replace('{' + self.__downcase_first_letter('appendFile' + '}'), request.append_file if request.append_file is not None else '')
        else:
            if request.append_file is not None:
                query_params.append((self.__downcase_first_letter('appendFile'), request.append_file))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_search_context_image(self, request, **kwargs):  # noqa: E501
        """Update image and images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_search_context_image_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_search_context_image_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_search_context_image_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_search_context_image_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_search_context_image_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def put_search_context_image_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update image and images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_search_context_image_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_search_context_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_context_id' is set
        if request.search_context_id is None:
            raise ValueError("Missing the required parameter `search_context_id` when calling `put_search_context_image`")  # noqa: E501
        # verify the required parameter 'image_id' is set
        if request.image_id is None:
            raise ValueError("Missing the required parameter `image_id` when calling `put_search_context_image`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/ai/imageSearch/{searchContextId}/image'
        path_params = {}
        if request.search_context_id is not None:
            path_params[self.__downcase_first_letter('searchContextId')] = request.search_context_id  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('imageId') in path:
            path = path.replace('{' + self.__downcase_first_letter('imageId' + '}'), request.image_id if request.image_id is not None else '')
        else:
            if request.image_id is not None:
                query_params.append((self.__downcase_first_letter('imageId'), request.image_id))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_search_context_image_features(self, request, **kwargs):  # noqa: E501
        """Update images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_search_context_image_features_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_search_context_image_features_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_search_context_image_features_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_search_context_image_features_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_search_context_image_features_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def put_search_context_image_features_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update images features in search context. Image data may be passed as zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_search_context_image_features_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_search_context_image_features" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_context_id' is set
        if request.search_context_id is None:
            raise ValueError("Missing the required parameter `search_context_id` when calling `put_search_context_image_features`")  # noqa: E501
        # verify the required parameter 'image_id' is set
        if request.image_id is None:
            raise ValueError("Missing the required parameter `image_id` when calling `put_search_context_image_features`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/ai/imageSearch/{searchContextId}/features'
        path_params = {}
        if request.search_context_id is not None:
            path_params[self.__downcase_first_letter('searchContextId')] = request.search_context_id  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('imageId') in path:
            path = path.replace('{' + self.__downcase_first_letter('imageId' + '}'), request.image_id if request.image_id is not None else '')
        else:
            if request.image_id is not None:
                query_params.append((self.__downcase_first_letter('imageId'), request.image_id))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.image_data is not None:
            local_var_files.append((self.__downcase_first_letter('imageData'), request.image_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def storage_exists(self, request, **kwargs):  # noqa: E501
        """Check if storage exists  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request storage_exists_request object with parameters
        :return: StorageExist
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.storage_exists_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.storage_exists_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.storage_exists_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.storage_exists_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def storage_exists_with_http_info(self, request, **kwargs):  # noqa: E501
        """Check if storage exists  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request storage_exists_request object with parameters
        :return: StorageExist
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method storage_exists" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'storage_name' is set
        if request.storage_name is None:
            raise ValueError("Missing the required parameter `storage_name` when calling `storage_exists`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/storage/{storageName}/exist'
        path_params = {}
        if request.storage_name is not None:
            path_params[self.__downcase_first_letter('storageName')] = request.storage_name  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StorageExist',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upload_file(self, request, **kwargs):  # noqa: E501
        """Upload file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request upload_file_request object with parameters
        :return: FilesUploadResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.upload_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.upload_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.upload_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.upload_file_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def upload_file_with_http_info(self, request, **kwargs):  # noqa: E501
        """Upload file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request upload_file_request object with parameters
        :return: FilesUploadResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if request.path is None:
            raise ValueError("Missing the required parameter `path` when calling `upload_file`")  # noqa: E501
        # verify the required parameter 'file' is set
        if request.file is None:
            raise ValueError("Missing the required parameter `file` when calling `upload_file`")  # noqa: E501

        collection_formats = {}
        path = '/imaging/storage/file/{path}'
        path_params = {}
        if request.path is not None:
            path_params[self.__downcase_first_letter('path')] = request.path  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('storageName') in path:
            path = path.replace('{' + self.__downcase_first_letter('storageName' + '}'), request.storage_name if request.storage_name is not None else '')
        else:
            if request.storage_name is not None:
                query_params.append((self.__downcase_first_letter('storageName'), request.storage_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.file is not None:
            local_var_files.append((self.__downcase_first_letter('File'), request.file))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT'] # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilesUploadResult',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    # Helper method to convert first letter to downcase
    def __downcase_first_letter(self, s):
        if len(s) == 0:
            return s
        else:
            return s[0].lower() + s[1:]

    def __request_token(self):
        config = self.api_client.configuration
        request_url = "/connect/token"
        form_params = [('grant_type', 'client_credentials'), ('client_id', config.api_key['app_sid']),
                       ('client_secret', config.api_key['api_key'])]

        header_params = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

        api_version = self.api_client.configuration.api_version
        self.api_client.configuration.api_version = ''

        data = self.api_client.call_api(request_url, 'POST',
                                        {},
                                        [],
                                        header_params,
                                        post_params=form_params,
                                        response_type='object',
                                        files={}, _return_http_data_only=True)
        access_token = data['access_token'] if six.PY3 else data['access_token'].encode('utf8')
        self.api_client.configuration.access_token = access_token

        self.api_client.configuration.api_version = api_version

