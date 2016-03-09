from peewee import *
from .base_model import BaseModel

class Url(BaseModel):
    name = CharField()
    href = CharField()

if __name__ == "__main__":
    pass
