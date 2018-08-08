"""
@author: MH
@contact: menghedianmo@163.com
@file: enums.py
@time: 2018/8/8 10:48
"""
from enum import Enum


class PendingStatus(Enum):
    Waiting = 1
    Success = 2
    Reject = 3
    Redraw = 4
