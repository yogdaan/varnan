import sqlite3
from flask_restful import Resource, reqparse
from models.usageCount import UsageCountModel


class UsageCount(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('url',
                        type=str,
                        action='append',
                        help=""
                        )

    def post(self):
        data = UsageCount.parser.parse_args()
        usage = UsageCountModel(**data)
        usage.save_to_db()
        return {
                   "success": "true",
               }, 201
