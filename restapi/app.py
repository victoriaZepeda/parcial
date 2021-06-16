from flask import Flask
from flask_restful import Api
from resources.store_resource import Store

app = Flask(__name__)
api = Api(app)

api.add_resource(Store, "/store")

if __name__ == "__main__":
    app.run(debug=True, port=23512)
