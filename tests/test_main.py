import json

import pytest

from src.main import Category, Product, data_transactions


@pytest.fixture
def category():
    return Category(
        "Смартфоны",
        """Смартфоны, как средство не только коммуникации,
                                        но и получение дополнительных функций для удобства жизни""",
        ["Samsung Galaxy C23 Ultra", "Iphone 15", "Xiaomi Redmi Note 11"],
    )


def test_init_category(category):
    assert category.title == "Смартфоны"
    assert (category.description == """Смартфоны, как средство не только коммуникации,
                                        но и получение дополнительных функций для удобства жизни""")
    assert category.products == ["Samsung Galaxy C23 Ultra", "Iphone 15", "Xiaomi Redmi Note 11"]


@pytest.fixture
def product():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_init_product(product):
    assert product.title == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity_in_stock == 5


def test_category_count(category):
    assert Category.total_number_categories == 3
    assert len(Category.total_number_unique_products) == 4


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
