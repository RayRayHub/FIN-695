from bs4 import BeautifulSoup
textfile = open("UKYexample.html", encoding=('utf8'))
soup = BeautifulSoup(textfile, "html.parser")
ptags = soup.findAll("p")
print(ptags)