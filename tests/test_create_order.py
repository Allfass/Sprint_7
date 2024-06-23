import allure
import pytest
import requests
from data import TestData
from test_requests.order import Order


class TestCreateOrder:

    test_data = [
        {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                "BLACK"
            ]
        },
        {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                "GREY"
            ]
        },
        {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                "BLACK",
                "GREY"
            ]
        },
        {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": []
        }
    ]

    @allure.title("Проверка возможности создания заказа")
    @allure.description(
        "При отправке корректного запроса создания заказа возвращается код 201"
    )
    @pytest.mark.parametrize("testing_dict", test_data)
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
        assert response.status_code == 201

    def test_creating_order_return_track(self):
        order = Order()
        order.create_order()
        assert order.track != 0
