import functools
from flask import abort
from flask_jwt_extended import *
from app.models import RevokedToken

jwt = JWTManager()


@jwt.token_in_blacklist_loader
def is_token_revoked(decrypted_token):
  jti = decrypted_token.get('jti')
  return RevokedToken.is_revoked(jti)


def with_permission(permission):
  def idk(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      verify_jwt_in_request()

      claims = get_jwt_claims()

      user_permission = claims.get('permission')

      if permission not in user_permission:
        abort(403)

      return func(*args, **kwargs)
    
    return wrapper
  
  return idk


def authenticated_role(permitted):
  def idk(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      verify_jwt_in_request()

      claims = get_jwt_claims()

      user_role = claims.get('role')

      if type(permitted) is str:
        if user_role != permitted:
          abort(403)

      elif type(permitted) is list:
        if user_role not in permitted:
          abort(403)

      return func(*args, **kwargs)

    return wrapper
    
  return idk
