from flask import Blueprint, request, jsonify
from app.util.jwt_manager import authenticated_role, get_raw_jwt
from app.database.models import RegisteredUser

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route("/users")
@authenticated_role('admin')
def get_users():
  return jsonify({ 'users': RegisteredUser.query.all() })
  
  
@admin_bp.route("/user/<user_id>", methods=["GET", "PUT"])
@authenticated_role("admin")
def get_user(user_id):
  if request.method == "GET":
    user = RegisteredUser.get_complete(user_id)

    return jsonify({ 'user': user })

  elif request.method == "PUT":
    user = RegisteredUser.query.get(user_id)

