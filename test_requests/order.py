import allure
import random
from faker import Faker
import requests
from data import TestData
import datetime


class Order:
    """Class collect methods to test order functional\
       on yandex scooter service
    """

    def __init__(self) -> None:
        self.test_data = TestData()
        self.track = 0
        self.order_list = {}

    @allure.step("Создаём заказ")
    def create_order(self):
        """Uses the generated data to create a order

        Returns to self.track:
            int: track
        """
        fake = Faker("ru_RU")
        first_name = fake.first_name()
        last_name = fake.last_name()
        address = fake.address()
        metro_station =  random.randint(1, 10)
        phone = fake.phone_number()
        rent_time = random.randint(1, 10)
        delivery_date = (datetime.date.today()+datetime.timedelta(3)).strftime('%Y-%m-%d')
        comment = fake.first_name()
        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment
            }
        response = requests.post(
            self.test_data.ORDER_URL, data=payload, timeout=10
        )
        if response.status_code == 201:
            self.track = response.json()["track"]

    def get_order_list(self, courier_id):
        url = f'{self.test_data.ORDER_URL}?courierId={courier_id}'
        response = requests.get(url, timeout=60)
        self.order_list = response.json()
        return response.status_code
