'''
post_bp endpoints should be used to get and submit posts.
to get posts specific to a given user, use the user_bp endpoints
'''

from flask import Blueprint, request, jsonify, abort
from app.util.jwt_manager import with_permission, get_jwt_identity, jwt_optional
from app.database.models import Post

post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/', methods=['GET', 'POST'])
# @with_permission('contributer')
@jwt_optional
def post():
  user_id = get_jwt_identity() # if no jwt is sent in header, `user_id` will be None

  if request.method == 'GET':
    try:
      requested_status = request.args.get('status')
      print('REQUESTED STATUS ----------------------', requested_status)
      # posts_list = [p.get_complete() for p in UserPost.query.all()]
      
      return jsonify(posts_list)
    
    except:
      abort(500)

  elif request.method == 'POST':
    try:
      # body = request.get_json()

      # user_post = UserPost(user_id=user_id, post_prompt_id=body['post_prompt_id'])

      # user_post.save_to_db()

      # post_content = PostContent(user_post_id=user_post.id, text=body['text'])

      # post_content.save_to_db()

      return 'success', 201

    except BaseException as e:
      print(e)
      abort(500)
