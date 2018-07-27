"""
@author: MH
@contact: menghedianmo@163.com
@file: book.py
@time: 2018/7/20 15:58
"""
from flask import jsonify, request, render_template, flash
from app.forms.book import SearchForm
from app.view_models.book import BookCollection
from . import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
import json


@web.route('/book/search')
def search():
    """
        q:普通关键字，isbn
        page(start,count)
    """
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
    else:
        flash('搜索的官架子不符合要求，请重新输入')
    return render_template('search_result.html', books=books)


@web.route('/test')
def test():
    r = {
        'name': 'aaa',
        'age': 27
    }
    flash('hello,dm', category='error')
    flash('hello,zy', category='warring')
    return render_template('test.html', data=r)
