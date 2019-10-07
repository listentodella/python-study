#!/usr/bin/env python
# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
import time
import sys
import urllib.request
import xlwt
from lxml import etree
from multiprocessing import Pool

def getHTMLText(url,cookies):
    try:
        r = requests.get(url,cookies)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("Failed!")



    
def getVideoInfo(html):
    soup=BeautifulSoup(html,"html.parser")
    videoContentList=soup.find('div',attrs={'id':'videobox'})
    #print(videoContentList)#���Դ�ӡ����

    videoInfoList=[]
    
    i=0
    selector=etree.HTML(html)
    
    for videoLi in videoContentList.find_all('div',attrs={'class':'listchannel'}):
        
        videoName=videoLi.find('img',attrs={'width':'120'}).get('title')
        videoUrl=videoLi.find('a',attrs={'target':'blank'}).get('href')

        timetext=selector.xpath('//div[@class="listchannel"]/text()')[4+i*17].strip()
        addtimetext=selector.xpath('//div[@class="listchannel"]/text()')[6+i*17].strip()
        try:
            videoAuthorContent=videoLi.find('a',attrs={'target':'_parent'}).getText()
        except AttributeError:
            videoAuthorContent="None"
        
            
        #print(videoUrl+str(i))
        try:
            videoAuthorUrl=videoLi.find('a',attrs={'target':'_parent'}).get('href')
        except AttributeError:
            videoAuthorUrl="None"
        viewNumber=selector.xpath('//div[@class="listchannel"]/text()')[10+i*17].strip()
        likeNumber=selector.xpath('//div[@class="listchannel"]/text()')[11+i*17].strip()
        commentNumber=selector.xpath('//div[@class="listchannel"]/text()')[13+i*17].strip()
        
        videoInfoList.append(videoUrl)#����
        videoInfoList.append(videoName)#��Ƶ��
        videoInfoList.append(timetext)#��Ƶʱ��
        videoInfoList.append(addtimetext)#�ϴ�ʱ��
        videoInfoList.append(videoAuthorContent)#�ϴ���id
        videoInfoList.append(videoAuthorUrl)#�ϴ�����ҳ
        videoInfoList.append(viewNumber)#�ۿ���
        videoInfoList.append(likeNumber)#�ղ���
        videoInfoList.append(commentNumber)#������
        
        i+=1
        #print(videoUrl)
    return videoInfoList



def saveToExcel(videoInfoList):
    workbook=xlwt.Workbook()
    sheet1=workbook.add_sheet('sheet1',cell_overwrite_ok=True)

    k=0
    for i in range(10000):
        for j in range(9):
            print('col row', i,j)
            #print("����д����к����� %d %d", %(i, j))
            sheet1.write(i,j,videoInfoList[k])
            k+=1
    workbook.save('E:\\MyFile\\PythonSpider\\91Best\\top78000.xls')

def main():
    cookies=''#ʹ���Լ���cookies
    top10000List=[]
    
    for page in range(1,505):#1��500����5��ֹ�������
        FvUrl=url+str(page)
        #print('���ڱ����ҳ��Ϊ��'+str(page)+'ҳ')
        print('saving page is '+str(page)+'page')
        top10000List+=getVideoInfo(getHTMLText(FvUrl,cookies))
    saveToExcel(top10000List)
    
    
if __name__=='__main__':
    main()


