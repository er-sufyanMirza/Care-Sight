import requests

payload = {'k1':'v1', 'k2':'v2'}
r = requests.get("https://httpbin.org/get", params = payload)
print(r.text)