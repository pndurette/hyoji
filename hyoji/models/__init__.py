from hyoji import app
from playhouse.flask_utils import FlaskDB

# DB init
flask_db = FlaskDB(app)
db = flask_db.database

# Import models
from .url import Url

# Create tables from models
db.create_tables([Url], safe=True)
