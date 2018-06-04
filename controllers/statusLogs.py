import sqlite3
from flask_restful import Resource, reqparse
from models.statusLogs import StatusLogsModel


class StatusLogs(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('url',
                        type=str,
                        required=True,
                        help=""
                        )

    parser.add_argument('status',
                        type=str,
                        required=True,
                        help=""
                        )

    def post(self):
        data = StatusLogs.parser.parse_args()
        statuslogs = StatusLogsModel(**data)
        statuslogs.save_to_db()

        return {
                   "success": "ture",
               }, 201
