import requests ##导入requests
from bs4 import BeautifulSoup ##导入bs4中的BeautifulSoup
import os

def find_ing(tag):
    return tag.has_attr('class')

def mkdir(path):
    path = path.strip()
    isExists = os.path.exists(os.path.join("D:\zhuomian",path))
    if not isExists:
        os.makedirs(os.path.join("D:\zhuomian",path))
        return "D:\zhuomian"+'\\'+path
    else:
        return "D:\zhuomian"+'\\'+path

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
all_url = 'http://wallpaperswide.com/'  ##开始的URL地址
start_html = requests.get(all_url,  headers=headers)                     #打开网址，搜索所有分类
Soup = BeautifulSoup(start_html.text,'lxml')
all_a = Soup.find('ul',class_='side-panel categories').find_all('a')
for a in all_a:
    title = a.get_text()
    print(u'开始保存：', title)
    path = str(title).replace("?", '_')
    imgpath = mkdir(path)
    href = a['href']
    href = 'http://wallpaperswide.com/'+href
    img_html = requests.get(href, headers=headers)                          #打开分类，搜索所有图片
    img_Soup = BeautifulSoup(img_html.text, 'lxml')
    for img in img_Soup.find_all('img',class_ = 'thumb_img'):
        img_dizhi = img.attrs['src']
        img_name = img_dizhi[37:]
        img_HDbianhuan = list(img_name)
        img_HDbianhuan[-6:]='wallpaper-1920x1080.jpg'
        img_HDdizhi = "".join(img_HDbianhuan)
        img_HDdizhi = "http://wallpaperswide.com/download/"+img_HDdizhi          #获取1080P图片地址
        img_content = requests.get(img_HDdizhi, headers=headers)
        f = open(imgpath + '\\' + img_name, 'ab')
        print(f)
        f.write(img_content.content)                                        #保存本地
