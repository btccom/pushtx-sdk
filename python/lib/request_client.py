#!/usr/bin/env python
# coding: utf-8

# The MIT License (MIT)
#
# Copyright (c) 2016 BTC.COM
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from abc import abstractmethod, abstractproperty

import requests

class HttpClient(object):
    """Abstract Base Classes of HttpClient."""
    DEFAULT_TIMEOUT = 5

    def __init__(self, timeout=DEFAULT_TIMEOUT):
        """__init__ method.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`DEFAULT_TIMEOUT`
        :type timeout: float | tuple(float, float)
        :rtype: T <= :py:class:`HttpResponse`
        :return: HttpResponse instance
        """
        self.timeout = timeout

    @abstractmethod
    def get(self, url, headers=None, params=None, stream=False, timeout=None):
        """GET request.
        :param str url: Request url
        :param dict headers: (optional) Request headers
        :param dict params: (optional) Request query parameter
        :param bool stream: (optional) get content as stream
        :param timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`self.timeout`
        :type timeout: float | tuple(float, float)
        :rtype: T <= :py:class:`HttpResponse`
        :return: HttpResponse instance
        """
        raise NotImplementedError

    @abstractmethod
    def post(self, url, headers=None, data=None, timeout=None):
        """POST request.
        :param str url: Request url
        :param dict headers: (optional) Request headers
        :param data: (optional) Dictionary, bytes, or file-like object to send in the body
        :param timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`self.timeout`
        :type timeout: float | tuple(float, float)
        :rtype: T <= :py:class:`HttpResponse`
        :return: HttpResponse instance
        """
        raise NotImplementedError


class RequestsHttpClient(HttpClient):
    """HttpClient implemented by requests."""

    def __init__(self, timeout=HttpClient.DEFAULT_TIMEOUT):
        """__init__ method.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`DEFAULT_TIMEOUT`
        :type timeout: float | tuple(float, float)
        """
        super(RequestsHttpClient, self).__init__(timeout)

    def get(self, url, headers=None, params=None, stream=False, timeout=None):
        """GET request.
        :param str url: Request url
        :param dict headers: (optional) Request headers
        :param dict params: (optional) Request query parameter
        :param bool stream: (optional) get content as stream
        :param timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`self.timeout`
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`RequestsHttpResponse`
        :return: RequestsHttpResponse instance
        """
        if timeout is None:
            timeout = self.timeout

        response = requests.get(
            url, headers=headers, params=params, stream=stream, timeout=timeout
        )

        return RequestsHttpResponse(response)

    def post(self, url, headers=None, data=None, timeout=None):
        """POST request.
        :param str url: Request url
        :param dict headers: (optional) Request headers
        :param data: (optional) Dictionary, bytes, or file-like object to send in the body
        :param timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`self.timeout`
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`RequestsHttpResponse`
        :return: RequestsHttpResponse instance
        """
        if timeout is None:
            timeout = self.timeout
        response = requests.post(
            url, headers=headers, json=data, timeout=timeout
        )
        return RequestsHttpResponse(response)


class HttpResponse():
    """HttpResponse."""

    @abstractproperty
    def status_code(self):
        """Get status code."""
        raise NotImplementedError

    @abstractproperty
    def headers(self):
        """Get headers."""
        raise NotImplementedError

    @abstractproperty
    def text(self):
        """Get request body as text-decoded."""
        raise NotImplementedError

    @abstractproperty
    def content(self):
        """Get request body as binary."""
        raise NotImplementedError

    @abstractproperty
    def json(self):
        """Get request body as json-decoded."""
        raise NotImplementedError

    @abstractmethod
    def iter_content(self, chunk_size=1024, decode_unicode=False):
        """Get request body as iterator content (stream).
        :param int chunk_size:
        :param bool decode_unicode:
        """
        raise NotImplementedError


class RequestsHttpResponse(HttpResponse):
    """HttpResponse implemented by requests lib's response."""

    def __init__(self, response):
        """__init__ method.
        :param response: requests lib's response
        """
        self.response = response

    @property
    def status_code(self):
        """Get status code."""
        return self.response.status_code

    @property
    def headers(self):
        """Get headers."""
        return self.response.headers

    @property
    def text(self):
        """Get request body as text-decoded."""
        return self.response.text

    @property
    def content(self):
        """Get request body as binary."""
        return self.response.content

    @property
    def json(self):
        """Get request body as json-decoded."""
        return self.response.json()

    def iter_content(self, chunk_size=1024, decode_unicode=False):
        """Get request body as iterator content (stream).
        :param int chunk_size:
        :param bool decode_unicode:
        """
        return self.response.iter_content(chunk_size=chunk_size, decode_unicode=decode_unicode)