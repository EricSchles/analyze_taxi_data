import pandas as pd
import numpy as np

df = pd.DataFrame()
columns = ["A", "B", "C", "D", "E"]
for column in columns:
    df[column] = np.random.randn(1000)

df.to_csv("random_data.csv", index=False)

