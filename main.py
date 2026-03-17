import pandas as pd
import numpy as np
import matplotlib 
import matplotlib.pyplot as mpl

viewingActivity = pd.read_csv("ViewingActivity.csv", header=0, sep=",")


viewingActivity['Duration']= viewingActivity['Duration'].astype('timedelta64[us]')
viewingActivity['Start Time']= viewingActivity['Start Time'].astype('datetime64[ns]')
viewingActivity['Profile Name']= viewingActivity['Profile Name'].astype('category')


print(viewingActivity.info())

# print(viewingActivity["Profile Name"].value_counts())

# viewingActivity["Profile Name"].value_counts().plot(kind= 'bar')
# mpl.show()