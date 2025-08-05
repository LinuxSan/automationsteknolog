# 05-time-series.py
# Tidsserier med Pandas

import pandas as pd
import numpy as np

datoer = pd.date_range('2025-01-01', periods=5)
data = np.random.randint(0, 100, size=5)
df = pd.DataFrame({'dato': datoer, 'værdi': data})
print(df)

# Sæt dato som index
df.set_index('dato', inplace=True)
print(df)
