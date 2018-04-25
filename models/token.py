from db import db
import md5
import json

class Token(db.Model):

    __tablename__ = 'Tokens'

    token = db.Column(db.string(32))
    url = db.Column(db.string(80))
    user = db.Column(db.string(80))

    def __init__(self, url, user):
        self.url = url
        self.user = user
        self.generateToken()

    def generateToken(self):
        MD5 = md5.new()
        tokenObject = json.dumps({
            'user' : self.user,
            'url' : self.url
        })
        MD5.update(tokenObject)
        self.token = MD5.hexdigest

    def save_to_db(self):
        db.session.commit(self)
        db.session.commit()

    @classmethod
    def find_by_token(cls, token):
        return cls.query.filter_by(token=token).first()