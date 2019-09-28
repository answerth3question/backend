from app.database.db import db

class ReviewStatusKind(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, primary_key=True)