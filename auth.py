import httpx


def get_Zoho_Oauthtoken(
    client_id: str = '1000.T6LDKB524O263IW5YWAH741EGWJ0OV',
    client_secret: str = 'f4271109effcb2e4ca78d227ccf854e881089e8270',
    code: str = None
) -> object:
    """Retorna um objeto _reponse_ contendo o Zoho_Oauthtoken

    Parameters
    ----------
    client_id: str
    client_secret: str
    code: str

    Returns
    -------
    ZohoOauthtoken: object
    """

    auth_url = 'https://accounts.zoho.com/oauth/v2/token'
    params = {
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type':  	'authorization_code',
        'redirect_uri': ''
    }

    r = httpx.post(url=auth_url, params=params)

    if r.status_code == 200:
        return r


client_id = '1000.T6LDKB524O263IW5YWAH741EGWJ0OV',
client_secret = 'f4271109effcb2e4ca78d227ccf854e881089e8270'
get_Zoho_Oauthtoken(client_id, client_secret)
