import httpx
from typing import Dict


class ZohoDesk:
    """"""
    client_id: str = '1000.T6TDKB524O263IW5YWHH741EGWJ0OV',
    client_secret: str = 'f4271109effcb2e4da78d227ccf874e881089e8280'

    def get_Zoho_Oauthtoken(
        client_id: str = client_id,
        client_secret: str = client_secret,
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

    def get_interface(
        oauth_token: str = None,
        interface: str = None,
        query_params: Dict[str, str] = None,
        service: str = None
    ) -> object:
        """Requisita um _endpoint_ da API do Zoho Desk

        Parameters
        ----------
        oauth_token: str
        interface: str, 
        query_params: str, 
        service: str

        Returns
        -------
        response: object

        """
        url = f'https://desk.zoho.com/api/v1/{interface}'
        headers = {
            "authorization": f"Zoho-Oauthtoken {oauth_token}"
        }
        r = httpx.get(url=url, headers=headers, params=query_params)

        if r.status_code == 200:
            return r
