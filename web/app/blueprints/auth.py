# this is a useful stackoverflow post on how to decode RS256 JWTs
# https://stackoverflow.com/questions/20159782/how-can-i-decode-a-google-oauth-2-0-jwt-openid-connect-in-a-node-app

from datetime import timedelta
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_raw_jwt

from app.database.models import UserLogin
import app.helpers.auth as auth_helper

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route("/login", methods=["POST"])
def login_user():
  strategy = request.args.get('strategy', 'local')

  if strategy == 'google':
    user = auth_helper.google_login()

  elif strategy == 'local':
    pass

  login_record = UserLogin(user_id=user.id)

  login_record.save_to_db()

  if user.role.name == 'admin':
    token_exp = timedelta(hours=0.5) if user.email != 'jacob.albright23@gmail.com' else timedelta(hours=2) # half hour

  elif user.role.name == 'reviewer':
    token_exp = timedelta(hours==1) # 1 hour
  
  else:
    token_exp = timedelta(days=6) # 6 days

  token = create_access_token(identity=user.id,
                              expires_delta=token_exp,
                              user_claims={ 
                                'role': user.role.name,
                                'permission': [perm.name for perm in user.role.permission]
                              })

  return jsonify({ 'id_token': token })


@auth_bp.route('/revoke-access', methods=["POST"])
@jwt_required
def revoke_access():
  token_dict = get_raw_jwt()

  jti = token_dict.get('jti')

  auth_helper.revoke_access_token(jti)

  return 'success', 200
