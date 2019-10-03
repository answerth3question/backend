from flask.json import JSONEncoder
from flask_sqlalchemy import Pagination
from datetime import date, tzinfo, timedelta
from uuid import UUID
from app.database.db import db

class SimpleUTC(tzinfo):
  def tzname(self, **kwargs):
    return 'UTC'

  def utcoffset(self, dt):
    return timedelta(0)

  
class CustomJSONEncoder(JSONEncoder):
  def default(self, obj):
    if isinstance(obj, date):
      return obj.replace(tzinfo=SimpleUTC()).isoformat()
    elif isinstance(obj, timedelta):
      return str(obj)
    elif isinstance(obj, UUID):
      return str(obj)
    elif isinstance(obj, db.Model):
      return obj.as_dict()
    elif isinstance(obj, Pagination):
      return dict(
        page=obj.page,
        per_page=obj.per_page,
        total=obj.total,
        items=obj.items,
        has_next=obj.has_next,
        next_num=obj.next_num,
        has_prev=obj.has_prev,
        prev_num=obj.prev_num
      )
    return JSONEncoder.default(obj)

    