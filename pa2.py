######
#	ex1，做成大小写不敏感(And, and算一个词)
#	ex2，忽略了有标点/数字的bigram。dict好像是无序的，所以我转成list然后再sort...
#	ex3，生成出来的随机文本并不符合句法。可以使用HMM？
######
from random import shuffle

import nltk
from nltk.book import *

def gen_next(cfdist):
	cnt = []
	for i in cfdist:
		cnt += [i] * cfdist[i]
	if cnt == []: return false
	shuffle(cnt)	
	return cnt[0]

print('------ex1------')
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
emma = [s.lower() for s in emma]	#	all lower
print(len(emma))
print(len(set(emma)))

print('------ex2------')
stopw = nltk.corpus.stopwords.words('english')
bg = [(a, b) for (a, b) in nltk.bigrams(emma) if a.isalpha() and b.isalpha() and a not in stopw and b not in stopw]
freq_bg = nltk.FreqDist(bg)
print([i for i in freq_bg.most_common(50)])

#	optional
print('------ex3------')
bg = nltk.bigrams(text3)
cfdist = nltk.ConditionalFreqDist(bg)
start_word = 'then'
for i in range(1000):
	print(start_word, end = ' ')
	start_word = gen_next(cfdist[start_word])
print('...')
