from flask import Blueprint, request, jsonify, abort
from app.util.jwt_manager import with_permission, get_jwt_identity
from app.models import PostPrompt

prompt_bp = Blueprint('prompt_bp', __name__)

@prompt_bp.route('/', methods=['GET', 'POST'])
@with_permission('contributer')
def prompt():
  user_id = get_jwt_identity()

  if request.method == 'GET':
    try:
      pass
    except:
      abort(500)
  
  elif request.method == 'POST':
    try:
      body = request.get_json()

      prompt = PostPrompt(content=body['content'])

      prompt.save_to_db()

    except:
      abort(500)