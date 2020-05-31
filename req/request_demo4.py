###ip地址归属地自动查询

import requests

url = "http://ip.taobao.com/service/getIpInfo.php"
kv = {"ip":"60.186.222.254"}
head = {"User-Agent": "Mozilaa/5,0"}
try:
    r = requests.get(url, params=kv, headers = head)
    print(r.request.url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500])
except:
    print('ip地址查询失败')
