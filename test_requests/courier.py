import random
import string
import allure
import requests
from data import TestData


class Courier:
    """Class collect methods to test couriers functional\
       on yandex scooter service
    """

    def __init__(self) -> None:
        self.credentials = []
        self.test_data = TestData()
        self.id = 0

    @allure.step("Создаём нового курьера и возвращаем учётные данные")
    def register_new_courier(self):
        """Uses the generated data to create a new courier

        Returns to self.credentials:
            list: login:str,
                  password:str,
                  firstName:str
        """
        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)

        payload = {"login": login, "password": password, "firstName": first_name}

        response = requests.post(
            self.test_data.COURIER_CREATE_URL, data=payload, timeout=10
        )

        if response.status_code == 201:
            self.credentials.append(login)
            self.credentials.append(password)
            self.credentials.append(first_name)

    @allure.step("Авторизуемся в сервисе")
    def login_courier(self):
        payload = {"login": self.credentials[0], "password": self.credentials[1]}
        response = requests.post(
            self.test_data.COURIER_LOGIN_URL, data=payload, timeout=10
        )
        self.id = response.json()["id"]

    @staticmethod
    def generate_random_string(length):
        """Generates a random string of length size

        Args:
            length (int): size of string

        Returns:
            str: generated string
        """
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string
