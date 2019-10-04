import uuid
from voluptuous import *

def json_from(source, template):
  def strong_schema(schema_dict):
    accum = {}
    for key in schema_dict:
      val = schema_dict[key]
      if type(key) is tuple:
        field = key[0]
        if len(key) == 2:
          accum.update({ Required(field, default=key[1]): val })
        else:
          raise 'Incorrect number of items in key tuple. Did you forget to specify a default value?'
      elif type(key) is str:
        accum.update({ Required(key, default=None): val })
    return accum

  schema = Schema(strong_schema(template), extra=REMOVE_EXTRA)
  return schema(dict(source))

class Custom:
  UUID = lambda val: val and str(uuid.UUID(val))
