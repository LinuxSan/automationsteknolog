# 04-data-cleaning.py
# Data cleaning med Pandas

import pandas as pd

data = {'navn': ['Anna', 'Bent', None], 'alder': [23, None, 19]}
df = pd.DataFrame(data)

# Fjern rækker med manglende værdier
df_clean = df.dropna()
print("Uden manglende værdier:")
print(df_clean)

# Udfyld manglende værdier
df_fill = df.fillna({'navn': 'Ukendt', 'alder': 0})
print("Udfyldt:")
print(df_fill)
