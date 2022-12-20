import pytest

from src import create_app, db


@pytest.fixture(scope='session')
def app():
    app = create_app("testing")
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.session.close_all()
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def init_cache(request):
    request.config.cache.set('username', "testuser")
    request.config.cache.set('password', "123123")
