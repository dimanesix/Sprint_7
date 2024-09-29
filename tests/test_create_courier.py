import allure
import test_data
from api import courier


class TestCreateCourier:
    @allure.title('Проверка, что курьера можно создать')
    def test_can_create_courier(self, create_courier, delete_courier):
        with allure.step('Создать курьера'):
            result = create_courier
        assert (result['response'].status_code == 201 and
                result["response"].text == '{"ok":true}'), 'Невозможно создать курьера!'

    @allure.title('Проверка, что нельзя создать двух одинаковых курьеров')
    def test_cannot_create_identical_couriers(self, create_courier, delete_courier):
        with allure.step('Создать курьера'):
            result = create_courier
        with allure.step('Создать нового курьера с точно такими же данными'):
            response = courier.CourierApi().create_courier(result["courier"][0], result["courier"][1], result["courier"][2])
        assert (response.status_code == 409 and
                response.json()["message"] == 'Этот логин уже используется. Попробуйте другой.'), 'Можно создать идентичных курьеров!'

    @allure.title('Проверка, что можно создать курьера без необязательнго поля')
    def test_can_create_courier_without_first_name(self, create_login):
        login = create_login
        with allure.step('Создать курьера без необязательного поля first_name'):
            response = courier.CourierApi().create_courier(login, test_data.TEST_PASSWORD, None)
        assert (response.status_code == 201 and
                response.text == '{"ok":true}'), 'Невозможно создать курьера!'

    @allure.title('Проверка, что нельзя создать курьера без логина')
    def test_cannot_create_courier_without_login(self):
        with allure.step('Создать курьера без логина'):
            response = courier.CourierApi().create_courier(None, test_data.TEST_PASSWORD, test_data.TEST_FIRST_NAME)
        assert (response.status_code == 400 and
                response.json()["message"] == 'Недостаточно данных для создания учетной записи')

    @allure.title('Проверка, что нельзя создать курьера без пароля')
    def test_cannot_create_courier_without_password(self):
        with allure.step('Создать курьера без пароля'):
            response = courier.CourierApi().create_courier(test_data.TEST_LOGIN, None, test_data.TEST_FIRST_NAME)
        assert (response.status_code == 400 and
                response.json()["message"] == 'Недостаточно данных для создания учетной записи')

    @allure.title('Проверка, что нельзя создать двух курьеров с одинаковым логином')
    def test_cannot_create_courier_with_identical_login(self, create_courier, delete_courier):
        with allure.step('Создать курьера'):
            result = create_courier
        with allure.step('Создать курьера с таким же логином'):
            response = courier.CourierApi().create_courier(result["courier"][0], test_data.TEST_PASSWORD, test_data.TEST_FIRST_NAME)
        assert (response.status_code == 409 and
                response.json()["message"] == 'Этот логин уже используется. Попробуйте другой.'), 'Можно создать курьеров с идентичным логином!'