from flask import Flask
from flask_bootstrap import Bootstrap
import os
from replit import db
from flask_session import Session
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
sentry_sdk.init(
	dsn="https://375201f2d9b34ae18c4680298d45ae91@o515423.ingest.sentry.io/5662383",
integrations=[FlaskIntegration()],
traces_sample_rate=1.0
)
app = Flask(__name__)

def create_app():
	app = Flask('__main__')

	Bootstrap(app)
	Session(app)


	return app


class Config:
	app = create_app()
	app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
	logged_in_key = os.getenv('LOGGED_IN')
	logged_out_key = os.getenv('LOGGED_OUT')





	db = db