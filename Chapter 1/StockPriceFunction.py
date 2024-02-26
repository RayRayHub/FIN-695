def StockPrice(div, g, r):
    Price = (div*(1+g)/(r-g)) #
    return Price #
print(StockPrice(2, 0.05, 0.1)) #

