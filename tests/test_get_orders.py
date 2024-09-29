import allure
import test_data
from api import orders


class TestGetOrder:

    @allure.title('Проверка, что можно получить список заказов')
    def test_can_get_orders(self):
        with allure.step(f'Сделать заказ самоката'):
            orders.OrdersApi().create_order(test_data.TEST_ORDER)
        with allure.step(f'Получить список заказов'):
            response = orders.OrdersApi().get_orders()
        assert (response.status_code == 200 and
                isinstance(response.json()["orders"], list)), f'Невозможно получить список заказов!'
