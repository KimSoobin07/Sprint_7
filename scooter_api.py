import allure
import requests
from data import Urls
from helpers import generate_courier_payload


class ScooterApi:

    @staticmethod
    @allure.step("Регистрация нового курьера и возврат его данных")
    def register_new_courier_and_return_login_password():
        login_pass = []
        payload = generate_courier_payload()

        response = requests.post(Urls.CREATE_COURIER, json=payload)

        if response.status_code == 201:
            login_pass.append(payload["login"])
            login_pass.append(payload["password"])
            login_pass.append(payload["firstName"])

        return login_pass

    @staticmethod
    @allure.step("Логин курьера для получения ID и его удаление")
    def delete_courier_by_credentials(login, password):
        login_response = requests.post(
            Urls.LOGIN_COURIER,
            json={"login": login, "password": password}
        )
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
            if courier_id:
                requests.delete(f"{Urls.DELETE_COURIER}{courier_id}")

    @staticmethod
    @allure.step("Отмена заказа по трек-номеру")
    def cancel_order_by_track(track):
        if track:
            requests.put(Urls.CANCEL_ORDER, params={"track": track})
