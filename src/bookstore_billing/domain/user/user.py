import uuid

from bookstore_billing.settings import db


class User(db.Model):
	__tablename__ = "users"

	id = db.Column(db.String, primary_key=True, default=uuid.uuid4)
	username = db.Column(db.String, unique=True)
	first_name = db.Column(db.String)
	last_name = db.Column(db.String)
	email = db.Column(db.String)
	user_status = db.Column(db.Boolean, default=True)
	bills = db.relationship('SimplifiedBill', backref='simplified_bills')
