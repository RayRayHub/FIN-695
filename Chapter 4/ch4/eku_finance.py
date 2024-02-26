#import needed modules
from bs4 import BeautifulSoup
import requests
#provide the web address of the live web
url = 'https://finance.eku.edu/people#_ga=2.106102083.1757686072.1659636719-6595508.1659636719'
#obtain information from the live web
page = requests.get(url)
# parse the page to obtain the parent div tag
soup = BeautifulSoup(page.text, "html.parser")
profs = soup.find_all('div', class_="people-profile")
# Now use a loop to print out all four professors' info
for prof in profs:
    name = prof.find("h2")
    print(name.text)
    listings=prof.find_all("li")
    email=listings[4].text
    print(email)
    phone=listings[5].text
    print(phone)
    
    
    