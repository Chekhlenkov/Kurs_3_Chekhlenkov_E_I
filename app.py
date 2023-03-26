from flask import Flask, jsonify

import logger
from main.view import main_blueprint
from utils import get_post_by_pk, get_all

log = logger.get_logger('api')

app = Flask(__name__)
app.register_blueprint(main_blueprint)

@app.errorhandler(500)
def server_error(e):
    return "Ошибка на сервере, ты тут не при чём =)"


@app.errorhandler(404)
def server_error(e):
    return "Такой страницы неть и не будет"


@app.route('/api/')
def api_main_page():
    posts = get_all()
    log.info("api - > {len(posts)}")
    return jsonify(posts)


@app.route('/api/post/<int:pk>/')
def watch_post_api(pk):
    post = get_post_by_pk(pk)
    log.info("api_posts - > {pk}")
    return jsonify(post)



if __name__ == "__main__":
    app.run(debug=True)