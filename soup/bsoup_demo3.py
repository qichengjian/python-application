### 使用js动态生成网页内容的网页无法使用bsoup来爬取
import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("")


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag) :
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[4].string])

def printUnivList(ulist, num):

    tplt = "{0:^10}\t{1:{3}^10}\t{2:10}"
    print(tplt.format("排名", "学校", "总分", chr(12288)))  #修改中文空格填充不对齐问题
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


if __name__ == '__main__':
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2020.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20) # 20 univs

""""
    排名    	　　　　学校　　　　	总分        
    1     	　　　清华大学　　　	852.5     
    2     	　　　北京大学　　　	746.7     
    3     	　　　浙江大学　　　	649.2     
    4     	　　上海交通大学　　	625.9     
    5     	　　　南京大学　　　	566.1     
    6     	　　　复旦大学　　　	556.7     
    7     	　中国科学技术大学　	526.4     
    8     	　　华中科技大学　　	497.7     
    9     	　　　武汉大学　　　	488.0     
    10    	　　　中山大学　　　	457.2     
    11    	　　西安交通大学　　	452.5     
    12    	　哈尔滨工业大学　　	450.2     
    13    	　北京航空航天大学　	445.1     
    14    	　　北京师范大学　　	440.9     
    15    	　　　同济大学　　　	439.0     
    16    	　　　四川大学　　　	435.7     
    17    	　　　东南大学　　　	432.7     
    18    	　　中国人民大学　　	409.7     
    19    	　　　南开大学　　　	402.1     
    20    	　　北京理工大学　　	395.6    
"""