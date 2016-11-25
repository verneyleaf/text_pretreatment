import re, urllib.request

response = urllib.request.urlopen('http://www.bbc.com/news')
html = response.read().decode('utf-8')
res_url = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
link = re.findall(res_url ,  html, re.I|re.S|re.M)
#for url in link:
#    print (url)
#linksList = re.findall('<a href=(.*?)>.*?</a>',html)
#pattern = re.compile(r"/news")
head = "http://www.bbc.com"
item = 0
pattern = re.compile(r"^/news/.*?-\d{8}")
with open("url.txt", "w") as f:
	for url in link:
		match = pattern.search(url)
		if match:
			f.write(url + "\n")
		#print (link)
		#print (type(url))
		#f.write(url + "\n")
		    #with open("content_%d.txt" %(item), "w") as ff:

			subresponse = urllib.request.urlopen(head + url)
			subhtml = subresponse.read().decode('utf-8')
			subres_url = r'<div class="story-body_inner" property="articleBody"'
			sublink = re.findall(subres_url, subhtml)
			ff = open("content_%d.txt" %(item), "w")
			for subitem in sublink:
				ff.write(subitem)
			item += 1
			ff.close()
