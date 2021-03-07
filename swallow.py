import os
os.system("pip install --upgrade 'sentry-sdk[flask]'")
from flask import *
from sentry_sdk import set_user
# the Config class in python/config.py
from python.config import Config
# python.user = python/user.py
from python.user import login_check, User
# python.forms = python/forms.py
from python.forms import *

# Creating the server!
app = Config.app
app.config['SECRET_KEY']
non_login_paths = ['/', '/login', '/ping', '/static/style.css']


# When the user goes to any page, this is ran first:
@app.before_request
def before_request():
	# If the user is not logged in:
	if login_check() == False:
		# Set the user to none (for sentry.io)
		set_user(None)
		# If the user is going to a route that requires login, redirect him to the login page.
		if request.path not in non_login_paths:
			return redirect('/login?redirect=' + str(request.path) + '&login=' + Config.logged_out_key)
	# If the user is logged in:
	else:
		# Get the user's username
		user = login_check()[1]
		# Set the user for sentry
		set_user(user)



# The home page
@app.route('/')
def index():
	return render_template('index.html')
	

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	# If the form validates:
	if form.validate_on_submit:
		# Get the form data
		username = form.username.data
		password = form.password.data

		# Initialize the User class from python/user.py
		user = User(username, password)

		# If the username and password are correct:
		if user.validate():
			# Save the fact that the user is now logged in
			session['login'] = [True, username]
			session['mesage'] = 'You are now logged in!'
			return redirect(url_for('index'))
		# If the user is not validated:
		else:

			session['message'] = 'Username or password not correct.'
			return redirect(url_for('login'))
		

		

	return render_template('login.html', form=form)






app.run('0.0.0.0', debug=True)