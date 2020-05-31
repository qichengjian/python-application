import requests
from bs4 import BeautifulSoup

url = "http://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text

soup = BeautifulSoup(demo, "html.parser")###使用BeautifulSoup(美味汤)来解析html

print(soup.prettify()) ###标签元素格式化显示

print(soup.title) ###获取title标签和内容


print(soup.a)
title = soup.a.attrs  ###获取标签的属性
print(title)    ###title是一个字典格式的数据

print(type(title))
print(title["href"])

data = soup.a.string  ###标记内的数据
print(data)


content = soup.a.contents
print(content)
print(content[0])

for child in soup.body.children: ###访问标签儿子节点
    print("children :" + str(child))

for child in soup.body.descendants: ###访问标签的子孙节点
    print("descentents: "+ str(child))

for parent in soup.a.parents:
    if parent is None: ### 区别遍历到最上层的parent为None时，没有name属性
        print(parent)
    else:
        print(parent.name)
###beatuifulsoup安装语法
###pip3 install beautifulsoup4
###beautifulsoup常用方法
### BeautifulSoup():构造方法，获取soup对象， attrs(获取标签属性),使用字典方式访问属性值， string(获取标签内数据)

### 标签树下行遍历方法 contents(获取平行节点数据，使用list访问其中数据)
### children(获取儿子节点，使用list访问其中数据) descendants（获取子孙节点，使用list访问其中数据）
### 标签树上行遍历方法 parent(节点的父标签) parents(节点的先辈标签)

