from flask import Flask
from flask_basicauth import BasicAuth, Response

from .api import Api
from .models import db
from .utils.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.run()
db.init_app(app)
db.app = app
db.create_all()
api = Api()
basic_auth = BasicAuth(app)


@app.route('/', methods=['GET'])
def health():
    return Response(status=200)


@app.route('/quotes', methods=['GET'])
@basic_auth.required
def list_quotes():
    return api.quotes.list_quotes()


@app.route('/quotes/add', methods=['POST'])
@basic_auth.required
def add_quotes():
    return api.quotes.add_quotes()


@app.route('/quotes/edit/<id>', methods=['PUT'])
@basic_auth.required
def update_quotes(id):
    return api.quotes.update_quote(id)


@app.route('/quotes/delete/<id>', methods=['DELETE'])
@basic_auth.required
def delete_quotes(id):
    return api.quotes.delete_quote(id)


@app.route('/categories', methods=['GET'])
@basic_auth.required
def list_categories():
    return api.categories.list_categories()


@app.route('/categories/add', methods=['POST'])
@basic_auth.required
def add_categories():
    return api.categories.add_categories()


@app.route('/categories/edit/<id>', methods=['PUT'])
@basic_auth.required
def edit_categories(id):
    return api.categories.edit_category(id)


@app.route('/categories/delete/<id>', methods=['DELETE'])
@basic_auth.required
def delete_categories(id):
    return api.categories.delete_category(id)
