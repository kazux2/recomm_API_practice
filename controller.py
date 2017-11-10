from flask import Flask
from flask_restful import Resource, Api
import recomm
import json

# Create of CRUD
class apiV0Add(Resource):
    def post(self):
        return {'hello world': 'post'}

# Read of CRUD
class apiV0All(Resource):
    def get(self):
        all_list = recomm.scores
        result = json.dumps(all_list.tolist())
        return result

class apiV0Main(Resource):
    def get(self,user_id):
        target_user_index = int(user_id)
        print(target_user_index)
        similarities = recomm.get_correlation_coefficents(recomm.scores, target_user_index)
        suggestion = recomm.rank_items(recomm.scores, similarities, target_user_index)
        return {user_id: suggestion}

# Update of CRUD
class apiV0Evaluation(Resource):
    def put(self, user_id, item_id, evaluation):

        return {'hello world': 'post'}

# Delete of CRUD
class apiV0Delete(Resource):
    def delete(self):
        return {'hello world': 'delete'}










