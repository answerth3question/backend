'''
prompt_bp endpoints should be used to get and submit prompts.
'''


from flask import Blueprint, request, jsonify, abort
from app.util.jwt_manager import with_permission, get_jwt_identity
from app.database.models import Prompt

prompt_bp = Blueprint('prompt_bp', __name__)

@prompt_bp.route('/', methods=['GET', 'POST'])
# @with_permission('contributer')
def prompt():
  user_id = get_jwt_identity()

  if request.method == 'GET':
    try:
      return jsonify({ 'prompts': Prompt.query.all() })

    except BaseException as e:
      print(e)
      abort(500)
  
  elif request.method == 'POST':
    try:
      # body = request.get_json()

      # prompt = PostPrompt(text=body['text'])

      # prompt.save_to_db()

      return 'success', 201

    except BaseException as e:
      print(e)
      abort(500)