import requests

HOST = 'http://127.0.0.1:5000'

data = requests.post(f'{HOST}/user/',
                     json={
                         'user_name': 'admin1',
                         'password': '12345'
                     })

print(data.json())