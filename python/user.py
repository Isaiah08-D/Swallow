from flask import session
from python.config import Config


def login_check():
	if session['login'] == None or session['login'] == False:
		return False
	return True

def key_find(key):
	db = Config.user_db
	for name, data in db.items():
		if data['key'] == key:
			return name
	return False