# -*- coding:utf-8 -*-

import os
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

# 获取要处理的文件
def getFilelist(filename):
	filelist = []
	files = os.listdir(filename)
	for f in files:
		filelist.append(f)
	return filelist


def Tfidf(filelist):
	corpus = [] # 存取分词结果
	path = "CN/"
	for item in range(1,501):
		fname = path + "weibo%d.txt" %(item)
		with open(fname, "r") as f:
			content = f.read()
			corpus.append(content)
	vectorizer = CountVectorizer()
	transformer = TfidfTransformer()
	tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
	word = vectorizer.get_feature_names() # 所有文本的关键字
	weight = tfidf.toarray() # 对应的tf-idf矩阵
	
	sFilePath = "TFIDf/"
	for i in range(len(weight)):
		f = open(sFilePath + "weibo%d.txt" %(i+1), "w")
		for j in range(len(word)):
			f.write(word[j] + ":" + str(weight[i][j]) + "\n")
		f.close()

if __name__ == "__main__":
	filelist = getFilelist("CN/")
	Tfidf(filelist)
