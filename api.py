from flask import Flask
from flask_restful import Api
from controllers.statusLogs import StatusLogs
from controllers.exceptionLogs import ExceptionLogs
from controllers.usageCount import UsageCount
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

api = Api(app)

api.add_resource(StatusLogs, '/statusLogs')
api.add_resource(ExceptionLogs, '/expetionLogs')
api.add_resource(UsageCount, '/usageCount')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
