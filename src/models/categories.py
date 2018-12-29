from flask import jsonify, request, Response

from . import db, ma


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    img_url = db.Column(db.String(255), nullable=False)
    paid = db.Column(db.Boolean, nullable=False)
    quotes = db.relationship('Quotes', backref='categories', lazy=True)

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

        if paid == 'False':
            paid = False
        elif paid == 'True':
            paid = True

        category = Categories(None, name, img_url, paid)
        db.session.add(category)
        db.session.commit()
        return Response(status=201)

    def __repr__(self):
        return '<Category %r>' % self.name


class CategorySchema(ma.ModelSchema):
    class Meta:
        model = Categories
        exclude = ['quotes']
