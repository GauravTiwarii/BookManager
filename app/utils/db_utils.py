from mongoengine import Document, IntField

class AutoIncrementId(Document):
	auto_increment_id = IntField()


class DBUtils(object):

	@classmethod
	def setup(self):
		pass


class DBAutoIncrementId(DBUtils):

	@classmethod
	def setup(self):
		try:
			id = AutoIncrementId.objects.first().auto_increment_id

		except:
			AutoIncrementId(auto_increment_id=0).save()

	@classmethod
	def get_auto_increment_id(self):
		current_id = AutoIncrementId.objects().first().auto_increment_id
		AutoIncrementId.objects().first().update(auto_increment_id=current_id+1)
		return AutoIncrementId.objects.first().auto_increment_id
