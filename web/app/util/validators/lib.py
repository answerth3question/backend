import uuid
from voluptuous import *

def json_from(source, schema_dict):
  if source:
    schema = Schema(schema_dict, extra=REMOVE_EXTRA)
    return schema(dict(source))
  return {}

class Custom:
  UUID = lambda val: str(uuid.UUID(val))
