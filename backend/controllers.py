from flask_restful import Resource, Api
from flask import request

from models import db, User

class UserResource(Resource):
    
    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
            if user:
                return {'msg': "user found", 'email': user.email, 'name': user.name}
            return {'msg': "User not found!"}, 404
        users = User.query.all()
        users = [user.to_dict() for user in users]
        return {"msg": "All users", "users": users}
    
    def post(self):
        data = request.get_json()
        email = data.get('email', None)
        name = data.get('name', None)
        if not email or not name:
            return {'msg': "Please provide all required information!"}, 400
        user = User.query.get(email)
        if user:
            return {'msg': "User already exists!"}, 400
        user = User(email=email, name=name)
        db.session.add(user); db.session.commit()
        return {'msg': "Successfully created user!"}
    
    def put(self, user_id=None):
        if not user_id:
            return {'msg': "User id is required to update!"}, 400
        user = User.query.get(user_id)
        if not user:
            return {'msg': "User not exists to update!"}, 404
        data = request.get_json()
        name = data.get('name', None)
        if not name:
            return {'msg': "Please provide all required information!"}, 400
        user.name = name
        db.session.commit()
        user = user.to_dict()
        return {'msg': "User information updated!", 'user': user}, 200
    
    def delete(self, user_id=None):
        if not user_id:
            return {'msg': "User id is required to delete!"}, 400
        user = User.query.get(user_id)
        if not user:
            return {'msg': "User not exists to delete!"}, 404
        db.session.delete(user)
        db.session.commit()
        return {'msg': "User has been delete!"}, 200
