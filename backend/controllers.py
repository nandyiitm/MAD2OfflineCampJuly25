from flask_restful import Resource, Api
from flask import request
from flask_caching import Cache

cache = Cache()

from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from models import db, User, Quote

class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email', None)
        password = data.get('password', None)
        if not email or not password:
            return {'msg': "Please provide all required information!"}, 400
        user = User.query.filter_by(email=email).first()
        if not user:
            return {'msg': "User doesn't exists!"}, 404
        if user.password != password:
            return {'message': "Invalid credentials"}, 400
        token = create_access_token(identity=user.email)
        return {'message': "Successfully Loggedin!", 'token': token, 'user': user.to_dict()}
    
class RegisterResource(Resource):
    def post(self):
        data = request.get_json()
        name = data.get('name', None)
        email = data.get('email', None)
        password = data.get('password', None)
        if not email or not name or not password:
            return {'msg': "Please provide all required information!"}, 400
        user = User.query.filter_by(email=email).first()
        if user:
            return {'msg': "User already exists!"}, 404
        user = User(email=email, name=name, password=password)
        db.session.add(user); db.session.commit()
        return {'msg': "Successfully Registered!"}, 200

def is_admin():
    identity = get_jwt_identity()
    print(identity)
    user = User.query.filter_by(email=identity).first()
    if user.role != 'admin':
        return False
    return True

import time

class QuoteResource(Resource):

    # @jwt_required()
    @cache.cached(timeout=60)
    def get(self, quote_id=None):

        time.sleep(10)
        
        if quote_id:
            quote = Quote.query.get(quote_id)
            if quote:
                return {'msg': "quote found", 'quote': quote.to_dict()}
            return {'msg': "Quote not found!"}, 404
        quotes = Quote.query.all()
        quotes = [quote.to_dict() for quote in quotes]
        return {"msg": "All quotes", "quotes": quotes}
    
    @jwt_required()
    def post(self, quote_id=None):
        print(get_jwt_identity())
        if not is_admin(): return {'message': 'Not authorized'}, 401

        data = request.get_json()
        author = data.get('author', None)
        author_image = data.get('author_image', None)
        text = data.get('text', None)
        if not author or not author_image or not text:
            return {'msg': "Please provide all required information!"}, 400
        quote = Quote(author=author, author_image=author_image, text=text)
        db.session.add(quote); db.session.commit()
        return {'msg': "Successfully created quote!", 'quote': quote.to_dict()}
    
    @jwt_required()
    def put(self, quote_id=None):
        if not is_admin(): return {'message': 'Not authorized'}, 401

        if not quote_id:
            return {'msg': "Quote id is required to update!"}, 400
        quote = Quote.query.get(quote_id)
        if not quote:
            return {'msg': "Quote not exists to update!"}, 404
        data = request.get_json()
        author = data.get('author', None)
        author_image = data.get('author_image', None)
        text = data.get('text', None)
        if not author or not author_image or not text:
            return {'msg': "Please provide all required information!"}, 400
        quote.author = author; quote.author_image = author_image; quote.text = text
        db.session.commit()
        return {'msg': "Quote information updated!", 'quote': quote.to_dict()}, 200
    
    @jwt_required()
    def delete(self, quote_id=None):

        if not is_admin(): return {'message': 'Not authorized'}, 401

        if not quote_id:
            return {'msg': "Quote id is required to delete!"}, 400
        quote = Quote.query.get(quote_id)
        if not quote:
            return {'msg': "Quote not exists to delete!"}, 404
        db.session.delete(quote)
        db.session.commit()
        return {'msg': "Quote has been delete!"}, 200
