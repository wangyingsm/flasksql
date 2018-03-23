# -*- coding: utf8 -*-

from flask import Blueprint, jsonify, request, abort, make_response
import service.user_service as us
from app import logger

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/', methods=['GET'])
def getAllUsers():
    logger.debug('find all users')
    users = list(map(lambda x: x.to_dict(), us.findAllUsers()))
    return jsonify(users)

@user_controller.route('/<int:id>', methods=['GET'])
def getUserById(id):
    user = us.findUserById(id)
    return jsonify(user.to_dict())

@user_controller.route('/', methods=['POST'])
def addUser():
    if not request.json:
        abort(403)
    if not request.json['name']:
        abort(403)
    name = request.json.get('name')
    fullname = request.json.get('fullname', None)
    password = request.json.get('password', None)
    code, user = us.insertUser(name, fullname, password)
    return make_response(jsonify(user), code)

@user_controller.route('/<int:id>', methods=['PUT'])
def modifyUser(id):
    if not request.json:
        abort(403)
    user = us.findUserById(id)
    if not user:
        abort(404)
    name = request.json.get('name', user.name)
    fullname = request.json.get('fullname', user.fullname)
    password = request.json.get('password', user.password)
    code, msg = us.updateUser(id, name, fullname, password)
    return make_response(jsonify(msg), code)

@user_controller.route('/<int:id>', methods=['DELETE'])
def deleteUser(id):
    user = us.findUserById(id)
    if not user:
        abort(404)
    code, msg = us.deleteUser(user)
    return make_response(jsonify(msg), code)