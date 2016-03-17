from flask import jsonify
from flask_restful import Resource, abort, reqparse
from flask_restful import inputs, fields, marshal_with
from hyoji import models

# Args
parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('name')
parser.add_argument('href', required=True, type=inputs.url)

# Ouput formatting
url_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'href':  fields.String
}

class Url(Resource):
    def get(self, url_id):
        try:
            url = models.Url.get(models.Url.id == url_id)
        except models.Url.DoesNotExist:
            abort(404, message="url {} does not exist".format(url_id))
        return url.to_dict()

    def post(self):
        args = parser.parse_args()
        q = models.Url.insert(name=args['name'], href=args['href'])
        new_id = q.execute()
        return self.get(new_id), 201

    def put(self, url_id):
        args = parser.parse_args()
        try:
            # If 'get' works then the row exists
            # We then do an update
            url = models.Url.get(models.Url.id == url_id)
            q = models.Url.update(name=args['name'], href=args['href']).where(models.Url.id == url_id)
            q.execute()
        except models.Url.DoesNotExist:
            # Otherwise, we do an insert
            q = models.Url.insert(id=url_id, name=args['name'], href=args['href'])
            new_id = q.execute()
        return self.get(url_id), 201

    def delete(self, url_id):
        q = models.Url.delete().where(models.Url.id == url_id)
        q.execute()
        return "Deleted url {}".format(url_id) 

class UrlList(Resource):
    def get(self):
        q = models.Url.select()
        urls = []
        for url in q:
            urls.append(url.to_dict())
        return urls
