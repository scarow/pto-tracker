""" Cornice services.
"""
import os
import binascii
import json

from webob import Response, exc
from cornice import Service

from app.models import DBSession
from app.models.users import User

users = Service(name='users', path='/users', description="Users")
_USERS = {}


#
# Helpers
#
def _create_token():
    return binascii.b2a_hex(os.urandom(20))


class _401(exc.HTTPError):
    def __init__(self, msg='Unauthorized'):
        body = {'status': 401, 'message': msg}
        Response.__init__(self, json.dumps(body))
        self.status = 401
        self.content_type = 'application/json'


def valid_token(request):
    header = 'X-Messaging-Token'
    htoken = request.headers.get(header)
    if htoken is None:
        raise _401()
    try:
        user, token = htoken.split('-', 1)
    except ValueError:
        raise _401()

    valid = user in _USERS and _USERS[user] == token
    if not valid:
        raise _401()

    request.validated['user'] = user


def unique(request):
    name = request.body
    if name in _USERS:
        request.errors.add('url', 'name', 'This user exists!')
    else:
        user = {'name': name, 'token': _create_token()}
        request.validated['user'] = user


#
# Services - User Management
#
@users.get(validators=valid_token)
def get_users(request):
    """Returns a list of all users."""
    return {'users': _USERS.keys()}


@users.post(validators=unique)
def create_user(request):
    """Adds a new user."""
    user = request.validated['user']
    new_user = User(user['name'], user['token'])
    print new_user
    DBSession.add(new_user)
    DBSession.commit()
    _USERS[user['name']] = user['token']
    return {'user': '%s-%s' % (user['name'], user['token'])}


@users.delete(validators=valid_token)
def del_user(request):
    """Removes the user."""
    name = request.validated['user']
    del _USERS[name]
    return {'Goodbye': name}
