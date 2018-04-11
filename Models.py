from api import db

class StatusLogs(db.Model):
    __tablename__ = 'StatusLogs'
    id = db.Column(db.Integer, db.Sequence('id', start=1, increment=1),primary_key=True)
    url = db.Column(db.String(80))
    status = db.Column(db.String(120))

    def __init__(self, url, status):
        self.url = url
        self.status = status

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    