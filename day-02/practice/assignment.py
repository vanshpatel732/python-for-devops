import requests
import json

url = "https://api.frankfurter.dev/v1/"
base = "USD"
query = f"latest?base={base}"

response = requests.get(url+query)
#print(response.json())
data = response.json()

print(f"The currect exchange rate of {base} and INR is ", data["rates"]["INR"])
# I am going to try to find INR or whatever rates that user wants conversion 
input1 = input("Input the symbol you want to convert from ")
input2 = input("Input the symbol you want to convert to ")

rate1 = data["rates"][input1]
rate2 = data["rates"][input2]
final_rate = rate2/rate1
print(f"The converted rate from {input1} to {input2} is {final_rate}")

data_to_save = {
    "input1" : input1,
    "input2" : input2,
    "rate1" : rate1,
    "rate2" : rate2,
    "converted rate": final_rate,
}

with open ('output.json', 'w') as json_file:
    json.dump(data_to_save, json_file)