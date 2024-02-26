news=(
'''The fastest growing segment of the U.S. electorate is seniors.
They supported President Trump in 2016 but aren’t squarely
in his camp as the 2020 campaign picks up.
In 2016, despite polling showing an advantage for Democrat Hillary Clinton,
voters over 65 backed Mr. Trump in the presidential election by a margin,
according to exit polls.
''').lower()
wordcount=dict() #
words=news.split()
for word in words:
    wordcount[word]=wordcount.get(word,0)+1
lst=list() #
for wd, cnt in list(wordcount.items()): #
    lst.append((cnt,wd))
    lst.sort(reverse=True, ) #
print(lst)