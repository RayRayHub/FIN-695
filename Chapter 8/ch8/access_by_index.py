import pandas as pd
series = pd.Series({'a': 1, 'b': 2, 'c':3})
print(series['a'])

wine_dict = {
'red_wine': [3, 6, 5],
'white_wine':[5, 0, 10]
}
sales = pd.DataFrame(wine_dict, index=["adam", "bob", "charles"])
