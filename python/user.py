from flask import session
from config import Config


def login_check():
	if session.get('login') == None or session.get('login') == False:
		return False
	return [True, session.get('login')[1]]

def key_find(key):
	db = Config.user_db
	for name, data in db.items():
		if data['key'] == key:
			return name
	return False

class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
	def validate(self):
		try:
			return Config.db[self.username]['password'] == self.password
		except:
			return False
			