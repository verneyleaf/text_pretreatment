# -*- coding: UTF-8 -*-

import http.client
from bs4 import BeautifulSoup
from time import sleep
import jieba

url = "http://www.cnblogs.com/bwangel23/p/4485394.html"
url1 = "http://supercomputingblog.com/cuda/cuda-tutorial-4-atomic-operations"
conn = http.client.HTTPConnection("www.cnblogs.com")
conn.request(method = "GET", url = url)
response = conn.getresponse()
res = response.read() # 返回html文档
soup = BeautifulSoup(res) # 解析html文档，并返回BeautifulSoup对象
div_html = soup.find_all("div", id = "cnblogs_post_body") # 找到所有<p>标签的内容
#for item in div_html:
#	print (item.get_text())

#print (div_html.get_text())
#print (div_html)
#print (soup.prettify()) # 将html对象按照标准的缩进格式输出
#print (soup.title())
#print (soup.title().name)
filename = "./text1.text"
test = soup.get_text()
#print (type(test))

seg_list = jieba.cut("我爱中华人民共和国")
print ("/".join(seg_list))
#file_obj = open(filename, "w")
#file_obj.write(test)
#file_obj.close()
#print (soup.get_text()) # 获取所有文字的内容

