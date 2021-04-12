from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'disposable_tableware_rest.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_of_dishes = db.Column(db.String(80))
    amount_of_pieces = db.Column(db.Integer)
    origin_country = db.Column(db.String(80))
    material = db.Column(db.String(80))
    price = db.Column(db.Integer)
    brand = db.Column(db.String(80))
    thickness = db.Column(db.String(10))
    date_of_manufacture = db.Column(db.String(10))

    def __init__(self, type_of_dishes, amount_of_pieces, origin_country, material, price, brand, thickness,
                 date_of_manufacture):
        self.type_of_dishes = type_of_dishes
        self.amount_of_pieces = amount_of_pieces
        self.origin_country = origin_country
        self.material = material
        self.price = price
        self.brand = brand
        self.thickness = thickness
        self.date_of_manufacture = date_of_manufacture


class ItemSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('type_of_dishes', 'amount_of_pieces', 'origin_country', 'material', 'price', 'brand', 'thickness',
                  'date_of_manufacture')


item_schema = ItemSchema()
items_schema = ItemSchema(many=True)


# endpoint to create new item
@app.route("/item", methods=["POST"])
def add_item():
    type_of_dishes = request.json['type_of_dishes']
    amount_of_pieces = request.json['amount_of_pieces']
    origin_country = request.json['origin_country']
    material = request.json['material']
    price = request.json['price']
    brand = request.json['brand']
    thickness = request.json['thickness']
    date_of_manufacture = request.json['date_of_manufacture']

    new_item = Item(type_of_dishes, amount_of_pieces, origin_country, material, price, brand, thickness,
                    date_of_manufacture)

    db.session.add(new_item)
    db.session.commit()

    return jsonify(new_item)


# endpoint to show all items
@app.route("/item", methods=["GET"])
def get_item():
    all_items = Item.query.all()
    result = items_schema.dump(all_items)
    return jsonify(result)


# endpoint to get item detail by id
@app.route("/item/<id>", methods=["GET"])
def item_detail(id):
    item = Item.query.get(id)
    return item_schema.jsonify(item)


# endpoint to update item
@app.route("/item/<id>", methods=["PUT"])
def item_update(id):
    item = Item.query.get(id)
    type_of_dishes = request.json['type_of_dishes']
    amount_of_pieces = request.json['amount_of_pieces']
    origin_country = request.json['origin_country']
    material = request.json['material']
    price = request.json['price']
    brand = request.json['brand']
    thickness = request.json['thickness']
    date_of_manufacture = request.json['date_of_manufacture']

    item.type_of_dishes = type_of_dishes
    item.amount_of_pieces = amount_of_pieces
    item.origin_country = origin_country
    item.material = material
    item.price = price
    item.brand = brand
    item.thickness = thickness
    item.date_of_manufacture = date_of_manufacture

    db.session.commit()
    return item_schema.jsonify(item)


# endpoint to delete item
@app.route("/item/<id>", methods=["DELETE"])
def item_delete(id):
    item = Item.query.get(id)
    db.session.delete(item)
    db.session.commit()

    return item_schema.jsonify(item)


if __name__ == '__main__':
    app.run(debug=True)
