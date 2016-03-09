from peewee import Model

from hyoji.models import db

class BaseModel(Model):
    class Meta:
        database = db
