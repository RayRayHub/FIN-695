#Question 1
print("Output for question 1:")
for i in range(5): print(i) # 0,1,2,3,4
for i in range(10,15): print(i) # 10,11,12,13,14
for i in range(10,15,2): print(i) # 10,12,14
print()

#Question 2
print("Output for question 2:")
def printcellpos(rows):
    for col in ("A","B"):
        for row in range(1, rows+1):
            print("{0}{1}".format(col, row))
            
printcellpos(6) # A1,A2,A3,A4,A5,A6,B1,B2,B3,B4,B5,B6
print()

#Question 3
print("Output for question 3:")
from CreateLocalModule import StockPrice as OriginalStockPrice
print(OriginalStockPrice(5, 0.08, 0.1)) # 269.99999999999994
print()

#Question 4
print("Output for question 4:")
import ImportLocalModule1
print(ImportLocalModule1.CreateLocalModule.StockPrice(5, 0.08, 0.1))
print()

#Question 5
print("Output for question 5:")
from ImportLocalModule2 import *
print(StockPrice(5, 0.08, 0.1))
print()

#Question 6
print("Output for question 6:")
from ImportTotalSales import TotalSales
print(TotalSales([100,200,300]))
print(TotalSales([500,600,900]))