from api import db

class StatusLogs(db.Model):
    __tablename__ = 'StatusLogs'
    id = db.Column(db.Integer, db.Sequence('id', start=1, increment=1),primary_key=True)
    url = db.Column(db.String(80))
    status = db.Column(db.String(120))

    def __init__(self, url, status):
        self.url = url
        self.status = status

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
    
if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    