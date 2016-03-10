from flask import jsonify
from flask_restful import Resource, abort, reqparse, inputs
from hyoji import models

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('name', required=True)
parser.add_argument('href', required=True, type=inputs.url)

class Url(Resource):
    def get(self, url_id):
        try:
            url = models.Url.get(models.Url.id == url_id)
        except models.Url.DoesNotExist:
            abort(404, message="url {} does not exist".format(url_id))
        return url.to_dict()

    def put(self):
        args = parser.parse_args()
        q = models.Url.insert(name=args['name'], href=args['href'])
        new_id = q.execute()
        return self.get(new_id), 201

class UrlList(Resource):
    def get(self):
        # TODO: Guard against empty table
        q = models.Url.select()
        urls = []
        for url in q:
            urls.append(url.to_dict())
        return urls
