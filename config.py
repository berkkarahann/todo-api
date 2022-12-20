import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def db_url(env):
    return "sqlite:///" + os.path.join(BASEDIR, env)


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret key for todolist api"
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = db_url("todolist-test.db")
    import logging

    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    logging.getLogger().setLevel(logging.DEBUG)


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = db_url("todolist-prod.db")
    JSON_SORT_KEY = False


config = {
    "testing": TestingConfig,
    "production": ProductionConfig,
}
