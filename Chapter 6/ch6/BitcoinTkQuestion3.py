#import the needed modules
from tkinter import *

import arrow
import requests

# specify the url to find the bitcoin price
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
# create a root window hold all widgets
root = Tk()
#specify the title and size of the root window
root.title("Bitcoin Watch")
root.geometry("1000x400")
# create a first label using hte Label() function
label = Label(text="", fg="Blue", font=("Helvetica", 80))
label.pack()
# create a second label
label2 = Label(text="", fg="Red", font=("Helvetica", 60))
label2.pack()
# define the BitcoinWatch() function
def BitcoinWatch():
    global oldprice
    #get the live information from bitcoin url, put the price in m1
    response = requests.get(url)
    response_json = response.json()
    price=response_json['bpi']['USD']['rate']
    #obtain current date and time infomration         
    tdate=arrow.now().format('MMMM DD, YYYY')
    tm=arrow.now().format('hh:mm:ss A')
    #put the date and time information in the first label         
    label.configure(text=tdate+"\n"+tm)
    #put all the five messages on the stock market in the second label        
    label2.configure(text=f'Bitcoin: {price}', justify=LEFT)     
    #call the BitcoinWatch() function after 1000 milliseconds
    root.after(800, BitcoinWatch)
# call the BitcoinWatch() function
BitcoinWatch()  
# run the game loop
root.mainloop()
