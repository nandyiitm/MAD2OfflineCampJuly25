from flask import Flask, render_template, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

CORS(app)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

# connecting database
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_database.db'
db.init_app(app)

# connecting api resources to endpoints
from controllers import UserResource, LoginResource

api.add_resource(LoginResource, '/login')
api.add_resource(UserResource, '/users', '/users/<user_id>')




if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        # users = {
        #     User(email='user0@mad2.com', name='User0', password='12345678'),
        #     User(email='user1@mad2.com', name='User1', password='12345678'),
        #     User(email='user2@mad2.com', name='User2', password='12345678'),
        #     User(email='user3@mad2.com', name='User3', password='12345678')
        # }
        # for user in users:
        #     db.session.add(user)
        # db.session.commit()

        admin = User.query.filter_by(email='admin@mad2.com').first()
        if not admin:
            user = User(email='admin@mad2.com', name='Admin', password='12345678', role='admin')
            db.session.add(user)
            db.session.commit()
            print('Admin Created!\n email: admin@mad2.com, password: 12345678')

        app.run(debug=True)