import uuid
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from app.db import db

class PostContent(db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  text = db.Column(db.String(1000) , nullable=False)
  user_post_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user_post.id'), nullable=False)

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()