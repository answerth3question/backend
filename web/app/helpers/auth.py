import os
import jwt
import requests
from requests import RequestException # should use
from flask import request, abort
from app.models import User

def google():
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
    
    app_user = User.find(decoded_id_token['sub'])
    
    if app_user:
      return app_user
    
    app_user = User(id=decoded_id_token['sub'], username=decoded_id_token['given_name'], email=decoded_id_token['email'])
    
    app_user.save_to_db()
    
    return app_user

  except BaseException as e:
    print('ERROR IN GOOGLE HELPER', e)

    abort(500)