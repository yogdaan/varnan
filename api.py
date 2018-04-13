from flask import Flask
from flask_restful import Api
import createVarnanApp as cva
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
api.add_resource(cva.createApp, '/api/hello')

if __name__ == '__main__':
    app.run(debug=True)
