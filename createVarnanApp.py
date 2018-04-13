from flask_restful import Resource, reqparse
import Models as mada

class createApp(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('app', type=str)
        k = mada.StatusLogs("asd","asd")
        return parser.parse_args()



    
