import requests ##导入requests
from bs4 import BeautifulSoup ##导入bs4中的BeautifulSoup
import os


def mkdir(path):
    path = path.strip()
    isExists = os.path.exists(os.path.join("D:\mzitu",path))
    if not isExists:
        os.makedirs(os.path.join("D:\mzitu",path))
        return "D:\mzitu"+'\\'+path
    else:
        return "D:\mzitu"+'\\'+path

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
all_url = 'http://www.mzitu.com/all'  ##开始的URL地址
start_html = requests.get(all_url,  headers=headers)
Soup = BeautifulSoup(start_html.text,'lxml')
all_a = Soup.find('div',class_='all').find_all('a')
for a in all_a:
    title = a.get_text()
    print(u'开始保存：', title)
    path = str(title).replace("?", '_')
    imgpath = mkdir(path)
    href = a['href']
    html = requests.get(href,headers=headers)
    html_Soup = BeautifulSoup(html.text, 'lxml')
    max_span = html_Soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
    for page in range(1,int(max_span)+1):
        page_url = href+'/'+str(page)
        img_html = requests.get(page_url,headers=headers)
        img_Soup = BeautifulSoup(img_html.text, 'lxml')
        img_url = img_Soup.find('div', class_='main-image').find('img')['src']
        name = img_url[-9:-4]
        img = requests.get(img_url,headers = headers)
        f = open(imgpath+'\\'+name+'.jpg','ab')
        print(f)
        f.write(img.content)
        f.close()
