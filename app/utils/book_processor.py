import datetime

from app.models import Book
from db_utils import DBAutoIncrementId
from mongoengine.queryset.visitor import Q

class BookProcessor(object):
	@classmethod
	def process(self, book):
		pass

class GetBookProcessor(BookProcessor):
	@classmethod
	def process(self, id):
		book = Book.objects(id=int(id)).first()
		fetched_book = BookFormatProcessor.get_book_in_json(book)

		return fetched_book
		

class UpdateBookProcessor(BookProcessor):
	@classmethod
	def process(self, id, update_book_schema):
			book = Book.objects(id=int(id)).first()
			for key, value in update_book_schema.items():
				book[key] = value
			book.save()
			book.reload()
			
			book = {
				"id":book["id"],
				"name": book["name"], 
				"isbn": book["isbn"],
				"authors": book["authors"],
				"country": book["country"],
				"number_of_pages": book["number_of_pages"],
				"publisher": book["publisher"],
				"release_date": str(book["release_date"]).split(" ")[0]
			}
			return book

class SearchBookProcessor(BookProcessor):
	@classmethod
	def process(self, name, country, publisher, release_date):
		results = []
		if name or country or publisher or release_date :
			filtered_books = Book.objects(Q(publisher=publisher) | Q(name="My First Book") | Q(country=country) | Q(release_date=release_date))
			results = BookFormatProcessor.get_books_array_in_json(filtered_books)
		else :
			results = BookFormatProcessor.get_books_array_in_json(Book.objects)
		return results

class CreateBookProcessor(BookProcessor):
	@classmethod
	def process(self, book):
		saved_book = Book(id=DBAutoIncrementId.get_auto_increment_id(),
						name=book["name"], 
						isbn=book["isbn"],
						authors=book["authors"],
						country=book["country"],
						number_of_pages=book["number_of_pages"],
						publisher=book["publisher"],
						release_date=book["release_date"]
						)
		return book

class DeleteBookProcessor(BookProcessor):
	@classmethod
	def process(self, id):
			book = Book.objects(id=int(id)).first()
			deleted_book = BookFormatProcessor.get_book_in_json(book)
			book.delete()
			return deleted_book


class BookFormatProcessor(object):
	@classmethod
	def get_book_in_json(self, book_object):
			book = {
				"id":book_object["id"],
				"name": book_object["name"], 
				"isbn": book_object["isbn"],
				"authors": book_object["authors"],
				"country": book_object["country"],
				"number_of_pages": book_object["number_of_pages"],
				"publisher": book_object["publisher"],
				"release_date": str(book_object["release_date"]).split(" ")[0]
			}

			return book

	@classmethod
	def get_books_array_in_json(self, books_array_object):
			books_array = []
			for item in books_array_object:				
					book = {
							"id":item["id"],
							"name": item["name"], 
							"isbn": item["isbn"],
							"authors": item["authors"],
							"country": item["country"],
							"number_of_pages": item["number_of_pages"],
							"publisher": item["publisher"],
							"release_date": str(item["release_date"]).split(" ")[0]
						}
					books_array.append(book)

			return books_array