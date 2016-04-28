from flask.ext.wtf import Form
from wtforms.fields import TextField, PasswordField
from wtforms.validators import Email, Required, EqualTo

class SignupForm(Form):
	fname = TextField('First Name: ' , validators=[Required()])
	lname = TextField('Last Name: ' , validators=[Required()])
	email = TextField('Email: ' , validators=[Required(), Email()])
	password = PasswordField('Password: ' , validators=[Required()]) #change to password field
	pass_conf = PasswordField('Re-Enter Password: ' , validators=[Required(), EqualTo('password')])


class LoginForm(Form):
	email = TextField('Email Address: ' , validators=[Required(), Email()])
	password = PasswordField('Password: ' , validators=[Required()])

class ItemForm(Form):
	name = TextField('Item Name: ' , validators=[Required()])
	item_url = TextField('Url: ' , validators=[Required()])
	description = TextField('Description: ' , validators=[Required()])