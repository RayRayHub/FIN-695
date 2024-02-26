'''
In this program, we simply create a display
of the time and date, and make it animated
so you can see the clock ticking each second

No stock price information yet
This shows you how graphics and animation works 
'''

# import needed modules
import tkinter as tk

import arrow
from yahoo_fin import stock_info as si

# create a root window hold all widgets
root = tk.Tk()
#specify the title and size of the root window
root.title("U.S. Stock Market Watch")
root.geometry("1000x800")
# create a first label using hte Label() function
label = tk.Label(text="", fg="Blue", font=("Helvetica", 80))
label.pack()

# create a second label for indexes
label2 = tk.Label(text="", fg="Green", font=("Helvetica", 60))
label2.pack()

# set up tickers and names
tickers = ['^DJI','^GSPC',"AAPL","MSFT","TLSA"]
names = ['DOW JONES','S&P500','APPLE','MICROSOFT','TESLA']

oldprice=[]
maxprice=[]
minprice=[]

for i in range(len(ticker)):
    prc=round(si.get_live_price(tickers[i]),2)
    oldprice.append(prc)
    maxprice.append(prc*1.01)
    minprice.append(prc*99)

# define the StockWatch() function
def StockWatch():

    #obtain current date and time infomration         
    tdate=arrow.now().format('YYYY-MM-DD')
    tm=arrow.now().format('HH:mm:ss')
    #put the date and time information in the first label         
    label.configure(text=tdate+"\n"+tm) 
    m=""
    #loop
    for i in range(len(tickers)):
        prc = round(float(si.get_live_price(tickers[i])), 2)
        if i<=1:    
            mi=f"{names[i]}: {prc}\n"
        else:
            mi=f"{names[i]}: ${prc}\n"

        m+=mi
        # trigger alerts
        if prc>maxprice[i]:
            print(f"{names[i]} went up by more than 1 percent.")
        if prc<minprice[i]:
            print(f"{names[i]} went up by more than 1 percent.")
        
    label2.config(text=m)
    #call the StockWatch() function after 5000 milliseconds
    root.after(1000, StockWatch)

# call the StockWatch() function
StockWatch()  
# run the game loop
root.mainloop()



