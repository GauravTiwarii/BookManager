import requests, datetime

class ExternalBooks(object):
	
	def setup(self):
		pass


class IceAndFireExternalBooks(ExternalBooks):
	
	def setup(self):
		self.url = "https://anapioficeandfire.com/api/books"


class SearchIceAndFireExternalBooks(IceAndFireExternalBooks):

	def search(self, name):
		self.setup()
		books = requests.get(url=self.url + '?name=' + name).json()
		return self.sanitize_response(books)


	def sanitize_response(self, books):
		#  numberOfPages, release_date, publisher, authors, country, name, isbn
		sanitized_books = []
		for book in books:
			sanitized_book = {
				"name": book["name"],
				"isbn": book["isbn"],
				"authors": book["authors"],
				"number_of_pages": book["numberOfPages"],
				"publisher": book["publisher"],
				"country": book["country"],
				"release_date": self.get_formatted_release_date(book["released"])
			}

			sanitized_books.append(sanitized_book)


		return sanitized_books

	def get_formatted_release_date(self, release_date):
		return datetime.datetime.strptime(release_date, '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m-%d')
