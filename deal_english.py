import re

def chuli1(name1, name2):
	content = []
	with open("english\\english_stopkey.txt", "r") as f:
		for line in f.readlines():
			line = line.strip("\n")
			line = line.strip(" ")
			content.append(line)
	fnew = open(name2, "w")
	with open(name1, "r") as ff:
		thing = ff.read()
		thing = thing.split(" ")
		for i in thing:
			if i not in content:
				i = i.strip("!")
				i = i.strip(",")
				i = i.strip(".")
				fnew.write(i + " ")
	fnew.close()


for item in range(78):
	name1 = "content_%d.txt" %(item)
	name2 = "english\\english_%d.txt" %(item)
	chuli1(name1, name2)