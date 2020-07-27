import json
from flask import (
    Blueprint,
    render_template,
    url_for,
    request,
    session,
    flash,
    jsonify
)
from config import node

main = Blueprint('main',
    __name__,
    template_folder='templates'
)


@main.route('/insert', methods=['POST', 'GET'])
def insert_code():
	code = request.args.get('code')
	print('code: ', code)
	if code and not node.search_code(code):
		node.insert_code(code)
		return jsonify({'success':True, 'data':f'{code} was created'}), 201, {'ContentType':'application/json'} 
	else:
		return jsonify({'success':True, 'data':f'{code} code already exists'}), 200, {'ContentType':'application/json'} 


@main.route('/search', methods=['POST', 'GET'])
def search_code():
	code = request.args.get('code')
	print('search: ', code)
	if code:
		results = node.search_code(code)
		print('search result: ', results)
		if not results:
			results = f'{code} code not found'
	return jsonify({'success':True, 'data':results}), 200, {'ContentType':'application/json'} 


@main.route('/all', methods=['GET'])
def all_codes():
	results = list(set(node.all_codes()))
	print('all: ', results)
	if not results:
		results = 'Empty tree'
	return jsonify({'success':True, 'data':results}), 200, {'ContentType':'application/json'} 
	# return jsonify({'success':True, 'data':'Not found'}), 200, {'ContentType':'application/json'} 


@main.route('/childrens', methods=['POST', 'GET'])
def childrens():
	code = request.args.get('code')
	print('code: ')
	if code:
		results = []
		node.childrens(code, results)
		print('childrens for: ', code, results)
		results = results[1::]
		if not results:
			results = 'Not found'
	return jsonify({'success':True, 'data':results}), 200, {'ContentType':'application/json'} 
	# return jsonify({'success':True, 'data':'Not found'}), 200, {'ContentType':'application/json'} 


@main.route('/parents', methods=['POST', 'GET'])
def parents():
	code = request.args.get('code')
	print('parent for: ', code)
	if code:
		results = list(set(node.parents(code)))
		print('results: ', results)
		if not results:
			results = 'Not found'
	return jsonify({'success':True, 'data':results}), 200, {'ContentType':'application/json'} 
	# return jsonify({'success':True, 'data':'Not found'}), 204, {'ContentType':'application/json'} 


