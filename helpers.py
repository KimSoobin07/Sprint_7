import random
import string
import requests
from data import Urls


def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_courier_payload():
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }


def register_new_courier_and_return_login_password():
    login_pass = []
    payload = generate_courier_payload()

    response = requests.post(Urls.CREATE_COURIER, json=payload)

    if response.status_code == 201:
        login_pass.append(payload["login"])
        login_pass.append(payload["password"])
        login_pass.append(payload["firstName"])

    return login_pass


def delete_courier_by_credentials(login, password):
    login_response = requests.post(
        Urls.LOGIN_COURIER,
        json={"login": login, "password": password}
    )
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        if courier_id:
            requests.delete(f"{Urls.DELETE_COURIER}{courier_id}")


def cancel_order_by_track(track):
    if track:
        requests.put(Urls.CANCEL_ORDER, params={"track": track})
