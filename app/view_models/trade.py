"""
@author: MH
@contact: menghedianmo@163.com
@file: trade.py
@time: 2018/8/6 10:38
"""


class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]

    def __map_to_trade(self, single):
        if single.create_time:
            time = single.create_datetime.strftime('%Y-%M-%d')
        return dict(
            user_name=single.user.nickname,
            time=time,
            id=single.id
        )
