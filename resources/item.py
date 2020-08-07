from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
import sqlite3

class Item(Resource):
    TABLE_NAME = 'ნაყინი'  # ცხრილის დასახელება

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="გთხოვთ შეიყვანოთ პროდუქტის ღირებულება")

    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': f'მონაცემი {name} ბაზაში ვერ მოიძებნა'}, 404

    def post(self, name):
        # check if item is already in db
        # if no > add the item
        # if yes > return the message
        if ItemModel.find_by_name(name):
            return {'message': f'მონაცემი {name} ბაზაში უკვე არსებობს'}, 400

        data = Item.parser.parse_args()  # data = {"price" : 2.5}


        item = ItemModel(name, data["price"])

        try:
            item.save_to_db()
        except Exception as e:
            return {"message": f"{e}"}
        else:
            return item.json()

    def put(self, name):
        # check if the item is in the db
        # if item > Update
        # if item is None > Insert

        item = ItemModel.find_by_name(name)  # check the db
        data = Item.parser.parse_args()  # take the params from request

        if item: # UPDATE
            item.price = data['price']

        else: # INSERT
            item = ItemModel(name, data['price'])

        item.save_to_db()

        return {"item": item.json()}

    def delete(self, name):
        item = ItemModel.find_by_name(name)

        if item:
            item.delete_from_db()
            return {'message': 'მონაცემი წარმატებით წაიშალა'}
        else:
            return {'message': 'მონაცემი ბაზაში ვერ მოიძებნა'}


class ItemList(Resource):
    @jwt_required()
    def get(self):

        return {"მენიუ": items}
