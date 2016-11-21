# -*- coding:utf-8 -*-

import re
import urllib
import string
import requests
from bs4 import BeautifulSoup
from lxml import etree
import jieba



cookie = {"Cookie": "_T_WM=_T_WM=19ff03cbc7ae63d41274267753197ad7; SCF=AqTJzb8Uorfs1URvdi_U7LCqbHuI7DlLjjyUQlJUwUDIv477ZPrJCbMfTvd007rPTtFB5G1GUrebBDodxIdt5Gc.; SUB=_2A251LCU3DeTxGeVO6loR9ijIzT2IHXVW70t_rDV6PUJbkdBeLUSlkW2FWxVMMueR2FSbKOqsk8woKvoK_A..; SUHB=09P9H-oual6J2D; SSOLoginState=1479038311"}

url = "http://weibo.cn/u/5220650532?filter=1&page=1"
html = requests.get(url, cookies = cookie).content
selector = etree.HTML(html) # ?
pageNum = (int)(selector.xpath('//input[@name="mp"]')[0].attrib['value'])

#pattern = r"\d+\.?\d"

result = ""
#weibos = []
#urllist_set = set()
word_count = 1

for page in range(1, 56):
	url2 = "http://weibo.cn/u/5220650532?filter=1&page=%d" %(page)
	lxml = requests.get(url2, cookies = cookie).content
	
	selector = etree.HTML(lxml)
	content = selector.xpath('//span[@class="ctt"]')
	for each in content:
		text = each.xpath('string(.)')
		if word_count >= 3:
			#text_ = jieba.cut(text)
			#text = "/".join(text_) + "\n\n"
			text = "%d :" %(word_count - 3) + text + "\n\n"
		else:
			text = text + "\n\n"
		result = result + text
		name = "chinese/weibo%d.txt" %(word_count)
		fo = open(name, "w")
		fo.write(text)
		fo.close()
		word_count += 1

	#content = selector.xpath('//div[@class="c"]')
	#for i in range(0, len(content)-2):
		#text = content[i].xpath("div/span[@class='ctt']")
		#weibo = text[0].xpath('string(.)').encode('gbk', 'ignore')	
		#weibos.append(weibo)
		#print(weibo)
fo = open("weibo.txt", "w")
fo.write(result)
fo.close()

#soup = BeautifulSoup(html)
#content = soup.get_text()
#print (content)
