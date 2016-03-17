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
    """Standard api json reponse"""
    #resp = make_response(json.dumps(data), code)
    resp = make_response(json.dumps({'response': data, 'status': code}), code)
    resp.headers.extend(headers or {})
    return resp
