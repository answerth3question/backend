from flask import Blueprint, request, jsonify

from app.models import PostPrompt

prompt_bp = Blueprint('prompt_bp', __name__)
