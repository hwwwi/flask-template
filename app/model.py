""" SQLAlchemy Models """

from app import db


class Customer(db.Model):
    """ SQLAlchemy model for customer """

    cid = db.Column(db.String(255), primary_key=True)
    phone_number = db.Column(db.String(255), primary_key=True)
