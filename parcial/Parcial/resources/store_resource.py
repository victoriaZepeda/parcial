from flask_restful import Resource, reqparse
from logic.store_logic import StoreLogic


class Store(Resource):
    def __init__(self):
        self.store_put_args = self.createParser()
        self.logic = StoreLogic()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("manager", type=str, help="numero de manager")
        args.add_argument("address", type=str, help="numero de direccion")
        args.add_argument("lastUpdate", type=int, help="ultimo update realizado")
        return args

    def head(self, id):
        pass

    def get(self, id):
        result = self.logic.getStoreById(id)
        if len(result) == 0:
            return {}
        else:
            return {"rowsAffefcted":rows},200

    def post(self, id):
        result = self.logic.getStoreById(id)
        if len(result) == 0:
            return {}
        else:
            return {"rowsAffefcted":rows},200

    def put(self, id):
        store = self.store_put_args.parse_args()
        rows = self.logic.insertStore(store)
        return {"rowsAffefcted": rows}, 200

    def patch(self, id):
        store = self.store_put_args.parse_args()
        rows = self.logic.updateStore(id, store)
        return {"rowsAffefcted": rows}, 200

    def delete(self, id):
        rows = self.logic.deleteStore(id)
        return {"rowsAffefcted": rows}, 200
