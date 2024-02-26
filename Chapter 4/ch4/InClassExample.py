from bs4 import BeautifulSoup

txtfile = open("UKYexample.html", encoding=("utf8"))

soup = BeautifulSoup(txtfile, "html.parser")
print(soup)

atags = soup.findAll("a")
print(soup)

first_atag = atags[0]
print(first_atag)

#find the url for CNN
cnn_url = first_atag["href"]
cnn_text = first_atag.text
print(cnn_url)
print(cnn_text)

second_atag = atags[1]
print(second_atag)

#find the url for CNN
directories_url = second_atag["href"]
directories_text = second_atag.text
print(directories_url)
print(directories_text)