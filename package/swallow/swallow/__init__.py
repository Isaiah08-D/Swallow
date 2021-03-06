from python.config import Config
from python.user import key_find
from python.config import errors

__version__ = '0.1.0'




class DB:
	def __init__(self, key):
		if key_find(key) == False:
			raise errors.AuthError(key + ' is not a valid key!')

		self.key = key
		self.db = Config.db
		self.user = key_find(self.key)
		self.project = self.db[self.user]['projects'][key]
		self.categories = self.project['categories']
		self.current_category = None
	def set_category(self, category):
		try:
			self.current_category = self.categories[category]
		except:
			raise SyntaxError(category + ' is not a valid category!')
	def reset_category(self):
		pass
	
