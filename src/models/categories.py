from flask import jsonify, request, Response

from src.models.quotes import Quotes
from . import db, ma, get_paid_or_free_category


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    img_url = db.Column(db.String(255), nullable=False)
    paid = db.Column(db.Boolean, nullable=False)
    quotes = db.relationship(Quotes, backref='categories', lazy=True)

    def __init__(self, id=None, name=None, img_url=None, paid=None):
        self.id = id
        self.name = name
        self.img_url = img_url
        self.paid = paid

    def list_categories(self):
        categories = Categories.query.all()
        category_schema = CategorySchema(many=True)
        out = category_schema.dump(categories).data
        return jsonify({'categories': out})

    def add_categories(self):
        name = request.form['name']
        img_url = request.form['img_url']
        paid = request.form['paid']
        paid = get_paid_or_free_category(paid)

        category = Categories(None, name, img_url, paid)
        db.session.add(category)
        db.session.commit()
        return Response(status=201)

    def edit_category(self, id):
        name = request.form['name']
        img_url = request.form['img_url']
        paid = request.form['paid']
        paid = get_paid_or_free_category(paid)

        category = db.session.query(Categories).filter_by(id=id).first()
        category.name = name
        category.img_url = img_url
        category.paid = paid
        db.session.add(category)
        db.session.commit()
        return Response(status=200)

    def delete_category(self, id):
        category = db.session.query(Categories).filter_by(id=id).first()
        db.session.delete(category)
        db.session.commit()
        return Response(status=200)

    def __repr__(self):
        return '<Category %r>' % self.name


class CategorySchema(ma.ModelSchema):
    class Meta:
        model = Categories
        exclude = ['quotes']
