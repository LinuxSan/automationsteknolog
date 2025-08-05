# 03-import-export.py
# Import og eksport af CSV-filer med Pandas

import pandas as pd

# Læs en CSV-fil (eksempel.csv skal findes)
df = pd.read_csv('eksempel.csv')
print(df.head())

# Gem DataFrame til ny CSV-fil
df.to_csv('ny_fil.csv', index=False)
