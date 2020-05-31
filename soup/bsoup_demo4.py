###淘宝商品信息定向爬虫 待解决模拟登录问题
import requests
import re


def getHTMLText(url):
    try:
        headers_kv = {"User-Agent": "Mozalla/5.0"}
        r = requests.get(url, headers =headers_kv, timeout=20)

        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("请求淘宝接口异常")


def parsePage(infoList, html):
    try:
        price_list= re.findall(r'\"view_price\":\"[\d\.]*\"', html)
        title_list = re.findall(r'\"row_title\":\".*?\"', html)
        for i in range(len(price_list)):
            price = eval(price_list[i].split(":")[1])
            title = eval(title_list[i].split(":")[1])
            infoList.append([price, title])
    except:
        print("解析html异常")



def printGoodsList(infoList):
    template_list = "{:4}\t{:8}\t{:16}"
    print(template_list.format("序号","价格","商品名称"))
    count=0
    for g in infoList:
        count+=1
        print(template_list.format(count, g[0], g[1]))


if __name__ == '__main__':

    string = "http://quote.eastmoney.com/sh500015.html"
    t = re.findall(r"[s][hz]\d{6}", string)[0]
    print(t)
    goods = "书包"
    dept = 2
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList = []
    for i in range(dept):
        try:
            url = start_url + "&s=" + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
