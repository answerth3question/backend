from flask import Blueprint, request, jsonify, abort
from app.util.jwt_manager import with_permission, get_jwt_identity
from app.models import UserPost, PostContent

post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/', methods=['GET', 'POST'])
# @with_permission('contributer')
def post():
  user_id = get_jwt_identity()

  if request.method == 'GET':
    try:
      posts_list = [p.get_complete() for p in UserPost.query.all()]
      
      return jsonify(posts_list)
    
    except:
      abort(500)

  elif request.method == 'POST':
    try:
      body = request.get_json()

      user_post = UserPost(user_id=user_id, post_prompt_id=body['post_prompt_id'])

      user_post.save_to_db()

      post_content = PostContent(user_post_id=user_post.id, text=body['text'])

      post_content.save_to_db()

      return 'success', 201

    except BaseException as e:
      print(e)
      abort(500)
