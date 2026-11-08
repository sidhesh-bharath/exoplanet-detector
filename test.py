import pandas as pd

df = pd.read_csv("./src/targets.csv", header=None, dtype=str, skipinitialspace=True).iloc[0].tolist()

for i in df:
    print(i)