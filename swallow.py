from flask import *
from python.config import Config
from python.user import login_check
app = Config.app


@app.before_request
def before_request():
	if 'user_id=' in request.path and login_check() == False:
		return redirect('/login?redirect=' + str(request.path) + '&login=' + Config.logged_out_key)


@app.route('/')
def index():
	return render_template('index.html')


	
app.run('0.0.0.0')