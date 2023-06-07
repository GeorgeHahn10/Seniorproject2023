import matplotlib.pyplot as plt
import json

URL = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&interval=1min&outputsize=full&adjusted=false&apikey=PJNT54CJJ4A2CTA8"

FILE = "data/BA_2023-06-07 14:39:38.824716.json"

file = open(FILE)

data = json.loads(file.readlines()[0].replace("'", "\""))

stock_price = []

time_series = data["Time Series (1min)"]

for key in time_series.keys():
    stock_price.append(float(time_series[key]["4. close"]))

fig, ax = plt.subplots()
ax.plot(stock_price)
plt.title("Stock Prices")
plt.xlabel("Minute of Day")
plt.ylabel("Stock Price")
plt.show()

