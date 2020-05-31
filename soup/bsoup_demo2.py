###查找元素
###示例：提取html中所有的URL链接

from bs4 import BeautifulSoup
import requests
import re

url = "http://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser");
for link in soup.find_all('a'):
    print(link.get("href"))


soup.find_all("a") ###查找一个标签
soup.find_all(["a", "b"])   ###查找多个标签
soup.find_all(True)   ###查找所有标签


for tag in soup.find_all(re.compile("b")):  ###re库(正则表达式的库，以'b'开头)
    print(tag.name)

soup.find_all("p", "course") ###查找'p'标签名，属性值为'course'的标签

soup.find_all(id="link1")   ###通过id属性来查找

print(soup.find_all(string = "Basic Python")) ###通过标签内的数据完全匹配, 精确匹配

print(soup.find_all(string = re.compile("Python"))) ###通过正则表达式检索出全部含有'python'的标签
print(soup.body(string = "Basic Python"))  ###直接通过标签调用find_all方法
print(soup.body.find_all(string = "Basic Python"))  ###与上述方法等效


### fina_all 返回一个列表类型，存储查找的结果
