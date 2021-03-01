from flask import *
# the Config class in python/config.py
from python.config import Config
# python.user = python/user.py
from python.user import login_check

# Creating the server!
app = Config.app

# When the user goes to any page, this is ran first:
@app.before_request
def before_request():
	# If the user is not 
	if 'user_id=' in request.path and login_check() == False:
		return redirect('/login?redirect=' + str(request.path) + '&login=' + Config.logged_out_key)


@app.route('/')
def index():
	return render_template('index.html')
	


Config.run()