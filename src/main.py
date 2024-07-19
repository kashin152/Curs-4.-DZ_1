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
        self.__products = products

        Category.total_number_categories += 1
        Category.total_number_unique_products += len(products)

    def __len__(self):
        return len(self.__products)

    def __str__(self):
        return f"Категория: {self.title}, количество продуктов {len(self)}"

    @property
    def products(self):
        return self.__products

    def add_product(self, product):
        if product not in self.__products:
            self.__products.append(product)
            Category.total_number_unique_products += 1
        else:
            print(f"Товар '{product['name']}' уже существует в категории '{self.title}'.")


class Product:
    title: str
    description: str
    price: float
    quantity_in_stock: int
    list_of_products: []

    def __init__(self, title, description, price, quantity_in_stock):
        self.title = title
        self.description = description
        self.__price = price
        self.quantity_in_stock = quantity_in_stock

    def __str__(self):
        return f"{self.title}, {self.price} руб. Остаток: {self.quantity_in_stock} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return (self.price * self.quantity_in_stock) + (other.price * other.quantity_in_stock)
        else:
            raise TypeError("Объект должен быть экземпляром класса Product")

    @classmethod
    def create_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print("Некорректная цена. Цена должна быть больше нуля.")

    @price.deleter
    def price(self):
        self.__price = None


def data_transactions(file):
    with open(file, encoding="utf-8") as date_json:
        list_data_transactions = json.load(date_json)
        return list_data_transactions


list_products = data_transactions(os.path.join(os.path.dirname(__file__), "products.json"))


category_list = []
for categories in list_products:
    products = [
        Product(product["name"], product["description"], product["price"], product["quantity"])
        for product in categories["products"]
    ]
    category = Category(categories["name"], categories["description"], products)
    category_list.append(category)


new_product = {
    "name": "Телевизоры",
    "description": """Телевизор обладает множеством преимуществ, которые делают его
             идеальным выбором для любого пользователя.""",
    "products": [
        {"name": "Smart TV Q90-35", "description": "Оснащен технологией Smart TV", "price": 14997.0, "quantity": 10}
    ],
}

for category in category_list:
    if category.title == new_product["name"]:
        for product in new_product["products"]:
            new_product_obj = Product.create_product(
                product["name"], product["description"], product["price"], product["quantity"]
            )
            category.add_product(new_product_obj)


for category in category_list:
    print(str(category))
    for product in category.products:
        print(product)

product_a = Product("Product A", "Описание A", 100, 10)
product_b = Product("Product B", "Описание B", 200, 2)
print(f"Сумма: {product_a + product_b} руб.")

# product = Product("Test", "Description", 10.0, 5)
# print(product.price)
#
# product.price = -5.0
# print(product.price)
#
# product.price = 20.0
# print(product.price)
