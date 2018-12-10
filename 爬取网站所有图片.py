import requests
from bs4 import BeautifulSoup
import os

def getHTML(url):
    try:
        r=requests.get(url,headers={'user-agent':'Mozilla/5.0'})
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('Fail')

def geturl(html,ulist):
    soup=BeautifulSoup(html,'html.parser')
    alist=soup.find_all('img')
    for i in range(len(alist)):
        ulist.append(alist[i].attrs['src'])
    print(ulist)
     
def download(url):
    root='D:/pics/'
    path=root+url.split("/")[-1]
    print(path)
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):            
            r=requests.get(url)
            r.raise_for_status()
            with open(path,'wb') as k:
                k.write(r.content)
                k.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("失败")
        
def main():
    ulist=[]
    url=str(input('输入网址'))
    html=getHTML(url)
    geturl(html,ulist)
    for k in ulist:
        download(k)
        print('finish')

main()