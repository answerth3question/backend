import os
import functools
from flask import abort
from flask_jwt_extended import *
from app.models import RevokedToken

jwt = JWTManager()

@jwt.token_in_blacklist_loader
def is_token_revoked(decrypted_token):
  return RevokedToken.is_revoked(decrypted_token)

# Custom Decorators
def admin_required(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    verify_jwt_in_request()
    claims = get_jwt_claims()
    if claims.get('role') != 'admin':
      abort(403)
    return func(*args, **kwargs)
  return wrapper

