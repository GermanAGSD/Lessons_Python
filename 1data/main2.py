import os
import requests
import pandas as pd
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://kaspi.kz/shop/api/v2"
TOKEN = "QpKvqTmmHSxMjW4EWWM/N2w3lwTtvw0v9hRz17O30pk="

HEADERS = {
    "Accept": "application/json",
    "X-Auth-Token": TOKEN,
}

START_DATE = datetime(2025, 12, 1, tzinfo=timezone.utc)
END_DATE = datetime.now(timezone.utc)

TIMEOUT = 15


def get_orders():
    orders = []
    page = 0
    page_size = 50

    while True:
        params = {
            "page[number]": page,
            "page[size]": page_size,
            "include": "entries"
        }

        r = requests.get(
            f"{BASE_URL}/orders",
            headers=HEADERS,
            params=params,
            timeout=TIMEOUT
        )
        r.raise_for_status()
        data = r.json()

        if not data.get("data"):
            break

        for order in data["data"]:
            created_at = datetime.fromisoformat(
                order["attributes"]["creationDate"].replace("Z", "+00:00")
            )
            if START_DATE <= created_at <= END_DATE:
                orders.append(order)

        page += 1

    return orders


def parse_orders(orders):
    orders_rows = []
    items_rows = []

    for order in orders:
        attr = order["attributes"]

        orders_rows.append({
            "order_id": order["id"],
            "status": attr.get("status"),
            "total_price": attr.get("totalPrice"),
            "creation_date": attr.get("creationDate"),
            "delivery_mode": attr.get("deliveryMode"),
        })

        for entry in attr.get("entries", []):
            items_rows.append({
                "order_id": order["id"],
                "product_code": entry.get("offer", {}).get("code"),
                "product_name": entry.get("offer", {}).get("name"),
                "price": entry.get("basePrice"),
                "quantity": entry.get("quantity"),
            })

    return orders_rows, items_rows


def get_products():
    products = []
    page = 0

    while True:
        params = {
            "page[number]": page,
            "page[size]": 50
        }

        r = requests.get(
            f"{BASE_URL}/products",
            headers=HEADERS,
            params=params,
            timeout=TIMEOUT
        )
        r.raise_for_status()
        data = r.json()

        if not data.get("data"):
            break

        for p in data["data"]:
            attr = p["attributes"]
            products.append({
                "product_code": attr.get("code"),
                "name": attr.get("name"),
                "brand": attr.get("brand"),
                "category": attr.get("category"),
                "price": attr.get("price"),
                "available": attr.get("available"),
            })

        page += 1

    return products


def export_to_excel(orders, items, products):
    with pd.ExcelWriter("kaspi_export.xlsx", engine="openpyxl") as writer:
        pd.DataFrame(orders).to_excel(writer, sheet_name="orders", index=False)
        pd.DataFrame(items).to_excel(writer, sheet_name="order_items", index=False)
        pd.DataFrame(products).to_excel(writer, sheet_name="products", index=False)


def main():
    print("📥 Загружаем заказы...")
    orders_raw = get_orders()

    print("🔎 Обрабатываем заказы...")
    orders, items = parse_orders(orders_raw)

    print("📦 Загружаем товары...")
    products = get_products()

    print("📊 Записываем в Excel...")
    export_to_excel(orders, items, products)

    print("✅ Готово: kaspi_export.xlsx")


if __name__ == "__main__":
    main()
