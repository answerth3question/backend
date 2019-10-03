import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from flask import request
from app.database.db import db

class Prompt(db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  date_created = db.Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
  created_by = db.Column(UUID(as_uuid=True), db.ForeignKey('registered_user.id'), nullable=False)
  content = db.Column(db.String(240), nullable=False)
  status = db.Column(db.String, db.ForeignKey('review_status_kind.name'), default='pending')
  posts = db.relationship('Post', lazy='dynamic', 
                          backref=db.backref('prompt', lazy='joined', uselist=False))
  reviews = db.relationship('PromptReview', lazy='dynamic')

  def as_dict(self, include_reviews=False):
    ret = {}
    if include_reviews:
      ret.update({'reviews': self.reviews.all()})
    ret.update({ c.name: getattr(self, c.name) for c in self.__table__.columns })
    return ret

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_paginated(cls, status='', include_reviews=False, order_by='date_created', desc=True):
    result = cls.query.filter_by(status=status)\
      .order_by(getattr(cls, order_by).desc() if desc else getattr(cls, order_by).asc())\
      .paginate()
    
    return dict(
      page=result.page,
      has_next=result.has_next,
      per_page=result.per_page,
      items=[x.as_dict(include_reviews) for x in result.items]
    )
