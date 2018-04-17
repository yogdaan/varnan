import os

from flask import Flask
from flask_restful import Api
from controllers.statusLogs import StatusLogs

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

api = Api(app)

api.add_resource(StatusLogs, '/statusLogs')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
    