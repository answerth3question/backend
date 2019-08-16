from flask import Blueprint, request, jsonify
from app.util.jwt_manager import admin_required, authenticated_role, get_raw_jwt
from app.models import User

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route("/users")
@authenticated_role('admin')
def users():
  return jsonify({ 'users': User.query.all() })
  