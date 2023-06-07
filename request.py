import requests
from datetime import datetime

URL = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&interval=1min&outputsize=full&adjusted=false&apikey=PJNT54CJJ4A2CTA8"

def request(ticker):
    r = requests.get(URL + "&symbol=" + ticker).json()
    r = str(r).replace("'", "\"")
    with open("data/" + ticker + "_" + str(datetime.now()) + ".json", "w+") as file:
        file.write(r)
    print(r)


if __name__ == "__main__":
    request("BA")