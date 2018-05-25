import os

from flask import Flask
from flask_restful import Api
from controllers.statusLogs import StatusLogs
from controllers.exceptionLogs import ExceptionLogs

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

api = Api(app)

api.add_resource(StatusLogs, '/statusLogs')
api.add_resource(ExceptionLogs, '/expetionLogs')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
    