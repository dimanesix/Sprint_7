import pytest
import helpers
import test_data
from api import courier


@pytest.fixture
def create_courier():
    result = helpers.Helpers().register_new_courier_and_return_login_password_response()
    return result


@pytest.fixture
def delete_courier(create_courier):
    yield
    #   [0] - login, [1] - password
    id = courier.CourierApi().get_courier_id(create_courier["courier"][0], create_courier["courier"][1])
    courier.CourierApi().delete_courier(id)


@pytest.fixture
def create_login():
    login = helpers.Helpers().generate_random_string(10)
    yield login
    id = courier.CourierApi().get_courier_id(login, test_data.TEST_PASSWORD)
    courier.CourierApi().delete_courier(id)
