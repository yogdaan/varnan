from flask_restful import Resource

class testController(Resource):

    def get(self):
        return {"test" : "test"} 
