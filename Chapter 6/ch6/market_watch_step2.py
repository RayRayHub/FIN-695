'''
In this program, we simply create a display
of the time and date, and make it animated
so you can see the clock ticking each second

We added information on two indices and 3 stocks. Note that we put $ in front 
of stock prices, but we don't do that for index values

Note I refresh the frame every 5 seconds
root.after(5000, StockWatch)
otherwise there is information overload and the screen freezes


'''

from tkinter import *

import arrow
from yahoo_fin import stock_info as si

# create a root window hold all widgets
root = Tk()
#specify the title and size of the root window
root.title("U.S. Stock Market Watch")
root.geometry("1100x750")
# create a first label using hte Label() function
label = Label(text="", fg="Blue", font=("Helvetica", 80))
label.pack()
# create a second label
label2 = Label(text="", fg="Red", font=("Helvetica", 60))
label2.pack()
# set up tickers and names
tickers = ['^DJI','^GSPC','AAPL','AMZN','TSLA']
names = ['DOW JONES','S&P500', 'Apple', 'Amazon', 'Tesla']

# define the StockWatch() function
def StockWatch():

    #obtain current date and time infomration         
    tdate=arrow.now().format('MMMM DD, YYYY')
    tm=arrow.now().format('hh:mm:ss A')
    #put the date and time information in the first label         
    label.configure(text=tdate+"\n"+tm)


    #obtain live information about the DOW JONES index from Yahoo
    p1=round(float(si.get_live_price("^DJI")),2)
    m1=f'DOW JONES: {p1}'
    #obtain live information about the SP500 index from Yahoo 
    p2=round(float(si.get_live_price("^GSPC")),2)
    m2=f'S&P500: {p2}'      
    #obtain live price information for Apple stock from Yahoo        
    p3=round(float(si.get_live_price("AAPL")),2)
    m3=f'Apple: ${p3}'
    #obtain live price information for Amazon stock from Yahoo                
    p4=round(float(si.get_live_price("AMZN")),2)
    m4=f'Amazon: ${p4}'
    #obtain live price information for Tesla stock from Yahoo                
    p5=round(float(si.get_live_price("TSLA")),2)
    m5=f'Tesla: ${p5}'


    #put all the five messages on the stock market in the second label        
    label2.configure(text=m1+"\n"+m2+"\n"+m3+"\n"+m4+"\n"+m5, justify=LEFT)

    #call the StockWatch() function after 5000 milliseconds
    root.after(5000, StockWatch)
# call the StockWatch() function
StockWatch()  
# run the game loop
root.mainloop()




