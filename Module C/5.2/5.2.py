import requests
import json

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
d = json.loads(r.content)
print(r.content)