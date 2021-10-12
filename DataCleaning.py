import pandas as pd
import numpy as np

s = pd.Series(['a', 3, np.nan, 1, np.nan])

print(s.notnull().sum())

s = pd.Series([np.nan, 1, 2, np.nan, 3])
#s = s.fillna(method='ffill')
p = pd.Series([1, 2, 1, 2, 4])


#print(s)
print(s.duplicated())
print(p.duplicated())