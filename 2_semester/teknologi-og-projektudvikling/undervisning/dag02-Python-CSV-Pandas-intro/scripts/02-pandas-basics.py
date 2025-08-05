# 02-pandas-basics.py
# Grundlæggende Pandas: Series og DataFrame

import pandas as pd

# Opret en Series
s = pd.Series([1, 2, 3, 4])
print("Series:")
print(s)

# Opret en DataFrame
data = {'navn': ['Anna', 'Bent', 'Carla'], 'alder': [23, 31, 19]}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
