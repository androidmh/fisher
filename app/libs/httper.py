"""
@author: MH
@contact: menghedianmo@163.com
@file: http.py
@time: 2018/7/20 13:53
"""
import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        """
            发送get请求
            :param url:api地址
            :param return_json:是否返回json
            :return:返回结果
        """
        r = requests.get(url)

        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
