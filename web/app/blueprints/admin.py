from flask import Blueprint, request, jsonify
from app.util.jwt_manager import admin_required, authenticated_role, get_raw_jwt
from app.models import User

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route("/users")
@authenticated_role('admin')
def get_users():
  return jsonify({ 'users': User.query.all() })
  
  
@admin_bp.route("/user/<user_id>", methods=["GET", "PUT"])
@authenticated_role("admin")
def get_user(user_id):
  if request.method == "GET":
    user = User.find(user_id)

    logins = [l.ts for l in user.logins.all()]

    return jsonify({ 'user': user, 'logins': logins })

  elif request.method == "PUT":
    user = User.find(user_id)

    