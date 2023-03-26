from app import app



def test_posts():
    response = app.test_client().get('/api/')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert list(response.json[0].keys()) == ['content', 'likes_count', 'pic', 'pk', 'poster_avatar', 'poster_name', 'views_count']


def test_post():
    response = app.test_client().get('/api/post/1/')
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert set(response.json.keys()) == {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}




