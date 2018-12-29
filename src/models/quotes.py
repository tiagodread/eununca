from flask import jsonify, request, Response

from . import db, ma


class Quotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    quality = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    def __init__(self, id=None, description=None, quality=None, category_id=None):
        self.id = id
        self.description = description
        self.quality = quality
        self.category_id = category_id

    def list_quotes(self):
        quotes = Quotes.query.all()
        quote_schema = QuoteSchema(many=True)
        out = quote_schema.dump(quotes).data
        return jsonify({'quotes': out})

    def add_quotes(self):
        description = request.form['description']
        quality = request.form['quality']
        category_id = request.form['category_id']
        quote = Quotes(None, description, quality, category_id)
        db.session.add(quote)
        db.session.commit()
        return Response(status=201)


class QuoteSchema(ma.ModelSchema):
    class Meta:
        model = Quotes
        include_fk = True
