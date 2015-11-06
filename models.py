from db import database

class tim3(database.Model):
	__tablename__ = 'collaboration'

	id = database.Column(database.Integer, primary_key=True)
	pict = database.Column(database.String())
	about = database.Column(database.String())
	activities = database.Column(database.String())
	contact1 = database.Column(database.String())
	contact2 = database.Column(database.String())
	contact3 = database.Column(database.String())	

	def __repr__(self):
		return '<collaboration{}>'.format(self.activities)