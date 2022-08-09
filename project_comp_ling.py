import nltk
import csv
import collections
from collections import Counter
from nltk import pos_tag

#FOR MEN
fileM1 = open('/Users/yana/Documents/OneDrive/Studies/Old/КЛ/Project/MEN_COUNTER.csv', 'w')
text = []
chars = ['.', ',', '!', '...', ':', ';', '-', '(', ')', '"', '?', ' - ', '«', '»', '— ']
fM1 = open('/Users/yana/Documents/OneDrive/Studies/Old/КЛ/Project/Texts/Erofeev.txt', 'r').read()
fM1 = fM1.lower()
for char in chars:
    fM1 = fM1.replace(str(char), '')
postags = pos_tag(fM1.split(), lang='rus')

for p in postags:
    print(str(p) + '\n')

for p in postags:
    text.append(p[1])
count = Counter(text).most_common()
for c in count:
    s = str(c[0]) + ';' + str(c[1])
    fileM1.write(s + '\n')
fileM1.close()

fileM2 = open('/Users/yana/Documents/OneDrive/Studies/Old/КЛ/Project/MEN_RATIO.csv', 'w')
count = Counter(text).most_common()
for cc in count:
    s = str(cc[1]/len(fM1.split()))
    fileM2.write(s + '\n')
fileM2.close()

i=0
n=0
fileM3 = open('/Users/yana/Documents/OneDrive/Studies/Old/КЛ/Project/MEN_LENGTH.csv', 'w')
FM3 = open('/Users/yana/Documents/OneDrive/Studies/Old/КЛ/Project/Texts/Erofeev.txt', 'r').read()
fM3 = FM3.split('.' or '?' or '!')
for fm3 in fM3:
    i+=len(fm3.split())
    n+=1
s=str(i/n)
fileM3.write(s)
fileM3.close()


#FOR WOMEN
fileW1 = open('/Users/yana/Documents/OneDrive/Studies/Old/КЛ/Project/WOMEN_COUNTER.csv', 'w')
text = []
chars = ['.', ',', '!', '...', ':', ';', '-', '(', ')', '"', '?', ' - ', '«', '»', '— ']
fW1 = open('/Users/yana/Documents/OneDrive/Studies/Old/КЛ/Project/Texts/Tokareva.txt', 'r').read()
fW1 = fW1.lower()
for char in chars:
    fW1 = fW1.replace(str(char), '')
postags = pos_tag(fW1.split(), lang='rus')

for p in postags:
    print(str(p) + '\n')

for p in postags:
    text.append(p[1])
count = Counter(text).most_common()
for c in count:
    s = str(c[0]) + ';' + str(c[1])
    fileW1.write(s + '\n')
fileW1.close()

fileW2 = open('/Users/yana/Documents/OneDrive/Studies/Old/КЛ/Project/WOMEN_RATIO.csv', 'w')
count = Counter(text).most_common()
for cc in count:
    s = str(cc[1]/len(fW1.split()))
    fileW2.write(s + '\n')
fileW2.close()

i=0
n=0
fileW3 = open('/Users/yana/Documents/OneDrive/Studies/Old/КЛ/Project/WOMEN_LENGTH.csv', 'w')
FW3 = open('/Users/yana/Documents/OneDrive/Studies/Old/КЛ/Project/Texts/Tokareva.txt', 'r').read()
fW3 = FW3.split('.' or '?' or '!')
for fw3 in fW3:
    i+=len(fw3.split())
    n+=1
s=str(i/n)
fileW3.write(s)
fileW3.close()
