import httpx

url = 'https://accounts.zoho.com/oauth/v2/token'


def get_Zoho_Oauthtoken():
    params = {
        'code': '1000.980a09156c45f38c5352372219c8a037.b77f1e3c5b851d5d97bc1729e66b58ba',
        'client_id': '1000.T6LDKB524O263IW5YWAH741EGWJ0OV',
        'client_secret': 'f4271109effcb2e4ca78d227ccf854e881089e8270',
        'grant_type':  	'authorization_code',
        'redirect_uri': ''
    }

    r = httpx.post(url=url, params=params)
