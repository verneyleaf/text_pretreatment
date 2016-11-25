import re
import urllib.request
from multiprocessing import Pool

def get_url():
	response = urllib.request.urlopen('http://www.bbc.com/news')
	html = response.read().decode('utf-8')
	res_url = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
	link = re.findall(res_url ,  html, re.I|re.S|re.M)
	pattern = re.compile(r"^/news/.*?-\d{8}")
	with open("url.txt", "w+") as f:
		for url in link:
			match = pattern.search(url)
			if match:
				f.write(url + "\n")
	return link

def get_content(url, item):
		#print (link)
		#print (type(url))
		#f.write(url + "\n")
		#with open("content_%d.txt" %(item), "w") as ff:
		head = "http://www.bbc.com"
		subresponse = urllib.request.urlopen(head + url)
		subhtml = subresponse.read().decode('utf-8')
		subres_url = re.compile(r'<p>.*?</p>')
		sublink = subres_url.findall(subhtml)
		ff = open("content_%d.txt" %(item), "w")
		for subitem in sublink:
			ff.write(subitem)
		ff.close()
if __name__ == "__main__":
	#link =get_url()
	item = 0
	f = open("url.txt", "r")
	url = f.readlines()
	p = Pool(4)
	for i in range(81):
		p.apply_async(get_content, args = (url[i].strip("\n"), item))
		item += 1
		print (url[i].strip("\n"))
	p.close()
	p.join()
	f.close()