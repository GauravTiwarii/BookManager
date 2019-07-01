# app/__init__.py
import os, requests
from flask_api import FlaskAPI
from mongoengine import connect
from flask import request, jsonify, abort

# local import
from instance.config import app_config
from models import Book
from utils.db_utils import DBAutoIncrementId
from utils.book_processor import CreateBookProcessor, SearchBookProcessor, UpdateBookProcessor, GetBookProcessor, DeleteBookProcessor
from services.external_books import SearchIceAndFireExternalBooks

# initialize mongoengine
db = connect('book_manager', host=os.getenv('MONGODB_URI'))

# setup auto-increment id
DBAutoIncrementId.setup()

def create_app(config_type):
	'''Configures Flask API based on config_type
	@params
		config_type - configuration type 

	@returns
		app - app reference with applied configurations
	'''

	app = FlaskAPI(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_type])

	@app.route('/api/external-books', methods=['GET'])
	def external_books_handler():
		name = request.args.get('name')
		response = { "status_code" : 200,
					 "status" : "success"}
		response["data"] = SearchIceAndFireExternalBooks().search(name)

		return jsonify(response)


	@app.route('/api/v1/books', methods=['GET','POST'])
	def books_handler():
		if request.method == 'POST':
			response = {"status_code" : 200,
						 "status" : "success"}
			data = request.get_json()
			response["data"] = [{"book" : CreateBookProcessor.process(data)}]
			return jsonify(response)

		else:
			results = []
			response = {"status_code" : 200,
						"status" : "success"}
			name = request.args.get('name', None)
			country = request.args.get('country', None)
			publisher = request.args.get('publisher', None)
			release_date = request.args.get('release_date', None)
			response["data"] = SearchBookProcessor.process(name, country, publisher, release_date)
			return jsonify(response)

	@app.route('/api/v1/books/<id>', methods=['DELETE','GET','PATCH'])
	def books_id_handler(id):
		if request.method == 'PATCH':
			response = {"status_code" : 200,
						"status" : "success"}
			update_book_schema = request.get_json()
			response["data"] = UpdateBookProcessor.process(id, update_book_schema)
			return response

		elif request.method == 'GET':
			response = {"status_code" : 200,
						"status" : "success"}
			response["data"] = GetBookProcessor.process(id)
			return response
		else:
			response = {"status_code": 200,
						"status" : "success"}
			book = DeleteBookProcessor.process(id)
			response["data"] = book
			message = "The book " + book["name"] +  " was deleted successfully"
			response["message"] = message
			response["data"] = []
			return jsonify(response)

			
	return app