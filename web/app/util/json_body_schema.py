import uuid
from voluptuous import Schema, All, Required, Date, Invalid, REMOVE_EXTRA

date_formats = {
  'date': '%Y-%m-%d',
  'timestamptz': '$Y-%m-%dT%H:%M:%S.%f%z',
}

def json_from(source, schema):
  if source:
    return schema(dict(source), extra=REMOVE_EXTRA)
  return {}

class CustomValidators:
  UUID = lambda val: str(uuid.UUID(val))
  Coerce = lambda some_python_type: lambda val: some_python_type(val)


class JSONSchema:
  @classmethod
  def oauth_register_user(source, Schema({
    Required("sub"): str,
  }))
