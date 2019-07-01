from mongoengine import Document, StringField, ListField, IntField, DateTimeField

class Book(Document):
	id = IntField(primary_key=True)
	name = StringField()
	isbn = StringField()
	authors = ListField()
	country =  StringField()
	number_of_pages =  IntField()
	publisher = StringField()
	release_date = DateTimeField()