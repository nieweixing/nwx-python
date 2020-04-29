import requests
import json

base_url = "https://www.baidu.com/"

r_get = requests.get(base_url)

print(r_get.status_code)
print(r_get.text)

json.loads(r_get.text)

