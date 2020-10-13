from application import db # as if from __init__ import db

class Set(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    w = db.Column(db.Float, nullable=False)
    r = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.name} on {self.week}: {self.w} x {self.r}'
