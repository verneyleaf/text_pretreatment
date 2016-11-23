# -*- coding: utf-8 -*-
import jieba
from multiprocessing import Pool
import os

def fenci(name1, name2, content):
	file1 = open(name1, "w")
	with open(name2, "r") as file2:
		thing = file2.read()
		#thing = thing.decode("utf-8")
		for i in jieba.cut(thing):
			i = ''.join(i.split())
			#i = i.decode("utf-8")
			if i in content:
				pass
			else:
				file1.write(i + " ")
	file1.close()



if __name__ == "__main__":
	content = []
	with open("CNstopword.txt", "r") as f:
		for line in f.readlines():
			#line = line.decode("utf-8")
			line = line.strip("\n")
			line = line.strip(" ")
			content.append(line)

	#name1 = "CN\\weibo1.txt"
	#name2 = "Chinese\\weibo1.txt" 
	#fenci(name1, name2, content)

	p = Pool(4)
	for i in range(1,501):
		name1 = "CN/weibo%d.txt" %(i)
		name2 = "chinese/weibo%d.txt" %(i)
		print (name1 + " " + name2)
		p.apply_async(fenci, args=(name1, name2, content))
	p.close()
	p.join()
