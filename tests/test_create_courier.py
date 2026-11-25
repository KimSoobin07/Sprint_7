import pytest
import requests
import allure
from data import Urls, ResponseMessages
from helpers import generate_courier_payload


class TestCreateCourier:

    @allure.title("Успешное создание нового курьера")
    def test_create_courier_success(self, courier_payload):
        response = requests.post(Urls.CREATE_COURIER, json=courier_payload)

        assert response.status_code == 201
        assert response.json() == ResponseMessages.COURIER_CREATED

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier_error(self, courier_payload):
        first_response = requests.post(Urls.CREATE_COURIER, json=courier_payload)
        assert first_response.status_code == 201

        second_response = requests.post(Urls.CREATE_COURIER, json=courier_payload)

        assert second_response.status_code == 409
        assert ResponseMessages.COURIER_ALREADY_EXISTS in second_response.json().get("message", "")

    @allure.title("Ошибка при создании курьера с уже существующим логином")
    def test_create_courier_existing_login_error(self, created_courier):
        existing_login, _, _ = created_courier
        payload = generate_courier_payload()
        payload["login"] = existing_login

        response = requests.post(Urls.CREATE_COURIER, json=payload)

        assert response.status_code == 409
        assert ResponseMessages.COURIER_ALREADY_EXISTS in response.json().get("message", "")

    @allure.title("Ошибка при отсутствии обязательного поля при создании курьера")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_required_field_error(self, missing_field):
        payload = generate_courier_payload()
        del payload[missing_field]

        response = requests.post(Urls.CREATE_COURIER, json=payload)

        assert response.status_code == 400
        assert ResponseMessages.COURIER_NOT_ENOUGH_DATA_CREATE in response.json().get("message", "")
