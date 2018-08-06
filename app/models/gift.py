"""
@author: MH
@contact: menghedianmo@163.com
@file: gift.py
@time: 2018/7/30 11:30
"""
from flask import current_app
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from app.models.base import Base
from sqlalchemy.orm import relationship


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def recent(cls):
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            Gift.create_time).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gift
