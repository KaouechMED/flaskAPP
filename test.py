import requests

url="http://127.0.0.1:5000/api/register"

data={
    "username":"emna",
    "email_address":"emna@gmail.com",
    "cin":"15856456",
    "password":"azerty123",
    "password_confirm":"azerty123"
}

response = requests.post(url, json=data)

print(response)