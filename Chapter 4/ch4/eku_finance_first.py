#import needed modules
from bs4 import BeautifulSoup
import requests
#provide the web address of the live web
url = 'https://finance.eku.edu/people#_ga=2.106102083.1757686072.1659636719-6595508.1659636719'
#obtain information from the live web
page = requests.get(url)
# parse the page to obtain the parent div tag
soup = BeautifulSoup(page.text, "html.parser")
# find all div tags with class attribute people-profile
profs = soup.find_all('div', class_="people-profile")
# Let's first work on the first profile 
prof1=profs[0]
#print(prof1)
# name is in the <h2> tag
name = prof1.find("h2")
print(name.text)
# find all listings for this faculty
listings=prof1.find_all("li")

#print(listings)

# The fifth listing is the email
# first method to get email
email=listings[4].text
print(email)
# second method to get email
email2=listings[4].find("a")["href"]
print(email2)
# The sixth listing is the phone number
# get phone number 
phone=listings[5].text
print(phone)
