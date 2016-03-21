from .version import __version__
from flask import Flask, Blueprint

import hyoji.config

# Flask init
app = Flask(__name__)
app.config.from_object(hyoji.config)

import hyoji.models
import hyoji.api 
#import hyoji.views

# Blueprints and global endpoint prefixes
app.register_blueprint(hyoji.api.api_bp, url_prefix='/api')
