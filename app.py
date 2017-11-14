from flask import Flask
from flask_restful import Resource, Api
import controller

# from redis import Redis

app = Flask(__name__)
api = Api(app)

# Create of CRUD
api.add_resource(controller.apiV0AddU, '/api/v1/post/user')
api.add_resource(controller.apiV0AddI, '/api/v1/post/item')

# Read of CRUD
api.add_resource(controller.apiV0All, '/api/v1/get/all')
api.add_resource(controller.apiV0Main, '/api/v1/get/<user_id>')

# Update of CRUD
### error: if <user_id> is <int:user_id>, this part causes an error. So the data type is changed in model.update method.
api.add_resource(controller.apiV0Evaluation, '/api/v1/put/<user_id>/<item_id>/<evaluation>')


# Delete of CRUD
api.add_resource(controller.apiV0DeleteUser, '/api/v1/delete/user/<int:user_id>')
api.add_resource(controller.apiV0DeleteItem, '/api/v1/delete/item/<int:item_id>')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)