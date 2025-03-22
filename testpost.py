import requests

# result = requests.get('http://127.0.0.1:5000')
# print(result.text)

# result = requests.get('http://127.0.0.1:5000/testpost')
# print(result.text)

# result = requests.post('http://127.0.0.1:5000/testpost', json={'key':'value'})
# print(result.text)

url = "http://localhost:5000/payload"
payload = {'key1': 'value1', 'key2': 'value2'}
headers = {"Content-Type": "application/json"}

# Send the request
result = requests.post(url, json=payload, headers=headers)
print(result.text)