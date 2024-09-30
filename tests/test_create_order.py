import allure
import pytest
import test_data
from api import orders


class TestCreateOrder:
    @pytest.mark.parametrize('test_color', [[], ["BLACK"], ["GREY"], ["BLACK", "GREY"]])
    @allure.title('Проверка, что можно сделать заказ самоката')
    def test_can_create_order(self, test_color):
        with allure.step(f'Сделать заказ самоката c цветом {test_color}'):
            data = test_data.TEST_ORDER
            data["color"] = test_color
            response = orders.OrdersApi().create_order(data)
        assert (response.status_code == 201 and
                isinstance(response.json()["track"], int)), f'Невозможно создать заказ с цветом {test_color}!'

