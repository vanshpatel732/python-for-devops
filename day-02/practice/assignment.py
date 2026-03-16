import requests

response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo")

print(type(response.json()))

#print(response.json())
data = response.json()
for (key, value) in data["Time Series (5min)"].items():
    print("timestamp:", key)

    if key == "2026-03-13 11:25:00":
        open1 = value["1. open"]

print(f"The stock opened at {open1}")