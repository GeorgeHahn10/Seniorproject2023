import matplotlib.pyplot as plt
import json
from request import request
from MarketData import MarketData


def parse(raw_data):
    market_data = []

    time_series = json.loads(raw_data)["Time Series (1min)"]

    for key in time_series.keys():
        datetime = key.split(" ")
        date = datetime[0]
        time = datetime[1]
        price = float(time_series[key]["4. close"])
        market_data.append(MarketData(date, time, price))
    return market_data


class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.market_data = {} # key: date, value: list(double(market data))

    def populate(self, date, file):
        self.market_data[date] = parse(json.loads(file.readlines()[0].replace("'", "\"")))

    def populate(self):
        market_data = parse(request(self.ticker))
        for md in market_data:
            if md.date not in self.market_data:
                self.market_data[md.date] = []
            self.market_data[md.date].append(md)

    def plot(self, date):
        market_data = self.market_data[date]
        prices = [md.price for md in market_data]
        times = [md.time for md in market_data]

        fig, ax = plt.subplots()
        ax.plot(times, prices)
        plt.title(self.ticker + " Stock Prices")
        plt.xlabel("Minute of Day")
        plt.ylabel("Stock Price")
        plt.show()
