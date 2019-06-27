# -*- coding: utf-8 -*-

def get_auth_url():
    weibo_auth_url = 'https://api.weibo.com/oauth2/authorize'
    redirect_url = 'http://127.0.0.1:8000/goods/'
    auth_url = weibo_auth_url + '?client_id={client_id}&redirect_uri={redirect_url}'.format(client_id=1458129973,redirect_url=redirect_url)

    print(auth_url)

def get_access_token(code = '515b3f812b7646020598e82fa27cb0f0'):
    access_token_url = 'https://api.weibo.com/oauth2/access_token'
    import requests
    re_dict = requests.post(access_token_url, data={
        'client_id': 1458129973,
        'client_secret': '3439d8472f562cc3fd2e03cc33dbe4ce',
        'grant_type' :'authorization_code',
        'code': code,
        'redirect_uri': 'http://127.0.0.1:8000/goods/'
    })
    pass
# '{"access_token":"2.00JLfecF4NKgaB5008673fcfdlNoHC","remind_in":"129202","expires_in":129202,"uid":"5151856343","isRealName":"true"}'

def get_user_info(access_token='', uid=''):
    user_url = 'https://api.weibo.com/2/users/show.json?access_token={token}&uid={uid}'.format(token=access_token, uid=uid)
    print(user_url)

if __name__ == '__main__':
    # get_auth_url()

    # get_access_token(code = 'a0e3accfcef0f24e8c6adc4ee8b55b86')

    get_user_info(access_token='2.00JLfecF4NKgaB5008673fcfdlNoHC', uid='5151856343')