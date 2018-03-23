# -*- coding: utf8 -*-

import dao.user_mapper as um
from model.user import t_user

def findAllUsers():
    return um.findAllUsers()

def findUserById(id):
    return um.findUserById(id)

def insertUser(name, fullname, password):
    user = t_user(name=name, fullname=fullname, password=password)
    try:
        um.insertUser(user)
    except:
        return 400, {'msg': '新增用户时发生错误'}
    return 201, user.to_dict()

def updateUser(id, name, fullname, password):
    try:
        params = {'id': id, 'name': name, 'fullname': fullname, 'password': password}
        um.updateUser(params)
    except:
        return 400, {'msg': '修改用户时发生错误'}
    return 202, {'msg': '修改成功'}

def deleteUser(user):
    try:
        um.deleteUser(user)
    except:
        return 400, {'msg': '删除用户时发生错误'}
    return 204, None