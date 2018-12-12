import requests
from bs4 import BeautifulSoup
import re
import os

def geturllist(url,ulist):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        print('爬取成功')
    except:
        print('爬取失败')
    soup=BeautifulSoup(r.text,'html.parser')
    lista=soup.find_all('a',attrs={'href':re.compile(r'\d+\.html')})
    lista=lista[1:]
    
    for i in lista:
        ulist.append(i['href'])
    
    return ulist

def getHTML(url):
    try:
        r=requests.get(url)
        r.raise_for_status
        r.encoding=r.apparent_encoding           
        return r.text
    except:
        print('解析页面失败')
        return ''
    

def parsepage(html):
    
    soup=BeautifulSoup(html,'html.parser')
    a=soup.find('div',attrs={'class':"yd_text2"})
    title=soup.find('h1')    
    return [a.text,title.string]
   

def writefile(text):
    with open('D:/貌似高手在异界.txt','a',encoding='utf-8') as f:
        f.write('\t\t\t\t\t\t\t\t\t\t'+text[1]+'\n\n\n'+text[0])

def main():
    url='https://www.88dush.com/xiaoshuo/0/653'
    ulist=[]

    geturllist(url,ulist)

    for i in ulist:
        aurl=url+'/'+i
        html=getHTML(aurl)
        text=parsepage(html)
        writefile(text)       
        print('正在爬取')
    print('下载完毕')

main()



        