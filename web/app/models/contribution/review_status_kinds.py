from app.db import db

class ReviewStatusKind(db.Model):
  name = db.Column(db.String, primary_key=True)