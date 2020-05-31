###图片爬取和保存
import requests
import os


image_url = "https://www.nationalgeographic.com/content/dam/travel/2020-digital/" \
            "molokai-national-park/009_jdk-140412-8650.adapt.210.1.jpg"
image_path = "./img/"
image_name = image_url.split("/")[-1];
image_local_url = image_path+image_name

try:
    if not os.path.exists(image_path): ###图片目录不存在
        os.mkdir(image_path)
    if not os.path.exists(image_local_url): ###图片文件不存在
        r = requests.get(image_url)
        with open(image_local_url, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")

