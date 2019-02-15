from app.models.categories import Categories
from app.models.quotes import Quotes


class Api(object):
    categories = Categories()
    quotes = Quotes()
