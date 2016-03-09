from flask import jsonify
from flask_restful import Resource
from hyoji import models

class Url(Resource):
    def get(self):
        urls = models.Url.select().dicts().get()
        return jsonify(urls)
