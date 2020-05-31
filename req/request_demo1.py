import requests

### 获取京东商品信息
url = 'https://item.jd.com/100013208056.html'
# r = requests.get(url)
# print(r.status_code)
# print(r.encoding)
# print(r.text[:1000])
# print(r.request.headers)

kv = {"User-Agent":"Mozilla/5.0"}

r = requests.get(url, headers = kv) ###如何这里不设置会返回登录页信息
print(r.status_code)
print(r.encoding)
print(r.text[:1000])
print(r.request.headers)
