import requests
import pandas as pd
from datetime import datetime, timezone

# ---------------- НАСТРОЙКИ ----------------

TOKEN = "QpKvqTmmHSxMjW4EWWM/N2w3lwTtvw0v9hRz17O30pk="
BASE_URL = "https://kaspi.kz/shop/api/v2/orders"

HEADERS = {
    "Content-Type": "application/vnd.api+json",
    "X-Auth-Token": TOKEN
}

PAGE_SIZE = 100

# ---------------- ДАТЫ ----------------

def to_ms(dt: datetime) -> int:
    return int(dt.timestamp() * 1000)

date_from = to_ms(datetime(2025, 12, 1, tzinfo=timezone.utc))
date_to = to_ms(datetime.now(tz=timezone.utc))

# ---------------- ЗАПРОС ЗАКАЗОВ ----------------

def get_orders():
    page = 0
    all_orders = []

    while True:
        params = {
            "page[number]": page,
            "page[size]": PAGE_SIZE,

            "filter[orders][creationDate][$ge]": date_from,
            "filter[orders][creationDate][$le]": date_to,

            # можно менять фильтры
            # "filter[orders][state]": "DELIVERY",
            # "filter[orders][status]": "COMPLETED",

            "include[orders]": "user"
        }

        response = requests.get(BASE_URL, headers=HEADERS, params=params)
        response.raise_for_status()

        data = response.json().get("data", [])
        if not data:
            break

        print(f"📦 Страница {page}, заказов: {len(data)}")
        all_orders.extend(data)
        page += 1

    return all_orders

# ---------------- ОБРАБОТКА ----------------

orders = get_orders()

rows = []

for order in orders:
    attr = order.get("attributes", {})
    user = attr.get("customer", {})

    rows.append({
        "order_code": attr.get("code"),
        "status": attr.get("status"),
        "state": attr.get("state"),
        "total_price": attr.get("totalPrice"),
        "delivery_type": attr.get("deliveryMode"),
        "payment_mode": attr.get("paymentMode"),
        "creation_date": attr.get("creationDate"),
        "customer": attr.get("customer"),
        "delivery_cost": attr.get("deliveryCost"),
        "is_kaspi_delivery": attr.get("isKaspiDelivery"),
    })

# ---------------- EXCEL ----------------

df = pd.DataFrame(rows)
df.to_excel("kaspi_orders.xlsx", index=False)

print("✅ Готово: kaspi_orders.xlsx")
