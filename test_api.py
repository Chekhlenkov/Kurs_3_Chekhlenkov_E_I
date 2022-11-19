from mainn import app
from pytest import fixture

@fixture()
def post_keys():
    return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

def test_posts():
    response = app.test_client().get('/api')
    assert isinstance(response.json, list)

def test_posts1():
    response = app.test_client().get('/api/post')
    assert response.status_code == 200


def test_posts2():
    response = app.test_client().get('/api/post')
    assert list(response.json.keys()) == post_keys()

def test_post():
    response = app.test_client().get('/api/post/1')
    assert response.status_code == 308



def test_post1():
    response = app.test_client().get('/api/post/1')
    assert isinstance(response.json, dict)

def test_post2():
    response = app.test_client().get('/api/post/1')
    assert set(response.json.keys()) == post_keys()