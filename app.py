#!/bin/env python
# -*- coding: utf8 -*-

from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/test?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)



if __name__=='__main__':
    from controller.user_controller import user_controller
    from controller.index_controller import index_controller
    app.register_blueprint(user_controller, url_prefix='/user')
    app.register_blueprint(index_controller, url_prefix='')
    app.run(port=5001, debug=True)