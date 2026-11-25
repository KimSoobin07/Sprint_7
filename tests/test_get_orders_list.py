import requests
import allure
from data import Urls


class TestGetOrdersList:

    @allure.title("Получение списка заказов")
    def test_get_orders_list_success(self):
        response = requests.get(Urls.ORDERS)

        assert response.status_code == 200
        response_body = response.json()
        assert "orders" in response_body
        assert isinstance(response_body["orders"], list)
        assert len(response_body["orders"]) > 0
