# -*- coding:utf-8 -*-

import jieba
#import codecs

content = []
def fenci(name):
	with open(name, 'r') as f:
		file = f.read()
		f_ = open("stopwords.txt", "r")
		#print(f_.read().decode())
		for line in f_.readlines():
			#print (type(line))
			line = line.strip('\n')
			#print (line)
			content.append(line)
			#print (line.encode('utf-8'))
		for i in jieba.cut(file):
			if i in content:
				pass
			else:
				print(i)
				#content.append(i)	
		f_.close()


fenci("chinese/weibo181.txt")
print (content)
	                                                                                                                                                                                                                                                                                                                                          
	
