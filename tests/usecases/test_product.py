from typing import List
from uuid import uuid4
import pytest
from store.core.exceptions import NotFoundException
from store.schemas.product import ProductOut, ProductUpdateOut
from store.usecases.product import product_usecase


@pytest.fixture
async def created_product(mongo_client, product_in):
    # Cria o produto antes do início do teste
    created_product = await product_usecase.create(body=product_in)
    return created_product


async def test_usecases_should_return_sucess(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_should_return_sucess(product_id):
    result = await product_usecase.get(id=product_id)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_should_not_found():
    random_id = uuid4()  # Gera um UUID que provavelmente não existe no banco
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id=random_id)

    assert err.value.message == f"Product not found with filter: {random_id}"


async def test_usecases_query_should_return_success():
    result = await product_usecase.query()

    assert isinstance(result, List)


async def test_usecases_update_should_return_success(product_id, product_up):
    product_up.price = 7.500
    result = await product_usecase.update(id=product_id, body=product_up)

    assert isinstance(result, ProductUpdateOut)
