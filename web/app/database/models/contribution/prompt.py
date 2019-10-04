import uuid
from datetime import datetime
from sqlalchemy import func
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


  # def as_dict(self, include_reviews=False):
  #   ret = {}
  #   if include_reviews:
  #     ret.update({'reviews': self.reviews.all()})
  #   ret.update({ c.name: getattr(self, c.name) for c in self.__table__.columns })
  #   return ret


  def save_to_db(self):
    db.session.add(self)
    db.session.commit()


  @classmethod
  def get_paginated(cls, status='', include_reviews=False, desc=True):
    result = cls.query.filter_by(status=status)\
      .order_by(cls.date_created.desc() if desc else cls.date_created.asc())\
      .paginate()
    
    return dict(
      page=result.page,
      has_next=result.has_next,
      per_page=result.per_page,
      items=[x.as_dict(include_reviews) for x in result.items]
    )
    

  @classmethod
  def new_to_old(cls, status='', cursor=None, limit=50):
    if not status:
      raise ValueError('no status provied')

    conditions = cls.status == status, # tuple
    if cursor:
      prompt = cls.query.get(cursor)
      conditions = cls.status == status, cls.date_created < prompt.date_created # tuple

    return cls.query.filter(*conditions)\
      .order_by(cls.date_created.desc())\
      .limit(limit)\
      .all()


  @classmethod
  def old_to_new(cls, status='', cursor=None, limit=50):
    if not status:
      raise ValueError('no status provied')

    conditions = cls.status == status,
    if cursor:
      prompt = cls.query.get(cursor)
      conditions = cls.status == status, cls.date_created > prompt.date_created
    
    return cls.query.filter(*conditions)\
      .order_by(cls.date_created.asc())\
      .limit(limit)\
      .all()


  # @classmethod
  # def get_cursored(cls, status='', reviews=False, order_by='date_created', sort_order='desc'):
  #   items = cls.query.filter_by(status=status)\
  #     .limit(20)\
  #     .order_by(cls.date_created.desc())
  #   # count = db.session.query(func.count(cls.id)).scalar()
  #   # items = cls.query.filter(cls.status==status).all()
  #   # return (count, items)
