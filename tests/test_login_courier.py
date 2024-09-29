import allure
import helpers
from api import courier


class TestAuthorizationCourier:
    @allure.title('Проверка, что курьер может авторизоваться')
    def test_courier_can_login(self, create_courier, delete_courier):
        with allure.step('Создать курьера'):
            result = create_courier
        with allure.step('Авторизоваться курьером'):
            response = courier.CourierApi().login_courier(result["courier"][0], result["courier"][1])
        assert (response.status_code == 200 and
                isinstance(response.json()["id"], int)), 'Курьер не может авторизоваться'

    @allure.title('Проверка, что курьер не может авторизоваться без указания пароля')
    def test_courier_cannot_login_without_pwd(self, create_courier, delete_courier):
        with allure.step('Создать курьера'):
            result = create_courier
        with allure.step('Авторизоваться курьером без пароля'):
            response = courier.CourierApi().login_courier(result["courier"][0], None)
        assert (response.status_code == 400 and
                response.json()[
                    "message"] == "Недостаточно данных для входа"), 'Курьер не может авторизовываться без указания пароля'

    @allure.title('Проверка, что курьер не может авторизоваться без указания логина')
    def test_courier_cannot_login_without_login(self, create_courier, delete_courier):
        with allure.step('Создать курьера'):
            result = create_courier
        with allure.step('Авторизоваться курьером без логина'):
            response = courier.CourierApi().login_courier(None, result["courier"][1])
        assert (response.status_code == 400 and
                response.json()[
                    "message"] == "Недостаточно данных для входа"), 'Курьер не может авторизовываться без указания логина'

    @allure.title('Проверка, что курьер не может авторизоваться с неправильным логином')
    def test_courier_cannot_login_with_incorrect_login(self, create_courier, delete_courier):
        with allure.step('Создать курьера'):
            result = create_courier
        with allure.step('Авторизоваться курьером с неверным логином'):
            response = courier.CourierApi().login_courier(result["courier"][1], result["courier"][1])
        assert (response.status_code == 404 and
                response.json()[
                    "message"] == "Учетная запись не найдена"), 'Курьер не может авторизовываться с неправильным логином'

    @allure.title('Проверка, что курьер не может авторизоваться с неправильным паролем')
    def test_courier_cannot_login_with_incorrect_pwd(self, create_courier, delete_courier):
        with allure.step('Создать курьера'):
            result = create_courier
        with allure.step('Авторизоваться курьером с неверным паролем'):
            response = courier.CourierApi().login_courier(result["courier"][0], result["courier"][0])
        assert (response.status_code == 404 and
                response.json()[
                    "message"] == "Учетная запись не найдена"), 'Курьер не может авторизовываться с неправильным паролем'

    @allure.title('Проверка, что курьер не может авторизоваться с неправильным паролем')
    def test_courier_cannot_login_with_incorrect_pwd(self, create_courier, delete_courier):
        with allure.step('Создать курьера'):
            result = create_courier
        with allure.step('Авторизоваться курьером с неверным паролем'):
            response = courier.CourierApi().login_courier(result["courier"][0], result["courier"][0])
        assert (response.status_code == 404 and
                response.json()[
                    "message"] == "Учетная запись не найдена"), 'Курьер не может авторизовываться с неправильным паролем'

    @allure.title('Проверка, что несуществующий пользователь не может авторизоваться')
    def test_non_existent_user_cannot_login(self):
        with allure.step('Авторизоваться несуществующим пользователем'):
            response = courier.CourierApi().login_courier(helpers.Helpers().generate_random_string(10),
                                                           helpers.Helpers().generate_random_string(10))
        assert (response.status_code == 404 and
                response.json()[
                    "message"] == "Учетная запись не найдена"), 'Несуществующий пользователь не может авторизоваться'
