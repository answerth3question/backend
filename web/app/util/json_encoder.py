from flask.json import JSONEncoder
from datetime import date, tzinfo, timedelta
from app.db import db

class SimpleUTC(tzinfo):
  def tzname(self, **kwargs):
    return 'UTC'

  def utcoffset(self, dt):
    return timedelta(0)

  
class CustomJSONEncoder(JSONEncoder):
  def default(self, obj):
    if isinstance(obj, date):
      return obj.replace(tzinfo=SimpleUTC()).isoformat()
    if isinstance(obj, timedelta):
      return str(obj)
    if isinstance(obj, db.Model):
      return str(obj.__dict__)
    return JSONEncoder.default(obj)