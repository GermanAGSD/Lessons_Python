# Словари
import json

dictionary = {
    "house": "house",
    "car": "mashina",
    "tree": "derevo",
    "road": "doroga",
    "river": "reka"
}

js = json.dumps(dictionary)
print(js)
print(dictionary["car"])
print(len(dictionary))
del dictionary["car"]
print(dictionary)
