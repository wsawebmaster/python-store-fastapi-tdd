from store.schemas.product import ProductIn


def test_schemas_validated():
    product = ProductIn(name="Iphone 14 pro Max", quantity=10, price=8.500, status=True)

    assert product.name == "Iphone 14 pro Max"
