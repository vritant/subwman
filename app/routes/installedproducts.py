from app import app, db
from app.models import installedProducts
from flask import abort, jsonify, request
import datetime
import json

@app.route('/subwman/installedproducts', methods = ['GET'])
def get_all_installedproducts():
    entities = installedProducts.InstalledProducts.query.all()
    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/subwman/installedproducts/<int:id>', methods = ['GET'])
def get_installedProducts(id):
    entity = installedProducts.InstalledProducts.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())

@app.route('/subwman/installedproducts', methods = ['POST'])
def create_installedProducts():
    entity = installedProducts.InstalledProducts(
        name = request.json['name']
    )
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201

@app.route('/subwman/installedproducts/<int:id>', methods = ['PUT'])
def update_installedProducts(id):
    entity = installedProducts.InstalledProducts.query.get(id)
    if not entity:
        abort(404)
    entity = installedProducts.InstalledProducts(
        name = request.json['name'],
        id = id
    )
    db.session.merge(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 200

@app.route('/subwman/installedproducts/<int:id>', methods = ['DELETE'])
def delete_installedProducts(id):
    entity = installedProducts.InstalledProducts.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204
