from flask_restful import Api
from flask import Blueprint, make_response
import json

# API as a Flask Blueprint
api_bp = Blueprint('api', __name__)

# Flask-Restful init w/ Blueprint
api = Api(api_bp)

# Import models that the API wll need
from hyoji import models

# Import our own
from .url import Url, UrlList

# Register endpoints
api.add_resource(Url,     '/url/<int:url_id>')
api.add_resource(UrlList, '/urls', '/urls/')

@api.representation('application/json')
def output_json(data, code, headers=None):
    """General API JSON response format
    This API follows the simple JSend JSON response format.
    http://labs.omniti.com/labs/jsend
    """
    
    # Top-level payload format
    if http_status_is_bad(code):
        # In case of error, flask-restful returns a dict
        # of the form `{'message': <str or list of stt>}`.
        # We inject the status string.
        # {"status": "error", "message": "<an error>"}
        payload = data
        payload['status'] = 'error'
    else:
        # In case of a succes, flask-restful returns
        # the object as-is. We encapsulate it
        # as the value of a "data" key.
        # {"status": "success", "data": <data>}
        payload = {}
        payload['status'] = 'success'
        payload['data'] = data

    # Flask response
    resp = make_response(json.dumps(payload), code)
    resp.headers.extend(headers or {})
    return resp

def http_status_is_bad(status_code):
    """Returns true if `code` is [400,600[."""
    if 400 <= status_code < 600: return True
    else: return False
