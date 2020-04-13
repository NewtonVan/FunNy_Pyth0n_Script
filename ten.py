# -*- coding: UTF-8 -*-
import urllib.request as rqst
# import logging
import re
import retrieve

def getJpg(URL):
	html= retrieve.getHtml(URL)
	jpgURL= retrieve.getImg(html)
	ImgURL= host+jpgURL[0]
	return ImgURL

def saveImg(URL):
	destURL=getJpg(URL)
	pic_response= rqst.urlopen(destURL)
	pic= pic_response.read()
	fp= open('.\\u_bing.jpg', 'wb')
	fp.write(pic)
	fp.close()

host= "https://cn.bing.com"
saveImg(host)
# print(getJpg(host))