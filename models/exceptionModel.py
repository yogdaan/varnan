from db import db


class ExceptitonLogsModel(db.Model):
    __tablename__ = 'exceptions'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(80))
    exception = db.Column(db.String(80))
    message = db.Column(db.String(80))

    def __init__(self, url, exception, message):
        self.url = url
        self.exception = exception
        self.message = message

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_url(cls, url):
        return cls.query.filter_by(url=url).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
