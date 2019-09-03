from flask import Blueprint, request, jsonify

from app.models import UserPost, PostReview, PostStatus

post_bp = Blueprint('post_bp', __name__)

