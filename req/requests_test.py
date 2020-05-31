### reqq.request(), 构造一个请求，是以下方法的基础
### reqq.get(), head(), put(), delete(), post(),patch()
### requests属性： status_code, text(字符串), encoding(分析请求头得到的),
### apparent_encoding(分析内容得到的), content(二进制，例如图片内容)
### requests异常：

import requests


def test():
    try:
        url = 'http://www.baidu.com'
        r = requests.get(url, timeout=30)
        r.raise_for_status()##如果响应状态码非200，就产生一个异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '请求异常'
