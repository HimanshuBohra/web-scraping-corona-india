import requests
import json

url = "https://dashboards-dev.sprinklr.com/data/9043/global-covid19-who-gis.json"
r = requests.get(url)
cont = json.loads(r.content.decode())
a=0
for i in cont['rows']:
        if i[1]=="IN":
            a+=i[5] 
print(a)
