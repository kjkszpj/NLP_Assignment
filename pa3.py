######
#	第一题
#	[a-zA-Z]+:	匹配任意个大或小写字母组成的单词
#	[A-Z][a-z]*:	匹配大写字母开头的单词
#	p[aeiou]{,2}t:	匹配p*t或p**t类型的单词，*是元音字母
#	\d+(\.\d+)?:	匹配整数和小数
#	([^aeiou][aeiou][^aeiou])*:匹配babbabbabbab类型的字符串? a是小写元音字母，b是不是小写元音字母的东西??
#	\w+|[^\w\s]+:	匹配连续的字母或者连续的非字母非空白字符
######

#	第二题
#	假设单词不包含空格
content = open('a.in').readlines()
result0 = []
for s in content:
	a, b = s.split(' ')
	if b[-1] == '\n': b = b[:-1]
	result0.append([a, int(b)])
print(result0)

#	第三题
silly = 'newly formed bland ideas are inexpressible in an infuriating way'
bland = silly.split(' ')
print(''.join([s[1] for s in bland]))
print(' '.join(bland))

