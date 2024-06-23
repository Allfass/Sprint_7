import allure
import pytest
import requests
from test_requests.courier import Courier
from data import TestData


class TestLoginCourier:
    @allure.title("Проверка возможности авторизации курьера")
    @allure.description(
        "При отправке корректного запроса авторизации курьера возвращается код 200"
    )
    def test_login_courier_return_200(self):
        test_courier = Courier()
        test_courier.register_new_courier()
        payload = {
            "login": test_courier.credentials[0],
            "password": test_courier.credentials[1],
        }
        response = requests.post(TestData.COURIER_LOGIN_URL, data=payload, timeout=10)
        assert response.status_code == 200

    @allure.title("Проверка возвращаемого значения при корректной авторизации курьера")
    @allure.description(
        "При отправке корректного запроса авторизации курьера возвращается идентификатор"
    )
    def test_login_courier_return_id(self):
        test_courier = Courier()
        test_courier.register_new_courier()
        payload = {
            "login": test_courier.credentials[0],
            "password": test_courier.credentials[1],
        }
        response = requests.post(TestData.COURIER_LOGIN_URL, data=payload, timeout=10)
        assert response.json()["id"]

    @allure.title(
        "Проверка отсутствия обязательного поля login при авторизации курьера"
    )
    @allure.description("Отправляем запрос без поля login")
    def test_login_courier_without_nessesary_login_field_return_400(self):
        test_courier = Courier()
        test_courier.register_new_courier()
        payload = {"password": test_courier.credentials[1]}
        response = requests.post(TestData.COURIER_LOGIN_URL, data=payload, timeout=10)
        assert response.status_code == 400

    @pytest.mark.skip(reason="long timeout for service")
    @allure.title(
        "Проверка отсутствия обязательного поля password при авторизации курьера"
    )
    @allure.description("Отправляем запрос без поля password")
    def test_login_courier_without_nessesary_password_field_return_400(self):
        test_courier = Courier()
        test_courier.register_new_courier()
        payload = {"login": test_courier.credentials[0]}
        response = requests.post(TestData.COURIER_LOGIN_URL, data=payload, timeout=10)
        assert response.status_code == 400

    @allure.title(
        "Проверка авторизации с незарегистрированной парой логин-пароль"
    )
    @allure.description("Отправляем запрос с незарегистрированной парой логин-пароль вернёт ошибку 404")
    def test_login_courier_with_unexist_credentials_return_404(self):
        login = Courier.generate_random_string(10)
        password = Courier.generate_random_string(10)
        first_name = Courier.generate_random_string(10)
        payload = {"login": login, "password": password, "firstName": first_name}
        response = requests.post(TestData.COURIER_LOGIN_URL, data=payload, timeout=10)
        assert response.status_code == 404
