from db import db

class StatusLogsModel(db.Model):

    __tablename__ = 'StatusLogs'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(80))
    status = db.Column(db.String(80))

    def __init__(self, url, status):
        self.url = url
        self.status = status

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_url(cls, url):
        return cls.query.filter_by(url=url).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
