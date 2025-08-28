import pandas as pd
import matplotlib.pyplot as plt

print("pandas version:", pd.__version__)
data = pd.DataFrame({"x": [1, 2, 3], "y": [1, 4, 9]})
print(data)
data.plot(x="x", y="y", kind="line")
plt.show()
