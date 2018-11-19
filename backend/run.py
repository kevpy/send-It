"""Run a Flask instance"""
import os
from my_app import create_app

config = os.getenv('APP_SETTINGS')
app = create_app(config)
