from fyers_api import fyersModel
from fyers_api import accessToken
from config.utils import get_user_config
from django.shortcuts import redirect


config = get_user_config('fyers')
app_id = config.get('app_id', '')
secret_key = config.get('secret_key', '')
redirect_url = config.get('redirect_url', '')


class FyersLogin:

    fyers_model = None

    def __init__(self):
        pass

    def login(self, args):

        auth_code = args.get('auth_code', '')
        if len(auth_code):
            session = self.generate_session()
            session.set_token(auth_code)
            response = session.generate_token()
            access_token = response["access_token"]
            FyersLogin.fyers_model = fyersModel.FyersModel(client_id=app_id,
                                                     token=access_token)
            return redirect('/home')
        else:
            session = self.generate_session()
            broker_login_url = session.generate_authcode()
            return redirect(broker_login_url)

    @staticmethod
    def generate_session():
        session = accessToken.SessionModel(client_id=app_id, secret_key=secret_key,
                                           redirect_uri=redirect_url,
                                           response_type='code',
                                           grant_type='authorization_code',
                                           state='hello world')
        return session
