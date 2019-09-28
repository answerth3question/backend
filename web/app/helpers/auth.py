import os
import jwt
import requests
from requests import RequestException # should use
from flask import request, abort
from app.database.models import RegisteredUser, RevokedToken

def revoke_access_token(jti):
  try:
    token_to_revoke = RevokedToken(jti=jti)

    token_to_revoke.save_to_db()

  except BaseException as e:
    print('ERROR REVOKING ACCESS TOKEN', e)

    abort(500)

  return True


def google_login():
  GOOGLE_DISCOVERY_DOCUMENT = 'https://accounts.google.com/.well-known/openid-configuration'
  try:
    body = request.get_json()

    discovery_document = requests.get(GOOGLE_DISCOVERY_DOCUMENT).json()
    
    token_payload = {
      'code': body.get('code'),
      'redirect_uri': body.get('redirect_uri'),
      'client_id': os.environ.get('GOOGLE_CLIENT_ID'),
      'client_secret': os.environ.get('GOOGLE_CLIENT_SECRET'),
      'grant_type': 'authorization_code',
    }
    google_user = requests.post(url=discovery_document['token_endpoint'], data=token_payload).json()
    
    decoded_id_token = jwt.decode(google_user['id_token'], verify=False)
    
    app_user = RegisteredUser.query.filter_by(oauth_openid=decoded_id_token['sub']).first()
    
    if app_user:
      return app_user
    
    app_user = RegisteredUser(oauth_openid=decoded_id_token['sub'],
                    username=decoded_id_token['given_name'],
                    email=decoded_id_token['email'],
                    role_id=1) # deault role is 'contributer'

    app_user.save_to_db()
    
    return app_user

  except BaseException as e:
    print('ERROR IN GOOGLE HELPER', e)

    abort(500)