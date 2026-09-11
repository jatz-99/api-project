import requests
response = requests.get("https://dog.ceo/api/breeds/image/random")
y= response.json()
print (y["message"], y["status"])