from flask import Flask
from flask_restful import Resource, Api
import controller

# from redis import Redis

app = Flask(__name__)
api = Api(app)
# redis = Redis(host='redis', port=6379)

api.add_resource(controller.apiV0Main, '/api/v1/get/<user_id>')
api.add_resource(controller.apiV0Evaluation, '/api/v1/post')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)