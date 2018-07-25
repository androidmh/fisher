"""
@author: MH
@contact: menghedianmo@163.com
@file: __init__.py
@time: 2018/7/20 16:37
"""
from flask import Blueprint

web = Blueprint('web', __name__)
from app.web import book
from app.web import user
