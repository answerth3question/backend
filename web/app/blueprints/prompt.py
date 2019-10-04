'''
prompt_bp endpoints should be used to get and submit prompts.
'''
from flask import Blueprint, request, jsonify, abort
from app.util.jwt_manager import with_permission, get_jwt_identity, jwt_optional, get_jwt_claims
from app.database.models import Prompt
from app.util.validators import PromptReq

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
@jwt_optional
def get_approved_prompts():
  try:
    args = PromptReq.get(request.args)
    claims = get_jwt_claims()
    is_reviewer = 'reviewer' in claims.get('permission', [])
    approved = Prompt.get_paginated(status='approved',
                                    include_reviews=is_reviewer)
    return jsonify(approved)
  except BaseException as e:
    print('hshdhdhd',e)
    abort(500)


@prompt_bp.route('/pending', methods=['GET'])
# @with_permission('reviewer')
def get_pending_prompts():
  try:
    args = PromptReq.get(request.args)
    print('ARRRRGS', args)
    if args['sort_order'] == 'desc':

      pending = Prompt.new_to_old(status='pending',
                                  cursor=args['cursor'],
                                  limit=args['limit'])
    else:
      pending = Prompt.old_to_new(status='pending',
                                  cursor=args['cursor'],
                                  limit=args['limit'])

    # pending = Prompt.get_paginated(status='pending',
    #                               include_reviews=True,
    #                               desc=False)
    return jsonify(pending)
  except BaseException as e:
    print('error getting pending prompts:', e)
    abort(500)


@prompt_bp.route('/rejected', methods=['GET'])
@with_permission('reviewer')
def get_rejected_prompts():
  try:
    args = PromptReq.get(request.args)
    rejected = Prompt.get_paginated(status='rejected',
                                    include_reviews=True,)
    return jsonify(rejected)
  except BaseException as e:
    print(e)
    abort(500)


@prompt_bp.route('/page', methods=['GET'])
def get_page():
  cursor = request.args.get('cursor')
  limit = request.args.get('limit', 2, type=int)
  status = request.args.get('status', 'pending')
  try:
    no = Prompt.new_to_old(cursor=cursor, status='approved', limit=limit)
    on = Prompt.old_to_new(cursor=cursor, status='approved', limit=limit)
    return jsonify({ 'new_to_old': no, 'old_to_new': on })
  except ValueError as e:
    print(e)
    abort(500)

  
