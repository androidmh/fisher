from app.models.gift import Gift
from . import web


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    books = []
    return 'hello'


@web.route('/personal')
def personal_center():
    pass
