from app.util.validators.lib import json_from, Coerce, All, Any, Required

class PromptReq:

  @classmethod
  def get(cls, src):
    return json_from(src, {
      # Required('include_reviews', default=0): Coerce(int),

      Required('page', default=1): Coerce(int),

      Required('per_page', default=20): Coerce(int),

      Required('order_by', default='date_created'): All(str, Any('date_created')),

      Required('sort_order', default='desc'): All(str, Any('asc', 'desc'))
    })