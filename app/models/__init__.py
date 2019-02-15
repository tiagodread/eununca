from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()


def get_paid_or_free_category(type):
    if type == 'False':
        return False
    elif type == 'True':
        return True
