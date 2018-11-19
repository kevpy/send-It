"""Create environment specific configurations settings for the app"""
import os


class Config(object):
    """Parent configuration class."""
    DEBUG = True
    CSRF_ENABLED = True  # Cross-Site Request Forgery
    SECRET = os.environ.get('SECRET_KEY')
    DATABASE_URL = os.getenv("APP_DB_URI")


class DevelopmentConfig(Config):
    """Configurations for development environment."""
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    """Configurations for testing environment."""
    TESTING = True
    DEBUG = True
    DATABASE_URL = os.getenv("TEST_DB_URI")


class ProductionConfig(Config):
    """Configurations for production envoronment."""
    DEBUG = False
    TESTING = False


app_config = {'development': DevelopmentConfig,
              'testing': TestingConfig,
              'production': ProductionConfig
              }
