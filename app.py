from flask import Flask
from exceptions import NoDataSource
from main.views import main_blueprint
from api_test.api_views import api_blueprint


def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.register_blueprint(main_blueprint, name="main")
    app.register_blueprint(api_blueprint, name="api")
    return app


app = create_app()


@app.errorhandler(404)
def notfound(error):
    return f"Страница не найдена - {error}", 404


@app.errorhandler(500)
def internal_server_error(error):
    return f"Внутренняя ошибка сервера - {error}", 500


@app.errorhandler(NoDataSource)
def page_error_data_source_broken(error):
    return f'Ошибка, не найден файл с данными - {error}', 500


@app.errorhandler(ValueError)
def internal_server_error(error):
    return f"{error}", 500


if __name__ == '__main__':
    app.run(debug=True)
