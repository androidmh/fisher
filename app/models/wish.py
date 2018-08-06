"""
@author: MH
@contact: menghedianmo@163.com
@file: gift.py
@time: 2018/7/30 11:30
"""
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from app.models.base import db, Base
from sqlalchemy.orm import relationship


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)
