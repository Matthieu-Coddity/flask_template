#core/config.py

'''
Config file
should add class DevelopmentTestConfig(BaseConfig) for unittest
'''
import os
basedir = os.path.abspath(os.path.dirname(__file__))

#database configuration base
sqllite_local_base = ''
database_name = ''

class BaseConfig:
    """Base configuration."""
    #secret key env variable, 'my_precious' default
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    #debug
    DEBUG = False
    #DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    #debug
    DEBUG = True
    #DB
    SQLALCHEMY_DATABASE_URI = sqllite_local_base + database_name 

class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE')
