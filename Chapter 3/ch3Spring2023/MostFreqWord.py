news=(
'''The fastest growing segment of the U.S. electorate is seniors.
They supported President Trump in 2016 but aren’t squarely
in his camp as the 2020 campaign picks up.
In 2016, despite polling showing an advantage for Democrat Hillary Clinton,
voters over 65 backed Mr. Trump in the presidential election by a margin,
according to exit polls.
''')
wdcnt=dict()
words=news.split()
for word in words:
    wdcnt[word]=wdcnt.get(word,0)+1
lst=list()

for wd, cnt in list(wdcnt.items()):
    lst.append((cnt,wd))
lst.sort(reverse=True)
print(lst)