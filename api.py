from flask import Flask
from flask_restful import Api
from controllers import testController, createVarnanApp
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

api = Api(app)

api.add_resource(testController.testController, '/')
api.add_resource(createVarnanApp.createApp, '/create')

if __name__ == '__main__':
    app.run(debug=True)

