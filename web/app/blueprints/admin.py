from flask import Blueprint, request, jsonify
from app.util.jwt_manager import with_permission, get_raw_jwt
from app.database.models import RegisteredUser

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route("/users")
@with_permission('admin')
def get_users():
  '''get list of all app users'''
  return jsonify({ 'users': RegisteredUser.query.all() })
  
  
@admin_bp.route("/users/<user_id>", methods=["GET", "PUT"])
@with_permission("admin")
def user(user_id):
  '''admin endpoint for actions releated to specific user'''
  if request.method == "GET":
    user = RegisteredUser.get_profile_admin(user_id)

    return jsonify({ 'user': user })

  elif request.method == "PUT":
    user = RegisteredUser.query.get(user_id)

