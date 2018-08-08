"""
@author: MH
@contact: menghedianmo@163.com
@file: config.py
@time: 2018/7/18 14:15
"""
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123123@localhost:3306/fisher'
SECRET_KEY = 'CACB66F154CB72AD8AEB416FA3F40FD0'

# Email配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = '857575129@qq.com'
MAIL_PASSWORD = 'qrtlgnsrxdfubeie'
# MAIL_SUBJECT_PREFIX = '[鱼书]'
# MAIL_SENDER = '鱼书 <hello@yushu.im>'
