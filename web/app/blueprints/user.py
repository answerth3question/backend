from flask import Blueprint, request, jsonify, abort
from app.util.jwt_manager import jwt_required, get_jwt_identity
from app.database.models import RegisteredUser

user_bp = Blueprint('user_bp', __name__)

@user_bp.route("/profile")
@jwt_required
def profile():
  user_id = get_jwt_identity()
  user = RegisteredUser.query.get(user_id)
  if user:
    return jsonify({
      'username': user.username,
      'email': user.email,
      'role': user.role.name
    })
  abort(404)

