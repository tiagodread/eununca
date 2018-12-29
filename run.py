from flask_basicauth import BasicAuth

from src.api import Api
from src.app import create_app

if __name__ == '__main__':
    app = create_app()
    api = Api()
    basic_auth = BasicAuth(app)


    @app.route('/quotes', methods=['GET'])
    @basic_auth.required
    def list_quotes():
        return api.quotes.list_quotes()


    @app.route('/quotes/add', methods=['POST'])
    @basic_auth.required
    def add_quotes():
        return api.quotes.add_quotes()


    @app.route('/categories', methods=['GET'])
    @basic_auth.required
    def list_categories():
        return api.categories.list_categories()


    @app.route('/categories/add', methods=['POST'])
    @basic_auth.required
    def add_categories():
        return api.categories.add_categories()


    app.run()
