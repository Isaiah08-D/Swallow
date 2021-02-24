from flask import session

def login_check():
	if session['login'] == None or session['login'] == False:
		return False
	return True