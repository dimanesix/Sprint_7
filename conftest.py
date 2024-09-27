# 1 фикстуа - создание курьера, и однвременно подчищаем -> удаление курьера
# 2 фикстура - создание заказа и одновременно подчищаем -> удаление заказа
import allure
import pytest

import helpers
import test_data
from api import courier
from helpers import Helpers


# @pytest.fixture
# def create_courier():
#     login = Helpers().generate_random_string(10)
#     password = Helpers().generate_random_string(10)
#     first_name = Helpers().generate_random_string(10)
#
#     data = {
#         "login": login,
#         "password": password,
#         "firstName": first_name
#     }
#
#     #response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

@allure.step('Создать курьера')
@pytest.fixture
def create_courier():
    result = helpers.Helpers().register_new_courier_and_return_login_password_response()
    return result


@allure.step('Удалить курьера')
@pytest.fixture
def delete_courier(create_courier):
    yield
    #   [0] - login, [1] - password
    id = courier.CouriersApi().get_courier_id(create_courier["courier"][0], create_courier["courier"][1])
    response = courier.CouriersApi().delete_courier(id)
    print(response.status_code, response.text)


@pytest.fixture
def create_login():
    login = helpers.Helpers().generate_random_string(10)
    yield login
    id = courier.CouriersApi().get_courier_id(login, test_data.TEST_PASSWORD)
    courier.CouriersApi().delete_courier(id)
