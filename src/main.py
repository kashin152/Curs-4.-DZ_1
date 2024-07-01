import json
import os


class Category:
    total_number_categories = 0
    total_number_unique_products = 0

    title: str
    description: str
    products: list

    def __init__(self, title, description, products):
        self.title = title
        self.description = description
        self.products = products

        Category.total_number_categories += 1
        Category.total_number_unique_products += len(set(products))


class Product:
    title: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, title, description, price, quantity_in_stock):
        self.title = title
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock


def data_transactions(file):
    with open(file, encoding="utf-8") as date_json:
        list_data_transactions = json.load(date_json)
        return list_data_transactions


list_products = data_transactions(os.path.join(os.path.dirname(__file__), "products.json"))

for categories in list_products:
    category = Category(
        categories["name"], categories["description"], [category["name"] for category in categories["products"]]
    )
    print(f"Название категории: {category.title}")
    print(f"Описание категории: {category.description}")
    print(f"Список товаров: {category.products}")

    for product in categories["products"]:
        product = Product(product["name"], product["description"], product["price"], product["quantity"])
        print(f"Название продукта: {product.title}")
        print(f" Описание: {product.description}")
        print(f" Цена: {product.price}")
        print(f" Количество в наличии: {product.quantity_in_stock}")

print(f"Общее количество категорий: {Category.total_number_categories}")
print(f"Общее количество уникальных продуктов: {Category.total_number_unique_products}")
