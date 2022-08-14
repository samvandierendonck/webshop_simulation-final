from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Selected_item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000),default='')
    img = db.Column(db.String(10000),default='')
    base_price = db.Column(db.String(10000),default='')
    base_price_type = db.Column(db.String(10000),default='')
    big_price = db.Column(db.String(10000),default='')
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Purchases(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.relationship('Ordered_item')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class Ordered_item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000),default='')
    img = db.Column(db.String(10000),default='')
    base_price = db.Column(db.String(10000),default='')
    base_price_type = db.Column(db.String(10000),default='')
    big_price = db.Column(db.String(10000),default='')
    purchase_id = db.Column(db.Integer, db.ForeignKey('purchases.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    shoppinglist = db.relationship('Selected_item')
    total_price = db.Column(db.Float,default=0)
    #for item in shoppinglist:
        #total_price += item.base_price

