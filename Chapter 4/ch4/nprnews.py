#import needed modules
import requests
import bs4
import webbrowser
#locate the website for the NPR news brief
url = 'https://www.npr.org/podcasts/500005/npr-news-now'
#convert the source code to a soup string
response=requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html')
#locate the tag that contains the mp3 files
casts = soup.findAll('a', {'class': 'audio-module-listen'})
print(casts)
#obtain the weblink for the mp3 file related to the latest news brief
cast=casts[0]['href']
print(cast)
#remove the unwanted compoents in the link
pos=cast.find("?")
print(cast[0:pos])
#extract the mp3 file link, and play the file
mymp3=cast[0:pos]
webbrowser.open(mymp3)   
