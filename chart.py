import numpy as np # for math ops
import matplotlib.pyplot as plt # making figures of graphs
import pandas as pd # handle table like data, excel
import sys
import datetime # for handling date and time in python


## Read price dataset from a CSV file.
price = pd.read_csv("../dataset/pricedata_reshaped.csv") # DataFrame is returned
price_apple = price["AAPL"] # get Apple's price
price_nvidia = price["NVDA"] # get Nvidia's price

## Convert strings like "2015-10-01" to Python datetime objects. We can't
## feed strings directly to Matplotlib.
date_strings = price["date"].to_list() # ["2015-10-01", "2015-10-02", ...]
date = []
# convert strings to datetime objects
for i in range(len(date_strings)): # i = 0, ...., 1413
    # append to list
    date += [datetime.datetime.strptime(date_strings[i], "%Y-%m-%d")]


## Make a fugre and graph
fig = plt.figure() # make a canvas
plt.plot(date, price_apple, label="Apple (AAPL)") # draw line chart
plt.plot(date, price_nvidia, label="Nvidia (NVDA)") # add one more line
plt.grid() # add grid line (optional)
plt.xlabel("date") # add label to the x-axis (optional)
plt.ylabel("price") # add label to the y-axis (optional)
plt.legend(loc="best") # add label of the lines (optional)
plt.suptitle("Apple's price - 5Y") # add title of figure (optional)
fig.savefig("prices.png") # save as image