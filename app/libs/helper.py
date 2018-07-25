"""
@author: MH
@contact: menghedianmo@163.com
@file: helper.py
@time: 2018/7/20 13:43
"""


def is_isbn_or_key(word):
    """
        判断搜索输入的是isbn或书籍关键字
        :param word: 输入内容
        :return: 返回判断结果
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
        short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
