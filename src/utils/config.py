class Config(object):
    DEBUG = True
    DB_USER = 'ejrmoqqsvrdlsb'
    DB_PASS = '7e673d42dc60e1d06649d1bf8858a9adfce2324023c065983618544dd80b52cd'
    DB_PORT = '5432'
    DB_NAME = 'd2r6n717ei51ka'
    DB_HOST = 'ec2-54-225-237-84.compute-1.amazonaws.com'
    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    BASIC_AUTH_USERNAME = 'tiago.goes2009@gmail.com'
    BASIC_AUTH_PASSWORD = '#q1w2e3#'
