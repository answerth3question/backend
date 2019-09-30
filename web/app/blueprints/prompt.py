'''
prompt_bp endpoints should be used to get and submit prompts.
'''
from flask import Blueprint, request, jsonify, abort
from app.util.jwt_manager import with_permission, get_jwt_identity
from app.database.models import Prompt

prompt_bp = Blueprint('prompt_bp', __name__)

@prompt_bp.route('/create', methods=['POST'])
@with_permission('contributer')
def create_prompt():
  try:
    user_id = get_jwt_identity()
    body = request.get_json()
    prompt = Prompt(created_by=user_id, 
                    content=body['content'])
    prompt.save_to_db()
    return 'success', 201
  except BaseException as e:
    print(e)
    abort(500)

@prompt_bp.route('/approved', methods=['GET'])
def get_approved_prompts():
  try:
    approved = Prompt.get_approved()
    return jsonify(approved)
  except BaseException as e:
    print(e)
    abort(500)

@prompt_bp.route('/pending', methods=['GET'])
@with_permission('reviewer')
def get_pending_prompts():
  try:
    pending = Prompt.get_pending()
    return jsonify(pending)
  except BaseException as e:
    print(e)
    abort(500)

@prompt_bp.route('/rejected', methods=['GET'])
@with_permission('reviewer')
def get_rejected_prompts():
  try:
    rejected = Prompt.get_rejected()
    return jsonify(pending)
  except BaseException as e:
    print(e)
    abort(500)

@prompt_bp.route('/all', methods=['GET'])
@with_permission('reviewer')
def get_all_prompts():
  try:
    return jsonify({
      'pending': Prompt.get_pending(),
      'rejected': Prompt.get_rejected(),
      'approved': Prompt.get_approved(),
    })
  except BaseException as e:
    print(e)
    abort(500)
