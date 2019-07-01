import os

from app import create_app

config_type = os.getenv('CONFIG_TYPE')
app = create_app(config_type)


if __name__ == '__main__':
	app.run()