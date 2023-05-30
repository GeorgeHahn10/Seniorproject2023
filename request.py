import requests
from datetime import datetime

URL = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&interval=1min&outputsize=full&adjusted=false&apikey="

def request(ticker):
    r = requests.get(URL + "&symbol=" + ticker).json()
    with open(ticker + "_" + str(datetime.now()) + ".json", "w+") as file:
        file.write(str(r))
    print(r)


if __name__ == "__main__":
    print("hello")
    request("BA")