from hyoji import app
from flask_restful import Api

# Flask Restfull init
api = Api(app)

# Import models that the API wll need
from hyoji import models

# Import our own
from .url import Url, UrlList

# Register endpoints
api.add_resource(Url,     '/url/<url_id>', '/url')
api.add_resource(UrlList, '/urls')
