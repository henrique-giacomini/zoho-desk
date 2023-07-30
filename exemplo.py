import httpx

url = 'https://desk.zoho.com/api/v1/tickets'
headers = {"authorization": "Zoho-Oauthtoken 1000.e674e46f0fd78547a66e80d584829e46.f4b4ca3198b0ac1881d4d4c3b3728999"}

r = httpx.get(url=url, headers=headers)

data = r.json()

print(data)
