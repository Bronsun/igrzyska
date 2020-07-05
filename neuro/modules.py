from datetime import datetime
from neuro import db


class Duda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)  
    answer = db.Column(db.Text, nullable=True)
    
    def __repr__(self):
        return f"Duda('{self.answer}', '{self.date_posted}')"


class Trzask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    answer = db.Column(db.Text, nullable=True)
   
    def __repr__(self):
        return f"Trzask('{self.answer}', '{self.date_posted}')"

