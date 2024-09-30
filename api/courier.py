import requests
import test_data


class CourierApi:

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

