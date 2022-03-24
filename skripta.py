import http.client
import json

conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
payload = json.dumps({
  "ime": "Petar",
  "username": "pvukovic",
  "ocena": 21
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/users", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


url = "https://jsonplaceholder.typicode.com/users"

payload = json.dumps({
  "ime": "stefan",
  "username": "peja",
  "ocena": "4"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
