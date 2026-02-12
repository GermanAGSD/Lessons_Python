import requests
import pandas as pd
from datetime import datetime

# 1. Конфигурация
API_TOKEN = 'QpKvqTmmHSxMjW4EWWM/N2w3lwTtvw0v9hRz17O30pk='
HEADERS = {
    'X-Auth-Token': API_TOKEN,
    'Accept': 'application/json'
}
BASE_URL = 'https://kaspi.kz/shop/api'

# Период выгрузки (с 1 декабря 2025 по сегодня)
END_DATE = datetime.now().strftime('%Y-%m-%d')
START_DATE = '2025-12-01'

def fetch_orders():
    """Получение списка заказов за указанный период"""
    print("Получение списка заказов...")
    url = f'{BASE_URL}/orders'
    params = {'startDate': START_DATE, 'endDate': END_DATE}
    all_orders = []

    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        data = response.json()
        all_orders = data.get('data', [])
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении заказов: {e}")

    return all_orders

def fetch_products():
    """Получение списка товаров"""
    print("Получение списка товаров...")
    # ВАЖНО: уточните точный эндпоинт в вашем кабинете Kaspi
    url = f'{BASE_URL}/products'
    all_products = []

    try:
        # Возможно, потребуется реализовать постраничную загрузку
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        all_products = data.get('data', [])
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении товаров: {e}")

    return all_products

def process_orders_data(orders):
    """Обработка и структурирование данных заказов"""
    processed = []
    for order in orders:
        # Адаптируйте извлечение полей под реальную структуру ответа API
        order_info = {
            'order_id': order.get('id', ''),
            'code': order.get('attributes', {}).get('code', ''),
            'creation_date': order.get('attributes', {}).get('creationDate', ''),
            'total_price': order.get('attributes', {}).get('totalPrice', ''),
            'status': order.get('attributes', {}).get('status', ''),
            'customer_name': order.get('attributes', {}).get('customer', {}).get('name', ''),
        }
        processed.append(order_info)
    return processed

def process_products_data(products):
    """Обработка и структурирование данных товаров"""
    processed = []
    for product in products:
        # Адаптируйте извлечение полей под реальную структуру ответа API
        product_info = {
            'sku': product.get('attributes', {}).get('sku', ''),
            'title': product.get('attributes', {}).get('title', ''),
            'brand': product.get('attributes', {}).get('brand', ''),
            'category': product.get('attributes', {}).get('category', ''),
        }
        processed.append(product_info)
    return processed

def export_to_excel(orders_data, products_data):
    """Экспорт данных в файл Excel с разными листами"""
    filename = f'kaspi_export_{END_DATE}.xlsx'

    # Создаем DataFrame
    orders_df = pd.DataFrame(orders_data)
    products_df = pd.DataFrame(products_data)

    # Записываем в Excel
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        if not orders_df.empty:
            orders_df.to_excel(writer, sheet_name='Заказы', index=False)
        if not products_df.empty:
            products_df.to_excel(writer, sheet_name='Товары', index=False)

    print(f"Данные успешно экспортированы в файл: {filename}")
    return filename

def main():
    """Основная функция"""
    print(f"Выгрузка данных за период с {START_DATE} по {END_DATE}")

    # Получение данных
    orders_raw = fetch_orders()
    products_raw = fetch_products()

    # Обработка данных
    orders_processed = process_orders_data(orders_raw)
    products_processed = process_products_data(products_raw)

    # Экспорт в Excel
    if orders_processed or products_processed:
        export_to_excel(orders_processed, products_processed)
    else:
        print("Нет данных для экспорта.")

if __name__ == "__main__":
    main()