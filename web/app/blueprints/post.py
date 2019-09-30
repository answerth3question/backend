'''
post_bp endpoints should be used to get and submit posts.
to get posts specific to a given user, use the user_bp endpoints
'''
from flask import Blueprint, request, jsonify, abort
from app.util.jwt_manager import with_permission, get_jwt_identity
from app.database.models import Post

post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/create', methods=['POST'])
@with_permission('contributer')
def create_post():
  try:
    user_id = get_jwt_identity()
    body = request.get_json()
    post = Post(created_by=user_id,
                content=body['content'],
                prompt_id=body['prompt_id'])
    post.save_to_db()
    return 'success', 201
  except BaseException as e:
    print(e)
    abort(500)

@post_bp.route('/approved', methods=['GET'])
def get_approved_posts():
  try:
    approved = Post.get_approved()
    return jsonify(approved)
  except BaseException as e:
    print(e)
    abort(500)  

@post_bp.route('/pending', methods=['GET'])
@with_permission('reviewer')
def get_pending_posts():
  try:
    pending = Post.get_pending()
    return jsonify(pending)
  except BaseException as e:
    print(e)
    abort(500)  

@post_bp.route('/rejected', methods=['GET'])
@with_permission('reviewer')
def get_rejected_posts():
  try:
    rejected = Post.get_rejected()
    return jsonify(rejected)
  except BaseException as e:
    print(e)
    abort(500)  

@post_bp.route('/all', methods=['GET'])
@with_permission('reviewer')
def get_all_posts():
  try:
    return jsonify({
      'pending': Post.get_pending(),
      'rejected': Post.get_rejected(),
      'approved': Post.get_approved(),
    })
  except BaseException as e:
    print(e)
    abort(500)

