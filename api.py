from flask import Flask
from flask_restful import Api
from controllers import testController

app = Flask(__name__)

api = Api(app)

api.add_resource(testController.testController, '/')

if __name__ == '__main__':
    app.run(debug=True)

