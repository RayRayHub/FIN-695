# import needed modules
from tkinter import *

import arrow
from yahoo_fin import stock_info as si

# create a root window hold all widgets
root = Tk()
#specify the title and size of the root window
root.title("U.S. Stock Market Watch")
root.geometry("1150x700")
# create a first label using hte Label() function
label = Label(text="", fg="Blue", font=("Helvetica", 80))
label.pack()
# create a second label
label2 = Label(text="", fg="Red", font=("Helvetica", 60))
label2.pack()
# set up tickers and names
tickers = ['^IRX','^FVX','^TNX','^TYX']
names = ['13-Week Treasury Bill','Five-Year Treasury Bond', 'Ten-Year Treasury Bond', '30-Year Treasury Bond']
# set up the oldprice values and price bounds
oldprice=[]
maxprice=[]
minprice=[]
for i in range(4):
    p=round(float(si.get_live_price(tickers[i])),2)
    oldprice.append(p)
    maxprice.append(p*1.05)
    minprice.append(p*0.95)
    #if i<=1:
    print(f'The latest value for {names[i]} is {p}!')            
    #else:
        #print(f'The latest stock price for {names[i]} is ${p}!') 
# define the StockWatch() function
def StockWatch():
    #declare global variables 
    global oldprice
    #obtain live information about the 13-Week Treasury Bill rate from Yahoo
    p1=round(float(si.get_live_price("^IRX")),2)
    m1=f'13-Week Treasury Bill: {p1}'
    #obtain live information about the Five-Year Treasury Bond rate from Yahoo 
    p2=round(float(si.get_live_price("^FVX")),2)
    m2=f'Five-Year Treasury Bond: {p2}'      
    #obtain live price information for Ten-Year Treasury Bond rate from Yahoo        
    p3=round(float(si.get_live_price("^TNX")),2)
    m3=f'Ten-Year Treasury Bond: {p3}'
    #obtain live price information for 30-Year Treasury Bond rate from Yahoo                
    p4=round(float(si.get_live_price("^TYX")),2)
    m4=f'30-Year Treasury Bond: {p4}'
    # #obtain live price information for Tesla stock from Yahoo                
    # p5=round(float(si.get_live_price("TSLA")),2)
    # m5=f'Tesla: ${p5}'
    # put the five prices in a list p
    p=[p1,p2,p3,p4]
    #obtain current date and time infomration         
    tdate=arrow.now().format('MMMM DD, YYYY')
    tm=arrow.now().format('hh:mm:ss A')
    #put the date and time information in the first label         
    label.configure(text=tdate+"\n"+tm)
    #put all the five messages on the stock market in the second label        
    label2.configure(text=m1+"\n"+m2+"\n"+m3+"\n"+m4, justify=LEFT)
    # if there is update in the marekt, announce it
    for i in range(4):     
        if p[i]!=oldprice[i]:
            oldprice[i]=p[i]
           # if i<=1:
            print(f'The latest value for {names[i]} is {p[i]}!')            
            #else:
                #print(f'The latest stock price for {names[i]} is ${p[i]}!') 
    # if price goes out of bounds, announce it
    # for i in range(4):     
    #     if p[i]>maxprice[i]:
    #         print(f'{names[i]} has moved above the upper bound!')            
    #     if p[i]<minprice[i]:
    #         print(f'{names[i]} has moved below the lower bound!')            
    #call the StockWatch() function after 5000 milliseconds
    root.after(12000, StockWatch)
# call the StockWatch() function
StockWatch()  
# run the game loop
root.mainloop()
