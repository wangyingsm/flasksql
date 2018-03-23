# -*- coding: utf8 -*-

from app import db
from model.user import t_user
from sqlalchemy.exc import DatabaseError
from sqlalchemy import text
from traceback import print_exc

def findAllUsers():
    return db.session.query(t_user).all()

def findUserById(id):
    return db.session.query(t_user).filter(t_user.id == id).one_or_none()

def insertUser(user):
    try :
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print_exc()
        raise DatabaseError('插入用户数据时发生错误', e.message, e)

def updateUser(params):
    try :
        sql = text('update t_user set name=:name, fullname=:fullname, password=:password '
            'where id=:id')
        print(sql)
        db.session.execute(sql, params)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print_exc()
        raise DatabaseError('插入用户数据时发生错误', e.message, e)

def deleteUser(user):
    try:
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print_exc()
        raise DatabaseError('删除用户数据时发生错误', e.message, e)