# -*- coding: utf8 -*-

from sqlalchemy_serializer import SerializerMixin as mixin
from app import db


class User(db.Model, mixin):
    __tablename__ = "t_user"

    id = db.Column("id", db.Integer, primary_key=True, nullable=False)
    name = db.Column("name", db.String(32))
    fullname = db.Column("fullname", db.String(200))
    password = db.Column("password", db.String(32), nullable=False)
    mobilePhone = db.Column("mobile_phone", db.String(20))

