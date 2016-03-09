import os

# Run directory
APP_DIR = os.path.dirname(os.path.realpath(__file__))

# Enable debug mode
DEBUG = True

# Secret key for session management.
SECRET_KEY = 'chest flower enemy paper'

# Connect to the database
DATABASE = 'sqliteext:///%s' % os.path.join(APP_DIR, 'hyoji.db')
