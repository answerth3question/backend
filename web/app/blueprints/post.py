from flask import Blueprint, request, jsonify, abort
from app.util.jwt_manager import with_permission, get_jwt_identity
from app.models import UserPost, PostContent, PostReview

post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/', methods=['GET', 'POST'])
@with_permission('contributer')
def post():
  user_id = get_jwt_identity()

  if request.method == 'GET':
    try:
      posts = UserPost.query.all()

      return jsonify({ 'posts': posts })
    
    except:
      abort(500)

  elif request.method == 'POST':
    try:
      body = request.get_json()

      # new_post_status = UserPost()

      # new_post_status.save_to_db()

      # new_post = UserPost(body=body['body'],
      #                     prompt_id=body['prompt_id'],
      #                     user_id=user_id,
      #                     status_id=new_post_status.id)

      # new_post.save_to_db()

      # return 'success', 201

    except:
      abort(500)
