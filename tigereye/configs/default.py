class DefaultConfig(object):

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/tigereye1703'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True