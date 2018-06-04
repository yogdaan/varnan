import sqlite3
from flask_restful import Resource, reqparse
from models.exceptionModel import ExceptitonLogsModel


class ExceptionLogs(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('url',
                        type=str,
                        required=True,
                        help=""
                        )
    parser.add_argument('exception',
                        type=str,
                        required=True,
                        help=""
                        )

    parser.add_argument('message',
                        type=str,
                        required=True,
                        help=""
                        )

    def post(self):
        data = ExceptionLogs.parser.parse_args()
        model = ExceptitonLogsModel(**data)
        model.save_to_db()

        return {
                   "success": "ture"
               }, 201
