import pytest
from app import create_app
from app.models import Book

@pytest.fixture(scope='module')
def test_client():
	'''Configure app for testing'''

	flask_app = create_app('testing')
	# creating Werkzeug test client
	testing_client = flask_app.test_client()

	# establish an application context for each test execution
	context = flask_app.app_context()
	context.push()

	yield testing_client 

	context.pop()



@pytest.fixture(scope='module')
def init_database():
	'''Setup the database with two entries'''

	#Insert user data
	book1 = Book(id=3,
				name='My First Book',
				isbn='123-3212322',
				authors= [
					'John Doe'
				],
				number_of_pages= '350',
				publisher='Acme Books',
				country= 'United States',
				release_date='2019-08-01').save()

	book2 = Book(id=5,
				name='My First Book',
				isbn='123-3212322',
				authors= [
					'John Doe'
				],
				number_of_pages= '350',
				publisher='Acme Books',
				country= 'United States',
				release_date='2019-08-01').save()

	yield Book

	# Book.drop_collection()
