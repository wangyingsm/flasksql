from flask import render_template, request, Blueprint, send_from_directory
import service.user_service as us
from app import app
import os

index_controller = Blueprint('index_controller', __name__)

@index_controller.route('/')
def showIndex():
    id = request.args.get('userid', None)
    if not id:
        username = 'Guest'
    else:
        user = us.findUserById(id)
        if not user:
            username = 'Guest'
        else:
            username = user.fullname
    return render_template('index.html', username=username)
