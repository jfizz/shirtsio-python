import ast
import sys
import time
import datetime
import types
import urllib
import urlparse
import requests
import VERSION
from shirtsio.exception import APIError, InvalidRequestError, AuthenticationError


api_key = None
api_base = 'https://www.shirts.io/api/v1/'
api_version = None


class APIRequestor(object):
    def __init__(self, key=None):
        self.api_key = key

    @classmethod
    def api_url(cls, url=''):
        return '%s%s' % (api_base, url)

    def request(self, url, params, method='get', files=None):
        response = None
        try:
            if method == 'get':
                response = requests.get(url, params=params)
            elif method == 'post':
                response = requests.post(url, data=params, files=files)

            if response.status_code == 200:
                results = response.json()["result"]
                if type(results) == unicode:
                    return ast.literal_eval(results)
            else:
                results = response.json()["error"]

            return results
        except requests.exceptions.RequestException:
            print "Send request to Shirt.io failed."
            # raise Exception(err)
        except ValueError:
            print "request error:", response.text
            # raise Exception(err)