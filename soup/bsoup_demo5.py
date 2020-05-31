###获取上交所和深交所所有股票的名称和交易信息

import requests
from bs4 import BeautifulSoup
import re
import traceback


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("请求接口发生异常")
        traceback.print_exc()


def getStockList(lst, stockUrl):
    html = getHTMLText(stockUrl)
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.find_all("a")
    for i in tags:
        try:
            href = i.attrs["href"]
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            # traceback.print_exc()
            continue


def getStockInfo(lst, stockUrl, fpath):
    count = 0
    for stock in lst:
        url = stockUrl + stock + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, "html.parser")
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})
            name = stockInfo.find_all(attrs={"class":"bets-name"})[0]
            infoDict.update({"股票名称":name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList= stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                value=valueList[i].text
                infoDict[key] = value
            with open(fpath, 'a', encoding="utf-8") as f:
                f.write(str(infoDict)+"\n")
                count+=1
                print("\r当前进度: {:.2f}%".format(count * 100 / len(lst)), end=' ')

        except:
            count+=1
            print('\r当前进度: {:.2f}%'.format(count * 100 / len(lst)), end=' ')
            continue


if __name__ == '__main__':
    lst = []
    stock_list_url = "http://quote.eastmoney.com/stockList.html"
    stock_info_url = "http://quote.cfi.cn/"
    out_path="./stockInfo.txt"
    getStockList(lst, stock_list_url)
    getStockInfo(lst, stock_info_url, out_path)
