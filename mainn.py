from flask import Flask
from main.view import main_blueprint


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.register_blueprint(main_blueprint)

@app.errorhandler(500)
def server_error(e):
    return "Ошибка на сервере, ты тут не при чём =)"

@app.errorhandler(404)
def server_error(e):
    return "Такой страницы неть и не будет"



if __name__ == "__main__":
    app.run()