#core/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#creation de l'app
app = Flask(__name__)

#SETTINGS
#looking for env variable APP_SETTINGS, core.config.DevelopementConfig by default
app_settings = os.getenv(
    'APP_SETTINGS',
    'core.config.DevelopmentConfig'
)
app.config.from_object(app_settings)
#intialisation de la base
db = SQLAlchemy(app)

from core.app import *