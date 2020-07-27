import os
import pickle
from models import Node


basedir = os.path.abspath(os.path.dirname(__file__))
is_file = os.path.isfile(os.path.join(basedir, 'db.pickle'))


# def get_node():
# 	if is_file:
# 		with open('db.pickle', 'rb') as f:
# 			# print(pickle.load(f).__dict__)
# 			node = pickle.load(f)
# 	else:
# 		node = Node()
# 	return node


node = Node()

class Configuration(object):
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')