'''
prompt_bp endpoints should be used to get and submit prompts.
'''
from flask import Blueprint, request, jsonify, abort
from app.util.jwt_manager import with_permission, get_jwt_identity, jwt_optional, get_jwt_claims
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
@jwt_optional
def get_approved_prompts():
  try:
    claims = get_jwt_claims()
    include_reviews = request.args.get('include_reviews', type=int)
    include_reviews = include_reviews and 'reviewer' in claims.get('permission', [])
    approved = Prompt.get_paginated('approved', include_reviews)
    return jsonify(approved)
  except BaseException as e:
    print('hshdhdhd',e)
    abort(500)

@prompt_bp.route('/pending', methods=['GET'])
@with_permission('reviewer')
def get_pending_prompts():
  try:
    include_reviews = request.args.get('include_reviews', type=int)
    pending = Prompt.get_paginated('pending', include_reviews, desc=False)
    return jsonify(pending)
  except BaseException as e:
    print(e)
    abort(500)

@prompt_bp.route('/rejected', methods=['GET'])
@with_permission('reviewer')
def get_rejected_prompts():
  try:
    include_reviews = request.args.get('include_reviews', type=int)
    rejected = Prompt.get_paginated('rejected', include_reviews)
    return jsonify(rejected)
  except BaseException as e:
    print(e)
    abort(500)

@prompt_bp.route('/page', methods=['GET'])
def get_page():
  include = request.args.get('include', '').split(',')

  print(include)

  items = Prompt.query\
    .order_by(Prompt.date_created.desc())\
    .paginate()


  return jsonify(items)
