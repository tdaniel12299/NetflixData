import pandas as pd
import numpy as np

viewingActivity = pd.read_csv("ViewingActivity.csv", header=0, sep=",")


print(viewingActivity.shape)

print(viewingActivity["Profile Name"].unique())

print(viewingActivity["Device Type"].unique())

print(viewingActivity.dtypes)