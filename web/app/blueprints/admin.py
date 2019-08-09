from flask import Blueprint, request, jsonify
from app.util.jwt_manager import admin_required, get_raw_jwt
from app.models import User

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route("/users")
@admin_required
def users():
  return jsonify({ 'users': User.query.all() })
  