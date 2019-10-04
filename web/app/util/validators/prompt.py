from app.util.validators.lib import json_from, Custom, Coerce, All, Any

class PromptReq:

  @classmethod
  def get(cls, src):
    return json_from(src, {
      'cursor': Custom.UUID,

      ('limit', 50): Coerce(int),

      ('sort_order', 'desc'): All(str, Any('asc', 'desc')),
    })