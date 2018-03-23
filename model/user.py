# -*- coding: utf8 -*-

from sqlalchemy_serializer import SerializerMixin as mixin
from app import db


class t_user(db.Model, mixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(32))
    fullname = db.Column(db.String(200))
    password = db.Column(db.String(32))

