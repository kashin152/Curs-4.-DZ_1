import json

import pytest

from src.main import Category, Product, data_transactions


@pytest.fixture
def category():
    return Category(
        "Смартфоны",
        """Смартфоны, как средство не только коммуникации,
                                        но и получение дополнительных функций для удобства жизни""",
        [
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5,
            },
            {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
            {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
        ],
    )


def test_init_category(category):
    assert category.title == "Смартфоны"
    assert (
        category.description
        == """Смартфоны, как средство не только коммуникации,
                                        но и получение дополнительных функций для удобства жизни"""
    )
    assert category.products == [
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        },
        {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
        {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
    ]


@pytest.fixture
def product():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_init_product(product):
    assert product.title == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity_in_stock == 5


def test_category_count(category):
    assert Category.total_number_categories == 4
    assert Category.total_number_unique_products == 11


def test_data_transactions():
    test_file = "test_products.json"
    with open(test_file, "w", encoding="utf-8") as f:
        json.dump(
            [
                {
                    "name": "Смартфоны",
                    "description": """Смартфоны, как средство не только коммуникации,
                                        но и получение дополнительных функций для удобства жизни""",
                    "products": [
                        {
                            "name": "Samsung Galaxy C23 Ultra",
                            "description": "256GB, Серый цвет, 200MP камера",
                            "price": 180000.0,
                            "quantity": 5,
                        }
                    ],
                }
            ],
            f,
            ensure_ascii=False,
        )
    list_products = data_transactions(test_file)

    assert isinstance(list_products, list)
    assert len(list_products) > 0
    assert "name" in list_products[0]
    assert "description" in list_products[0]
    assert "products" in list_products[0]


@pytest.fixture
def categorys():
    products = [
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        },
        {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
        {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
    ]
    products = [
        Product(product["name"], product["description"], product["price"], product["quantity"]) for product in products
    ]
    return Category(
        "Смартфоны",
        """Смартфоны, как средство не только коммуникации,
                                        но и получение дополнительных функций для удобства жизни""",
        products,
    )


def test_print_products(categorys):
    expected_products = [
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.",
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.",
    ]
    actual_products = [
        f"{product.title}, {product.price} руб. Остаток: {product.quantity_in_stock} шт."
        for product in categorys._Category__products
    ]
    for product in expected_products:
        assert product in actual_products


def test_add_product():
    category = Category(
        "Смартфоны",
        """Смартфоны, как средство не только коммуникации,
                                        но и получение дополнительных функций для удобства жизни""",
        [],
    )
    product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    category.add_product(product)
    assert product in category._Category__products
    assert Category.total_number_unique_products == 15


def test_create_product():
    product = Product.create_product(
        "Samsung Galaxy C23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
    )
    assert isinstance(product, Product)
    assert product.title == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity_in_stock == 5


def test_price():
    product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.price == 180000.0
    product.price = -190000.0
    assert product.price == 180000.0


def test_price_del():
    product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    del product.price
    assert product.price is None
