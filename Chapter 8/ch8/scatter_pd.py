import pandas as pd
presidents_df = pd.read_csv('presidents.csv', index_col='name')

presidents_df.plot(kind = 'scatter', 
                    x = 'height', 
                    y = 'age',
                    title = 'U.S. presidents')
