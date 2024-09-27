# сюда добавить API для работы с курьерами
import requests

from helpers import Helpers
import test_data


class CouriersApi:

    def create_courier(self, login, password, first_name):
        data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(test_data.COURIER_ENDPOINT, json=data)
        return response

    def login_courier(self, login, password):
        data = {
            "login": login,
            "password": password
        }
        response = requests.post(test_data.COURIER_ENDPOINT + '/login', json=data)
        return response

    def get_courier_id(self, login, password):
        id = self.login_courier(login, password).json()["id"]
        return id

    def delete_courier(self, id):
        response = requests.delete(test_data.COURIER_ENDPOINT + f'/{id}')
        return response


#print(CouriersApi().create_courier('fgfgfg', 'qazxswea', 'wqasasaas').status_code)

courier = CouriersApi()
response = courier.create_courier('sadasdagh', 'dfgdfg', 'dsdsad')
print(response.text)
response = courier.login_courier('sadasdagh', 'dfgdfg')
print(response.text)
id = courier.get_courier_id('sadasdagh', 'dfgdfg')
response = courier.delete_courier(id)
print(response.text)

