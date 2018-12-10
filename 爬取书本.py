#py
import requests
from bs4 import BeautifulSoup
import os
def getHTML(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''

def parseHTML(html,ulist):
    soup=BeautifulSoup(html,'html.parser')
    booklist=soup.find_all('article')
    for i in range(len(booklist)):
        beforetag1=booklist[i].find('h3')
        beforetag2=booklist[i].find_all('p')
        name=beforetag1.find('a').attrs['title']
        price=beforetag2[1].string.split('£')[1]
        ulist.append([name,price])

def printans(ulist):
    for i in range(len(ulist)):
        print(ulist[i])

def createfile(ulist,path):
    output=open(path,'w',encoding='gb2312')
    output.write('书目')
    output.write('\t')
    output.write('价格\n')
    for i in range(len(ulist)):
        for j in range(len(ulist[i])):
            output.write(ulist[i][j])
            output.write('\t')
        output.write('\n')
    output.close()

def main():
    start_urls='http://books.toscrape.com/'
    html=getHTML(start_urls)
    ulist=[]
    parseHTML(html,ulist)
    printans(ulist)
    path='D:/books.xls'
    createfile(ulist,path)

if __name__=='__main__':
    main()