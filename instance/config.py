# /instance/config.py

import os

class Config(object):
	"""Parent configuration class."""
	
	DEBUG = False
	CSRF_ENABLED = True
	SECRET = os.getenv('SECRET')
	MONGODB_URI = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
	"""Configuratios for Development."""
	
	DEBUG = True

class TestingConfig(Config):
	"""Configurations for Testing. with a separate test database."""

	TESTING = True
	MONGODB_URL = 'mongodb://localhost:27017/test_book_manager'
	DEBUG = True

class StagingConfig(Config):
	"""Configurations for Staging."""
	
	DEBUG = True

class ProductionConfig(Config):
	"""Configurations for Production. """

	DEBUG = False
	TESTING = False


app_config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'staging': StagingConfig,
	'production': ProductionConfig
}

