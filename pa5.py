import nltk;
import nltk.corpus;

#	这里先把布朗库的tag转换成universal再做。
#	a
data = nltk.corpus.brown.tagged_words(tagset="universal")
tdata = [word for (word, tag) in data if tag == "NOUN"]
fd = nltk.FreqDist(tdata)
ans = []
for word in fd.keys():
	words = word + 's'
	if fd[words] / fd[word] > 1:
		ans = ans + [(-fd[words] / fd[word], word)]
ans = sorted(ans)
ans = [(word, -val) for (val, word) in ans]
print(ans[0:20])
print("")

#	b
data = nltk.corpus.brown.tagged_words()
tdata = list(set(data))
tdata = [word for (word, tag) in tdata]
print(nltk.FreqDist(tdata).most_common(20))
print("")

#	c
print(nltk.FreqDist([tag for (word, tag) in data]).most_common(20))
print("")
# NN 	名词
# IN 	介词
# AT  article?
# JJ  形容词
# .	句号
# ,	逗号
# NNS	名词复数
# CC	连词
# RB	副词
# NP	人名?
# VB 	动词
# VBN	动词过去分词
# VBD	动词过去式
# CS	连词?
# PPS 第三人称代词
# VBG	动词现在分词
# PP$	定词?
# TO	to
# PPSS非第三人称单数代词
# CD	数词

#	d
tdata = [tag for (word, tag) in data]
tdata = [tag2 for (tag1, tag2) in nltk.bigrams(tdata) if tag1[0:2] == 'NN']
print(nltk.FreqDist(tdata).most_common(20))
print("")
# IN	介词
# .	句号
# ,	逗号
# CC	连词
# NN	名词
# NNS	名词复数
# VBD	动词过去式
# CS	连词？
# MD	情态助词
# BEZ	is？
# ''	引号
# RB	副词
# TO	to
# BEDZwas
# VBN	动词过去分词
# WPS	wh-代词
# NN-TL
# VBZ	第三人称一般现在时
# VB	动词原形
# BER	are

#	2
#	train on data[:size], evaluate on the whole dataset
from nltk.corpus import brown
def performance(cfd, wordlist):
	lt = dict((word, cfd[word].max()) for word in wordlist)
	baseline_tagger = nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))
	return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))

def display():
	import pylab
	words = nltk.FreqDist(brown.words(categories='news'))
	sizes = 2 ** pylab.arange(15)
	print(sizes);
	perfs = []
	print(len(brown.tagged_words(categories='news')))
	for size in sizes:
		train_data = list(brown.tagged_words(categories='news'))
		train_data = train_data[:size]
		wordlist = [word for (word, times) in train_data]
		cfd = nltk.ConditionalFreqDist(train_data)
		perfs = perfs + [performance(cfd, wordlist)]
	pylab.plot(sizes, perfs, '-bo')
	pylab.title('Lookup Tagger Performance with Varying Model Size')
	pylab.xlabel('Model Size')
	pylab.ylabel('Performance')
	pylab.show()

display()