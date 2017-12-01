# -*- coding: utf-8 -*-
# Exceptions
class PushtxError(Exception):
    def __init__(self, message=None, http_body=None, http_status=None,
                 json_body=None):
        super(PushtxError, self).__init__(message)