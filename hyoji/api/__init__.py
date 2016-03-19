from hyoji import app
from flask_restful import Api
from flask import make_response
import json

# Flask Restful init
api = Api(app)

# Import models that the API wll need
from hyoji import models

# Import our own
from .url import Url, UrlList

# Register endpoints
api.add_resource(Url,     '/url/<url_id>', '/url')
api.add_resource(UrlList, '/urls')

@api.representation('application/json')
def output_json(data, code, headers=None):
    """General API JSON response format"""
    
    # 'status' field
    if http_status_is_bad(code):
        status = 'error'
        contents_label = 'message'
        contents = data['message']
    else:
        status = 'success'
        contents_label = 'data'
        contents = data

    # Response format
    resp_dict = {
        'status': status,
        contents_label: contents
    }

    # Flask response
    resp = make_response(json.dumps(resp_dict), code)
    resp.headers.extend(headers or {})
    return resp

def http_status_is_bad(status_code):
    """Returns true if `code` is [400,600["""
    if 400 <= status_code < 600: return True
    else: return False
