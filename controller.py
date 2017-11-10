from flask import Flask
from flask_restful import Resource, Api
import recomm
import json

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

class apiV0Evaluation(Resource):
    def post(self):
        return {'hello world': 'post'}
