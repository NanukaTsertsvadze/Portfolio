import requests
import json
import sqlite3

#Make a reques

url="https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"



parameters = {
  'start':'1',
  'limit':'5',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'da96bdd1-05d6-40e8-8b46-3b5b5acf451d',
}

response = requests.get(url, params=parameters, headers=headers)
# print(response)

# Making Json Structure
result =json.loads(response.text)
result = json.dumps(result, indent=4)
# print(type(result))

#Making Json File 
file = open("Crypto.json", "w")
file.write(result)
file.close()

#Creating Database and keeping info in it
connect = sqlite3.connect("Crypto.sqlite")
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS crypto(
                name TEXT,
                price FLOAT
);""")


#Taking info from Json file
response1 = requests.get(url, params=parameters, headers=headers).json()
coins = response1["data"]
for x in coins: 
    name = x["name"]
    price = x["quote"]["USD"]["price"]
    # print(name)
    # print(price)
    cursor.execute("INSERT INTO Crypto (name, price) VALUES (? ,?)", (name, price))
    connect.commit()

connect.close()








