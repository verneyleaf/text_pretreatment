# -*- coding: utf-8 -*-
import requests

response = requests.get('http://news.163.com/rank/')
content = response.content

print (response.headers)
#print (content)
