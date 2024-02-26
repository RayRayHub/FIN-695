#import needed modules
from bs4 import BeautifulSoup
import requests
#provide the web address of the live web
url = 'http://libraries.uky.edu/'
#obtain information from the live web
page = requests.get(url)
# parse the page to obtain the parent div tag
soup = BeautifulSoup(page.text, "html.parser")
contacts = soup.findChildren('table', {'class':"contact-table"})
table = contacts[0]

# Now use a loop to print out all four contact' info
for row in table.findChildren('tr'):
    name = row.find("th") 
    print(name.text)
    phone=row.find("p")
    print(phone.text)
    
    
    