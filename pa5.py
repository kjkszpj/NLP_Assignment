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

#	b
tdata = list(set(data))
tdata = [word for (word, tag) in tdata]
print(nltk.FreqDist(tdata).most_common(20))

#	c
print(nltk.FreqDist([tag for (word, tag) in data]).most_common(20))
#	TODO

#	d
#	TODO
