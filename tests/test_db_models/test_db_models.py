from app.models import Book

def test_new_book():
	"""
	GIVEN a Book model
	When a new Book is created
	THEN verify its attributes
	"""

	book = Book(id=1,
				name='My First Book',
				isbn='123-3212322',
				authors= [
					'John Doe'
				],
				number_of_pages= '350',
				publisher='Acme Books',
				country= 'United States',
				release_date='2019-08-01')

	assert book.name == 'My First Book'
	assert book.isbn  == '123-3212322'
	assert book.number_of_pages == 350
	assert book.publisher =='Acme Books'
	assert book.country == 'United States'
	assert book.release_date == '2019-08-01'