import matplotlib.pyplot as plt
import json
import numpy as np

FILE = "data/BA_2023-05-29 18:15:04.787691.json"

file = open(FILE)

data = json.loads(file.readlines()[0].replace("'", "\""))

stock_price = []

time_series = data["Time Series (1min)"]

for key in time_series.keys():
    stock_price.append(float(time_series[key]["4. close"]))


fig, ax = plt.subplots()
ax.plot(stock_price)
plt.show()

