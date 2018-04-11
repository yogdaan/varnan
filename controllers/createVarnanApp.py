from flask_restful import Resource, reqparse
class createApp(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('app', type=str)

        return parser.parse_args()



    
