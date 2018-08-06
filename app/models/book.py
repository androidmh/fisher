"""
@author: MH
@contact: menghedianmo@163.com
@file: book.py
@time: 2018/7/23 14:27
"""
from sqlalchemy import Column, Integer, String
from app.models.base import Base


class Book(Base):
    """
        primary_key主键, autoincrement自增, nullable是否可以为空, default默认值, unique是否可以重复
    """
    # id
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 标题
    title = Column(String(50), nullable=False)
    # 作者
    author = Column(String(30), default='未命名')
    # 是否精装
    binding = Column(String(20))
    # 出版社
    publisher = Column(String(50))
    # 价格
    price = Column(String(20))
    # 页数
    pages = Column(Integer)
    # 出版年月
    pubdate = Column(String(20))
    # isbn编号
    isbn = Column(String(15), nullable=False, unique=True)
    # 书籍简介
    summary = Column(String(10000))
    # 图片
    image = Column(String(50))

    def sample(self):
        pass
