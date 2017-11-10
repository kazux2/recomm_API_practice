from flask import Flask
from flask_restful import Resource, Api
import controller

# from redis import Redis

app = Flask(__name__)
api = Api(app)
# redis = Redis(host='redis', port=6379)

# Create of CRUD
api.add_resource(controller.apiV0Add, '/api/v1/post')

# Read of CRUD
api.add_resource(controller.apiV0All, '/api/v1/get/all')
api.add_resource(controller.apiV0Main, '/api/v1/get/<user_id>')

# Update of CRUD
api.add_resource(controller.apiV0Evaluation, '/api/v1/put/<user_id>/<item_id>/<evaluation>')

# Delete of CRUD
api.add_resource(controller.apiV0Delete, '/api/v1/delete/delete')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)