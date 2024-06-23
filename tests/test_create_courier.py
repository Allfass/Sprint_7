import allure
import requests
from test_requests.courier import Courier
from data import TestData

class TestCourier():
    @allure.title('Проверка возможности создания курьера')
    @allure.description('При отправке корректного запроса создания курьера возвращается код 201')
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

    @allure.title('Проверка возвращаемого значения при корректном создании курьера')
    @allure.description('При отправке корректного запроса создания курьера возвращается ok со значением true')
    def test_creating_courier_return_true(self):
        login = Courier.generate_random_string(10)
        password = Courier.generate_random_string(10)
        first_name = Courier.generate_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(TestData.courier_create_url, data=payload)
        assert response.json()["ok"]

    @allure.title('Проверка невозможности создания одинаковых курьеров')
    @allure.description('Отправляем дважды одинаковый запрос')
    def test_creating_courier_twice_return_409(self):
        login = Courier.generate_random_string(10)
        password = Courier.generate_random_string(10)
        first_name = Courier.generate_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        requests.post(TestData.courier_create_url, data=payload)
        final_response = requests.post(TestData.courier_create_url, data=payload)
        assert final_response.status_code == 409

    @allure.title('Проверка отсутствия обязательного поля login при создании курьера')
    @allure.description('Отправляем запрос без поля login')
    def test_creating_courier_without_nessesary_login_field_return_400(self):
        password = Courier.generate_random_string(10)
        first_name = Courier.generate_random_string(10)
        payload = {
            "password": password,
            "firstName": first_name
        }
        response = requests.post(TestData.courier_create_url, data=payload)
        assert response.status_code == 400

    @allure.title('Проверка отсутствия обязательного поля password при создании курьера')
    @allure.description('Отправляем запрос без поля password')
    def test_creating_courier_without_nessesary_password_field_return_400(self):
        login = Courier.generate_random_string(10)
        first_name = Courier.generate_random_string(10)
        payload = {
            "login": login,
            "firstName": first_name
        }
        response = requests.post(TestData.courier_create_url, data=payload)
        assert response.status_code == 400
