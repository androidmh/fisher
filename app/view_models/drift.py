"""
@author: MH
@contact: menghedianmo@163.com
@file: drift.py
@time: 2018/8/8 14:33
"""


class DriftViewModel:
    def __init__(self, drift):
        self.data = {}

    def __parse(self, drift):
        r = {
            'drift_id': drift.id,
            'book_title': drift.book_title,
            'book_author': drift.book_author,
            'book_img': drift.book_img,
            'date': drift.create_datetime.strftime('%Y-%m-%d'),
            'message': drift.message,
            'address': drift.address,
            'recipient_name': drift.recipient_name,
            'mobile': drift.mobile,
            'status': drift.pending
        }
