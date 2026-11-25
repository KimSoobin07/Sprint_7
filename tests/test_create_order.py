import pytest
import requests
import allure
from data import Urls, OrderData


class TestCreateOrder:

    @allure.title("Создание заказа с разными вариантами цвета самоката")
    @pytest.mark.parametrize("color", OrderData.COLOR_OPTIONS)
    def test_create_order_different_colors_success(self, color, order_track_cleaner):
        payload = OrderData.DEFAULT_ORDER.copy()
        if color:
            payload["color"] = color

        response = requests.post(Urls.ORDERS, json=payload)

        assert response.status_code == 201
        response_body = response.json()
        assert "track" in response_body
        assert isinstance(response_body["track"], int)

        order_track_cleaner.append(response_body["track"])
