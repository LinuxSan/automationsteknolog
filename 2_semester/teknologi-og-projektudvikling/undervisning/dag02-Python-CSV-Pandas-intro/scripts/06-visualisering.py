# 06-visualisering.py
# Visualisering med Pandas og Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

data = {'år': [2021, 2022, 2023], 'salg': [150, 200, 180]}
df = pd.DataFrame(data)

plt.plot(df['år'], df['salg'])
plt.xlabel('År')
plt.ylabel('Salg')
plt.title('Salg over tid')
plt.show()
