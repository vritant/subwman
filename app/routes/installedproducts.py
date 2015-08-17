from app import app, db
from app.models import installedProducts
from flask import abort, jsonify, request
import datetime
import json

@app.route('/subwman/installedproducts', methods = ['GET'])
def get_all_installedproducts():
    return '[\
        {\
            "id": "1",\
            "productId": "71",\
            "name": "Awesome OS Workstation",\
            "version": "1.2",\
            "arch": "x86_64",\
            "status": "Subscribed",\
            "subscriptions": "CUSTOM SKU",\
            "startDate": "2015-08-14T14:13:45.224+0000",\
            "endDate": "2015-08-14T14:13:45.224+0000",\
            "created": "2015-08-14T14:13:45.224+0000",\
            "updated": "2015-08-14T14:13:45.224+0000"\
        },\
        {\
            "id": "2",\
            "productId": "71",\
            "name": "Another Awesome OS Workstation",\
            "version": "1.223",\
            "arch": "x86_64",\
            "status": "Subscribed",\
            "subscriptions": "CUSTOM SKU",\
            "startDate": "2015-08-14T14:13:45.224+0000",\
            "endDate": "2015-08-14T14:13:45.224+0000",\
            "created": "2015-08-14T14:13:45.224+0000",\
            "updated": "2015-08-14T14:13:45.224+0000"\
        },\
        {\
            "id": "3",\
            "productId": "71",\
            "name": "Not Awesome OS Workstation",\
            "version": "231.2",\
            "arch": "x86_64",\
            "status": "Subscribed",\
            "subscriptions": "CUSTOM SKU",\
            "startDate": "2015-08-14T14:13:45.224+0000",\
            "endDate": "2015-08-14T14:13:45.224+0000",\
            "created": "2015-08-14T14:13:45.224+0000",\
            "updated": "2015-08-14T14:13:45.224+0000"\
        },\
        {\
            "id": "4",\
            "productId": "71",\
            "name": "So Awesome OS Workstation",\
            "version": "1.223",\
            "arch": "x86_64",\
            "status": "Expired",\
            "subscriptions": "CUSTOM SKU",\
            "startDate": "2011-08-14T14:13:45.224+0000",\
            "endDate": "2012-08-14T14:13:45.224+0000",\
            "created": "2011-08-14T14:13:45.224+0000",\
            "updated": "2012-08-14T14:13:45.224+0000"\
        },\
        {\
            "id": "5",\
            "productId": "179",\
            "name": "Awesome OS Developer Toolset (for Awesome Workstation)",\
            "version": "4.32",\
            "arch": "x86_64",\
            "status": "Subscribed",\
            "subscriptions": "CUSTOM SKU",\
            "startDate": "2015-08-14T14:13:45.224+0000",\
            "endDate": "2015-08-14T14:13:45.224+0000",\
            "created": "2015-08-14T14:13:45.224+0000",\
            "updated": "2015-08-14T14:13:45.224+0000"\
        }\
    ]'

@app.route('/subwman/installedproducts/<int:id>', methods = ['GET'])
def get_installedProducts(id):
    return '{\
            "id": "2",\
            "productId": "179",\
            "name": "Awesome OS Developer Toolset (for Awesome Workstation)",\
            "version": "4.32",\
            "arch": "x86_64",\
            "status": "Subscribed",\
            "subscriptions": "CUSTOM SKU",\
            "startDate": "2015-08-14T14:13:45.224+0000",\
            "endDate": "2015-08-14T14:13:45.224+0000",\
            "created": "2015-08-14T14:13:45.224+0000",\
            "updated": "2015-08-14T14:13:45.224+0000"\
        }'

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
