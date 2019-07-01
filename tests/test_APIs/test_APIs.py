import json

def test_external_books_search(test_client):
	'''Test API can search external books'''

	response = test_client.get('api/external-books?name=A Game of thrones',
		       					content_type='application/json'
		        			)
	json_response = json.loads(response.data)

	assert json_response["status_code"] == 200
	assert json_response["status"] == "success"
	assert isinstance(json_response["data"], list)


def test_create_book(test_client):
	'''Test API can create a book (POST request)'''

	response = test_client.post('/api/v1/books', data=json.dumps(dict(
				name='My First Book',
				isbn='123-3212322',
				authors= ['John Doe'],
				number_of_pages= 350,
				publisher='Acme Books',
				country= 'United States',
				release_date='2019-08-01')),
        		content_type='application/json'
        		)
	json_response = json.loads(response.data)

	assert json_response["status_code"] == 200
	assert json_response["data"][0]["book"]["name"] == "My First Book"

def test_update_book(test_client, init_database):
	'''Test API can create a book (POST request)'''

	response = test_client.patch('/api/v1/books/3', data=json.dumps(dict(
				name='My First Book',
				isbn='123-3212344',
				authors= ['John Doe'],
				number_of_pages= 350,
				publisher='Acme Books',
				country= 'United States',
				release_date='2019-08-01')),
        		content_type='application/json'
        		)
	json_response = json.loads(response.data)

	assert json_response["status_code"] == 200
	assert json_response["data"]["name"] == "My First Book"


def test_get_books(test_client, init_database):
	'''Test API can get the books (GET request)'''
	response = test_client.get('/api/v1/books')
	json_response = json.loads(response.data)
	print(json_response)
	assert json_response["status_code"] == 200
	assert json_response["data"][0]["name"] == "My First Book"

def test_get_book(test_client, init_database):
	'''Test API can get the books (GET request)'''
	response = test_client.get('/api/v1/books/3')
	json_response = json.loads(response.data)

	assert json_response["status_code"] == 200
	assert json_response["data"]["name"] == "My First Book"


def test_delete_books(test_client, init_database):
	'''Test API can update the books (PATCH request)'''
	response = test_client.delete('/api/v1/books/5',
        		content_type='application/json'
        		)
	json_response = json.loads(response.data)

	assert json_response["status_code"] == 200
	assert json_response["message"] != None
