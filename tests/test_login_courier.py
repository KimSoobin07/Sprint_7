import pytest
import requests
import allure
from data import Urls, ResponseMessages
from helpers import generate_random_string


class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_courier_success(self, created_courier):
        login, password, _ = created_courier
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(Urls.LOGIN_COURIER, json=payload)

        assert response.status_code == 200
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)

    @allure.title("Ошибка авторизации при отсутствии обязательного поля")
    @pytest.mark.parametrize("empty_field", ["login", "password"])
    def test_login_courier_missing_field_error(self, created_courier, empty_field):
        login, password, _ = created_courier
        payload = {
            "login": login,
            "password": password
        }
        payload[empty_field] = ""

        response = requests.post(Urls.LOGIN_COURIER, json=payload)

        assert response.status_code == 400
        assert ResponseMessages.COURIER_NOT_ENOUGH_DATA_LOGIN in response.json().get("message", "")

    @allure.title("Ошибка авторизации при неверном пароле")
    def test_login_courier_wrong_password_error(self, created_courier):
        login, _, _ = created_courier
        payload = {
            "login": login,
            "password": generate_random_string(12)
        }
        response = requests.post(Urls.LOGIN_COURIER, json=payload)

        assert response.status_code == 404
        assert ResponseMessages.COURIER_NOT_FOUND in response.json().get("message", "")

    @allure.title("Ошибка авторизации под несуществующим пользователем")
    def test_login_nonexistent_courier_error(self):
        payload = {
            "login": generate_random_string(12),
            "password": generate_random_string(12)
        }
        response = requests.post(Urls.LOGIN_COURIER, json=payload)

        assert response.status_code == 404
        assert ResponseMessages.COURIER_NOT_FOUND in response.json().get("message", "")
