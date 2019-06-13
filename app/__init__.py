import os

import dash_core_components as dcc
from flask import Flask

from app.config import Config
from app.sqlconnect import getData

print(dcc.__version__) # 0.6.0 or above is required

flask_server = Flask(__name__)
flask_server.config.from_object(Config)
flask_server.config.update(dict(
    SECRET_KEY=os.urandom(32),
    WTF_CSRF_SECRET_KEY=os.urandom(32)
))

from app import routes
from app import layout
