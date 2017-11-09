from flask import Flask
from flask_restful import Resource, Api
import recomm

class apiV0Main(Resource):
    def get(self,user_id):
        target_user_index = int(user_id)
        print(target_user_index)
        similarities = recomm.get_correlation_coefficents(recomm.scores, target_user_index)
        suggestion = recomm.rank_items(recomm.scores, similarities, target_user_index)
        return suggestion


class apiV0Evaluation(Resource):
    def post(self):
        return {'hello world': 'post'}








# from flask_restful import reqparse, Resource, Api
#
# def classproperty(func):
#     if not isinstance(func, (classmethod, staticmethod)):
#         func = classmethod(func)
#
#     return ClassPropertyDescriptor(func)
#
#
# class ApiController(Resource):
#     NAME_SPACE = "/api/v1"
#
#     def __init__(self):
#         self.__create_parser()
#
#     @classproperty
#     def endpoint(self):
#         '''
#         Get an endpoint path
#
#         Return: {String}
#         '''
#
#
#         return self.NAME_SPACE + self.path
#
#     @classproperty
#     # @abstractmethod
#     def path(self):
#         '''
#         Get a relative path
#
#         Expects:
#           Return: {String}
#         '''
#
#         pass