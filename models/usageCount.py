from db import db


class UsageCountModel(db.Model):
    __tablename__ = 'UsageCount'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(80))
    count = db.Column(db.Integer, default=1)

    def __init__(self, url):
        self.url = url

    def save_to_db(self):
        obj = self.find_by_url(self.url)
        if obj is None:
            db.session.add(self)
            db.session.commit()
        else:
            obj.count = obj.count + 1
            db.session.commit()

    @classmethod
    def find_by_url(cls, url):
        return cls.query.filter_by(url=url).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
