### mencoba belajar dictionary dari json file ###
import json

users = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    }
  }
print(users)
print(users["email"])
print(users["address"])
print(users["address"]["geo"])

print(users)
print(type(users))
print('\nUbah dct ke json')
import json
result = json.dumps(users)
print(type(result))
print(result)

with open('result json', 'w') as file:
    json.dump(users, file)
