import os
import functools
from flask import abort
from flask_jwt_extended import *
from app.models import RevokedToken

jwt = JWTManager()

@jwt.token_in_blacklist_loader
def is_token_revoked(decrypted_token):
  jti = decrypted_token.get('jti')
  return RevokedToken.is_revoked(jti)

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

def authenticated_role(role_name):
  def idk(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      verify_jwt_in_request()
      claims = get_jwt_claims()
      if role_name != claims.get('role'):
        abort(403)
      return func(*args, **kwargs)
    return wrapper
  return idk
