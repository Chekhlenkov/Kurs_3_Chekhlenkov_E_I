from flask import Blueprint, render_template, request, jsonify

import logger
from db import db
from utils import get_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates', url_prefix='/')
log = logger.get_logger('api')

@main_blueprint.route('/')
def main_page():
    posts = get_all()
    return render_template("index.html", posts=posts)


@main_blueprint.route('/post/<int:pk>/')
def watch_post(pk):
    post = get_post_by_pk(pk)
    comments = get_comments_by_post_id(pk)
    count_comments = len(comments)
    return render_template("post.html", post=post, comments=comments, count_comments=count_comments)

@main_blueprint.route('/search_start')
def search_():
    return render_template("search_start.html")

@main_blueprint.route('/search')
def search_posts():
    key_words = request.args.get('s')
    posts = search_for_posts(key_words)
    qty = len(posts)
    if posts == []:
        qty = "Ничего не найдено"
    return render_template("search.html", key_words=key_words, posts=posts, qty=qty)

@main_blueprint.route('/user-feed/<poster_name>/')
def posts_name(poster_name):
    posts = get_posts_by_user(poster_name)
    return render_template("user-feed.html", posts=posts)


@main_blueprint.route('/ping', methods=['GET'])
def ping():
    return 'pong'

@main_blueprint.route('/test_db', methods=['GET'])
def test_db():
    result = db.session.execute(
        '''
        SELECT 1;
        '''
    ).scalar()
    return jsonify({'result': result})
