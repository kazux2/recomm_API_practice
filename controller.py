from flask import Flask
from flask_restful import Resource, Api
import recomm
import json
import model

# Create of CRUD
class apiV0AddU(Resource):
    def post(self):
        new_user_id = model.createU()
        return {new_user_id: 'added'}


class apiV0AddI(Resource):
    def post(self):
        new_item_id = model.createI()
        return {new_item_id: 'added'}


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
        new_scores = model.update(user_id, item_id, evaluation)
        return {'renewed': new_scores}


# Delete of CRUD
class apiV0DeleteUser(Resource):
    def delete(self, user_id):
        result = model.deleteU(user_id)
        return {user_id: 'delete' + result}


class apiV0DeleteItem(Resource):
    def delete(self, item_id):
        result = model.deleteU(item_id)
        return {item_id: 'delete' + result}


