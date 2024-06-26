import allure
import requests
from test_requests.courier import Courier
from data import TestData

class TestCourier():
    @allure.title('Проверка возможности создания курьера')
    @allure.description('При отправке корректного запроса создания курьера возвращается код 201')
    def test_creating_courier_return_201_and_ok(self):
        login = Courier.generate_random_string(10)
        password = Courier.generate_random_string(10)
        first_name = Courier.generate_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(TestData.COURIER_CREATE_URL, data=payload, timeout=10)
        assert response.status_code == 201 and \
               response.json()["ok"] == True

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
        requests.post(TestData.COURIER_CREATE_URL, data=payload, timeout=10)
        final_response = requests.post(TestData.COURIER_CREATE_URL, data=payload, timeout=10)
        assert final_response.status_code == 409 and \
               final_response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Проверка отсутствия обязательного поля login при создании курьера')
    @allure.description('Отправляем запрос без поля login')
    def test_creating_courier_without_nessesary_login_field_return_400(self):
        password = Courier.generate_random_string(10)
        first_name = Courier.generate_random_string(10)
        payload = {
            "password": password,
            "firstName": first_name
        }
        response = requests.post(TestData.COURIER_CREATE_URL, data=payload, timeout=10)
        assert response.status_code == 400 and \
               response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверка отсутствия обязательного поля password при создании курьера')
    @allure.description('Отправляем запрос без поля password')
    def test_creating_courier_without_nessesary_password_field_return_400(self):
        login = Courier.generate_random_string(10)
        first_name = Courier.generate_random_string(10)
        payload = {
            "login": login,
            "firstName": first_name
        }
        response = requests.post(TestData.COURIER_CREATE_URL, data=payload, timeout=10)
        assert response.status_code == 400 and \
               response.json()["message"] == "Недостаточно данных для создания учетной записи"
