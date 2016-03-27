from hyoji import app
from playhouse.flask_utils import FlaskDB

db = FlaskDB()

# Import models
# Even though the database is not yet initialized,
# we can use it to create models.
from .url import Url

def init_db():
    db.init_app(app)
    
    # Create tables from models
    db.database.create_tables([Url], safe=True)
