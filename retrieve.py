# -*- coding: UTF-8 -*-
import requests
import re
import urllib.request as rqst
import logging
import sys

def getHtml(url):
	page= rqst.urlopen(url)
	html= page.read()
	if html:
		logging.debug("Get Response"+str(len(html)))
	else:
		logging.warning("Request failed!")
	fp= open(".\\bing_web.txt", "wb")
	fp.write(html)
	fp.close()
	return html.decode('utf-8')

def getImg(html):
	reg=r'(?<=href=")[^"]*jpg[^"]*'
	imgre= re.compile(reg)
	imglist= re.findall(imgre, html)
	if imglist:
		print(imglist)
		print(len(imglist))

	return imglist

# html= getHtml("https://cn.bing.com/")
# fp= open(".\\bing_web.html", "wb")
# fp.write(html)
# fp.close()
# jpglist=getImg(html.decode('utf-8'))
# print(jpglist)