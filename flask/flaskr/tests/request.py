# request.py
import requests , json

headers = {'MojioAPIToken': '6ae1f07c-6db7-4a49-b458-2a1ffdfdc52e'}
r = requests.get("https://api.moj.io:443/v1/Events/", headers=headers)

print r
print r.json()[Events]

r = requests.get("https://api.moj.io:443/v1/Events/", headers=headers)
