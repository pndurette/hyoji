from .version import __version__
from flask import Flask, Blueprint

import config

# Flask init
app = Flask(__name__)
app.config.from_object(config)

import models
import api 
#import hyoji.views

# Tests will initialize the DB
# with their own set of parameters
if not app.config['TESTING']:
    models.init_db()

# Blueprints and global endpoint prefixes
app.register_blueprint(api.api_bp, url_prefix='/api')
