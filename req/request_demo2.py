import requests

### 使用百度进行搜素
params_kv = {"wd": "Python"}
url = "http://www.baidu.com/s"
headers_kv = {"User-Agent":"Mozalla/5.0"}

r = requests.get(url, params=params_kv, headers = headers_kv)
print(r.request.url)  ###完整请求url
r.encoding = 'utf-8'
print(r.status_code)
print(r.text[:1000])
