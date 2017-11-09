from flask import Flask
from flask_restful import Resource, Api

# import recomm
# from redis import Redis

app = Flask(__name__)
api = Api(app)

"""THIS WORKED!! 11/09 14:40"""


# redis = Redis(host='redis', port=6379)

class apiV0Main(Resource):
    def get(self, user_id):
        # predict_score = recomm.predict_score
        # rank = recomm.rank
        got_user_id = user_id

        return {"id": got_user_id}


class apiV0Evaluation(Resource):
    def post(self):
        return {'hello world': 'post'}


api.add_resource(apiV0Main, '/api/v1/get/<user_id>')
api.add_resource(apiV0Evaluation, '/api/v1/post')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)