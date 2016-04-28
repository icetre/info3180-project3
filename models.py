from . import db
from sqlalchemy.orm import relationship

class User(db.Model):
	user_id =db.Column(db.Integer, primary_key = True)
	fname = db.Column(db.String(50))
	lname = db.Column(db.String(50))
	email = db.Column(db.String(50))
	password = db.Column(db.String(50))
	wishlist = relationship('Item')


	def __init__(self, fname, lname, email, password):

		self.fname = fname
		self.lname = lname
		self.email = email
		self.password = password

	def __repr__(self):
		return {"First Name: ", self.fname}


class Item(db.Model):
	item_id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50))
	item_url = db.Column(db.String(500))
	image_url = db.Column(db.String(500))
	description =db.Column(db.String(1000))

	user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

	def __init__(self, name, description, item_url,image_url, user_id):
		self.name = name
		self.description = description
		self.item_url = item_url
		self.image_url = image_url
		self.user_id = user_id


	def __repr__(self):
		return { "ID: ", self.item_id, "Name: ", self.name, "Description: ", self.description, "User:", self.user_id  }