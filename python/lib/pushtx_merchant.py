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
import config
from lib.client import Client
from .utils import create_nonce, create_sign


class PushtxMerchant(Client):
    def __init__(self, app_id, secret_key, endpoint, http_client=None):
        super(PushtxMerchant, self).__init__(endpoint, http_client)
        self.app_id = app_id
        self.secret_key = secret_key

    def get_balance(self):
        nonce = create_nonce()
        sign = create_sign([self.app_id, nonce, self.secret_key], nonce)
        return super(PushtxMerchant, self)._post(config.api_url['merchant_get_balance'], {
            'app_id': self.app_id,
            'nonce': nonce,
            'sign': sign
        })

    def create_order(self, txhash, description):
        nonce = create_nonce()
        sign = create_sign([txhash, description, self.app_id, nonce, self.secret_key], nonce)
        return super(PushtxMerchant, self)._post(config.api_url['merchant_create_order'], {
            'app_id': self.app_id,
            'nonce': nonce,
            'sign': sign,
            'txhash': txhash,
            'description': description
        })
