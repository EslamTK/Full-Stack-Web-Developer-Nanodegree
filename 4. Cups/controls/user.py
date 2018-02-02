from base64 import b64encode
from os import urandom, path

from oauth2client import client

from controls import *
from core import *
from models.user import User

userController = Blueprint('userController', __name__)


@userController.route('/connect', methods=['POST'])
def google_connect():
    """The google sign in route which will be used to sign in the User into the application"""

    if not request.headers.get('X-Requested-With'):
        abort(403)

    auth_code = request.data
    site_root = path.realpath(path.dirname(__file__)) + '/../'

    client_secret_file = path.join(site_root, 'static', 'client_secret.json')

    credentials = client.credentials_from_clientsecrets_and_code(
        client_secret_file,
        ['https://www.googleapis.com/auth/drive.appdata', 'profile', 'email'],
        auth_code)

    email = credentials.id_token['email']

    try:
        result = users.get_by_email(email=email)
        token = result.token
    except NoResultFound:
        token = b64encode(urandom(100)).decode('utf-8')
        new_user = User(email=email, token=token)
        users.add(new_user)
        unit_of_work.save()

    response = make_response(redirect(request.referrer))
    response.set_cookie('token', token)
    return response


@userController.route('/disconnect', methods=['POST'])
def google_disconnect():
    """The google sign out route which will be used to sign out the User from the application"""

    token = request.cookies.get('token', None)
    request_user = users.get_by_token(token=token)
    request_user.token = b64encode(urandom(100)).decode('utf-8')
    unit_of_work.save()

    response = make_response(redirect(request.referrer))
    response.set_cookie('token', '', expires=0)
    return response
