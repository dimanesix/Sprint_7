import requests
import test_data


class OrdersApi:

    def create_order(self, data):
        response = requests.post(test_data.ORDER_ENDPOINT, json=data)
        return response

    def get_orders(self):
        response = requests.get(test_data.ORDER_ENDPOINT)
        return response
