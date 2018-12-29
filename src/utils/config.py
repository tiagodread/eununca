class Config(object):
    DEBUG = True
    DB_USER = 'postgres'
    DB_PASS = 'admin'
    DB_PORT = '5432'
    DB_NAME = 'eununca'
    DB_HOST = 'localhost'
    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    BASIC_AUTH_USERNAME = 'tiago.goes2009@gmail.com'
    BASIC_AUTH_PASSWORD = '#q1w2e3#'
