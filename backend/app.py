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
from controllers import QuoteResource, LoginResource, RegisterResource

api.add_resource(LoginResource, '/login')
api.add_resource(RegisterResource, '/register')
api.add_resource(QuoteResource, '/quotes', '/quotes/<quote_id>')




if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        admin = User.query.filter_by(email='admin@mad2.com').first()
        if not admin:
            user = User(email='admin@mad2.com', name='Admin', password='12345678', role='admin')
            db.session.add(user)
            db.session.commit()
            print('Admin Created!\n email: admin@mad2.com, password: 12345678')

        app.run(debug=True)