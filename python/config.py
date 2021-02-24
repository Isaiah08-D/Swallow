from flask import Flask
from flask_bootstrap import Bootstrap
import os
def create_app():
	app = Flask('__main__')

	Bootstrap(app)
	app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

	return app
	
class Config:
	app = create_app()
	logged_in_key = os.getenv('LOGGED_IN')
	logged_out_key = os.getenv('LOGGED_OUT')
	secret_key = os.getenv('SECRET_KEY')