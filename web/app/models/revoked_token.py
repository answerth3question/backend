from app.db import db

class RevokedToken(db.Model):
  jti = db.Column(db.String(120), primary_key=True)

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def is_revoked(cls, jti):
    return bool(cls.query.filter_by(jti).first)