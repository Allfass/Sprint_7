import allure
import pytest
import requests
from data import TestData
from test_requests.order import Order
from test_requests.courier import Courier


class TestCreateOrder:

    @allure.title("Проверка возможности создания заказа")
    @allure.description(
        "При отправке корректного запроса создания заказа возвращается код 201"
    )
    @pytest.mark.parametrize("testing_dict", TestData.TEST_DATA)
    def test_choose_color_while_creating_order_return_201(self, testing_dict):
        payload = {
            "firstName": testing_dict["firstName"],
            "lastName": testing_dict["lastName"],
            "address": testing_dict["address"],
            "metroStation": testing_dict["metroStation"],
            "phone": testing_dict["phone"],
            "rentTime": testing_dict["rentTime"],
            "deliveryDate": testing_dict["deliveryDate"],
            "comment": testing_dict["comment"]
            }
        response = requests.post(
            TestData.ORDER_URL, data=payload, timeout=10
        )
        assert response.status_code == 201 and \
               response.json()["track"]

    @allure.title("Проверка возврата track после создания заказа")
    @allure.description(
        "При отправке корректного запроса создания заказа возвращается track"
    )
    def test_creating_order_return_track(self):
        order = Order()
        order.create_order()
        assert order.track != 0

    @allure.title("Проверка наличия заказа в списке заказов")
    @allure.description(
        "При поиске заказа по track возвращается 200, после регистрации курьера, авторизации и создания заказа"
    )
    def test_get_order_after_making_order_return_order_list(self):
        test_courier = Courier()
        test_courier.register_new_courier()
        test_courier.login_courier()
        order = Order()
        order.create_order()
        order.get_order_list(test_courier.id)
        assert order.order_list.status_code == 200 and\
               order.order_list.json()["orders"] == []
