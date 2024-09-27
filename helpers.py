import requests
import random
import string

import test_data


class Helpers:

    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def register_new_courier_and_return_login_password_response(self):
        login_pass = []

        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(test_data.COURIER_ENDPOINT, data=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        return {
            "courier": login_pass,
            "response": response}
        # "code": response.status_code,
        # "text": response.text}


# check how to generate
help = Helpers()
print(help.register_new_courier_and_return_login_password_response())
