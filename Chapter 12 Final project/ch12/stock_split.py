
import datetime as dt
import pandas as pd
import pandas_datareader.data as web

start = dt.datetime(2019, 7, 11)
end = dt.datetime(2019, 7, 24)


df = web.DataReader("AAPL", 'yahoo', start, end)
pd.options.display.float_format = "{:,.2f}".format
print(df)
