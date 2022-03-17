import http.client
import json

conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
payload = json.dumps({
  "userId": "5",
  "id": "5",
  "title": "Naslov",
  "body": "Tekst"
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/posts", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

