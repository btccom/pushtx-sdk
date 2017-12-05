#!/usr/bin/env python
# coding: utf-8

# The MIT License (MIT)
#
# Copyright (c) 2016 Frederic Guillot
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
from lib.error import PushtxError
from lib.request_client import RequestsHttpClient


class Client(object):
    DEFAULT_BASE_URL = 'https://pushtx.btc.com/api'

    def __init__(self, endpoint=DEFAULT_BASE_URL, http_client=RequestsHttpClient):
        self.endpoint = endpoint
        self.headers = {}
        if http_client:
            self.http_client = http_client()
        else:
            self.http_client = RequestsHttpClient()

    def _get(self, path, params=None, stream=False, timeout=None):
        url = self.endpoint + path
        headers = {'Content-Type': 'application/json'}
        headers.update(self.headers)
        response = self.http_client.get(
            url, headers=self.headers, params=params, stream=stream, timeout=timeout
        )
        self.__check_error(response)
        return response

    def _post(self, path, data=None, timeout=None):
        url = self.endpoint + path
        headers = {'Content-Type': 'application/json'}
        headers.update(self.headers)
        response = self.http_client.post(
            url, headers=headers, data=data, timeout=timeout
        )
        self.__check_error(response)
        return response

    def __check_error(self, response):
        if 200 <= response.status_code < 300:
            pass
        else:
            raise PushtxError(response.status_code, response.status_code)
