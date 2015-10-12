import nltk
from nltk.book import *

#	1
print('------Part 1------')
text2.dispersion_plot(['Elinor', 'Marianne', 'Edward', 'Willoughby'])

#	2
print('------Part 2------')
ans1 = set([w for w in text5 if len(w) > 0 and w[0] == 't'])
print(ans1)
ans2 = nltk.FreqDist([w for w in text5 if len(w) == 5])
print(ans2)

#	3
print('------Part 3------')
ans1 = list(set([w for w in text2 if len(w) >= 2 and w[-2:] == 'er']))
print('\n\tend with er')
print(ans1)
ans2 = list(set([w for w in text2 if 'w' in w]))
print('\n\tw')
print(ans2)
print('\n\tph')
ans3 = list(set([w for w in text2 if 'ph' in w]))
print(ans3)
print('\n\ttitlecase')
ans4 = list(set([w for w in text3 if w[0].isupper() and w[1:].islower()]))
print(ans4)
