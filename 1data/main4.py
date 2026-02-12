import requests

url = "https://kaspi.kz/shop/api/products/import/result"

params = {
    "i": "testproduct",   # код загрузки
}

headers = {
    "Accept": "application/json",
    "X-Auth-Token": "QpKvqTmmHSxMjW4EWWM/N2w3lwTtvw0v9hRz17O30pk=",
}

response = requests.get(
    url,
    headers=headers,
    params=params,
    timeout=30
)

print(response.status_code)
print(response.json())
