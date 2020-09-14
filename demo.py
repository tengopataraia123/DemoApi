import requests

url = "https://unilabdemoapi.herokuapp.com/FreqDist"

payload = "{\r\n\"text\" : \"This is my first demo text for hosted API\"\r\n} "
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
