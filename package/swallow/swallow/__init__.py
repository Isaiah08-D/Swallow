__version__ = '0.1.0'

@property
def db():
	raise AttributeError('db is not a readable attribute.')

def initialize():
	'''
	Intializes the database.
	'''
	global db
	db = {'categories': {}}

class CreateCategory:
	def __init__(self, name):
		self.db = db
		if name not in db['categories']:
			db['categories'][name] = {}
			self.category = db['categories'][name]
		else:
			raise AttributeError(name + ' had already been defined as a category.')

	def define(self, **info):
		for name, item_type in info:
			if item_type not in [list, dict, int, str, bool, float, tuple, bytes, bytearray, memoryview, set, frozenset, range, complex]:
				raise AttributeError(item_type + ' is not a valid type.')
			else:
				self.category[name] = item_type

class Category:
	def __init__(self, **connect, new=True):
		'''
		**connect: informatio defined in CreateCategory.define

		Connect to a portion of a category made in the CreateCategory class.
		'''

