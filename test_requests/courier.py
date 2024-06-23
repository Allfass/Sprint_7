import random
import string
import allure
import requests
from data import TestData


class Courier():
    """Test collect methods to test couriers functional 
       on yandex scooter service
    """
    def __init__(self) -> None:
        self.credentials = []
        self.test_data = TestData()

    @allure.step('Создаём нового курьера и возвращаем учётные данные')
    def register_new_courier_and_return_login_password(self):
        """Uses the generated data to create a new courier

        Returns:
            list: login:str,
                  password:str,
                  firstName:str
        """
        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(self.test_data.courier_create_url, data=payload)

        if response.status_code == 201:
            self.credentials.append(login)
            self.credentials.append(password)
            self.credentials.append(first_name)

        return self.credentials

    @staticmethod
    def generate_random_string(length):
        """Generates a random string of length size

        Args:
            length (int): size of string

        Returns:
            str: generated string
        """
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    