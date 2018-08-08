"""
@author: MH
@contact: menghedianmo@163.com
@file: __init__.py
@time: 2018/7/20 16:27
"""
from flask import Flask
from app.models.base import db
from flask_login import LoginManager
from flask_mail import Mail

login_manger = LoginManager()
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    login_manger.init_app(app)
    login_manger.login_view = 'web.login'
    login_manger.login_message = '请先登录或注册'

    mail.init_app(app)

    with app.app_context():
        db.create_all()
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
