from . import (
    OKRA_API_VERSION , OKRA_ENVIRONMENT , OKRA_SECRET
)
from okra.exceptions import (
    MissingAuthKeyError , InvalidMethodError
)
import requests
import json




class BaseConfig(object):
    """
    Base class that will be subclass by all other classes 
    """
    _BASE_END_POINT_DICTIONARY =  {
        'live': 'https://api.okra.ng/v2/',
        'sandbox' : "https://api.okra.ng/sandbox/v2/",
    }

    _API_VERSION = OKRA_API_VERSION

    _BASE_END_POINT = _BASE_END_POINT_DICTIONARY.get(OKRA_ENVIRONMENT )

    # _BASE_END_POINT_VERSION = _BASE_END_POINT 

    _CONTENT_TYPE = "application/json"
    
    



    def _headers(self):
        return {
            "Content-Type": self._CONTENT_TYPE,
            'Authorization':  OKRA_SECRET,
        }

    
    def _handle_request(self, method, url, data=None):

        """
        Generic function to handle all API url calls
        Returns a response object from the api call
        """
        method_map = {
            'GET': requests.get,
            'POST': requests.post,
        }

        payload = json.dumps(data) if data else data
        request = method_map.get(method)

        if not request:
            raise InvalidMethodError("Request method not recognized or implemented")

        response = request(url, headers=self._headers(), data=payload)

        return response
            