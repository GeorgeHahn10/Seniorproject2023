import requests
from datetime import datetime

URL = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&interval=1min&outputsize=full&adjusted=false&apikey="

URL_WEEK = "https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&apikey="

def request(ticker):
    r = requests.get(URL + "&symbol=" + ticker).json()
    r = str(r).replace("'", "\"")
    #with open("data/" + ticker + "_" + str(datetime.now()) + ".json", "w+") as file:
        #file.write(r)
    print(r)
    return r

def request_week(ticker):
    pass


if __name__ == "__main__":
    request("BA")