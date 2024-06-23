import allure
import requests
from test_requests.courier import Courier
from data import TestData

class TestCourier():
    @allure.title('Проверка возможности создания курьера')
    @allure.description('Формируются post запрос со случайными строками в 10 символов')
    def test_creating_courier_return_201(self):
        login = Courier.generate_random_string(10)
        password = Courier.generate_random_string(10)
        first_name = Courier.generate_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(TestData.courier_create_url, data=payload)
        assert response.status_code == 201
