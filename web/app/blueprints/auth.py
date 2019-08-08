# this is a useful stackoverflow post on how to decode RS256 JWTs
# https://stackoverflow.com/questions/20159782/how-can-i-decode-a-google-oauth-2-0-jwt-openid-connect-in-a-node-app


from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required

from app.models import User

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route("/login", methods=["POST"])
def register_user():
  body = request.get_json()
  print('at login', body)
  user = User.find(body.get('sub'))
  print('user exists? ', user, user.role)
  if user:
    token = create_access_token(user.id, user_claims={ 'role': user.role })
    return jsonify({ 'id_token': token })
  user = User(id=body.get('sub'), username=body.get('username'), email=body.get('email'))
  user.save_to_db()
  token = create_access_token(user.id, user_claims={ 'role': user.role })
  return jsonify({ 'id_token': token })


